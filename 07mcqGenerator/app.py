import streamlit as st
from dotenv import load_dotenv
load_dotenv()  # Must be at the top before using the API key

from openai_helper import generate_mcqs
import os


st.set_page_config(page_title="AI MCQ Generator", layout="centered")
st.title("🧠 AI-Based MCQ Generator")

topic = st.text_input("Enter a topic:", placeholder="e.g., Operating Systems, Networking")

num_mcqs = st.slider("Number of MCQs", 1, 10, 5)

if st.button("Generate MCQs"):
    if not topic.strip():
        st.error("Please enter a topic.")
    else:
        with st.spinner("Generating MCQs..."):
            mcqs = generate_mcqs(topic, num_mcqs)
            if mcqs:
                st.success("MCQs Generated!")
                for idx, mcq in enumerate(mcqs, 1):
                    st.markdown(f"**Q{idx}. {mcq['question']}**")
                    for opt in mcq["options"]:
                        st.markdown(f"- {opt}")
                    st.markdown(f"✅ **Answer:** {mcq['answer']}")
                    st.markdown("---")
            else:
                st.error("Something went wrong while generating MCQs.")
