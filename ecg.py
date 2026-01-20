import pandas as pd
import streamlit as st
import plotly.express as px
from scipy.signal import find_peaks

def analyze_ecg(file):
    df = pd.read_csv(file)
    signal = df.iloc[:,1]

    st.subheader("📈 ECG Signal")
    fig = px.line(signal)
    st.plotly_chart(fig, use_container_width=True)

    peaks, _ = find_peaks(signal, distance=150)
    hr = len(peaks) * 60 / (len(signal) / 250)

    st.subheader("🩺 Results")
    st.metric("Heart Rate", f"{int(hr)} BPM")

    if hr < 60:
        st.error("Low Heart Rate")
        st.info("Precaution: Avoid heavy exercise, consult doctor.")
    elif hr > 100:
        st.error("High Heart Rate")
        st.info("Precaution: Reduce stress, proper hydration.")
    else:
        st.success("Normal Heart Rate")
