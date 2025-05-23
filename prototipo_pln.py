from flask import Flask, request, jsonify
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import nltk
import string
import pandas as pd

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
df = pd.read_csv("C:\\Users\\juan.bocanegra\\Documents\\preguntas.csv", encoding='latin1')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
translator = str.maketrans('', '', string.punctuation)


def preprocess(text):
    text = text.lower()
    text = text.translate(translator)
    # Tokenizar
    tokens = nltk.word_tokenize(text)
    # Eliminar stopwords y lematizar
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    return " ".join(tokens)

# Preparar datos para entrenamiento
questions = df['question'].tolist()
answers = df['answer'].tolist()

processed_questions = [preprocess(q) for q in questions]

# Vectorización TF-IDF
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(processed_questions)

# Entrenamiento modelo Naive Bayes
model = MultinomialNB()
model.fit(X_train, range(len(questions)))

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_question = data.get('question', '')
    if not user_question:
        return jsonify({"error": "No question provided"}), 400
    
    processed_user_q = preprocess(user_question)
    X_user = vectorizer.transform([processed_user_q])
    
    # Predecir la pregunta más similar
    pred_index = model.predict(X_user)[0]
    response = answers[pred_index]
    
    return jsonify({"question": user_question, "answer": response})

if __name__ == '__main__':
    app.run(debug=True)
