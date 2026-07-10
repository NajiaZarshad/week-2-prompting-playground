import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

# Load API Key
load_dotenv(dotenv_path=".env")

st.write(os.getenv("GEMINI_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit Page
st.set_page_config(page_title="Few-Shot Prompt Builder")
st.title("🔮💻🔮 Few-Shot Prompt Builder")
st.write("Create prompts using Few-Shot Learning")
role = st.text_input("AI Role (Example: Teacher, Writer, Assistant)")

# Example 1
st.subheader("Example 1")
example1_input = st.text_input("Example 1 Input")
example1_output = st.text_input("Example 1 Output")

# Example 2
st.subheader("Example 2")
example2_input = st.text_input("Example 2 Input")
example2_output = st.text_input("Example 2 Output")
st.subheader("Example 3")
example3_input = st.text_input("Example 3 Input")
example3_output = st.text_input("Example 3 Output")
# User Input
st.subheader("Your Task")
user_input = st.text_area("Enter your input")

# Generate Button
if st.button("Generate"):

    prompt = f"""
Example 1:
Input: {example1_input}
Output: {example1_output}

Example 2:
Input: {example2_input}
Output: {example2_output}
Example 3:
Input: {example3_input}
Output: {example3_output}

Now complete this task:
Input: {user_input}
"""

try:
    response = model.generate_content(prompt)

    st.subheader("AI Response")
    st.write(response.text)

except Exception as e:
    st.error(f"Error: {e}")