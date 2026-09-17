# 📌 Project Summary

**NOVA** is a Python-based rule-based chatbot with a Streamlit web
interface.

The project demonstrates how predefined rules and keyword
matching can be used to create a simple conversational system.

The chatbot receives user input, processes the text, checks it
against predefined conditions, and returns the appropriate
response.

If no rule matches the input, NOVA uses a fallback response.

---

# 👩‍💻 Author

**Harshitha L**

**Internship Project — Rule-BasedChatbot**

---

# 📜 License

This project was created for educational and internship purposes.



# 🤖 NOVA — Rule-Based Chatbot

A beginner-friendly **rule-based chatbot built with Python and Streamlit**.

NOVA responds to user messages using predefined keywords and
`if / elif / else` decision-making logic. The project demonstrates
how a simple chatbot can understand common user inputs without using
machine learning or an external AI API.

---

## 📌 Internship Task 1

### Task

Build a simple chatbot that responds to user input using predefined
rules or keywords.

### Requirements

- Handle common greetings.
- Answer simple questions.
- Provide a fallback response for unknown input.
- Use Python with basic `if-else` or pattern-matching logic.
- Add comments explaining how the chatbot decides its responses.

### Requirement Status

| Requirement | Status |
|---|---|
| Predefined rules/keywords | ✅ Completed |
| Common greetings | ✅ Completed |
| Simple questions | ✅ Completed |
| Fallback for unknown input | ✅ Completed |
| Python implementation | ✅ Completed |
| If/elif/else logic | ✅ Completed |
| Comments explaining decision logic | ✅ Completed |
| Streamlit web interface | ✅ Added |
| Chat history | ✅ Added |
| Clear conversation option | ✅ Added |

---


### 👋 Greeting Detection

NOVA recognizes common greetings such as:

- `hello`
- `hi`
- `hey`
- `good morning`
- `good afternoon`
- `good evening`

Example:

