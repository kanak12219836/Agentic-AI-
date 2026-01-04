from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import sys

# Ensure the current directory is in the path so we can import 'app'
sys.path.append(os.getcwd())

from executor import Executor

app = FastAPI(
    title="Agentic AI System",
    description="API to run Agentic AI tasks",
    version="1.0"
)

agent = Executor()

class AgentRequest(BaseModel):
    goal: str
    input_file: str

@app.post("/run-agent")
def run_agent(request: AgentRequest):
    try:
        result = agent.execute(
            goal=request.goal,
            input_file=request.input_file
        )

        output_path = "output/output.txt"
        output_text = ""
        
        if os.path.exists(output_path):
            with open(output_path, "r", encoding="utf-8") as f:
                output_text = f.read()

        return {
            "status": "success",
            "message": result,
            "output": output_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))