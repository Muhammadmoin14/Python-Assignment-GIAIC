import random
import string
import streamlit as st

def check_password_strength(password):
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Password should contain at least one digit."
    if not any(char.islower() for char in password):
        return "Password should contain at least one lowercase letter."
    if not any(char.isupper() for char in password):
        return "Password should contain at least one uppercase letter."
    if not any(char in string.punctuation for char in password):
        return "Password should contain at least one special character."
    return "Password is strong."

def suggest_strong_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    strong_password = ''.join(random.choice(characters) for i in range(length))
    return strong_password

def main():
    st.title("Password Strength Checker")
    
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        strength_message = check_password_strength(password)
        st.write(strength_message)
        
        if strength_message != "Password is strong.":
            st.write("Suggested strong password: ", suggest_strong_password())

if __name__ == "__main__":
    main()