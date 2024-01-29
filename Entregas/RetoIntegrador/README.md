# Reto

<details>
<summary>Two-way communication</summary>
<br>

**Purpose**: Create an agent simulation where two agents communicate with each other to perform a task.

**Part A**. 

- Create a simulation that has 2 agents in it.
     - One Agent is the **Driver**
     - The other Agent is the **Vehicle**
- These agents must be using a BDI or a Logic-based architecture
- They must perform this tasks:
     - Go from space A to B and then from B to A.
     - The path from A to B must be at least 5 spaces long.
     - The path must have at least 3 turns.
- Rules:
     - 1. Agent Vehicle is the only one that can have "move" actions.
     - 2. Agent Driver is the only one making decisions of the next Vehicle Agent's action.
     - 3. Agent Driver must "see" the environment and lead Agent Vehicle each step.
          - This means that the Agent Vehicle has limited "see" function.
     - 4. You can assume that the Agent Driver is always at the same position of the Agent Vehicle.
- Messaging:
     - You can use either [FIPA ACL](http://www.fipa.org/specs/fipa00061/SC00061G.html) or KQML for the messaging language.
     - You must use "inform" and "request" [performatives](https://jmvidal.cse.sc.edu/talks/agentcommunication/performatives.html), [2](http://www.fipa.org/specs/fipa00037/SC00037J.html), [FIPA Semantic Language](http://www.fipa.org/specs/fipa00008/SC00008I.html).
     - Each time the Agent Vehicle executes an action (after a request from Agent Driver), it must reply back to inform that it has finished executing the action.
     - Remember that messages are also actions.
     - Message contents must have classes from the Ontology.
- Ontologies
     - Use either OWL or KIF.
     - The Ontologies of both Agents can be the same one.
     - At least it has to be in the form of an informal hierarchy.
     - You must use an ontology in an informal hierarchy form (at least) ——that is, an ontology with a super/sub class structure—— for the belief system.
- Basically you have the driver that is driving inside a vehicle, and it wants to go from A to B and return to A, using "voice commands".
- A graphical interface is not necessary.
     - But still, at least give some information each step of what are the positions of the agents.

**Part B**. 

</details>