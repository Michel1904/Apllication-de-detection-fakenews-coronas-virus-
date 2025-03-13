import streamlit as st
import joblib
import os

# Définition des chemins des fichiers
model_path = os.path.join(os.path.dirname(__file__), "../model/xgb_fake_news_model.pkl")
vectorizer_path = os.path.join(os.path.dirname(__file__), "../model/tfidf_vectorizer.pkl")

# Chargement du modèle et du vectorizer
@st.cache_data
def load_model():
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer

model, vectorizer = load_model()

# Interface utilisateur
st.title("📰 Fake News Detector")
st.write("Entrez un texte et vérifiez s'il s'agit d'une fake news.")

# Champ de texte utilisateur
user_input = st.text_area("Tapez votre texte ici :", "")

if st.button("Vérifier"):
    if user_input:
        # Transformation du texte
        user_input_tfidf = vectorizer.transform([user_input])

        # Prédiction
        prediction = model.predict(user_input_tfidf)[0]
        result = "🟢 Ce n'est pas une fake news." if prediction == 0 else "🔴 Attention, cela pourrait être une fake news !"

        st.subheader("Résultat :")
        st.write(result)
    else:
        st.warning("Veuillez entrer un texte avant de vérifier.")

