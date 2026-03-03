GenAI Engineer Roadmap – Day 1 Documentation
Objective
Understand foundational LLM concepts and build a controllable local chatbot using Ollama. Learn how system messages and temperature influence model behavior.
________________________________________
1. Core LLM Concepts
1.1 Tokens
•	A token is a chunk of text (word, subword, or character).
•	Models process and generate text token by token.
•	Every model has a maximum context window (token limit).
•	The context window includes:
o	System message
o	User input
o	Conversation history
o	Model output
•	API pricing (in hosted models) is based on input + output tokens.
•	More tokens = higher cost and longer response time.
________________________________________
1.2 Temperature
•	Temperature controls randomness in token selection.
•	The model assigns probabilities to possible next tokens.
•	Low temperature (0.0–0.3):
o	High-probability tokens dominate.
o	More deterministic and stable output.
o	Suitable for SQL, JSON, structured answers.
•	High temperature (0.8–1.2):
o	Flattens probability distribution.
o	Lower-probability tokens become more likely.
o	More creative, expressive, and variable output.
o	Higher chance of drift or irrelevant expansion.
Key Insight:
Temperature does not increase intelligence. It increases variability.
________________________________________
1.3 top_p (Nucleus Sampling)
•	Limits token selection to a subset of tokens whose cumulative probability reaches threshold p.
•	Trims unlikely tokens.
•	Temperature reshapes distribution.
•	top_p restricts selection pool.
•	Usually only one is tuned aggressively.
________________________________________
1.4 System Message
•	Defines behavior, tone, and constraints of the model.
•	Has higher priority than user instructions.
•	Acts as a behavioral controller.
•	Biases how the model interprets user prompts.
Example roles tested:
•	Friendly mentor
•	Strict interviewer
•	Sarcastic senior engineer
•	Kindergarten teacher
Observation:
Changing system role changes tone and structure significantly.
________________________________________
2. Virtual Environment (venv)
Purpose
Isolate project dependencies.
Why needed:
•	Prevent version conflicts.
•	Ensure reproducibility.
•	Maintain deployment reliability.
Each project:
•	Has its own packages.
•	Uses its own versions.
•	Does not interfere with system Python.
Professional standard practice.
________________________________________
3. Local LLM Setup (Free Mode)
Tool used: Ollama
Model: llama3
Hardware:
•	Intel i5 CPU
•	16GB RAM
•	No GPU acceleration
Observations:
•	First run slower (cold start).
•	Subsequent runs faster (model loaded in memory).
•	Longer responses increase inference time.
________________________________________
4. Chatbot Implementation
Features implemented:
•	System role control
•	User input loop
•	Temperature control
•	Response time measurement
Structure:
•	While loop for continuous chat
•	Role-based message injection
•	Temperature passed via options
•	Response time calculated using time module
________________________________________
5. Controlled Experiments
Same user input tested under:
•	Different system roles
•	Different temperature values
Experiment 1: Role Steering
System: Strict Interviewer
Result: Maintained interview tone even when user tried to shift context.
System: Kindergarten Teacher
Result: Switched to simplified, friendly explanations.
Conclusion:
System message strongly biases model behavior.
________________________________________
Experiment 2: Temperature Comparison
Temp = 0.2:
•	More stable
•	Less creative branching
•	More focused
•	Shorter responses
Temp = 1.0:
•	More expressive
•	Added imaginative details
•	Drifted slightly from strict role constraints
•	Longer responses
•	Higher response time
Conclusion:
Higher temperature increases variance and potential context drift.
________________________________________
6. Production Insights Learned
•	Low temperature preferred for enterprise systems.
•	High temperature increases hallucination risk.
•	More tokens increase inference time.
•	CPU inference is slower than GPU.
•	System role design is critical in enterprise AI systems.
________________________________________
7. Key Engineering Takeaways
•	LLMs generate text probabilistically.
•	Temperature modifies sampling variance.
•	System message shapes behavioral bias.
•	Token management affects performance and cost.
•	Controlled experiments are essential to understanding model behavior.
________________________________________
End of Day 1
Status: Foundation Built – Steering + Sampling Understood

