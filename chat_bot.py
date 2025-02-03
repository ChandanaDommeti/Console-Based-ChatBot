import json

def chatbot():
    with open("knowledge_base.json", "r") as file:
        knowledge_base = json.load(file)

    print("Chatbot: Welcome to the Java Learning Chatbot!")
    main_menu(knowledge_base)

def main_menu(knowledge_base):
    while True:
        print("\nMain Menu:")
        for key, value in knowledge_base["main_menu"].items():
            print(f"{key}. {value}")

        try:
            choice = int(input("\nChoose an option (1-4): "))
        except ValueError:
            print("Chatbot: Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            submenu("introduction_to_java", knowledge_base)
        elif choice == 2:
            submenu("loops_in_java", knowledge_base)
        elif choice == 3:
            submenu("oop_concepts", knowledge_base)
        elif choice == 4:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Invalid choice. Please try again.")

def submenu(topic, knowledge_base):
    while True:
        print(f"\n{topic.replace('_', ' ').title()}:")
        for key, value in knowledge_base[topic].items():
            print(f"{key}. {value}")

        choice = input("\nChoose an option: ").strip()
        if choice in knowledge_base[topic]:
            sub_option = knowledge_base[topic][choice]
            if sub_option == "Back to Main Menu":
                return
            elif sub_option in knowledge_base["answers"]:
                print(f"\nChatbot: {knowledge_base['answers'][sub_option]}")
            else:
                print("Chatbot: No answer available for this choice.")
        else:
            print("Chatbot: Invalid choice. Please try again.")

if __name__ == "__main__":
    chatbot()
