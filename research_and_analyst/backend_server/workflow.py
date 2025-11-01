import os 
import sys 
from datetime import datetime
from typing import Optional 
from langgraph.types import Send 

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from langgraph import StateGraph, START, END 
from langgraph.checkpoint.memory import MemorySaver 
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, get_buffer_string
from langchain_community.tools.tavily_search import TavilySearchResults 

from docx import Document 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from research_and_analyst.utils.model_loader import ModelLoader
from dotenv import load_dotenv
load_dotenv()

def build_interview_graph(llm, tavily_search=None):
    pass

    def generate_questions(state: InterviewState):
        pass

    def search_web(state: InterviewState):
        pass    

    def generate_answer(state: InterviewState):
        pass

    def save_interview(state: InterviewState):
        pass
    
    def write_section(state: InterviewState):
        pass

    
# one more import statement, look into the savit github
class AutonomousScientificReportGeneration:
    # NOTE: Add docstrings later

    def __init__(self, llm):
        self.llm = llm
        self.memory = MemorySaver()
        self.tavily_search = TavilySearchResults()

    def create_analyst(self, state: GenerateAnalystState):
        structured_llm = self.llm.with_structured_output(Perspective) 
          
        pass 

    def human_feedback(self):
        pass 

    def write_report(self):
        pass

    def write_introduction(self):
        pass

    def write_conclusion(self):
        pass

    def finalise_report(self):
        pass

    def save_report(self):
        pass

    def _save_as_docx(self):
        pass 

    def _save_as_pdf(self):
        pass

    def build_graph(self):
        pass

if __name__ == "main":
    # NOTE: For testing purposes only
    llm = ModelLoader.load_llm()
    print(llm.invoke("hello").content)

    reporter = AutonomousScientificReportGeneration()
    reporter.build_graph()
