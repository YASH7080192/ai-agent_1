from agent import Agent

def main():
    print("="*60)
    print("AI AGENT")
    print("="*60)
    print("type 'exit' to quit.")
    print()

    agent = Agent()

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            break

        try:
            response = agent.run(user_input)
            print(f"\nAgent: {response}\n")
        except Exception as e:
            print(f"\nError: {e}\n")

if __name__ == "__main__":
    main()  