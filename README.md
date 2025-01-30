📚 AI Quiz Generator

📝 Overview

The AI Quiz Generator is a Streamlit-powered application that allows users to generate multiple-choice questions (MCQs) from uploaded PDF or TXT files or pasted text. It utilizes Natural Language Processing (NLP) to extract key topics, generate quizzes, and summarize documents. Users can choose the number of questions (10, 20, 30, 40, or 50) and receive a final score at the end.

✨ Features

📂 Upload PDFs or TXT files

✏️ Paste text manually

🎯 Generate MCQs automatically

🏆 Score calculation in percentage

📄 Summarize documents

📱 Modern & clean UI with Streamlit

🚀 Installation

1️⃣ Clone the Repository

git clone https://github.com/your-username/ai-quiz-generator.git
cd ai-quiz-generator

2️⃣ Create a Virtual Environment

python -m venv quizgen_env
source quizgen_env/bin/activate  # On macOS/Linux
quizgen_env\Scripts\activate    # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Install Additional Dependencies

Ensure PyTorch (or TensorFlow) is installed for the summarization feature.

pip install torch

Or if you prefer TensorFlow:

pip install tensorflow

5️⃣ Run the Application

streamlit run app.py

📂 Project Structure

ai-quiz-generator/
│── app.py               # Streamlit frontend
│── quiz_generator.py    # NLP logic for quiz generation & summarization
│── requirements.txt     # Dependencies
│── README.md            # Documentation

🔍 How It Works

1️⃣ Upload a PDF or TXT file, or paste text manually.
2️⃣ Preview the extracted content to ensure accuracy.
3️⃣ Choose the number of MCQs to generate.
4️⃣ Attempt the quiz using radio button options.
5️⃣ View the final score after submission.
6️⃣ (Optional) Get a summary of the document.

🛠️ Technologies Used

Python 🐍

Streamlit (Frontend UI) 🎨

NLTK (Text processing) 📖

Transformers (Hugging Face) (Summarization) 🤖

PyPDF2 (PDF processing) 📑

🏆 Future Improvements

✅ Support for DOCX files

✅ More quiz types (True/False, Fill in the Blanks)

✅ Advanced distractor generation for MCQs

🎯 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

📜 License

This project is licensed under the MIT License.

⭐ If you found this useful, don't forget to star the repo!

