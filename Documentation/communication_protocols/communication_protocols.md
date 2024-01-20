<details>

<summary>Contract Net</summary>

**Purpose** : Contract Net is a specific communication protocol used among agents to allocate tasks efficiently. It is designed for scenarios where a task needs to be distributed among multiple agents, and these agents can bid for and undertake the task.

Contract Net is a specific protocol that utilizes FIPA ACL performatives for efficient task allocation in MAS. So Contract Net is a way agents can use FIPA ACL performatives.

[This is a simplified example of a scenario where multiple agents can bid for a printing task.](./example1.py)

Contract Net can develop into scenarios where we've to consider handling **timeouts**, **managing multiple tasks concurrently**, and **ensuring robust communication** in a **distributed environment**.

</details>

<hl>

<details>

<summary>FIPA ACL Performatives</summary>

**Purpose** : FIPA ACL defines a set of communication acts or performatives that agents can use to communicate with each other in a standardized way. It provides a common language for agents to exchange messages and perform various communication acts.

**Communication acts** : Performatives such as *request*, *inform*, *propose*, *confirm*, *agree*, *refuse*. 

**F**oundation for **I**ntelligent **P**hysical **A**gents : **A**gent **C**ommunication **L**anguages performatives are **communication acts** or messages used in multi-agent systems to facilitate interaction between agents.

What do we mean by a communication act? Well, each **performative** is or represents a specific *type of communication* that an agent can take.

There's 4 common **Types of communication**:

1. **cfp** : call for proposals.

     > An agent uses this performative to announce that it is seeking proposals from other agents for a particular task or action. Essentially, it's an invitation for other agents to make proposals.

2. **propose / refuse** : inform to make or not a proposal.

     > After receiving a call for proposals (cfp), an agent can respond with a **propose performative,** indicating its *willingness* to undertake the task. Conversely, the agent can respond with a **refusal performative** if it chooses to *refuse / not* to make a proposal.

3. **accept / reject** : inform to accept or not the task.

     > Once proposals are received, the agent issuing the cfp can respond with an **accept performative** to indicate acceptance of a proposal or a **reject performative** to decline a proposal.

4. **inform / failure** : inform the state of the task or its failure.

     > After the task has been allocated, an agent can use the **inform performative** to communicate the successful completion of the task. Alternatively, if the task cannot be completed, the agent can use the failure performative to inform about the failure.

</details>

<details>

<summary>Result Sharing</summary>

How do agents share their results from each task?

- Each agent has different progress.
- There's some task that depend on other task
- It might be the case that various agent depend from each other.

</details>