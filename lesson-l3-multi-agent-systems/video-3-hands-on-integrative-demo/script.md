# Video 3: Hands-On Integrative Demo — Building a Multi-Agent Query Router

## High-Level Script (with Timestamps & Talking Points)

### [0:00–1:30] Demo Overview & Setup
- Present demo goals: building a multi-agent query router.
- Display architecture diagram: Orchestrator Agent and specialized agents.

### [1:30–3:00] Environment Preparation
- Verify Python, LangChain, OpenAI SDK installations.
- Load starter code or notebook.

### [3:00–5:00] Defining the Orchestrator Agent
- Walk through code for Orchestrator Agent definition.
- Explain query classification logic.

### [5:00–8:00] Creating Specialized RAG Agents
- Implement HR and Tech agents with separate knowledge bases.
- Show retrieval and response logic.

### [8:00–11:00] Integrating OpenAI Function Calling
- Explain function calling feature.
- Show how Orchestrator delegates tasks via function calls.

### [11:00–14:00] Implementing Conversational Handoffs
- Demonstrate context preservation across agent transitions.
- Show passing of context/state objects.

### [14:00–16:00] Testing the Workflow
- Run sample HR and Tech queries.
- Display expected outputs and routing behavior.

### [16:00–17:30] Troubleshooting & Common Pitfalls
- Highlight common errors (misclassification, API errors, context loss).
- Demonstrate debugging and fixes.

### [17:30–18:00] Recap & Next Steps
- Summarize built workflow.
- Encourage extending system with additional agents or query handling.
- Preview next lesson on tracing and evaluation.
