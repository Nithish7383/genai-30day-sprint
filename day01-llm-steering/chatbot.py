import ollama
import time


def chat(system_role, temperature):
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Exiting chat...")
            break

        start_time = time.time()

        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": user_input}
            ],
            options={
                "temperature": temperature
            }
        )

        end_time = time.time()

        print("\nAssistant:", response["message"]["content"])
        print(f"\nResponse time: {round(end_time - start_time, 2)} seconds")
        print("-" * 50)


if __name__ == "__main__":
    system_prompt = "You are a strict technical interviewer. Give short answers and ask follow-up questions."
    
    temp = float(input("Enter temperature (0.0 - 1.5): "))
    
    chat(system_prompt, temp)