import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Parth Tomar | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title { font-size: 2.4rem; font-weight: 700; color: #1E88E5; margin-bottom: 0px; }
    .sub-title { font-size: 1.2rem; color: #555555; margin-bottom: 20px; font-weight: 500; }
    .card { background-color: #F8F9FA; padding: 20px; border-radius: 10px; border-left: 5px solid #1E88E5; margin-bottom: 15px; }
    .metric-box { background: #FFFFFF; border: 1px solid #E0E0E0; padding: 15px; border-radius: 8px; text-align: center; }
    .stButton>button { width: 100%; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation & Profile
with st.sidebar:
    st.markdown("## 🎯 Parth Tomar")
    st.markdown("**B.Tech IT Student (2025–2029)**  \n*Maharaja Agrasen Institute of Technology (MAIT), Delhi*")
    st.markdown("---")

    st.markdown("### 📌 Navigation")
    section = st.radio("Go to:", [
        "About Me", 
        "Coding Profiles", 
        "Projects", 
        "Certifications & Achievements", 
        "Extracurriculars & Goals"
    ])

    st.markdown("---")
    st.markdown("### 📫 Connect")
    st.markdown("[🔗 GitHub](https://github.com/parthtomar2706-ctrl)")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/parth-tomar-226328382)")
    st.markdown("[📧 Email](mailto:parthtomar2706@gmail.com)")

# --- Section 1: About Me ---
if section == "About Me":
    st.markdown('<p class="main-title">Parth Tomar</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">DSA Enthusiast | Aspiring Machine Learning Engineer</p>', unsafe_allow_html=True)

    st.markdown("### 📝 Profile Summary")
    st.write(
        "I am a B.Tech student with a rigorous focus on technical problem-solving and algorithmic efficiency. "
        "With over 400+ problems solved on LeetCode, I have built a strong foundation in C++ and Data Structures, "
        "focusing on writing optimized and scalable code."
    )
    st.write(
        "Currently, I am expanding my horizons into the world of Artificial Intelligence and Machine Learning. "
        "I am fascinated by how data-driven models can solve real-world problems and am actively seeking opportunities "
        "to apply my algorithmic skills to ML projects."
    )
    st.write(
        "Beyond the screen, my experience with the NCC has instilled in me the discipline and leadership required "
        "to thrive in collaborative, high-pressure environments."
    )

    st.markdown("---")
    st.markdown("### 🛠️ Technical Stack")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Languages**")
        st.code("C++\nPython", language="text")
    with col2:
        st.markdown("**ML & Data Science**")
        st.code("NumPy\nPandas\nMatplotlib\nSeaborn\nScikit-Learn", language="text")
    with col3:
        st.markdown("**Tools & Environment**")
        st.code("Git & GitHub\nJupyter Notebook\nVS Code", language="text")

# --- Section 2: Coding Profiles ---
elif section == "Coding Profiles":
    st.markdown("## 📊 Coding Profiles & Competitive Progress")
    st.write("Demonstrating strong foundational problem-solving abilities across competitive programming platforms.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-box">
            <h3>LeetCode</h3>
            <h2>431</h2>
            <p>Problems Solved</p>
            <p><strong>Rating: 1743</strong></p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.link_button("View LeetCode", "https://leetcode.com/u/Parth-tomar/")

    with col2:
        st.markdown("""
        <div class="metric-box">
            <h3>NeetCode</h3>
            <h2>108</h2>
            <p>Problems Solved</p>
            <p><strong>DSA Roadmap Progress</strong></p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.link_button("View NeetCode", "https://neetcode.io/user/GoldenAndorian508")

    with col3:
        st.markdown("""
        <div class="metric-box">
            <h3>HackerRank</h3>
            <h2>Verified</h2>
            <p>Problem Solving (Intermediate)</p>
            <p><strong>Certificate Earned</strong></p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.link_button("View HackerRank", "https://www.hackerrank.com/profile/parthtomar2706")

# --- Section 3: Projects ---
elif section == "Projects":
    st.markdown("## 💡 Machine Learning Projects")

    st.markdown("""
    <div class="card">
        <h3>Employee Attrition Retention Risk Predictor</h3>
        <p><strong>Tech Stack:</strong> Python | Pandas | Scikit-Learn | Matplotlib | Seaborn</p>
    </div>
    """, unsafe_allow_html=True)

    st.write(
        "Most companies treat employee resignations as a surprise. I built an ML pipeline to turn it into an early warning system. "
        "Predicting employee attrition isn’t just about raw accuracy—it’s a classic imbalanced data problem where default models miss critical churn risks."
    )

    with st.expander("🔍 Key Technical Highlights & Methodology"):
        st.markdown("""
        - **Imbalance Handling:** Balanced class weights and tuned decision thresholds to optimize for **Recall over simple accuracy** (prioritizing false negatives over false positives).
        - **Pipeline & Preprocessing:** Engineered numerical features using standard scaling and handled categorical variables via `One-Hot Encoding` inside a unified `ColumnTransformer`.
        - **Model Evaluation:** Evaluated Random Forest models using ROC-AUC, Precision-Recall curves, and Confusion Matrices.
        - **Key Domain Insight:** Compensation matters, but operational factors matter more. OverTime status, WorkLifeBalance, and DistanceFromHome outweighed raw monthly income in predicting attrition risk.
        """)

    st.link_button("📂 GitHub Repository", "https://github.com/parthtomar2706-ctrl/Employee-Attrition-Retention-Risk-Predictor")

# --- Section 4: Certifications & Achievements ---
elif section == "Certifications & Achievements":
    st.markdown("## 🏆 Certifications & Competition Achievements")

    st.markdown("""
    * **1166th Place - HackerRank Orchestrate May 2026**  
      *Building & Submitting an AI Agent* | HackerRank  
    * **Problem Solving (Intermediate) Certificate**  
      *HackerRank Skill Certification* | Earned: Nov 28, 2025  
    * **Yuva AI for All**  
      *INDIAai & NASSCOM FutureSkills Prime* | Issued: Jan 16, 2026  
    * **Deloitte Cyber Job Simulation Certificate**  
      *Forage* | Completed: Jan 7, 2026  
    * **Hackathon Participation**  
      *IBM Dev Days & Adobe University Hackathon 2026*
    """)

# --- Section 5: Extracurriculars & Goals ---
elif section == "Extracurriculars & Goals":
    st.markdown("## 🎖️ Extracurriculars & Future Vision")

    st.markdown("### 🪖 National Cadet Corps (NCC)")
    st.markdown("""
    * **Cadet** in **7 Delhi Battalion NCC**
    * Gained practical leadership training, military discipline, team cohesion, and high-pressure operational management experience.
    """)

    st.markdown("---")
    st.markdown("### 🎯 Future Career Goals")
    st.markdown("""
    * **Target Role:** Machine Learning Engineer
    * **Vision:** Combine strong Data Structures & Algorithms problem-solving with advanced ML pipelines, focusing on scalable AI agent development and real-world tabular data modeling.
    """)
