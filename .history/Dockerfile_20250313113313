FROM python:3.12.5

WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt


# Vérifier l'installation de Streamlit (optionnel)
RUN pip list

# Exposer le port de Streamlit (par défaut 8501)
EXPOSE 8501

# Lancer Streamlit
CMD ["streamlit", "run", "app/fake.py", "--server.port=8501", "--server.address=0.0.0.0"]
