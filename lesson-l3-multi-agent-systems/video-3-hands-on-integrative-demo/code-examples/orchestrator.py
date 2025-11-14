from hr_agent import HRAgent
from tech_agent import TechAgent

def classify_query(query: str) -> str:
    hr_keywords = ["salary", "leave", "vacation", "payroll"]
    if any(word in query.lower() for word in hr_keywords):
        return "hr"
    return "tech"

def orchestrator(query: str) -> str:
    classification = classify_query(query)
    if classification == "hr":
        agent = HRAgent()
        return agent.hr_agent_response(query)
    agent = TechAgent()
    return agent.tech_agent_response(query)

if __name__ == "__main__":
    user_query = input("Enter your query: ")
    response = orchestrator(user_query)
    print(response)
