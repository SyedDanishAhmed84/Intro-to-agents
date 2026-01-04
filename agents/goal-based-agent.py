class GoalBasedAgent:
    def __init__(self):
        self.state={}
        self.goal="Clean"

    def perceive(self,location,status):
        self.state[location]=status

    def act(self,location):
        if self.state[location]!=self.goal:
            self.state[location]="Clean"
            return f"Cleaning {location}"
        else:
             return f"{location} already clean, move to next room"

agent=GoalBasedAgent()

agent.perceive("Room 304","Dirty")
print(agent.act("Room 304"))

agent.perceive("Room 301","Clean")
print(agent.act("Room 301"))

agent.perceive("Room 401","Dirty")
print(agent.act("Room 401"))

agent.perceive("Room 402","Clean")
print(agent.act("Room 402"))

agent.perceive("Room 202","Clean")
print(agent.act("Room 202"))

agent.perceive("Room 201","Dirty")
print(agent.act("Room 201"))