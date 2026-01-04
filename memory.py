class AgentMemory:
    def __init__(self):
        self.memory = []

    def store(self, content: str):
        self.memory.append(content)

    def retrieve(self):
        return self.memory
