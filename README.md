# Java Learning Chatbot

A simple console-based chatbot that helps users learn the basics of Java by navigating through different topics and subtopics. The chatbot provides predefined answers from a JSON-based knowledge base.

## Features
- Console-based chatbot interface.
- Menu-driven navigation system.
- Topics include Introduction to Java, Loops, and OOP Concepts.
- Retrieves predefined answers from a JSON file.
- Allows users to return to the main menu or exit anytime.

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x

### Steps to Run the Chatbot
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/chatbot-repo.git
   cd chatbot-repo
   ```
2. Ensure you have a `knowledge_base.json` file in the project directory.
3. Run the chatbot script:
   ```sh
   python chatbot.py
   ```

## Usage
- Run the script and follow the on-screen menu options.
- Select a topic by entering the corresponding number.
- Choose a subtopic to get more details.
- Type the number for "Back to Main Menu" to return.
- Select the exit option to quit the chatbot.

## Project Structure
```
chatbot-repo/
│── chatbot.py         # Main chatbot script
│── knowledge_base.json # Knowledge base file
│── README.md          # Project documentation
```

## Example Interaction
```
Chatbot: Welcome to the Java Learning Chatbot!

Main Menu
1. Introduction to Java
2. Loops in Java
3. OOP Concepts
4. Exit

Choose an option (1-4): 1

Introduction to Java:
1. What is Java?
2. Features of Java
3. Back to Main Menu

Choose an option: 1

Chatbot: Java is a high-level, object-oriented programming language developed by Sun Microsystems.
```

## Future Enhancements
- Implement Natural Language Processing (NLP) for user queries.
- Add more topics and subtopics.
- Create a GUI-based chatbot interface.
- Extend support for other programming languages.

## Contributing
Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

## License
This project is open-source and available under the MIT License.

---
Feel free to update this README with your repository details. Happy coding! 🚀

