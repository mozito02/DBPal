# DBPal: Langchain-based AI System to Interact with Local MySQL Server

DBPal is an AI-powered system that allows users to interact with a local MySQL server using natural language queries. The system leverages Langchain for creating intelligent agents that can query and respond to database requests in an intuitive, human-like manner.

## Features

- **Natural Language Queries**: Users can query the MySQL database using natural language prompts.
- **AI-Powered Agent**: The system uses a large language model (LLM) via Langchain to process and respond to database queries intelligently.
- **SQL Integration**: Connects directly to a local MySQL server, enabling efficient data querying, retrieval, and analysis.
- **Interactive**: Designed to be deployed with Streamlit for an interactive, user-friendly interface.

## How It Works

1. **Database Connection**: DBPal connects to your local MySQL server via user-provided credentials (host, user, password, and database name).
2. **AI Agent**: The AI agent processes user queries in natural language and translates them into appropriate SQL queries.
3. **Result Interpretation**: The system fetches the relevant data from the MySQL server and presents it to the user in a conversational format.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/mozito02/DBpal.git
   cd dbpal
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your MySQL database and ensure that it's running locally.

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Enter your MySQL database credentials (host, user, password, and database name) in the provided fields.


3. Use the chat interface to ask questions about your **student data**. For example:
   - "How many students are enrolled in 'Mathematics'?"
   - "What is the average age of the students?"
   - "Show me the details of students with a GPA higher than 3.5."

## Example Queries

Here are some example queries you can ask DBPal using a basic **Student Database**:

- **General Queries**: 
   - "How many students are enrolled in the database?"
   - "What is the most popular major among the students?"

- **Performance-Based Queries**: 
   - "How many students have a GPA higher than 3.5?"
   - "How many students scored an 'A' in their final exam?"

- **Gender-Specific Queries**: 
   - "How many male students are enrolled in 'Computer Science'?"
   - "What is the average GPA of female students?"

- **Class-Specific Queries**: 
   - "How many students are in the 'Senior' class?"
   - "Show me the details of students in 'Freshman' year with a GPA above 3.0."

## Customization

You can easily extend DBPal by adjusting the prompt logic to cater to specific datasets and use cases. Modify the agent's behavior or add new features by leveraging the flexibility of Langchain and Streamlit.

## License

This project is licensed under the MIT License.
