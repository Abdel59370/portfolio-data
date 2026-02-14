import streamlit as st
from PIL import Image

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Rhany El Khayari - Data & AI Portfolio",
    page_icon="📊",
    layout="wide",
)

# -------------------------------
# OPTION 4 : LANDING PAGE RAPIDE
# -------------------------------
# Principe : le recruteur arrive sur une page "vitrine" ultra légère (chargement instant),
# puis clique sur un bouton pour ouvrir le portfolio complet (qui peut, lui, prendre plus de temps).

# Lire le mode d'affichage depuis les query params
view = st.query_params.get("view", "landing")  # "landing" (par défaut) ou "portfolio"


def go_portfolio():
    st.query_params["view"] = "portfolio"
    st.rerun()


def go_landing():
    st.query_params["view"] = "landing"
    st.rerun()


# -------------------------------
# LANDING PAGE (vitrine rapide)
# -------------------------------
if view == "landing":
    # (Optionnel) désactiver certains éléments lourds si tu en ajoutes plus tard
    st.markdown("## 👋 Rhany El Khayari")
    st.markdown("### Consultant **Data & AI** — Mobile (France & International)")

    c1, c2 = st.columns([2, 1], gap="large")

    with c1:
        st.markdown(
            """
**Profil :** Data Scientist / Data Analyst (5 ans) — Master Data & IA  
**Objectif :** transformer des données complexes en leviers décisionnels clairs et automatisés.

**Highlights :**
- ✅ Modèle de **Scoring Churn** déployé (Python/SQL) + dashboard Power BI (adoption large)
- ✅ Migration **SAS → Snowflake** + automatisation reportings (VBA / Power Query)
- ✅ Chaîne data complète : ETL/Cloud → Modélisation → BI
"""
        )

        st.success("✅ Disponible immédiatement (CDI ou Freelance)")

        btn1, btn2 = st.columns([1, 1])
        with btn1:
            st.button("🚀 Ouvrir le portfolio complet", use_container_width=True, on_click=go_portfolio)
        with btn2:
            st.link_button(
                "📧 Me contacter",
                "mailto:abdelrhanywrk@gmail.com",
                use_container_width=True
            )

    with c2:
        st.markdown("#### 📌 Contact")
        st.write("🌍 **Mobile** (France & International)")
        st.write("📧 abdelrhanywrk@gmail.com")
        st.write("📞 +33 7 52 30 08 01")
        st.write("🚗 Permis B + Véhicule personnel")

        st.markdown("---")
        st.markdown("#### 📄 CV")
        # Remplace data="..." par le contenu du PDF réel une fois uploadé
        st.download_button(
            label="Télécharger mon CV",
            data="Il faudra glisser votre PDF ici",
            file_name="CV_Rhany_El.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    st.markdown("---")
    st.markdown("### 🔎 Aperçu (rapide)")
    p1, p2, p3 = st.columns(3, gap="large")
    with p1:
        st.markdown("**Churn Scoring (Prod)**")
        st.caption("Python / SQL / Power BI — ciblage rétention")
    with p2:
        st.markdown("**Migration Cloud**")
        st.caption("SAS → Snowflake — réécriture + fiabilisation")
    with p3:
        st.markdown("**Automation & BI**")
        st.caption("VBA / Power Query — gains de temps reportings")

    st.markdown("---")
    st.caption("© 2025 - Landing page légère (accès portfolio complet via le bouton).")

    # IMPORTANT : on STOP ici pour ne pas charger le reste du portfolio
    st.stop()


# -------------------------------
# PORTFOLIO COMPLET (ton contenu)
# -------------------------------

# --- SIDEBAR (Infos, Soft Skills, Loisirs) ---
with st.sidebar:
    st.title("**Rhany El Khayari**")
    st.subheader("Consultant Data & AI")

    st.write("🌍 **Mobile** (France & International)")
    st.write("📧 abdelrhanywrk@gmail.com")
    st.write("📞 +33 7 52 30 08 01")
    st.write("🚗 Permis B + Véhicule personnel")

    st.markdown("---")

    st.download_button(
        label="📄 Télécharger mon CV complet",
        data="Il faudra glisser votre PDF ici",
        file_name="CV_Rhany_El.pdf",
        mime="application/pdf"
    )

    st.markdown("---")
    st.subheader("🧠 Atouts")
    st.write("⚡ Capacité d'apprentissage rapide")
    st.write("🧘 Gestion du stress")
    st.write("🤝 Adaptabilité & Autonomie")
    st.write("🎯 Persévérance")

    st.markdown("---")
    st.subheader("🗣️ Langues")
    st.write("🇬🇧 Anglais (**C1** - Avancé)")
    st.write("🇪🇸 Espagnol (**A2** - Intermédiaire)")

    st.markdown("---")
    st.subheader("🌟 Centres d'intérêt")
    st.write("🤖 Innovations en IA")
    st.write("🌍 Voyage (UK, Espagne, Maroc...)")
    st.write("🏃 Course à pied & Cinéma")

    st.markdown("---")
    st.button("⬅️ Retour page vitrine", use_container_width=True, on_click=go_landing)

# --- SECTION PRINCIPALE : INTRO ---
st.title("👋 Bonjour, je suis **Rhany El Khayari**")
st.markdown("""
### 🚀 Data Scientist & Data Analyst confirmé

Fort de **5 ans d'expérience** et titulaire d'un **Master Data & IA**, je suis un expert de la chaîne de valeur de la donnée : de l'ingénierie (**ETL, Cloud**) à la **modélisation prédictive (Machine Learning)**.

Mon objectif : **Transformer les données complexes en leviers décisionnels clairs et automatisés** pour optimiser la performance business.
""")

st.success("✅ **Disponible immédiatement** pour des missions en CDI ou Freelance.")
st.markdown("---")

# --- SECTION COMPÉTENCES ---
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

# --- SECTION EXPÉRIENCES ---
st.header("💼 Parcours Professionnel")

with st.expander("🛠️ **Data Scientist / Data Analyst - CASTORAMA** (Sept 2023 - Oct 2025)", expanded=True):
    st.markdown("""
**Contexte :** Projet stratégique de fidélisation client et de transformation Data-Driven.

**🎯 Missions & Réalisations :**
* **Modélisation Prédictive :** Conception et **déploiement en production** d'un modèle de *Scoring Churn* (Python/SQL).
* **Data Engineering :** Nettoyage et structuration de données (transactions magasin + CRM digital).
* **Reporting :** Dashboard Power BI clé en main pour pilotage fidélité.
* **Automatisation :** Scripts Python/VBA pour optimiser les campagnes marketing.

**🏆 Impact Business :**
* ✅ Adoption large du dashboard Power BI.
* ✅ Recommandations intégrées aux processus CRM.
* ✅ Pilotage plus précis des actions de rétention.

*Stack : Python, SQL, VBA, Power BI, Azure.*
""")

with st.expander("🏢 **Data Analyst / Ingénieur BI - CRÉDIT AGRICOLE** (Sept 2021 - Sept 2023)", expanded=True):
    st.markdown("""
**Contexte :** Modernisation des reportings et migration Cloud.

**🎯 Missions & Réalisations :**
* **Migration Cloud :** SAS → Snowflake (réécriture SQL).
* **Automatisation :** Réduction du temps de production via VBA, SAS, Power Query.
* **Outils Métier :** Interfaces Excel dynamiques pour équipes non-tech.
* **Analyse :** Études endettement client pour ajuster stratégies de recouvrement.

**🏆 Impact Business :**
* ✅ Pilotage fiabilisé des créances consolidées.
* ✅ Gain de temps reportings mensuels.
* ✅ Outils plus ergonomiques pour la décision.

*Stack : SAS, SQL, Snowflake, VBA, Excel, Power Query.*
""")

st.markdown("---")

# --- SECTION FORMATION ---
st.header("🎓 Formation Académique")

col_a, col_b = st.columns([1, 3])
with col_a:
    st.write("📅 **2023 - 2025**")
with col_b:
    st.subheader("**Master Data & IA**")
    st.write("INSA Hauts-de-France (Lille)")
    st.caption("Big Data (Spark), ETL, modélisation avancée, gestion de projet Agile (Scrum/Kanban).")

st.markdown("---")

col_c, col_d = st.columns([1, 3])
with col_c:
    st.write("📅 **2022 - 2023**")
with col_d:
    st.subheader("**Licence SID (Système d'Information Décisionnelle)**")
    st.write("Université de Lille")
    st.caption("Analyse de données, statistique appliquée, R, Python, SQL, SAS.")

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
st.markdown(
    """
<div style='text-align: center;'>
    <p>© 2025 - Portfolio développé par Rhany El avec Python & Streamlit.</p>
</div>
""",
    unsafe_allow_html=True
)
