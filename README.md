### Project Overview
TalentScout is an AI-powered hiring assistant chatbot designed to streamline the initial screening process for technical candidates. The chatbot collects candidate information, generates customized technical interview questions based on their tech stack, and allows candidates to submit answers. The responses are saved for further evaluation, enhancing efficiency in the hiring process.

### Installation Instructions
##### Prerequisites
Ensure you have the following installed on your system:
Python 3.8+
pip
Virtual environment (optional but recommended)
A Groq API Key (stored in a .env file)

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
