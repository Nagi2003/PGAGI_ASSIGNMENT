import streamlit as st
import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from datetime import datetime

# Load API Key from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("Groq API Key is missing! Please check your .env file.")
    st.stop()

# Initialize Groq Model via LangChain
llm = ChatGroq(model="llama3-8b-8192", api_key=GROQ_API_KEY)

# Define Prompt Template
question_prompt = PromptTemplate(
    input_variables=["tech_stack"],
    template="""You are a technical interviewer assessing candidates' skills.
Generate 3-5 technical interview questions based on the candidate's tech stack: {tech_stack}.
The questions should:
- Cover different aspects (problem-solving, best practices, real-world applications).
- Be appropriately challenging.
- Be formatted as a JSON array of objects. Each object should have the following structure:
  {{
    "question": "The technical question text",
    "answer": ""  // Leave the answer field empty for the candidate to fill in.
  }}

Example:
[
  {{
    "question": "Explain the difference between a list and a tuple in Python.",
    "answer": ""
  }},
  {{
    "question": "Describe a scenario where you would use a decorator in Python.",
    "answer": ""
  }}
]

Important: Ensure the ENTIRE output is valid JSON.  Do not include any text outside the JSON structure.
"""
)

question_chain = LLMChain(llm=llm, prompt=question_prompt)

def generate_technical_questions(tech_stack):
    response = question_chain.run(tech_stack)
    try:
        start = response.find('[')
        end = response.rfind(']')

        if start != -1 and end != -1:
            json_string = response[start:end+1]
            try:
                questions_json = json.loads(json_string)
                return questions_json
            except json.JSONDecodeError as e:
                st.error(f"JSON Decode Error: {e}")
                st.write("Raw LLM Response (for debugging):")
                st.write(response)
                return None
        else:
            st.error("Could not find valid JSON boundaries in LLM response.")
            st.write("Raw LLM Response (for debugging):")
            st.write(response)
            return None

    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.write("Raw LLM Response (for debugging):")
        st.write(response)
        return None

def save_to_json(data, full_name):
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    sanitized_name = full_name.replace(" ", "_")  
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{sanitized_name}_{timestamp}.json"
    file_path = os.path.join(output_dir, filename)
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    st.success(f"Data saved to {file_path}")

def chatbot():
    st.set_page_config(page_title="TalentScout - Hiring Assistant", layout="centered")
    st.title("🤖 TalentScout - Hiring Assistant Chatbot")
    st.write("Welcome! I'm here to assist with your initial screening. Let's get started.")

    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'candidate_data' not in st.session_state:
        st.session_state.candidate_data = {}
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    exit_keywords = ["exit", "quit", "end", "stop", "bye"]

    with st.form(key='candidate_form'):  
        full_name = st.text_input("📝 Full Name")
        email = st.text_input("📧 Email Address")
        phone = st.text_input("📞 Phone Number")
        experience = st.number_input("💼 Years of Experience", min_value=0, max_value=50, step=1)
        position = st.text_input("🎯 Desired Position(s)")
        location = st.text_input("📍 Current Location")
        tech_stack = st.text_area("💻 Tech Stack (Comma-separated, e.g., Python, Django, PostgreSQL)")
        submit_button = st.form_submit_button("🚀 Submit")

    if submit_button:
        if not full_name or not email or not phone or not position or not tech_stack:
            st.warning("⚠️ Please fill in all required fields.")
            st.stop()  # Stop execution if fields are missing

        if any(keyword in tech_stack.lower() for keyword in exit_keywords):
            st.success("👋 Goodbye! Thank you for using TalentScout.")
            st.stop()

        st.success(f"Thank you, {full_name}! Generating technical questions based on your tech stack...")
        tech_list = ", ".join([tech.strip() for tech in tech_stack.split(',')])
        questions = generate_technical_questions(tech_list)

        if questions:
            st.session_state.questions = questions  
            st.session_state.candidate_data = {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "experience": experience,
                "position": position,
                "location": location,
                "tech_stack": tech_stack,
                "questions": questions
            }

    if st.session_state.questions:
        st.subheader("🎯 Technical Questions")

        # Input areas are OUTSIDE the form
        for i, q_data in enumerate(st.session_state.questions):
            st.write(f"{i+1}. {q_data['question']}")
            st.session_state.answers[q_data['question']] = st.text_area(
                f"Answer for Question {i+1}", height=100, key=f"answer_{i}"
            )

        st.info("📢 Please answer the questions above.")

        if st.button("Submit Answers") and not st.session_state.submitted:  
            st.session_state.submitted = True
            st.write("--- Answers Submitted ---")
            st.session_state.candidate_data["answers"] = st.session_state.answers
            st.write(st.session_state.candidate_data)

            save_to_json(st.session_state.candidate_data, st.session_state.candidate_data["full_name"])

            st.success("Thank you for submitting your answers!")

    if st.session_state.submitted:
        if st.button("🔚 End Conversation"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]  
            st.success("👋 Thank you for using TalentScout. Have a great day!")
            st.rerun() 

if __name__ == "__main__":
    chatbot()
