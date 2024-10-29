import streamlit as st
from password import check_password
import student_responses  # Import your student responses page
import teacher_settings
import methodology
from PIL import Image

# region <--------- Streamlit Page password --------->
# Check if the password is correct
if not check_password():
    st.stop()
# endregion <--------- Streamlit Page password -------->

# Set page configuration
st.set_page_config(page_title="Checkmate App", page_icon="♟️", layout="wide")

# Initialize session state for modal display
if 'show_modal' not in st.session_state:
    st.session_state.show_modal = True  # Start with modal shown

# Sidebar options for navigation
st.sidebar.title("Make your move")
page = st.sidebar.selectbox("Select a page",
                             ("♟️ About Checkmate", "📋 Methodology", "⚙️ Teacher: Settings", "✏️ Student: Responses"))

def about_us_page():
    # Page title at the top
    st.title("♟️ Checkmate: *Feedback that moves you forward* ")

    # Add a subheader
    st.subheader("🤕 The Problem")
    st.write("Teachers often struggle to find time to provide personalised feedback for students for all their assignments. On the other hand, students would benefit from more detailed feedback that pinpoints specific errors or misconceptions, helping them improve their understanding and close learning gaps.")

    # Add a subheader for team introduction
    st.subheader("✅ The Solution")
    st.write("Enter *Checkmate* - an AI-powered feedback assistant, offers targeted, immediate annotated feedback that clarifies specific mistakes, fostering better understanding and actionable follow-ups. For teachers, *Checkmate* saves time from the onerous task of writing detailed feedback for each student, allowing them to focus on higher-order feedback.")

    # Add a subheader for team introduction
    st.subheader("👩🏻‍💻👩🏻‍💻 Meet Our Team")

    # Create two columns for images and descriptions
    col1, col2 = st.columns(2)

    # First column with Grace's profile
    with col1:
        try:
            st.image("images/Grace.png", width=200)
            st.markdown("**Grace, Design Researcher**")
            st.markdown("Grace is from the Information Technology Division and works with the AI in Education Office in MOE’s Educational Technology Division. She is committed in delivering the best user experiences for AI features.")
        except FileNotFoundError:
            st.write("Image for Grace not found.")

    # Second column with Zoe's profile
    with col2:
        try:
            st.image("images/Zoe.png", width=200)
            st.markdown(" **Zoe, Educational Technology Officer**")
            st.markdown("Zoe works in the AI in Education Office in MOE's Educational Technology Division. A former science educator, she is currently designing AI features within the Singapore Student Learning Space.")
        except FileNotFoundError:
            st.write("Image for Zoe not found.")

# Show the modal if it's supposed to be shown
if st.session_state.show_modal:
    with st.expander("Welcome to Checkmate!", expanded=True):
        st.write("⚠️ **IMPORTANT NOTICE** ⚠️: This web application is developed as a proof-of-concept prototype. The information provided here is **NOT** intended for actual usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters. Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output. Always consult with qualified professionals for accurate and personalised advice.")
        if st.button("I Agree"):
            st.session_state.show_modal = False  # Close the modal

# Load the selected page based on the session state
if not st.session_state.show_modal:
    if page == "♟️ About Checkmate":
        about_us_page()
    elif page == "📋 Methodology":
        methodology.app()
    elif page == "⚙️ Teacher: Settings":
        teacher_settings.app()
    elif page == "✏️ Student: Responses":
        student_responses.app()
