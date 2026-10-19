// Fails on any high or critical npm advisory that audit-allowlist.json doesn't list,
// and on allowlist entries that npm audit no longer reports. Run by test.sh.
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';

const BLOCKING = new Set(['high', 'critical']);

function auditJson() {
  try {
    return execFileSync('npm', ['audit', '--json'], { encoding: 'utf8', maxBuffer: 64 << 20 });
  } catch (error) {
    // npm audit exits non-zero whenever it finds anything; the report is still on stdout.
    if (error.stdout) return error.stdout;
    throw error;
  }
}

const report = JSON.parse(auditJson());
if (report.error) {
  console.error(`npm audit failed: ${report.error.summary ?? JSON.stringify(report.error)}`);
  process.exit(2);
}

// Each root advisory appears as an object in some package's `via`; everything else is propagation.
const advisories = new Map();
for (const vuln of Object.values(report.vulnerabilities ?? {})) {
  for (const via of vuln.via) {
    if (typeof via !== 'object') continue;
    const id = via.url.split('/').pop();
    advisories.set(id, { id, name: via.name, severity: via.severity, title: via.title });
  }
}

const allowlist = JSON.parse(readFileSync(new URL('../audit-allowlist.json', import.meta.url)));
const allowed = new Map(allowlist.advisories.map((entry) => [entry.id, entry]));
const today = new Date().toISOString().slice(0, 10);
let failed = false;

for (const advisory of advisories.values()) {
  const entry = allowed.get(advisory.id);
  if (entry) {
    const due =
      entry.review <= today ? ` — REVIEW DUE (${entry.review}): re-check and move the date` : '';
    if (entry.review <= today) failed = true;
    console.log(`allowed  ${advisory.severity.padEnd(8)} ${advisory.name} ${advisory.id}${due}`);
  } else if (BLOCKING.has(advisory.severity)) {
    console.log(
      `BLOCKING ${advisory.severity.padEnd(8)} ${advisory.name} ${advisory.id}: ${advisory.title}`
    );
    failed = true;
  } else {
    console.log(
      `note     ${advisory.severity.padEnd(8)} ${advisory.name} ${advisory.id}: ${advisory.title}`
    );
  }
}

for (const id of allowed.keys()) {
  if (!advisories.has(id)) {
    console.log(
      `STALE    ${id} (${allowed.get(id).package}) is allowlisted but no longer reported — remove it`
    );
    failed = true;
  }
}

console.log(
  `${advisories.size} root advisories, ${allowed.size} allowlisted — ${failed ? 'FAIL' : 'ok'}`
);
process.exit(failed ? 1 : 0);
