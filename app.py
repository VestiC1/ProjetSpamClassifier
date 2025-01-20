import streamlit as st
import string
import joblib

st.title("Spam ou Ham")
sms = st.text_input("saisir le sms", "")
st.write("votre sms >>", sms)

def preprocessing(text):
    longueur = len(text)
    Nombre_de_mots = len(text.split())
    presence_speciaux_chiffres = bool(set(text).intersection(set("0123456789" + string.punctuation)))
    return [[longueur, Nombre_de_mots, presence_speciaux_chiffres]]

model = joblib.load("svc.joblib")
st.header(f'Voici le resultat >> {model.predict(preprocessing(sms))[0]}')