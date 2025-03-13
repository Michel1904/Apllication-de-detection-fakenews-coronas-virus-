import streamlit as st
import joblib
import os

def load_model():
    model_path = os.path.join("model", "xgb_fake_news_model.pkl")
    vectorizer_path = os.path.join("model", "tfidf_vectorizer.pkl")

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Le fichier {model_path} est introuvable.")

    if not os.path.exists(vectorizer_path):
        raise FileNotFoundError(f"Le fichier {vectorizer_path} est introuvable.")

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
        result = "🟢 Ce n'est pas une fake news." if prediction == 1 else "🔴 Attention, cela pourrait être une fake news !"

        st.subheader("Résultat :")
        st.write(result)
    else:
        st.warning("Veuillez entrer un texte avant de vérifier.")

