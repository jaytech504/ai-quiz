import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from transformers import pipeline
import random

nltk.download('punkt_tab')
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

def summarize_text(input_text, max_length=100):
    """
    Generate a summary of the input text using the Hugging Face transformers pipeline.

    Parameters:
        input_text (str): The input text to summarize.
        max_length (int): The maximum length of the summary.

    Returns:
        str: The summary of the input text.
    """
    summarizer = pipeline("summarization", model="t5-small")
    summary = summarizer(input_text, max_length=max_length, min_length=30, do_sample=False)
    return summary[0]["summary_text"]

def generate_mcqs(input_text, num_questions):
    """
    Generate multiple-choice questions (MCQs) from input text.

    Parameters:
        input_text (str): The input text to process.
        num_questions (int): The number of MCQs to generate.

    Returns:
        list: A list of dictionaries, each containing a question, options, and correct answer.
    """
    sentences = sent_tokenize(input_text)
    words = word_tokenize(input_text)
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.isalnum() and word.lower() not in stop_words]

    word_freq = nltk.FreqDist(filtered_words)
    most_common_words = word_freq.most_common(num_questions)

    mcqs = []
    for word, _ in most_common_words:
        question_sentence = next((s for s in sentences if word in s), None)

        if question_sentence:
            question = question_sentence.replace(word, "_____")
            distractors = random.sample(filtered_words, 3)
            while word in distractors:
                distractors = random.sample(filtered_words, 3)

            options = distractors + [word]
            random.shuffle(options)

            mcqs.append({
                "question": question,
                "options": options,
                "correct_answer": word,
            })

    return mcqs