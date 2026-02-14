import streamlit as st
from PIL import Image

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Rhany El Khayari - Data & AI Professional Portfolio",
    page_icon="📊",
    layout="wide"
)

# --- SIDEBAR (Infos, Soft Skills, Loisirs) ---
with st.sidebar:
    st.title("**Rhany El Khayari**")
    st.subheader("Consultant Data & AI")
    
    # Coordonnées mises à jour
    st.write("🌍 **Mobile** (France & International)")
    st.write("📧 abdelrhanywrk@gmail.com")
    st.write("📞 +33 7 52 30 08 01")
    st.write("🚗 Permis B + Véhicule personnel")
    
    st.markdown("---")
    
    # Bouton CV (Pensez à bien mettre votre PDF dans le dossier avec ce nom !)
    st.download_button(
        label="📄 Télécharger mon CV complet",
        data="Il faudra glisser votre PDF ici",
        file_name="CV_Rhany_El.pdf",
        mime="application/pdf"
    )

    st.markdown("---")
    
    # Soft Skills (Atouts)
    st.subheader("🧠 Atouts")
    st.write("⚡ Capacité d'apprentissage rapide")
    st.write("🧘 Gestion du stress")
    st.write("🤝 Adaptabilité & Autonomie")
    st.write("🎯 Persévérance")

    st.markdown("---")

    # Langues
    st.subheader("🗣️ Langues")
    st.write("🇬🇧 Anglais (**C1** - Avancé)")
    st.write("🇪🇸 Espagnol (**A2** - Intermédiaire)")

    st.markdown("---")

    # Centres d'intérêt
    st.subheader("🌟 Centres d'intérêt")
    st.write("🤖 Innovations en IA")
    st.write("🌍 Voyage (UK, Espagne, Maroc...)")
    st.write("🏃 Course à pied & Cinéma")

# --- SECTION PRINCIPALE : INTRO ---
st.title("👋 Bonjour, je suis **Rhany El Khayari**")
st.markdown("""
### 🚀 Data Scientist & Data Analyst confirmé

Fort de **5 ans d'expérience** et titulaire d'un **Master Data & IA**, je suis un expert de la chaîne de valeur de la donnée : de l'ingénierie (**ETL, Cloud**) à la **modélisation prédictive (Machine Learning)**.

Mon objectif : **Transformer les données complexes en leviers décisionnels clairs et automatisés** pour optimiser la performance business.
""")

st.success("✅ **Disponible immédiatement** pour des missions en CDI ou Freelance.")

st.markdown("---")

# --- SECTION COMPÉTENCES (Détaillée à fond) ---
st.header("🛠 Compétences Techniques")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("#### **Data Science & ML**")
    st.write("🐍 **Python** (Pandas, Scikit-learn)")
    st.write("🔢 **SQL**, R, SAS, VBA")
    st.write("📈 Modélisation (Scoring, Régression)")

with col2:
    st.markdown("#### **BI & Reporting**")
    st.write("📊 **Power BI** (DAX) & Tableau")
    st.write("📋 Business Objects (BO), Qlik Sense")
    st.write("🤖 Automatisation (PowerAutomate/Apps)")

with col3:
    st.markdown("#### **Data Eng & Cloud**")
    st.write("❄️ **Snowflake**, Azure Databricks, GCP")
    st.write("🔄 ETL : Talend, Oracle DI, Knime")
    st.write("⚙️ Architecture de données")

with col4:
    st.markdown("#### **Méthodologie**")
    st.write("🔄 **Gestion de Projet : Scrum, Kanban**")
    st.write("🛠️ Outils : JIRA, Trello, Git/GitHub")
    st.write("🛡️ Conformité : RGPD, Cybersécurité")

st.markdown("---")

# --- SECTION EXPÉRIENCES (Détaillée à fond) ---
st.header("💼 Parcours Professionnel")

