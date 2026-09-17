# 🤖 Rule-Based AI Chatbot

A simple **rule-based chatbot built with Python** that responds to user messages using predefined keywords, patterns, and conditional logic.

The chatbot identifies common words or phrases in the user's input and provides an appropriate predefined response. When it cannot recognize the input, it uses a fallback response.

## 🚀 Live Demo

**Streamlit App:**
*https://rule-based---chatbot-by-moharshi.streamlit.app/*

## 📌 Project Overview

This project demonstrates the basic concept of a **rule-based chatbot** using Python.

Instead of using a machine learning model or external AI API, the chatbot uses predefined rules to determine how it should respond.

For example:

```text
User: Hello
Bot: Hello! 👋 How can I help you?

User: How are you?
Bot: I'm doing great! Thanks for asking. 😊

User: What is Python?
Bot: Python is a popular programming language.

User: Who are you?
Bot: I'm a simple rule-based chatbot.

User: Tell me something random
Bot: Sorry, I don't understand that yet.
```

## ✨ Features

* 🤖 Simple chatbot interface
* 💬 Responds to user messages
* 👋 Handles common greetings
* ❓ Handles predefined questions
* 🔑 Uses keyword matching
* 🧠 Uses basic `if-else` logic
* 🔄 Provides fallback responses
* 📝 Comments explain the chatbot's decision-making logic
* 🌐 Can be deployed as a Streamlit web application
* ⚡ Lightweight and easy to understand

## 🧠 How the Chatbot Decides Its Responses

The chatbot follows a simple rule-based decision process.

When the user enters a message:

1. The input is converted to lowercase.
2. The chatbot checks the message for predefined keywords or phrases.
3. If a matching rule is found, the corresponding response is returned.
4. If no rule matches the input, the chatbot provides a fallback response.

### Example

```python
if "hello" in user_input:
    response = "Hello! 👋 How can I help you?"

elif "how are you" in user_input:
    response = "I'm doing great! 😊"

elif "your name" in user_input:
    response = "I'm a rule-based chatbot."

else:
    response = "Sorry, I don't understand that yet."
```

The chatbot does **not** generate new answers using a language model. Its responses come from the predefined rules in the program.

## 🔄 Chatbot Flow

```text
           Start
             │
             ▼
     User enters a message
             │
             ▼
      Convert input to
        lowercase
             │
             ▼
   Check predefined rules
             │
       ┌─────┴─────┐
       │           │
     Match       No Match
       │           │
       ▼           ▼
 Return matching  Return
   response       fallback
       │           │
       └─────┬─────┘
             ▼
      Display response
             │
             ▼
        Continue chat
```

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Conditional Statements**
* **Keyword / Pattern Matching**
* **Git & GitHub**

## 📂 Project Structure

```text
rule-based-chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains:

* Streamlit chatbot interface
* User input handling
* Keyword matching
* Predefined chatbot rules
* Response selection
* Fallback response logic
* Comments explaining how the chatbot makes decisions

### `requirements.txt`

Contains the Python dependency required to run the Streamlit application.

```text
streamlit
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/harshitha2610-coder/Rule-Based---chatbot.git
```

### 2. Navigate to the project directory

```bash
cd rule-based-chatbot
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

The chatbot will open in your browser.

## 🌐 Deployment

The chatbot can be deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Push the project files to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the chatbot repository.
5. Set `app.py` as the main file.
6. Click **Deploy**.
7. Streamlit will provide a public URL for the chatbot.

## 💬 Example Conversations

### Greeting

```text
User: Hi

Bot: Hello! 👋 How can I help you?
```

### Asking about the chatbot

```text
User: What is your name?

Bot: I'm a simple rule-based chatbot.
```

### General Question

```text
User: What is Python?

Bot: Python is a popular programming language.
```

### Unknown Input

```text
User: What is the weather on Mars?

Bot: Sorry, I don't understand that yet.
```

The fallback response ensures that the chatbot can handle inputs that do not match any predefined rule.

## 🔑 Example Rules

The chatbot can be designed with rules such as:

| User Input / Keyword | Chatbot Response                          |
| -------------------- | ----------------------------------------- |
| `hello`              | Hello! 👋 How can I help you?             |
| `hi`                 | Hi there! 😊                              |
| `hey`                | Hey! 👋                                   |
| `how are you`        | I'm doing great!                          |
| `your name`          | I'm a rule-based chatbot.                 |
| `python`             | Python is a popular programming language. |
| `bye`                | Goodbye! Have a great day! 👋             |
| Unknown input        | Sorry, I don't understand that yet.       |

These rules can be expanded by adding additional conditions to the program.

## 🧩 Core Logic

The chatbot primarily uses **if-elif-else** statements.

```text
IF input matches greeting
        ↓
    Greeting response

ELSE IF input matches a known question
        ↓
    Predefined answer

ELSE IF input matches another keyword
        ↓
    Corresponding response

ELSE
        ↓
    Fallback response
```

This makes the chatbot's decision-making process simple, transparent, and easy to understand.

## 🎯 Learning Objectives

This project demonstrates:

* Python fundamentals
* Conditional statements
* String manipulation
* Keyword matching
* Pattern-based decision making
* Function usage
* User input handling
* Basic chatbot design
* Streamlit interface development
* GitHub project management
* Web application deployment

## ⚠️ Limitations

Since this is a rule-based chatbot:

* It only understands predefined keywords and patterns.
* It cannot understand complex natural language like modern AI assistants.
* It does not learn from conversations.
* It does not generate completely new responses.
* Similar questions may need multiple rules to be handled correctly.

For example, if a rule only checks for:

```text
"how are you"
```

then a differently worded question such as:

```text
"How are you doing today?"
```

may require additional pattern handling.

## 🔮 Future Improvements

Possible improvements include:

* Add more predefined rules
* Support more variations of user questions
* Use regular expressions for better pattern matching
* Add conversation history
* Add chatbot personality
* Add typing indicators
* Add timestamps to messages
* Add voice input and output
* Add multilingual support
* Upgrade from rule-based responses to an NLP/LLM-based chatbot
* Add intent classification
* Store frequently asked questions

## 📚 Concepts Demonstrated

This project introduces the fundamental idea behind **rule-based conversational systems**.

The chatbot follows explicit rules rather than learning patterns from a dataset.

```text
User Input
    ↓
Text Processing
    ↓
Keyword / Pattern Matching
    ↓
Rule Selection
    ↓
Predefined Response
    ↓
User
```

This makes the system predictable and easy to debug.

## 📜 License

This project is open-source and available for educational and personal use.

## 👩‍💻 Author

**Harshitha L**

GitHub:
*https://github.com/harshitha2610-coder*

---

⭐ If you found this project useful, consider giving the repository a **star**!
