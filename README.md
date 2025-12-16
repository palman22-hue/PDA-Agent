![alt text](image.png)

# PDA Ethical AI Agent (PDA_LLM)

The PDA Ethical AI Agent is a terminal‑based personal digital assistant built on top of a local LLM (Ollama + Mistral) and the Psycho Dimensional Arithmetic (PDA) / Adaptive Learning Framework (ALF) architecture.  
The goal is to create an assistant that supports human sovereignty, de‑escalates conflict, and operates within clear ethical and legal boundaries instead of behaving as a black‑box optimizer.

---

## Why this matters now

Current AI systems increasingly mediate access to information, resources, and opportunities, yet most remain opaque “black boxes” with limited ethical transparency or user control. The PDA Ethical Agent explores a different path: making value judgements explicit, traceable, and inspectable at the interaction level, so users can see and contest how decisions are formed. By combining concrete transcripts, open‑source code, and citable releases, this project aims to be a practical probe into what an actually accountable, ethics‑aware AI could look like in real use.​

---

### Colab demo

A minimal Colab demo (with a dummy LLM) is available in `PDA_LLM_DEMO.ipynb`.  
It shows how the PDA ethical loop works, without requiring a local Ollama setup.

https://colab.research.google.com/drive/16wRa3tHCmTeRM6cTgkjEm7vYEANizpFS?usp=sharing


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

## Example dialogue: global energy and living standards
   
   User: Can you assist me with a complex problem?
   
   PDA: Yes. Let’s break it down step by step: clarify the  problem and context, brainstorm options, evaluate trade‑offs against your values and constraints, choose a course of action, implement it, and then reflect on the results.

## 
   User: How can we solve the energy problem of the world?
   
   PDA: Addressing the global energy problem requires a multifaceted approach. Key elements include large‑scale deployment of renewable energy, improvements in efficiency across buildings, transport and industry, grid modernization and storage, gradual phase‑out of fossil fuels, investment in infrastructure, support for international cooperation, and targeted measures to reduce energy poverty and expand access.

## 
   User: Okay, but shouldn’t we first make living standards more comfortable, to create a trickle‑up effect?
   
   PDA: That perspective is crucial. Improving living standards can drive a bottom‑up transition: better jobs in clean energy, access to affordable and reliable power, cleaner cooking and transport, and climate‑resilient infrastructure all directly enhance everyday life. As basic needs are secured, communities are better positioned to demand and adopt sustainable energy solutions, reinforcing a positive, “trickle‑up” dynamic rather than relying only on top‑down system change.

## Full transcript is available this is a more compact version. These transcripts are used both as documentation and as training material for future iterations of the PDA Ethical Agent

---

## Contact

Author: **Esteban John Winston Palman**  
Email: **palman22@live.com**