# Expérience 1 : Castorama
with st.expander("🛠️ **Data Scientist / Data Analyst - CASTORAMA** (Sept 2023 - Oct 2025)", expanded=True):
    st.markdown("""
    **Contexte :** Projet stratégique de fidélisation client et de transformation Data-Driven.
    
    **🎯 Missions & Réalisations :**
    * **Modélisation Prédictive :** Conception et **déploiement en production** d'un modèle de *Scoring Churn* (Python/SQL) pour identifier les clients à risque.
    * **Data Engineering :** Mise en place des flux de nettoyage et de structuration de données complexes (transactions magasin + CRM digital).
    * **Reporting :** Création d'un dashboard Power BI clé en main pour le pilotage de la fidélité.
    * **Automatisation :** Scripts Python/VBA pour optimiser les campagnes marketing ciblées.

    **🏆 Impact Business :**
    * ✅ **Adoption nationale** du dashboard Power BI par le réseau de directeurs.
    * ✅ **Intégration des recommandations** stratégiques directement aux processus CRM.
    * ✅ **Pilotage précis** des actions de rétention.
    
    *Stack : Python, SQL, VBA, Power BI, Azure.*
    """)

# Expérience 2 : Crédit Agricole (Icone "bank" retirée -> remplacée par 🏢)
with st.expander("🏢 **Data Analyst / Ingénieur BI - CRÉDIT AGRICOLE** (Sept 2021 - Sept 2023)", expanded=True):
    st.markdown("""
    **Contexte :** Modernisation des systèmes de reporting et migration vers une architecture Cloud.
    
    **🎯 Missions & Réalisations :**
    * **Migration Cloud Majeure :** Pilotage technique de la migration des données de l'environnement **SAS vers Snowflake**, incluant la réécriture complète des scripts de transformation en SQL.
    * **Automatisation :** **Réduction significative du temps de production** des reportings réglementaires grâce à l'automatisation via VBA, SAS et Power Query.
    * **Outils Métier :** Création d'interfaces Excel dynamiques et ergonomiques, facilitant l'utilisation des reportings par les équipes non-techniques.
    * **Analyse :** Réalisation d'études détaillées sur l'endettement client pour **ajuster les stratégies de recouvrement**.

    **🏆 Impact Business :**
    * ✅ **Fiabilisation** du pilotage des créances consolidées.
    * ✅ **Gain de temps** sur la production des reportings mensuels.
    * ✅ **Création d'outils ergonomiques** facilitant la prise de décision en agence.

    *Stack : SAS, SQL, Snowflake, VBA, Excel, Power Query.*
    """)

st.markdown("---")

# --- SECTION FORMATION (Détaillée) ---
st.header("🎓 Formation Académique")

col_a, col_b = st.columns([1, 3])

with col_a:
    st.write("📅 **2023 - 2025**")
with col_b:
    st.subheader("**Master Data & IA**")
    st.write("INSA Hauts-de-France (Lille)")
    st.caption("Axé sur le Big Data (Spark), l'ETL, la modélisation avancée, et la gestion de projet Agile (Scrum/Kanban).")

st.markdown("---")

col_c, col_d = st.columns([1, 3])

with col_c:
    st.write("📅 **2022 - 2023**")
with col_d:
    st.subheader("**Licence SID (Système d'Information Décisionnelle)**")
    st.write("Université de Lille")
    st.caption("Approfondissement en analyse de données, statistique appliquée et informatique décisionnelle (R, Python, SQL, SAS).")

st.markdown("---")

col_e, col_f = st.columns([1, 3])

with col_e:
    st.write("📅 **2020 - 2022**")
with col_f:
    st.subheader("**DUT STID (Statistique et Informatique Décisionnelle)**")
    st.write("Université de Lille")
    st.caption("Socle solide en statistique, programmation et outils décisionnels.")


# --- FOOTER ---
st.markdown("---")
# Centering the footer text
st.markdown("""
<div style='text-align: center;'>
    <p>© 2025 - Portfolio développé par Rhany El avec Python & Streamlit.</p>
</div>
""", unsafe_allow_html=True)

