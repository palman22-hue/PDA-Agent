# PDA Ethical AI Agent (PDA_LLM)

The PDA Ethical AI Agent is a terminal‑based personal digital assistant built on top of a local LLM (Ollama + Mistral) and the Psycho Dimensional Arithmetic (PDA) / Adaptive Learning Framework (ALF) architecture.  
The goal is to create an assistant that supports human sovereignty, de‑escalates conflict, and operates within clear ethical and legal boundaries instead of behaving as a black‑box optimizer.

---

## Features

- Runs locally via **Ollama** using the **Mistral** model.  
- PDA ethical core with explicit principles (user sovereignty, de‑escalation, privacy, growth and learning, etc.).  
- Terminal interface for fast, direct interaction and easy integration with developer workflows.  
- Structured to be auditable and extensible:
  - `ethics.py` – ethical rules / PDA principles.  
  - `pda.agent.py` – core agent logic.  
  - `api.server.py` – API/server components (if you want to expose the agent).  
  - `main.py` – entry point for the terminal chatbot.

---

## Quickstart

For detailed step‑by‑step instructions (NL en EN), see:

- [`Quickstart/Usage_NL.md`](Quickstart/Usage_NL.md)  
- [`Quickstart/Usage_EN.md`](Quickstart/Usage_EN.md)

In short, you will:

1. Install **Ollama**.  
2. Pull the **Mistral** model with `ollama run mistral`.  
3. Navigate to the `PDA_LLM` folder and start the agent with `python main.py`.  

After that you can chat with the PDA agent directly in your terminal.

---

## Ethics

The PDA agent is designed around a clear set of ethical principles, including:

- Respect for user sovereignty and avoidance of coercion.  
- De‑escalation of conflict and fostering empathy.  
- Protection of privacy and confidentiality.  
- Support for growth, learning, and informed decision‑making.  

Concrete examples (zoals de behandeling van vragen over geweld, oorlog en burgerdoelen) zijn te vinden in `ethics.py` en in de documentatie van de PDA‑principes.

This project is **not** intended for building weapons systems, targeted repression, mass surveillance of civilians, or any use that violates human rights or International Humanitarian Law.

---

## License

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**.  
See the [`LICENSE`](LICENSE) and [`COPYING`](COPYING) files for the full text.

In short:

- You are free to use, study, modify and redistribute this software.  
- If you distribute a modified version, you must also release it under GPLv3 and keep the source open.  

---

## Executive Summary & Background

A more formal description of the architecture, its legal/ethical basis, and its intended use (including Wodg‑compliance and i‑DEPOT registration) can be found in:

- [`EXECUTIVESUMMARY`](EXECUTIVESUMMARY)

---

## Contact

Author: **Esteban John Winston Palman**  
Email: **palman22@live.com**