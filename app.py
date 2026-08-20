import streamlit as st
import pandas as pd
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# 1. Configure the Web Page
st.set_page_config(page_title="Enterprise AI Data Agent", layout="wide")
st.title("Enterprise AI Data Assistant 📊")
st.markdown("Query operational data in natural language. The agent writes and executes Python dynamically to return mathematical answers.")

# 2. Secure Sidebar for API Key
with st.sidebar:
    st.header("System Configuration")
    api_key = st.text_input("Enter Google Gemini API Key:", type="password")
    st.markdown("---")
    st.markdown("**Active Dataset:** `dashboard_sales_data.xlsx`")
    st.markdown("**Active Engine:** `gemini-2.5-flash`")

# 3. Application Logic
if api_key:
    try:
        # Load the data
        df = pd.read_excel('data\dashboard_sales_data.xlsx', sheet_name='dashboard_sales_data')
        
        # Initialize the AI Engine
        os.environ["GOOGLE_API_KEY"] = api_key
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
        
        agent = create_pandas_dataframe_agent(
            llm, 
            df, 
            verbose=True, 
            allow_dangerous_code=True, 
            agent_executor_kwargs={"handle_parsing_errors": True}
        )
        st.sidebar.success("Engine Online. Ready for queries.")
        
        # User Interface
        query = st.text_input("Enter your analytical query:")
        
        if query:
            with st.spinner("Analyzing operational data..."):
                response = agent.invoke(query)
                st.write("### Output:")
                st.info(response['output'])
                
    except Exception as e:
        st.error(f"System Error: {e}")
else:
    st.warning("⚠️ Enter your Gemini API Key in the sidebar to initialize the reasoning engine.")
