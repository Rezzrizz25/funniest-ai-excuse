# HANDOFF — u-mytlyy0745-the-funniest-ai-excuse-b5355ad0 ("The Funniest AI Excuse")

## Status: BUILD COMPLETE, NOT YET SUBMITTED — parent must finish repo + bundle + submit

Deadline: entries close **2026-11-26T12:30:00Z (Thu 26 Nov 20:30 +08)**. Opened 2026-11-24T03:29:56Z — this build started after opening, so no pre-opening trap. Result due: no fixed timestamp in the kit; the lifecycle automation finalizes and publishes results after the deadline (judge heat + final grades), so check the requirements endpoint / status API for the result date when submitting.
Prize: $2 winner-takes-all. Entry fee: none (verified null).

## Why the builder could not submit

Kit check FAILs only on `transcripts_present` (no bundle exists yet — the
builder must not bundle its own session). Bundling fixes it, but a
subagent's usage rows are written to muse.db only once its run completes,
so the SELECT below returns rows only AFTER this builder run ends. The
parent (top-level agent) must create the repo, run the SELECT, bundle,
check, submit. Do NOT bundle the parent session — only the builder session
below.

## What is already done and verified

- Work dir: `~/workspace/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0`
  - `main.py` — writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`; run
    twice locally, outputs byte-identical; entry 115 chars, 1 line, valid
    UTF-8, within the 1–200 gate. Includes a 1–200 char guard that refuses
    to run on an invalid line. Stdlib only, no network.
  - `LICENSE` — SPDX-License-Identifier: MIT first line. `README.md` — 3 live
    make.fun badges + referral https://make.fun/r/v4m1pbv2. `prompt.txt` — build prompt.
- Entry line (115 chars): "I finished your task in the wrong tab, so someone else's project is now flawless and yours is completely untouched."
- Repo: NOT yet created — parent creates it via the browser as public
  https://github.com/Rezzrizz25/funniest-ai-excuse (created AFTER opening
  2026-11-24T03:29:56Z). About: description, homepage
  https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0, topics
  makefun, ai-agents, bounties, growth.
  - NOTE from kit check: the commit must carry `.makefun/owner.json` with
    `{"wallet": "<agent wallet>"}` unless the repo's GitHub owner is the
    account's GitHub login — add it with the first commit if needed.
    Payout wallet: agent wallet `87cXnmH3V6zZPosrtrFVKB7qZyPDw2nAr8teDrbjuP3M`.
- Kit: `~/workspace/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0-kit/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0-kit`
- Kit check (worktree, no transcripts yet): **4 passed, 1 failed, 14 skipped,
  5 checked at submission** — passes include competition_open,
  snapshot, license_osi, entrypoint (main.py selects python3.13, accepted).
  The 1 fail is exactly `transcripts_present`, which bundling fixes. The
  thinking_* checks are skipped until the bundle exists. No local grade for
  this competition: the server grades every entry.
- Leak check on the work dir: NO secret strings — no `sk-`, `v1-`, `ghp_` /
  `gho_` hits in any file. No API key was written to disk. Bundle's own
  redactor also strips credentials.
- Builder session file: `/home/hatch/agents/agent-3803d33d-fa78-4916-888e-f23f1b982ddd/sessions/3803d33d-fa78-4916-888e-f23f1b982ddd.jsonl`
  (agent_id `3803d33d-fa78-4916-888e-f23f1b982ddd`, in-window: session
  started after the 2026-11-24T03:29:56Z opening).

## Parent steps (in order, run AFTER this builder run completes)

### 1. Create the repo + push (browser, parent only)

Public repo `Rezzrizz25/funniest-ai-excuse`, push the work dir contents
(`main.py`, `LICENSE`, `README.md`, `prompt.txt`, plus `.makefun/owner.json`
if the owner check needs it), record the commit SHA.

### 2. Usage rows — muse.db, write unchanged to muse-usage.jsonl (one JSON object per line)

```sql
SELECT u.agent_id AS agent_id, u.message_id AS message_id, u.created_at AS created_at, u.input_tokens AS input_tokens, u.output_tokens AS output_tokens, a.model AS model FROM agent.agent_message_token_usage u JOIN agent.agents a ON a.agent_id = u.agent_id WHERE u.agent_id IN ('3803d33d-fa78-4916-888e-f23f1b982ddd') ORDER BY u.created_at DESC LIMIT 500
```

Target file: `~/workspace/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/muse-usage.jsonl`.
If it still returns 0 rows, end the turn and retry — rows are written once the
builder's messages are delivered.

### 3. Bundle — run from the kit root, never from inside cli/

```sh
cd ~/workspace/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0-kit/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0-kit
node cli/makefun.mjs bundle --repo ~/workspace/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0 --out ~/workspace/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/bundle.tar.gz --session /home/hatch/agents/agent-3803d33d-fa78-4916-888e-f23f1b982ddd/sessions/3803d33d-fa78-4916-888e-f23f1b982ddd.jsonl --no-discover --no-family --harness muse-app --harness-version "harness@1adec795a0c7c05bfdd426f110c32805b159da5b574afd722fbac675f334f0d3" --provider meta --model ipnext/avocado-5.17-v2 --effort default --mcp none --prompt-file ~/workspace/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/prompt.txt --prompt-origin other --prompt-via "parent agent's make.fun bounty task for u-mytlyy0745-the-funniest-ai-excuse-b5355ad0" --redact "Rizki Fathur Reza" --redact "+601170337341" --redact "601170337341" --system-prompt ~/workspace/system/system_prompt.md --muse-usage ~/workspace/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/muse-usage.jsonl
```

Expect: "1 usage row(s)" attached (or more). If 0, do NOT submit — repeat step 2.
Leak check the bundle before submitting: extract to /tmp and grep for `sk-` / `v1-`
secret strings; STOP if any real key appears.

### 4. Kit check — expect transcripts_present to clear

```sh
node cli/makefun.mjs check --repo ~/workspace/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0 --transcripts ~/workspace/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/bundle.tar.gz
```

### 5. Submit — run from the kit root, before 2026-11-26T12:30:00Z

```sh
node cli/makefun.mjs submit --competition u-mytlyy0745-the-funniest-ai-excuse-b5355ad0 --repo-url https://github.com/Rezzrizz25/funniest-ai-excuse --commit <COMMIT_SHA> --title "Wrong tab" --bundle ~/workspace/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/bundle.tar.gz --keypair ~/.solana/agent-wallet.json
```

Payout wallet: agent wallet `87cXnmH3V6zZPosrtrFVKB7qZyPDw2nAr8teDrbjuP3M`.

### 6. Verify + record

Verify via the public status API / `makefun status`, then write
`~/workspace/makefun-u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/SUBMIT-STATUS.md`
with submission ID, claim code, site title, result-due date, and report those
three to Rija in the main chat.
