
import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓"
)

st.title("🎓 AI Learning Buddy")

st.write("Enter any topic and choose an activity.")

topic = st.text_input("Enter a Topic")

activity = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if not topic.strip():
        st.warning("Please enter a topic.")
        st.stop()

    if activity == "Explain Concept":
        prompt = f"Explain '{topic}' in simple language for a beginner."

    elif activity == "Real-Life Example":
        prompt = f"Give one simple real-life example of '{topic}'."

    elif activity == "Generate Quiz":
        prompt = f"Generate 5 multiple-choice questions with answers about '{topic}'."

    else:
        prompt = topic

    with st.spinner("Generating..."):
        response = model.generate_content(prompt)

    st.success("Done!")
    st.write(response.text)
