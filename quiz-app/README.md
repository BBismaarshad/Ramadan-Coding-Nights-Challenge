# 🎯 TypeScript Quiz App

A simple interactive quiz application built with Streamlit to test your TypeScript knowledge. The app presents random TypeScript questions and provides immediate feedback on your answers.

[TypeScript Quiz App ](https://quiz-app-nclwxemdsmzx8fwnzyqotv.streamlit.app/)

## Features

- 🚀 Random TypeScript questions from a curated list
- ✅ Instant feedback on answers
- 🎨 Clean and responsive UI with custom styling
- 🔄 Automatic question refresh after answering

## Technologies Used

- Python 3.x
- Streamlit (for web app framework)
- HTML/CSS (for custom styling)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/BBismaarshad/Ramadan-Coding-Nights-Challenge/tree/master/quiz-app
   ```
   ```
   cd quiz-app
   ```
## Install the required dependencies:
```
pip install streamlit
```
## Run the application:
```
streamlit run main.py
```
## Usage
1. The app will open in your default browser

2. Read the displayed TypeScript question

3. Select your answer from the dropdown

4. Click "Submit Answer" to check your response

5. The app will show if your answer was correct or not

6. After 3 seconds, a new random question will appear

## Customization
You can easily customize the quiz by modifying the questions list in the app.py file. Each question should follow this format:

```
{
    "question": "Your question here",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "correct_answer": "Correct option"
}
```
