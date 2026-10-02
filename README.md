# StudyBuddy 📚

## The Problem
My friend has long, dense study notes that are painful to revise. While there are many cloud AI tools that can summarize text, my friend didn't want to send their private university notes, personal thoughts, and study material to a third-party AI server. They wanted something that just works without sacrificing privacy.

## Built for a Friend
StudyBuddy was built specifically for this one friend. It is a targeted, focused tool that does exactly what they need—turning 10 pages of lecture notes into digestible study aids—without the bloat of generic AI chatbots.

## What It Does
StudyBuddy takes long text (like lecture notes) and allows the user to summarize it, explain it simply, generate a quiz, or create a targeted revision checklist. It processes everything locally on the user's machine.

## Key Features
- **Summarize**: Turn notes into a concise exam-focused summary using headings and bullet points.
- **Explain Simply**: Explain complex material to a beginner with intuitive examples.
- **Generate Quiz**: Create a 5-question quiz based ONLY on the supplied notes, with answers hidden at the end.
- **Revision Checklist**: Group topics logically into Must Know, Should Review, and Quick Recall.
- **100% Local Inference**: No data is sent to the cloud.

## How It Works
The user copies and pastes their notes into the Streamlit web interface. When they select a study mode and click "Generate", the application sends a formatted prompt containing the notes to a local Ollama instance running an open-weight model. The model generates the response locally and streams it back to the interface.

## AI Architecture
```text
User's Computer
├── Streamlit Interface (app.py)
│   ↓ HTTP POST (Localhost)
└── Ollama Server (Local Inference)
    ↓
    Llama 3.2 3B (llama3.2:3b)
```

## Why Open AI?
Open-weight models like Llama 3.2 3B democratize access to AI. Because the model weights can be downloaded and run via tools like Ollama, developers can build powerful AI applications that do not depend on proprietary APIs, do not incur per-request cloud costs, and can be customized endlessly.

## Privacy
**Your notes stay on this computer.** Because inference is performed entirely locally via Ollama, no data is ever sent to an external server. The application requires an initial internet connection to download the model (`ollama pull`), but after that, inference can occur entirely offline.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/studybuddy.git
   cd studybuddy
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally
1. Ensure Ollama is installed and the model is downloaded:
   ```bash
   ollama pull llama3.2:3b
   ```
2. Start the Ollama server (or ensure the desktop app is running).
3. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Demo
[Insert Demo Link or Video Here]

## Technology Stack
- **Frontend/Logic**: Python, Streamlit, Requests
- **Local AI Engine**: Ollama
- **Model**: Llama 3.2 3B (`llama3.2:3b` open-weight model)

## Project Structure
```text
studybuddy/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── DEV_SUBMISSION.md      # DEV.to hackathon submission article
├── DEMO_SCRIPT.md         # Script for the video demo
├── FRIEND_FEEDBACK.md     # Genuine feedback from the friend it was built for
├── COMPLIANCE_CHECKLIST.md# Hackathon rules compliance verification
├── demo_notes.txt         # Example study notes for testing
├── GITHUB_COMMANDS.md     # Git instructions
└── LICENSE                # MIT License
```

## Limitations
- Performance (speed of generation) depends heavily on the user's local CPU/GPU.
- The context window is limited by the model and local RAM; pasting an entire textbook at once may cause memory issues or truncation.

## Future Improvements
- Add a feature to save generated study guides locally as PDF or Markdown.
- Allow the user to select from different downloaded Ollama models via the UI.
- Support direct file uploads (PDF/DOCX) so the user doesn't have to copy-paste.
