import streamlit as st
from quiz_generator import generate_mcqs, summarize_text
import PyPDF2
import io

# Streamlit app setup
st.set_page_config(
    page_title="AI Quiz Generator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Header
st.markdown(
    """
    <style>
    h1, h2, h3 { text-align: center; color: #2c3e50; }
    .stRadio > label { font-size: 16px; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🧠 AI Quiz Generator")
st.subheader("📂 Upload a file, generate a quiz, and get a summary of the content!")

# Sidebar for user interaction
st.sidebar.title("⚙️ Options")
quiz_size = st.sidebar.selectbox(
    "Select the number of questions for the quiz:",
    options=[10, 20, 30, 40, 50],
    index=0,
)
show_summary = st.sidebar.checkbox("Show Summary", value=True)

# File upload
uploaded_file = st.file_uploader(
    "Upload a .txt or .pdf file to get started:", type=["txt", "pdf"]
)

# Process uploaded file
input_text = ""
if uploaded_file:
    if uploaded_file.type == "text/plain":
        input_text = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
        input_text = "".join([page.extract_text() for page in pdf_reader.pages])
        if not input_text.strip():
            st.error("The uploaded pdf does not have extractable text")

# Optional: Show the text extracted from the file
if input_text:
    st.markdown("### 📜 Extracted Content Preview")
    st.write(input_text[:1000])  # Show the first 1000 characters as a preview

# Show summary (if enabled)
if input_text and show_summary:
    st.markdown("### 📖 Summary of the Text")
    summary = summarize_text(input_text)
    st.write(summary)

# Allow manual text input if no file is uploaded
if not uploaded_file:
    input_text = st.text_area(
        "Or paste your text below:",
        placeholder="Enter or paste text here to generate a quiz and summary...",
    )

# Generate quiz
if st.button("📝 Generate Quiz"):
    if input_text.strip():
        st.markdown("### 🧩 Your Quiz")
        quiz = generate_mcqs(input_text, quiz_size)

        # Display the questions and collect answers
        user_answers = []
        for i, question in enumerate(quiz):
            st.write(f"**Question {i+1}:** {question['question']}")
            selected_option = st.radio(
                f"Choose your answer for Question {i+1}:",
                options=question["options"],
                key=f"q{i+1}",
            )
            user_answers.append((selected_option, question["correct_answer"]))

        # Submit button
        if st.button("🎯 Submit Answers"):
            correct_count = sum(
                1 for user_ans, correct_ans in user_answers if user_ans == correct_ans
            )
            total_questions = len(user_answers)
            score_percentage = (correct_count / total_questions) * 100
            st.success(
                f"**Your Total Score: {correct_count}/{total_questions} ({score_percentage:.2f}%)**"
            )
    else:
        st.error("Please provide text or upload a file to generate the quiz.")