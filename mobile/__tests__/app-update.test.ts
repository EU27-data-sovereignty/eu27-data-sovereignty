/**
 * The app's own over-the-air update (#115): a port the screens drive, with every outcome reported, and
 * nothing reached unless the port is enabled and the reader asked.
 */
import { checkForAppUpdate, describeAppUpdate, noAppUpdates } from '../src/update/appUpdate';
import { fakeAppUpdates } from './support';

const states = async (port: Parameters<typeof checkForAppUpdate>[0]) => {
  const seen: string[] = [];
  const last = await checkForAppUpdate(port, (s) => seen.push(s.kind));
  return { seen, last: last.kind };
};

describe('checkForAppUpdate', () => {
  it('does nothing in a build that cannot receive updates', async () => {
    expect(await states(noAppUpdates)).toEqual({ seen: ['disabled'], last: 'disabled' });
  });

  it('is up to date when the service has nothing newer', async () => {
    const { port, calls } = fakeAppUpdates({ available: false });
    expect(await states(port)).toEqual({ seen: ['checking', 'up-to-date'], last: 'up-to-date' });
    expect(calls).toEqual(['check']);
  });

  it('downloads a newer build and reports it ready', async () => {
    const { port, calls } = fakeAppUpdates({ available: true, isNew: true });
    expect(await states(port)).toEqual({
      seen: ['checking', 'downloading', 'ready'],
      last: 'ready',
    });
    expect(calls).toEqual(['check', 'fetch']);
  });

  it('treats a fetched update that is not new as up to date', async () => {
    const { port } = fakeAppUpdates({ available: true, isNew: false });
    expect((await states(port)).last).toBe('up-to-date');
  });

  it('keeps the build it has when the service is unreachable, at either step', async () => {
    expect((await states(fakeAppUpdates({ fail: 'check' }).port)).last).toBe('unreachable');
    expect((await states(fakeAppUpdates({ available: true, fail: 'fetch' }).port)).last).toBe(
      'unreachable'
    );
  });

  it('describes every state in a sentence', () => {
    for (const kind of [
      'disabled',
      'idle',
      'checking',
      'up-to-date',
      'downloading',
      'ready',
      'unreachable',
    ] as const) {
      expect(describeAppUpdate({ kind })).toMatch(/\.$|…$/);
    }
  });
});
