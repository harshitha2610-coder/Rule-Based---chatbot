"""
============================================================
NOVA — Rule-Based Chatbot
============================================================

Internship Task 1

Requirements Covered:
1. Responds to user input using predefined rules/keywords.
2. Handles common greetings.
3. Answers simple questions.
4. Provides help information.
5. Uses Python if/elif rule-based logic.
6. Provides a fallback response for unknown input.
7. Includes comments explaining how the chatbot decides
   which response to return.
8. Uses Streamlit to provide an attractive web interface.

IMPORTANT:
NOVA is a rule-based chatbot.
It does NOT use machine learning or an external AI API.

Author: Your Name
============================================================
"""

import streamlit as st
from datetime import datetime


# ============================================================
# PAGE CONFIGURATION
# ============================================================

# Configure the browser tab and overall page layout.
st.set_page_config(
    page_title="NOVA - Rule-Based Chatbot",
    page_icon="🤖",
    layout="centered"
)


# ============================================================
# CUSTOM CSS
# ============================================================

# Custom CSS makes the basic Streamlit application look
# more like a professional chatbot application.
st.markdown(
    """
    <style>

    /* Main application background */
    .stApp {
        background: linear-gradient(135deg, #eef2ff, #f8fafc);
    }

    /* Main title */
    .nova-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .nova-subtitle {
        text-align: center;
        color: #64748b;
        font-size: 17px;
        margin-bottom: 25px;
    }

    /* Information card */
    .info-card {
        padding: 18px;
        border-radius: 15px;
        background-color: white;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }

    /* Rule explanation box */
    .rule-box {
        padding: 15px;
        border-radius: 12px;
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        margin-top: 10px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 13px;
        margin-top: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HOW NOVA DECIDES ITS RESPONSES
# ============================================================

"""
NOVA uses a simple rule-based decision system.

The decision process works as follows:

1. The user enters a message.

2. The message is converted to lowercase using lower().
   This means:
       "HELLO"
       "Hello"
       "hello"
   are treated as the same input.

3. Extra spaces are removed using strip().

4. NOVA checks the message against predefined rules
   from top to bottom using if / elif statements.

5. If a condition matches, NOVA immediately returns the
   response associated with that rule.

6. Some rules check exact phrases, while other rules
   search for keywords inside the user's message.

7. If no predefined rule matches the user's input,
   the ELSE statement provides a fallback response.

Example:

    User: "hello"

    ↓

    Convert to lowercase

    ↓

    Check Rule 1
    Check Rule 2
    Check Rule 3 → MATCH!

    ↓

    Return greeting response

This is why NOVA is called a RULE-BASED CHATBOT.

No machine learning model is required.
No external API is required.
"""


# ============================================================
# CHATBOT RESPONSE FUNCTION
# ============================================================

def get_response(user_input):
    """
    Decide NOVA's response using predefined rules.

    The function checks the user's input against a series
    of if/elif conditions.

    Each condition represents one predefined chatbot rule.
    """

    # --------------------------------------------------------
    # STEP 1: NORMALIZE USER INPUT
    # --------------------------------------------------------

    # Convert input to lowercase and remove unnecessary spaces.
    # This allows different capitalization to work correctly.
    text = user_input.lower().strip()


    # --------------------------------------------------------
    # RULE 1: EMPTY INPUT
    # --------------------------------------------------------

    # If the user submits an empty message, ask them to
    # enter something instead of trying to process nothing.
    if not text:
        return (
            "⚠️ I didn't receive any message. "
            "Try typing something!"
        )


    # --------------------------------------------------------
    # RULE 2: GOODBYE / EXIT
    # --------------------------------------------------------

    # Exact matching is used for common exit commands.
    elif text in ["bye", "goodbye", "exit", "quit"]:
        return (
            "👋 Goodbye! Thanks for chatting with NOVA. "
            "Have a great day!"
        )


    # --------------------------------------------------------
    # RULE 3: GREETINGS
    # --------------------------------------------------------

    # Check whether the user's complete message matches
    # one of the predefined greeting phrases.
    elif text in [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]:
        return (
            "👋 Hello! I'm NOVA. "
            "It's nice to meet you!"
        )


    # --------------------------------------------------------
    # RULE 4: ASK NOVA'S NAME
    # --------------------------------------------------------

    # Keyword matching is used here.
    # If the message contains "your name" or "who are you",
    # NOVA identifies itself.
    elif "your name" in text or "who are you" in text:
        return (
            "🤖 I'm NOVA, a rule-based chatbot "
            "created with Python!"
        )


    # --------------------------------------------------------
    # RULE 5: ASK WHAT NOVA CAN DO
    # --------------------------------------------------------

    # NOVA searches for predefined phrases related to
    # its capabilities.
    elif (
        "what can you do" in text
        or "your features" in text
        or "what do you do" in text
    ):
        return (
            "💡 I can respond to greetings, answer simple "
            "questions, tell you the current time and date, "
            "provide help, and handle basic conversation."
        )


    # --------------------------------------------------------
    # RULE 6: ASK HOW NOVA IS DOING
    # --------------------------------------------------------

    # If the phrase "how are you" appears in the message,
    # NOVA returns a predefined friendly response.
    elif "how are you" in text:
        return (
            "😊 I'm doing great! Thanks for asking."
        )


    # --------------------------------------------------------
    # RULE 7: HELP
    # --------------------------------------------------------

    # The chatbot provides information about the commands
    # it understands.
    elif "help" in text:
        return (
            "📚 Here are some things you can ask me:\n\n"
            "👋 Say **hello**, **hi**, or **hey**\n\n"
            "🤖 Ask **what is your name?**\n\n"
            "💡 Ask **what can you do?**\n\n"
            "😊 Ask **how are you?**\n\n"
            "🕐 Ask **what time is it?**\n\n"
            "📅 Ask **what is today's date?**\n\n"
            "🙏 Say **thank you**\n\n"
            "🚪 Type **bye** to end the conversation."
        )


    # --------------------------------------------------------
    # RULE 8: CURRENT TIME
    # --------------------------------------------------------

    # If the keyword "time" appears, Python's datetime
    # module is used to obtain the current system time.
    elif "time" in text:
        current_time = datetime.now().strftime("%I:%M %p")

        return (
            f"🕐 The current time is **{current_time}**."
        )


    # --------------------------------------------------------
    # RULE 9: CURRENT DATE
    # --------------------------------------------------------

    # If the user asks about the date or today,
    # Python obtains the current date dynamically.
    elif "date" in text or "today" in text:
        current_date = datetime.now().strftime(
            "%A, %d %B %Y"
        )

        return (
            f"📅 Today is **{current_date}**."
        )


    # --------------------------------------------------------
    # RULE 10: THANK YOU / POSITIVE FEEDBACK
    # --------------------------------------------------------

    # any() checks whether at least one predefined keyword
    # appears in the user's message.
    elif any(
        word in text
        for word in ["thank", "thanks"]
    ):
        return (
            "😊 You're very welcome!"
        )


    # --------------------------------------------------------
    # RULE 11: POSITIVE CONVERSATION
    # --------------------------------------------------------

    # Handle simple positive words using keyword matching.
    elif any(
        word in text
        for word in ["great", "awesome", "good"]
    ):
        return (
            "✨ That's great to hear!"
        )


    # --------------------------------------------------------
    # FALLBACK RULE
    # --------------------------------------------------------

    # If NONE of the rules above match the user's input,
    # this ELSE block is executed.
    #
    # This is important because it ensures the chatbot
    # always provides a response instead of failing.
    else:
        return (
            "🤔 I'm not sure how to respond to that yet.\n\n"
            "💡 Try typing **help** to see what I understand."
        )


# ============================================================
# SESSION STATE
# ============================================================

# Streamlit reruns the Python script whenever the user
# interacts with the application.
#
# session_state allows us to preserve the conversation
# history between those reruns.

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="nova-title">🤖 NOVA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="nova-subtitle">'
    'Rule-Based Python Chatbot'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# INTRODUCTION CARD
# ============================================================

st.markdown(
    """
    <div class="info-card">

    <h3>💬 Welcome to NOVA!</h3>

    <p>
    I'm a simple chatbot built using
    <b>Python + predefined rules + Streamlit</b>.
    </p>

    <p>
    Ask me about the time, date, my features,
    or simply say hello!
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🧠 How NOVA Works")

    st.write(
        """
        NOVA uses a **rule-based decision system**.

        The user's message passes through predefined
        `if / elif / else` rules.
        """
    )

    st.divider()

    st.subheader("📋 Available Rules")

    st.write("👋 Greetings")
    st.write("🤖 Name / Identity")
    st.write("💡 Features")
    st.write("😊 How are you")
    st.write("🕐 Current time")
    st.write("📅 Current date")
    st.write("📚 Help")
    st.write("🙏 Thank you")
    st.write("✨ Positive messages")
    st.write("🤔 Unknown input → Fallback")

    st.divider()

    st.subheader("⚙️ Technology")

    st.write("🐍 Python")
    st.write("🎨 Streamlit")
    st.write("📅 Datetime")
    st.write("🧠 Rule-Based Logic")

    st.divider()

    st.info(
        "NOVA does not use machine learning. "
        "Responses are selected using predefined rules."
    )

    # Button to clear the complete conversation.
    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()


# ============================================================
# DISPLAY PREVIOUS CHAT MESSAGES
# ============================================================

# Every message stored in session_state is displayed again
# whenever Streamlit reruns the application.

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "Type your message here..."
)


# ============================================================
# PROCESS USER MESSAGE
# ============================================================

if user_input:

    # --------------------------------------------------------
    # STORE USER MESSAGE
    # --------------------------------------------------------

    # Save the user's message in Streamlit session state
    # so it remains visible after the application reruns.
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    # Display the user's message immediately.
    with st.chat_message("user"):
        st.markdown(user_input)


    # --------------------------------------------------------
    # GENERATE CHATBOT RESPONSE
    # --------------------------------------------------------

    # Send the user's message to our rule-based function.
    response = get_response(user_input)


    # --------------------------------------------------------
    # STORE NOVA'S RESPONSE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


    # Display NOVA's response.
    with st.chat_message("assistant"):
        st.markdown(response)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🤖 NOVA — Rule-Based Chatbot |
        Built with Python & Streamlit
        <br>
        Internship Task 1
    </div>
    """,
    unsafe_allow_html=True
)