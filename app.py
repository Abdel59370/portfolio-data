import streamlit as st
from PIL import Image

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Rhany El - Data Scientist Portfolio",
    page_icon="📊",
    layout="wide"
)

# --- SIDEBAR (Colonne de gauche avec vos infos de contact) ---
with st.sidebar:
    # Vous pourrez ajouter votre photo ici plus tard avec st.image("photo.jpg")
    st.title("Rhany El")
    st.subheader("Data Scientist / Data Analyst")
    
    st.write("📍 Bruxelles")
    st.write("📧 abdelrhanywrk@gmail.com")
    st.write("📞 +33 7 52 30 08 01")
    st.write("🚗 Permis B + Véhicule")
    
    st.markdown("---")
    
    # Bouton de téléchargement du CV (Il faudra mettre votre PDF dans le même dossier)
    # Pour l'instant c'est un bouton inactif pour la démo
    st.download_button(
        label="📄 Télécharger mon CV",
        data="Vous devrez lier votre fichier PDF ici",
        file_name="CV_Rhany_El.pdf",
        mime="application/pdf"
    )

    st.markdown("---")
    st.write("**Langues**")
    st.write("🇬🇧 Anglais (C1)")
    st.write("🇪🇸 Espagnol (A2)")

# --- SECTION PRINCIPALE : INTRO ---
st.title("👋 Bonjour, je suis Rhany")
st.markdown("""
**Data Scientist & Data Analyst** avec 4 ans d'expérience.  
Spécialisé dans l'exploitation des données (Python, SQL) et la Dataviz (Power BI) pour la prise de décision stratégique.
""")

st.info("🚀 **Disponible immédiatement** pour une mission (CDI, Freelance...) en Data & IA.")

st.markdown("---")

# --- SECTION COMPÉTENCES (Affichage en colonnes) ---
st.header("🛠 Compétences Techniques")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💻 Languages & Code")
    st.write("🐍 **Python**, SQL, R, SAS, VBA")
    st.write("🌐 HTML, CSS, PHP")
    st.write("⚙️ Git, GitHub")

with col2:
    st.subheader("📊 Dataviz & BI")
    st.write("📈 **Power BI**, Tableau, Qlik Sense")
    st.write("📋 Business Objects (BO)")
    st.write("🤖 PowerAutomate, PowerApps")

with col3:
    st.subheader("☁️ Cloud & Data Eng.")
    st.write("☁️ **Azure Databricks**, Snowflake, GCP")
    st.write("🔄 ETL: Talend, Oracle Data Integrator")
    st.write("🔒 Cybersécurité & RGPD")

st.markdown("---")

# --- SECTION EXPÉRIENCES (Détails interactifs) ---
st.header("💼 Expériences Professionnelles")

# Expérience 1 : Castorama
with st.expander("🏠 **Data Scientist / Data Analyst - Castorama** (Sept 2023 - Oct 2025)", expanded=True):
    st.write("**Contexte :** Mise en place d'un modèle de churn prédictif et transformation data-driven.")
    st.markdown("""
    * **Modélisation :** Développement d'un modèle de scoring client (Python/SQL) pour anticiper l'attrition. [Projet déployé en prod]
    * **Data Engineering :** Nettoyage et structuration de données multi-sources (Transactions, CRM digital).
    * **Dataviz :** Conception d'un dashboard Power BI adopté à l'échelle nationale par les directeurs de magasin.
    * **Stack technique :** Python, SQL, VBA, Power BI.
    """)

# Expérience 2 : Crédit Agricole
with st.expander("bank **Data Analyst - Crédit Agricole** (Sept 2021 - Sept 2023)"):
    st.write("**Contexte :** Support à la direction, automatisation des reportings et migration Cloud.")
    st.markdown("""
    * **Automatisation :** Création de scripts (VBA, SAS, Power Query) réduisant drastiquement le temps de reporting.
    * **Migration Cloud :** Migration des données de SAS vers **Snowflake** (réécriture de code SAS en SQL).
    * **Outils Métier :** Conception d'outils Excel/VBA dynamiques pour les équipes non techniques.
    * **Analyse :** Études sur le surendettement pour ajuster les stratégies de recouvrement.
    """)

st.markdown("---")

# --- SECTION FORMATION ---
st.header("🎓 Diplômes")
st.write("🎓 **Master Data & IA** - INSA Lille (2023 - 2025)")
st.write("🎓 **Licence SID (Système d'Information Décisionnelle)** - Université de Lille (2022 - 2023)")
st.write("🎓 **DUT Statistique et Informatique Décisionnelle** - Université de Lille (2020 - 2022)")

# --- FOOTER ---
st.markdown("---")
st.caption("Développé avec Python & Streamlit par Rhany El.")