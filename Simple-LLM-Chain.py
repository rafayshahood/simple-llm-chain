# import langsmith
from  dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "first project"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')


llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'))



from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are a world class cricket journalist. Write only in 1 sentence'),
    ('user','{input}')
])

# chain = prompt | llm

# final_answer = chain.invoke({"input" : "Name 3 top ODI batters?"})
# print(final_answer.content)


from langchain_core.output_parsers import StrOutputParser

chain = prompt | llm | StrOutputParser()
print(chain.invoke({"input" : "Name 3 top ODI batters?"}))
