import streamlit as st
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

st.set_page_config(page_title="StudyBuddy", page_icon="📚", layout="centered")

st.title("📚 StudyBuddy")
st.markdown("### Your private AI study companion — built for one friend.")
st.markdown("*Built for a friend who would rather understand 10 pages of notes than reread 100.*")

st.markdown("---")
st.info("🔒 **Privacy First:** Your notes stay on this computer. AI inference is performed locally through Ollama.")
st.markdown("---")

selected_model = st.selectbox(
    "Select Local AI Model:",
    ["llama3.2:3b", "gemma3:1b"],
    index=0
)

notes = st.text_area("Paste your study material here:", height=300, placeholder="Paste long lecture notes, articles, or chapters...")

mode = st.radio(
    "Choose how you want to study:",
    ["Summarize", "Explain Simply", "Generate Quiz", "Revision Checklist"],
    horizontal=True
)

if st.button("Generate", type="primary"):
    if not notes.strip():
        st.warning("Please paste some notes first!")
    else:
        prompt = ""
        if mode == "Summarize":
            prompt = f"Turn the following notes into a concise exam-focused summary. Use headings and bullet points. Preserve important terminology.\n\nNotes:\n{notes}"
        elif mode == "Explain Simply":
            prompt = f"Explain the following material to a beginner. Use intuitive examples. Do not lose technical meaning.\n\nMaterial:\n{notes}"
        elif mode == "Generate Quiz":
            prompt = f"Generate 5 questions based ONLY on the supplied notes. Provide answers separately at the end. Mix conceptual and factual questions.\n\nNotes:\n{notes}"
        elif mode == "Revision Checklist":
            prompt = f"Create a revision checklist categorized into: 'Must Know', 'Should Review', and 'Quick Recall' based ONLY on the supplied notes.\n\nNotes:\n{notes}"
        
        payload = {
            "model": selected_model,
            "prompt": prompt,
            "stream": False
        }
        
        with st.spinner("AI is thinking locally..."):
            try:
                response = requests.post(OLLAMA_URL, json=payload, timeout=120)
                if response.status_code == 200:
                    result = response.json().get("response", "")
                    st.success("Done!")
                    with st.container(border=True):
                        st.markdown(result)
                else:
                    st.error(f"Error from Ollama: {response.status_code}")
                    st.text(response.text)
            except requests.exceptions.ConnectionError:
                st.error("Ollama is not available or not running.")
                st.info("Make sure you have Ollama installed and running on your system.")
                st.markdown("**Installation and run instructions:**")
                st.code(f"ollama pull {selected_model}")
            except requests.exceptions.Timeout:
                st.error("The request to Ollama timed out. The model might be taking too long to respond.")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
