class Planner:
    def plan(self, goal: str):
        goal = goal.lower()
        steps = []

        if "summarize" in goal:
            steps.extend([
                "read_file",
                "summarize_text",
                "write_file"
            ])

        elif "analyze" in goal:
            steps.extend([
                "read_file",
                "analyze_text",
                "write_file"
            ])
        else:
            # Default fallback if goal is not recognized
             steps.extend([
                "read_file",
                "analyze_text",
                "write_file"
            ])

        return steps
