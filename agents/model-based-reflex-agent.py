class ModelBasedReflexAgent:
    def __init__(self):
        self.state={
            "A":"Dirty",
            "B":"Dirty"
        }
    def perceive(self,location,status):
        self.state[location]=status

    def act(self,location):
        if self.state[location]=="Dirty":
            return "Clean"
        else:
            return "Move to other room"


agent=ModelBasedReflexAgent() 
agent.perceive("Room 304","Dirty")
print("Room 304 Action:",agent.act("Room 304"))
               
agent.perceive("Room 301","Clean")
print("Room 301 Action:",agent.act("Room 301"))

agent.perceive("Room 401","Dirty")
print("Room 401 Action:",agent.act("Room 401"))

agent.perceive("Room 402","Clean")
print("Room 402 Action:",agent.act("Room 402"))

agent.perceive("Room 201","Dirty")
print("Room 201 Action:",agent.act("Room 201"))

agent.perceive("Room 202","Dirty")
print("Room 202 Action:",agent.act("Room 202"))