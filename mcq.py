import spacy
import random

nlp = spacy.load("en_core_web_sm")

def generate_mcqs(text, count):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents if len(sent.text.split()) > 6]

    mcqs = []

    for sent in sentences[:count]:
        words = [token.text for token in nlp(sent) if token.pos_ == "NOUN"]

        if not words:
            continue

        answer = random.choice(words)
        question = sent.replace(answer, "_____")

        distractors = random.sample(words, min(3, len(words))) if len(words) >= 3 else words

        options = distractors + [answer]
        random.shuffle(options)

        mcqs.append({
            "question": question,
            "answer": answer,
            "options": options
        })

    return mcqs