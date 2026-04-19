import streamlit as st
import pandas as pd
import os
import plotly.express as px

from analyzer import analyze_student
from recommender import recommend_path
from model import predict_next_score, risk_level

st.set_page_config(page_title="AI Learning System", layout="wide")

# 📊 Load data
data_path = os.path.join(os.path.dirname(__file__), "..", "data", "student_performance.csv")
df = pd.read_csv(data_path)

# 📌 Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", [
    "Dashboard",
    "Comparison",
    "Recommendations"
])

# 👤 Select student
students = df[["student_id","student_name"]].drop_duplicates()
display = students["student_name"] + " (ID: " + students["student_id"].astype(str) + ")"

selected = st.sidebar.selectbox("Select Student", display)
student_id = int(selected.split("ID: ")[1].replace(")", ""))

analysis = analyze_student(df, student_id)

# 🔴 Weak subject
weak_subject = min(analysis, key=lambda x: analysis[x]["average"])

# ================= DASHBOARD =================
if page == "Dashboard":

    st.title("🎓 Student Dashboard")

    overall_avg = sum([d["average"] for d in analysis.values()]) / len(analysis)

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Score", round(overall_avg,2))
    col2.metric("Risk Level", risk_level(overall_avg))

    all_scores = []
    for d in analysis.values():
        all_scores.extend(d["scores"])

    col3.metric("Predicted Score", predict_next_score(all_scores[:3]))

    st.markdown("---")

    st.subheader("📊 Subject Performance")

    cols = st.columns(2)
    i = 0

    for sub, data in analysis.items():
        with cols[i % 2]:

            dfc = pd.DataFrame({
                "Test Number": [1,2,3],
                "Score": data["scores"]
            })

            fig = px.line(
                dfc,
                x="Test Number",
                y="Score",
                markers=True,
                title=f"{sub} Performance"
            )

            st.plotly_chart(fig, use_container_width=True)

            # Highlight weak subject
            if sub == weak_subject:
                st.error(f"{sub} → Weak | Avg: {round(data['average'],2)} | {data['trend']}")
            else:
                st.info(f"{sub} | Avg: {round(data['average'],2)} | {data['trend']}")

        i += 1

# ================= COMPARISON =================
elif page == "Comparison":

    st.title("📊 Student Comparison")

    pivot = df.groupby(["student_name","subject"])["score"].mean().reset_index()

    fig2 = px.bar(
        pivot,
        x="student_name",
        y="score",
        color="subject",
        barmode="group",
        title="Performance Comparison"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ================= RECOMMENDATIONS =================
elif page == "Recommendations":

    st.title("📚 Learning Strategy")

    recs, weak = recommend_path(analysis)

    st.warning(f"Focus most on: {weak}")

    for r in recs:
        st.markdown(f"### 📘 {r['subject']}")
        st.write(f"**Topics:** {r['topics']}")
        st.write(f"**Action:** {r['action']}")
        st.write(f"[▶ Watch Video]({r['youtube']})")

        file_path = os.path.join(os.path.dirname(__file__), "..", "resources", r["pdf"])

        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                st.download_button("📥 Download Notes", f, file_name=r["pdf"])

        st.markdown("---")