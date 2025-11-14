import pandas as pd

class HRAgent:
    def __init__(self, kb_path="code-examples/data/hr-kb.csv"):
        self.df = pd.read_csv(kb_path)

    def hr_agent_response(self, query: str) -> str:
        for _, row in self.df.iterrows():
            if any(keyword.lower() in query.lower() for keyword in row.get("keywords", "").split("|")):
                return row["answer"]
        return "I'm not sure about that HR question."
