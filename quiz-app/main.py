import streamlit as st
import random
import time

# Custom CSS for better UI
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }stButton>button:hover {
        background-color: #45a049;
    }
    .stSuccess {
        font-size: 20px;
        color: green;
    }
    .stError {
        font-size: 20px;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 TypeScript Quiz App")

questions = [
    {
        "question": "What is TypeScript?",
        "options": ["A. A superset of JavaScript", "B. A subset of JavaScript", "C. A new programming language", "D. A framework for building web applications"],
        "correct_answer": "A. A superset of JavaScript"
    },
    {
        "question": "What is the purpose of the interface keyword in TypeScript?",
        "options": ["A. To define a new class", "B. To define a new function", "C. To define the shape of an object", "D. To define a new variable"],
        "correct_answer": "C. To define the shape of an object"
    },
    {
        "question": "Which of the following is a valid TypeScript type?",
        "options": ["A. number", "B. string", "C. boolean", "D. All of the above"],
        "correct_answer": "D. All of the above"
    },
    {
        "question": "What does the readonly keyword do in TypeScript?",
        "options": ["A. Makes a variable immutable", "B. Makes a variable optional", "C. Makes a variable private", "D. Makes a variable public"],
        "correct_answer": "A. Makes a variable immutable"
    },
    {
        "question": "What is the purpose of the enum keyword in TypeScript?",
        "options": ["A. To define a set of named constants", "B. To define a new class", "C. To define a new function", "D. To define a new variable"],
        "correct_answer": "A. To define a set of named constants"
    },
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question
st.subheader(question["question"])
selected_option = st.selectbox("Choose your answer", question["options"], key="selectbox")

if st.button("Submit Answer"):
    if selected_option == question["correct_answer"]:
        st.success("Correct!")
    else:
        st.error(f"Incorrect! The correct answer is {question['correct_answer']}")

    time.sleep(3)
    st.session_state.current_question = random.choice(questions)
    st.rerun()