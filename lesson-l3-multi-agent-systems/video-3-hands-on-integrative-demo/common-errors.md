# Common Errors and Solutions

**Error:** Misclassification of queries by Orchestrator.
**Solution:** Refine classification logic; use LLM intent detection if needed.

**Error:** Function calls fail due to schema mismatches.
**Solution:** Verify function schema completeness; match JSON schema precisely.

**Error:** Loss of conversational context during handoffs.
**Solution:** Pass explicit context/state objects; test multi-turn dialogues.

**Error:** API rate limits or authentication failures.
**Solution:** Ensure valid API key; implement rate limit handling.
