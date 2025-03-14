import streamlit as st
import random
import re


def check_password_strength(password):
    if not password:
        return "Please enter a password."
        
    length_of_password = len(password)
    score = 0
    
    # Check length
    if length_of_password >= 8:
        score += 1
    else:
        return "❌ Password is too short. It should be at least 8 characters long."
    if length_of_password > 12:
        score += 1
    # Check for uppercase and lowercase
    if password.islower():
        return "❌ Password should contain at least one uppercase letter."
    else:
        score += 1
        
    if password.isupper():
        return "❌ Password should contain at least one lowercase letter."
    else:
        score += 1
    
    # Check for digits
    if password.isalpha():
        return "❌ Password should contain at least one digit."
    else:
        score += 1
    
    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        return "❌ Include at least one special character (!@#$%^&*)."
    
    if score >= 6:
        return "✅ Strong Password!"
    elif score >=4 :
        suggested = suggest_strongpassword()
        return f"⚠️ Moderate Password - Consider adding more security features.\nSuggested strong password: {suggested}"
    else:
        suggested = suggest_strongpassword()
        return f"❌ Weak Password - Please follow the suggestions above.\nSuggested strong password: {suggested}"


def suggest_strongpassword():
    length = 4
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits= '0123456789'
    specialchar = '@#$%^&*'
    password = ''.join(random.choice(characters)+random.choice(digits)+random.choice(specialchar) for _ in range(length))
    return password

def main():
    st.title("Password Strength Checker")
    password = st.text_input("Enter your password:", type="password")
    strength_message = check_password_strength(password)
    st.write(strength_message)


if __name__ == "__main__":
    main()