import streamlit as st

def main():
    # Set page title and layout
    st.set_page_config(page_title="Simple Calculator", layout="centered")

    # Title and description
    st.title("Simple Calculator")
    st.write("Enter two numbers and choose an operation")

    # Create two columns for input fields
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter first number", value=0.0)

    with col2:
        num2 = st.number_input("Enter second number", value=0.0)

    # Dropdown for operation selection
    operation = st.selectbox("Choose operation", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]) 

    # Button to perform calculation
    if st.button("Calculate"): 
        try:
            if operation == "Addition (+)":
                result = num1 + num2 
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2 
                symbol = "-"
            elif operation == "Multiplication (*)":
                result = num1 * num2 
                symbol = "*"
            else:
                if num2 == 0:
                    st.error("Error: Division by Zero")
                    return  
                result = num1 / num2 
                symbol = "/" 
            
            # Display result with a success message
            st.success(f"{num1} {symbol} {num2} = {result}") 

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Optional: Add a sidebar for additional information or controls
    st.sidebar.title("About")
    st.sidebar.info(
        "This is a simple calculator app built with Streamlit. "
        "You can perform basic arithmetic operations like addition, subtraction, multiplication, and division."
    )

if __name__ == "__main__":
    main()