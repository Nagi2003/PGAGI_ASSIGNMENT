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

##### Usage Guide:
1. Enter your personal details, including your name, email, phone, experience, position, location, and tech stack.
2. Click Submit to generate technical questions based on the tech stack provided.
3. Answer the questions directly in the app.
4. Click Submit Answers to save your responses.
5. Optionally, end the conversation after submitting your answers.

### Technical Details

##### Libraries Used:
1. streamlit - UI framework for interactive web applications.
2. langchain - Provides an interface for interacting with the Groq API.
3. python-dotenv - Manages environment variables.
4. json - Handles structured storage of candidate data.
5. datetime - Adds timestamps for saved responses.

##### Model Details
1. The chatbot uses llama3-8b-8192, an LLM model from Groq, accessed via the LangChain framework.
2. The model generates technical questions based on a structured prompt.

##### Architectural Decisions
1. Prompt Engineering: The prompt ensures structured JSON output, making it easier to parse.
2. State Management: st.session_state maintains session persistence for candidate responses.
3. File Storage: Candidate responses are saved as JSON files in the output directory for later review.

##### Prompt Design
##### The prompt instructs the LLM to generate structured interview questions covering:
1. Problem-solving skills
2. Best practices
3. Real-world applications
4. The output is strictly formatted as a JSON array, ensuring consistency and ease of processing.

##### Future Enhancements
1. Add authentication for recruiter access.
2. Implement database storage instead of JSON files.
3. Improve question generation logic using a ranking system.
