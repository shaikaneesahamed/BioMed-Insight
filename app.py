import streamlit as st
from analysis.ecg import analyze_ecg

st.set_page_config(page_title="BioMed Insight", page_icon="🧬", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🧬 BioMed Insight</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Biomedical Signal Analysis Platform</p>", unsafe_allow_html=True)

signal = st.selectbox(
    "Select Biomedical Signal",
    ["-- Select --", "ECG", "EEG"]
)

if signal == "ECG":
    file = st.file_uploader("Upload ECG CSV File", type=["csv"])
    if file:
        analyze_ecg(file)
