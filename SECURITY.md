# Security Policy

## Supported versions

PDA-Agent is currently an experimental/prototype project and only the `main` branch and latest tagged release are actively maintained.  
Other branches or forks are not covered by security support.

## Deployment model

PDA-Agent is designed primarily for local use as a terminal-based assistant running on top of a local LLM runtime (Ollama + `mistral`).  
The repository includes optional server components (e.g. `api.server.py`) that **you may** use to expose the agent as an API or service; any such exposure is the responsibility of the deploying party, not the maintainer.

## Data & privacy

- Input data (prompts, context, transcripts) is processed locally via your chosen LLM runtime.  
- Any logs, transcripts, configuration files, and session data are stored locally on the user’s system.  
- The maintainer does not receive automatic telemetry or user data.

Users are responsible for:
- Protecting any sensitive or personal data they send through PDA-Agent.  
- Securing their host system, operating system, and runtime (Ollama, Python environment, containers, etc.).  
- Implementing appropriate authentication, authorization, and network controls if they expose `api.server.py` or related components over a network.

## Reporting a vulnerability

If you discover a potential vulnerability or serious misuse risk in PDA-Agent, please use **responsible disclosure**.

If Private Vulnerability Reporting is enabled for this repository:
1. Use the **“Report a vulnerability”** button on the repository’s GitHub page to submit a private report.

If Private Vulnerability Reporting is not available:
1. Open a minimal public issue that:
   - Only states that you have found a potential vulnerability.
   - Does **not** include technical details or exploit code.
2. Wait for the maintainer to respond with an appropriate private channel for sharing details.

Where possible, include:
- A description of the vulnerability or misuse scenario (e.g. unsafe defaults in the server, prompt logging issues, authorization gaps).  
- Reproduction steps or a proof-of-concept (shared only through a private channel).  
- Relevant environment details (OS, Python version, Ollama version, model version, network setup).

The goal is to provide an initial response within 14 days, including an indication of next steps.

## Scope

In scope:
- The code in this repository (`main` branch), including:
  - Core agent logic (`pda.agent.py`, ethics modules, temporal safeguards, etc.).  
  - Terminal entry point (`main.py`) and local interaction loop.  
  - Optional server components such as `api.server.py`.  
  - Quickstart scripts and documentation referenced in the README.

Out of scope:
- External LLM runtimes and models (Ollama, Mistral, or other models and their own vulnerabilities).  
- Third-party deployments, wrappers, or integrations that expose PDA-Agent to the internet (e.g. web UIs, chat platforms, production services).  
- Hardware- and OS-specific issues that do not directly originate from the code in this repository.

## Responsible use

PDA-Agent is intended as an **ethical** AI assistant that supports human sovereignty, de-escalates conflict, protects privacy, and operates within legal and human-rights boundaries.  
Users are strongly discouraged from using the system for:

- Building weapons systems or targeting tools.  
- Mass surveillance of civilians or targeted repression.  
- Any use that violates human rights or International Humanitarian Law.

If you observe misuse of PDA-Agent in the wild, you may report it using the same contact path as above.
