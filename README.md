### Project Overview
TalentScout is an AI-powered hiring assistant chatbot designed to streamline the initial screening process for technical candidates. The chatbot collects candidate information, generates customized technical interview questions based on their tech stack, and allows candidates to submit answers. The responses are saved for further evaluation, enhancing efficiency in the hiring process.

### Installation Instructions
##### Prerequisites
Ensure you have the following installed on your system:
1. Python 3.8+
2. pip
3. Virtual environment (optional but recommended)
4. A Groq API Key (stored in a .env file)

##### Clone the repository:
git clone https://github.com/Nagi2003/PAGAI_Assignment.git
cd PAGAI_Assignment

##### Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

##### Install dependencies:
pip install -r requirements.txt

##### Set up the Groq API key:
Create a .env file in the project directory.

##### Add the following line to the .env file:
GROQ_API_KEY="your_api_key_here"

##### Run the application:
streamlit run file.py

Access the chatbot in your browser at http://localhost:8501.

##### Usage Guide
--> Enter your personal details, including your name, email, phone, experience, position, location, and tech stack.
--> Click Submit to generate technical questions based on the tech stack provided.
--> Answer the questions directly in the app.
--> Click Submit Answers to save your responses.
--> Optionally, end the conversation after submitting your answers.

### Technical Details

##### Libraries Used:
streamlit - UI framework for interactive web applications.
langchain - Provides an interface for interacting with the Groq API.
python-dotenv - Manages environment variables.
json - Handles structured storage of candidate data.
datetime - Adds timestamps for saved responses.

##### Model Details
The chatbot uses llama3-8b-8192, an LLM model from Groq, accessed via the LangChain framework.
The model generates technical questions based on a structured prompt.

##### Architectural Decisions
Prompt Engineering: The prompt ensures structured JSON output, making it easier to parse.
State Management: st.session_state maintains session persistence for candidate responses.
File Storage: Candidate responses are saved as JSON files in the output directory for later review.

##### Prompt Design
##### The prompt instructs the LLM to generate structured interview questions covering:
Problem-solving skills
Best practices
Real-world applications
The output is strictly formatted as a JSON array, ensuring consistency and ease of processing.

##### Future Enhancements
Add authentication for recruiter access.
Implement database storage instead of JSON files.
Improve question generation logic using a ranking system.
