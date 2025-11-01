# import the classes from test.ipynb
import operator 
from typing import Annotated, List 
from langgraph.graph import MessagesState 
from pydantic import BaseModel, Field 
from typing_extensions import Literal 

# ---------------
# Model Section
# --------------- 

class Section(BaseModel):
    title: str 
    content: str 

# ---------------
# Analyst Models
# --------------- 

class Analyst(BaseModel): 
    affiliation: str = Field(description="Primary affiliation of the analyst")
    name: str = Field(description="Full name of the analyst") 
    role: str = Field(description="Role of the analyst")
    description:str = Field(description="Brief description of the analyst's expertise, motives, concerns and background")

    @property
    def persona(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Affiliation: {self.affiliation}\n"
            f"Role: {self.role}\n"
            f"Description: {self.description}\n"
        )
    
class Perspectives(BaseModel):
       analysts: List[Analyst] = Field(description="Comprehensive list of analysts with their roles and affiliations.") 


# -------------------------------
# Search Query Output Parser
# -------------------------------

class SearchQuery(BaseModel):
    search_query: str = Field(None, description="Search query for retrieval.")

# -------------------------------
# State Classes for Graphs
# -------------------------------

class GenerateAnalystsState(TypedDict):
    topic: str #research topic
    max_analysts: int # number of analyst
    human_analyst_feedback: str # Human feedback
    analysts: List[Analyst] # Analyst asking questions

class InterviewState(MessagesState):
    max_num_turns: int # max number of turns
    context: Annotated[list, operator.add] # Source docs 
    analyst: Analyst # Analyst asking questions
    interview: str  # interview transcript
    sections: list # Final key we import 

class ResearchGrapthState(TypedDict):
    topic: str
    max_analysts: int
    human_analyst_feedback: str
    analysts: List[Analyst]
    sections: Annotated[list, operator.add]
    introductions: str 
    content: str 
    conclusion: str 
    final_report: str