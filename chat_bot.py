import json

def chatbot():
    with open("knowledgebase.json", "r") as file:
        knowledgebase = json.load(file)

    print("Chatbot: Welcome to the Java Learning Chatbot!")
    main_menu(knowledgebase)

def main_menu(knowledgebase):
    while True:
        print("\nMain Menu:")
        for key, value in knowledgebase["main_menu"].items():
            print(f"{key}. {value}")

        try:
            choice = int(input("\nChoose an option (1-4): "))
        except ValueError:
            print("Chatbot: Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            submenu("introduction_to_java", knowledgebase)
        elif choice == 2:
            submenu("loops_in_java", knowledgebase)
        elif choice == 3:
            submenu("oop_concepts", knowledgebase)
        elif choice == 4:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Invalid choice. Please try again.")

def submenu(topic, knowledgebase):
    while True:
        print(f"\n{topic.replace('_', ' ').title()}:")
        for key, value in knowledgebase[topic].items():
            print(f"{key}. {value}")

        choice = input("\nChoose an option: ").strip()
        if choice in knowledgebase[topic]:
            sub_option = knowledgebase[topic][choice]
            if sub_option == "Back to Main Menu":
                return
            elif sub_option in knowledgebase["answers"]:
                print(f"\nChatbot: {knowledgebase['answers'][sub_option]}")
            else:
                print("Chatbot: No answer available for this choice.")
        else:
            print("Chatbot: Invalid choice. Please try again.")

if __name__ == "__main__":
    chatbot()
