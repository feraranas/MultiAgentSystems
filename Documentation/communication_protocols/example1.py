class Agent:
     def __init__(self, name):
          self.name = name

     # 1. Call For Proposals (cfp):
     #     Concept: The initiation of a task by an agent, broadcasting a request 
     #     for proposals from other agents in the system.
     def send_cfp(self, task):
          ''' Broadcasting cfp to other agents in the system '''
          print(f"{self.name} sends a Call For Proposals (cfp) for task: {task}")
          

     # 2. Proposal Submission:
     #     Concept: Interested agents respond to the cfp by submitting proposals 
     #     with their bids.
     def receive_proposal(self, sender, bid):
          print(f"{self.name} receives a proposal from {sender} with bid: {bid}")


     # 3. Bid Evaluation:
     #    Concept: The agent issuing the cfp evaluates the received proposals based
     #    on criteria such as cost, resources, or any other relevant factors.
     #         > Evaluate the bid and store it for decision making


     # 4. Acceptance and Rejection:
     #     Concept: The agent issuing the cfp decides which proposal to accept and 
     #     which ones to reject.
     def send_acceptance(self, selected_agent):
          ''' Notifies the selected agent that it has been chosen for the task '''
          
          print(f"{self.name} sends acceptance to {selected_agent}")

     def send_rejection(self, rejected_agent):
          ''' Notifies the rejected agent that its bid was not accepted '''
          print(f"{self.name} sends rejection to {rejected_agent}")

     # 5. Task Allocation:
     #    Concept: The agent issuing the cfp allocates the task to the selected
     #    aegnt, and the selected agent proceeds to perform the task.
          
     # 6. Communication between agents:
     #    Concept: Agents need to communicate effectively.


agent1 = Agent("Agent1")
agent2 = Agent("Agent2")
agent3 = Agent("Agent3")

# Agent 1 initiates a task by sending a Call For Proposals (cfp)
agent1.send_cfp("Print 100 copies, return the cost.")

# Agents 2 and 3 submit their proposals with bids
agent2.receive_proposal("Agent1", 50)
agent3.receive_proposal("Agent1", 40)

# Agent 1 evaluates the bids and selects the agent with the lowest bid (Agent 3)
selected_agent = "Agent3"

# Agent 1 sends acceptance to the selected agent -> Agent 3
agent1.send_acceptance(selected_agent)

# Agents 2 receive the reject decision
agent1.send_rejection(agent1.name)