import streamlit as st
import random
import re


def check_password_strength(password):
    length_of_password = len(password)
    score = 0
    if length_of_password >= 8:
        score += 1
    else:
        return "Password is too short. It should be at least 8 characters long."
    if password == password.lower():
        return "Password should contain at least one uppercase letter."
    else:
        score += 1
    if password == password.upper():
        return "Password should contain at least one lowercase letter."
    else:
        score += 1
    if password == password.isalpha():
        return "Password should contain at least one digit."
    else:
        score += 1
    if password == password.isdigit():
        return "Password should contain at least one alphabetic character."
    else:
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        print("❌ Include at least one special character (!@#$%^&*).")
        
    
    if score >= 4:
        return("✅ Strong Password!")
    elif score == 3:
        suggest_strongpassword()
        return("⚠️ Moderate Password - Consider adding more security features.")
    else:
        suggest_strongpassword()
        return("❌ Weak Password - Improve it using the suggestions above.")

def suggest_strongpassword():
    length = 12
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = '.join(random.choice(characters) for i in range(lenght))'
    return password

def main():
    st.title("Password Strength Checker")
    password = st.text_input("Enter your password:", type="password")
    strenght_message = check_password_strength(password)
    st.write(strenght_message)

main()