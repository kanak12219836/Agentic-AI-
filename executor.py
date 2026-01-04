from planner import Planner
from memory import AgentMemory
from file_tools import read_file, write_file
from text_tools import summarize_text, analyze_text
from logger import get_logger

logger = get_logger(__name__)

class Executor:
    def __init__(self):
        self.planner = Planner()
        self.memory = AgentMemory()

    def execute(self, goal: str, input_file: str):
        logger.info(f"Goal received: {goal}")
        steps = self.planner.plan(goal)

        context = ""

        for step in steps:
            logger.info(f"Executing step: {step}")

            if step == "read_file":
                context = read_file(input_file)
                self.memory.store(context)

            elif step == "summarize_text":
                context = summarize_text(context)
                self.memory.store(context)

            elif step == "analyze_text":
                context = analyze_text(context)
                self.memory.store(context)

            elif step == "write_file":
                write_file("output/output.txt", context)

        return "✅ Task completed successfully"