```text
You: hello

NOVA: 👋 Hello! I'm NOVA. It's nice to meet you!
🤖 Identity Questions
Users can ask NOVA about its identity.

Example:

You: Who are you?

NOVA: 🤖 I'm NOVA, a rule-based chatbot created with Python!
💡 Feature Information
NOVA can explain what it is capable of doing.

Example:

You: What can you do?

NOVA: 💡 I can respond to greetings, answer simple questions,
tell you the current time and date, provide help, and handle
basic conversation.
😊 Simple Conversation
NOVA can respond to basic conversational messages such as:

You: How are you?

NOVA: 😊 I'm doing great! Thanks for asking.
🕐 Current Time
NOVA uses Python's datetime module to display the current time.

Example:

You: What time is it?

NOVA: 🕐 The current time is 12:30 PM.
📅 Current Date
NOVA can also provide the current date.

Example:

You: What is today's date?

NOVA: 📅 Today is Thursday, 17 September 2026.
📚 Help Command
Users can type:

help
NOVA displays the commands and questions it understands.

🙏 Thank-You Detection
NOVA recognizes simple positive feedback.

Example:

You: Thank you

NOVA: 😊 You're very welcome!
🤔 Fallback Response
If NOVA does not recognize the user's input, it provides a
fallback response instead of crashing.

Example:

You: Tell me about quantum computing.

NOVA: 🤔 I'm not sure how to respond to that yet.

Try "help" to see what I understand.
This demonstrates how the chatbot handles unknown input.

## 🧠 How NOVA Decides Its Responses
NOVA uses a rule-based decision-making system.

The process is:

                 User Input
                     │
                     ▼
              Normalize Input
             lowercase + strip
                     │
                     ▼
              Check Rule 1
                     │
                     ▼
              Check Rule 2
                     │
                     ▼
              Check Rule 3
                     │
                    ...
                     │
                     ▼
             Matching Rule?
               /         \
             YES          NO
              │            │
              ▼            ▼
       Return Defined    Fallback
          Response       Response
The chatbot checks predefined conditions from top to bottom.

For example:

if text in ["hi", "hello", "hey"]:
    return "Hello! I'm NOVA."

elif "time" in text:
    return "The current time is..."

else:
    return "I'm not sure how to respond..."
The else condition acts as the fallback rule.

###🔍 Rule-Based Logic
The chatbot uses two main types of matching.

1. Exact Matching
Some inputs are checked against a list of predefined phrases.

Example:

if text in ["hi", "hello", "hey"]:
This handles common greetings.

2. Keyword Matching
Some rules search for keywords inside the user's message.

Example:

elif "time" in text:
This allows NOVA to respond to messages such as:

What time is it?
Can you tell me the time?
What is the current time?
3. Keyword List Matching
The any() function is also used for simple keyword detection.

Example:

elif any(word in text for word in ["thank", "thanks"]):
This allows NOVA to recognize different ways of expressing thanks.

## 🛠️ Technologies Used
- Technology	Purpose
- Python	Core programming language
- Streamlit	Web-based user interface
- datetime	Current date and time
- If/Elif/Else	Rule-based decision making
- Keyword Matching	Detecting user intent
- Session State	Maintaining chat history


## 📁 Project Structure
NOVA-Rule-Based-Chatbot/
│
├── app.py
├── requirements.txt
└── README.md
app.py
Contains:

Streamlit interface

Chat functionality

Predefined chatbot rules

Keyword matching

Date/time functionality

Fallback handling

Comments explaining the decision process

requirements.txt
Contains the Python dependency required to run the application.

README.md
Contains the project documentation, requirements, features,
technology details, and usage instructions.

## ⚙️ Installation
Step 1: Clone or Download the Project


Open the project folder in VS Code.
Windows : python -m venv venv
 Activate it: venv\Scripts\activate
Step 2: Install Dependencies
Open the VS Code terminal and run:

python -m pip install -r requirements.txt
Step 3: Run the Streamlit Application
Run: python -m streamlit run app.py
The application will start locally.

You should see a message similar to:

You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Open the displayed local URL in your browser.

💬 Example Conversations
Example 1 — Greeting
You: Hi

NOVA: 👋 Hello! I'm NOVA. It's nice to meet you!
Example 2 — Identity
You: What is your name?

NOVA: 🤖 I'm NOVA, a rule-based chatbot created with Python!
Example 3 — Time
You: What time is it?

NOVA: 🕐 The current time is 12:30 PM.
Example 4 — Date
You: What is today's date?

NOVA: 📅 Today is Thursday, 17 September 2026.
Example 5 — Help
You: Help

NOVA: 📚 Here are some things you can ask me...
Example 6 — Unknown Input
You: Explain artificial intelligence.

NOVA: 🤔 I'm not sure how to respond to that yet.
🎨 Streamlit Interface
The project uses Streamlit to provide a simple web-based chatbot
interface instead of a traditional command-line interface.

The interface includes:

🤖 NOVA branding

💬 Chat message interface

🧠 Rule explanation sidebar

📋 Available commands

⚙️ Technology information

🗑️ Clear conversation button

💡 Fallback responses

🧪 Testing
The chatbot can be tested using the following inputs:


🔒 No External AI API
NOVA is intentionally implemented as a rule-based chatbot.

It does not require:

❌ OpenAI API

❌ Gemini API

❌ Machine learning model

❌ External chatbot API

❌ Internet connection for chatbot responses

The chatbot's responses are generated from predefined rules
written in Python.

🎯 Learning Objectives
This project demonstrates the following programming concepts:

Python functions

Conditional statements

if / elif / else

Lists

String manipulation

Keyword matching

any() function

Exception handling

Date and time handling

Streamlit

Session state

User interface design

Basic chatbot architecture

### 🚀 Future Improvements
Although the current project is intentionally rule-based, it could
be extended in the future with:

More predefined conversation rules

More keyword categories

Sentiment detection

Multiple languages

Database-backed conversation history
