import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker by Haider Asghar", page_icon="🔐", layout="centered")

#custom CSS for the app
st.markdown("""
<style>
    .main {
        text-align: center;
    }
    .stTextInput {
        width: 60% !important;
        margin: auto;
    }
    .stButton button {
        width: 50%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        display: block;
        margin: auto;
    }
    .stButton button:hover {
        background-color: #73ba9b;
    }
</style>
""", unsafe_allow_html=True)


#page title & description
st.title("🔑 Password Strength Checker")
st.write("Enter your password below to check its security level. 🔍")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1 #increases score by 1 if password is 8 or more characters long
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Password Strength Rating display
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.info("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")

    # feedback
    if feedback:
        with st.expander("Improve your Password security"):
            for message in feedback:
                st.write(message)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong and secure.")

#Button working
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password to check its strength.") #show warning if password is empty        
