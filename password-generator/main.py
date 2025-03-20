import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

# Function to check password strength
def check_password_strength(password):
    strength = 0
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1
    if len(password) >= 12:
        strength += 1
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        strength += 1
    return strength

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stSlider div {
        color: #4CAF50;
    }
    .stCheckbox label {
        color: #4CAF50;
        font-weight: bold;
    }
    .stMarkdown h1 {
        color: #4CAF50;
        text-align: center;
    }
    .stMarkdown h3 {
        color: #4CAF50;
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        color: #777;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown("<h1>🔐 Password Generator</h1>", unsafe_allow_html=True)

# Password Length Slider
length = st.slider("Select Password Length", min_value=6, max_value=30, value=12)

# Checkboxes for Digits and Special Characters
use_digits = st.checkbox("Include Digits (0-9)")
use_special = st.checkbox("Include Special Characters (!@#$%^&*)")

# Generate Password Button
if st.button("Generate Password"):
    if length < 6:
        st.error("Password length must be at least 6 characters.")
    else:
        password = generate_password(length, use_digits, use_special)
        st.success("Password Generated Successfully!")
        st.markdown(f"<h3>Your Password: <code>{password}</code></h3>", unsafe_allow_html=True)

        # Check Password Strength
        strength = check_password_strength(password)
        if strength == 4:
            st.markdown("<p style='color:#4CAF50; font-weight:bold;'>Password Strength: Strong 💪</p>", unsafe_allow_html=True)
        elif strength == 3:
            st.markdown("<p style='color:#FFA500; font-weight:bold;'>Password Strength: Good 👍</p>", unsafe_allow_html=True)
        elif strength == 2:
            st.markdown("<p style='color:#FFA500; font-weight:bold;'>Password Strength: Medium 😐</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:#FF0000; font-weight:bold;'>Password Strength: Weak 😟</p>", unsafe_allow_html=True)

        # Copy to Clipboard Button
        st.markdown(f"""
        <button onclick="navigator.clipboard.writeText('{password}')" style="background-color: #008CBA; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
            Copy Password to Clipboard
        </button>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Built With ❤️ by Bisma</div>", unsafe_allow_html=True)