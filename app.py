import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
from langchain.prompts import SystemMessagePromptTemplate
from langchain_groq import ChatGroq
import urllib.parse

st.set_page_config(page_title="DBPal: Let's Chat with SQL DB", page_icon="🤝")
st.title("DBPal : Your 'Database'd way of communication")

LOCALDB="USE_LOCALDB"
MYSQL="USE_MYSQL"

db_uri=MYSQL
mysql_host=st.sidebar.text_input("Provide MySQL Host")
mysql_user=st.sidebar.text_input("MYSQL User")
mysql_password=st.sidebar.text_input("MYSQL password",type="password")
mysql_db=st.sidebar.text_input("MySQL database")
api_key=st.sidebar.text_input(label="GRoq API Key",type="password")

if not db_uri:
    st.info("Please enter the database information and uri")

if not api_key:
    st.info("Please add the groq api key")


#LLM Model used : Llama3-8b-8192
llm=ChatGroq(groq_api_key=api_key,model_name="Llama3-8b-8192",streaming=True)

# @st.cache_resource("1h")
def config_db(db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    encoded_user = urllib.parse.quote(mysql_user)
    encoded_password = urllib.parse.quote(mysql_password)
    if db_uri == MYSQL:
        # Validate inputs
        if not all([mysql_host, mysql_user, mysql_password, mysql_db]):
            st.error("Please provide all MySQL connection details.")
            st.stop()
        
        try:
            # Attempt to create the engine
            engine = create_engine(f"mysql+mysqlconnector://{encoded_user}:{encoded_password}@{mysql_host}/{mysql_db}")
            return SQLDatabase(engine)
        except Exception as e:
            st.error(f"Error connecting to the database: {e}")
            st.stop()
            
db=config_db(db_uri,mysql_host,mysql_user,mysql_password,mysql_db)

#toolkit(From Langchain Docs)
toolkit=SQLDatabaseToolkit(db=db,llm=llm)

system_prompt = SystemMessagePromptTemplate.from_template(
    template="""
    You are an intelligent agent designed to assist with SQL queries and database-related questions. 
    - If you have determined the final answer based on the database query, return only the final answer.
    - If you need to execute a query, provide only the query without offering a final answer yet.
    - Do not combine actions and final answers in the same response.
    - Be explicit and clear in your thought process, actions, and answers.
    """
)

#Agent Creation(From Langchain Docs)

agent=create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,#Monitoring all the operations of the agent

    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION ,#Zero_SHOT for not storing any sort of history
    handle_parsing_errors=True  
)

#Default chat from LLM(role is set to assistant)
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query=st.chat_input(placeholder="Ask anything related to the database")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback=StreamlitCallbackHandler(st.container())#controls  the output of the chat

        response=agent.run(user_query,callbacks=[streamlit_callback])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)