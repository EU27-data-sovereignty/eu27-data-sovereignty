/**
 * Vercel Function: POST /api/ask (DECISIONS.md #78). All logic is in _ask-core.ts; this file only
 * wires the real Anthropic client and the corpus. The API key is read by the SDK from the
 * ANTHROPIC_API_KEY environment variable, set in Vercel, never in the repository.
 */
import Anthropic from "@anthropic-ai/sdk";

import corpus from "./_corpus.json" with { type: "json" };
import {
  buildRequest,
  createHandler,
  type AskClient,
  type Corpus,
} from "./_ask-core.js";

const sdk = new Anthropic();

// Compile-time proof that the request the handler builds is a valid SDK request; the handler
// itself sees only the narrow structural client below.
type StreamParams = Parameters<typeof sdk.beta.messages.stream>[0];
const _typed: StreamParams = buildRequest(corpus as Corpus, "");
void _typed;

const client = sdk as unknown as AskClient;

export const POST = createHandler(client, corpus as Corpus);
