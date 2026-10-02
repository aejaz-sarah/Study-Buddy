# What I Built
My friend often struggles with long, dense university lecture notes. When exams approach, reading through 50 pages of raw text is overwhelming and inefficient. While there are many AI tools that can summarize text, my friend had a specific boundary: they didn't want to upload their private study material, personal notes, and university documents to a proprietary cloud AI service.

So, I built **StudyBuddy**—a private AI study companion designed specifically for them. 

StudyBuddy is a clean, minimal application that takes long text and allows the user to extract exactly what they need: a concise summary, a simple beginner-friendly explanation, a 5-question quiz, or a prioritized revision checklist. Best of all, because the AI runs completely locally using Ollama and an open-weight model, their study material never leaves their computer.

# Demo
[INSERT DEMO LINK OR VIDEO HERE]

# Code
[INSERT GITHUB REPOSITORY LINK HERE]

# How I Built It
I wanted the tool to be as distraction-free as possible, so I built the frontend using **Python** and **Streamlit**. Streamlit allowed me to rapidly prototype a clean UI with text areas, mode selectors, and loading indicators without getting bogged down in complex frontend state management.

For the AI brain, I integrated **Ollama** running locally, specifically using the **Llama 3.2 3B** open-weight model (`llama3.2:3b`). The Streamlit app communicates with the local Ollama API via standard HTTP POST requests to `http://localhost:11434/api/generate`.

I spent time carefully engineering the prompts for each study mode. For example, the "Generate Quiz" prompt explicitly instructs the model to base questions *only* on the supplied notes to prevent hallucinations, and to provide the answers separately at the bottom. I also implemented error handling to guide the user gracefully if Ollama isn't running or the model hasn't been downloaded yet, ensuring a smooth experience even for non-technical users.

# Why Does Open Innovation Matter?
Open innovation—specifically local open-weight AI—is the entire reason this project is viable for my friend. 

By building on open technology, StudyBuddy delivers:
* **Local Data Privacy:** Sensitive notes stay on the device. Once the model is downloaded, the app can be used entirely offline.
* **Model Control & Flexibility:** The architecture is modular. If my friend upgrades their laptop and wants to use a larger, more capable open-weight model, they can simply swap the model name in the code. We aren't locked into a single provider's ecosystem.
* **Zero Cost:** There are absolutely no per-request cloud AI API costs. My friend can generate 100 quizzes a night during finals week without worrying about a bill.
* **Behavior Control:** We own the prompts. We can tune exactly how the model behaves without fighting against a closed model's restrictive system guardrails.

Using an open-weight model running locally gave me the power of state-of-the-art AI while respecting my friend's privacy boundaries.

# My Agent Session
[INSERT DEVRELAY LINK / AGENT SESSION LOGS HERE]

# Prize Categories
- **Build for a Friend:** This was built for ONE specific friend to solve ONE real problem with ONE focused, useful solution.
- **Open Innovation:** The project relies entirely on open-weight models (Llama 3.2 3B) running locally via an open-source inference engine (Ollama), demonstrating how open AI enables privacy-first applications.

---

### A Note on Feedback
*[ADD MY FRIEND'S ACTUAL REACTION HERE]*
