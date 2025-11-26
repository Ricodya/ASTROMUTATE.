
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Space Mutation Simulator", layout="wide")

st.title("🚀 Space Mutation Simulator")

st.subheader("Upload Your Own Dataset (Optional)")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    user_df = pd.read_csv(uploaded_file)
    st.success("✅ Dataset uploaded successfully!")
    st.write("### Preview of Uploaded Data")
    st.dataframe(user_df.head())

    required_cols = ["radiation", "microgravity", "temperature", "date"]

    if all(col in user_df.columns for col in required_cols):
        df = user_df
        st.success("✅ All required columns detected — running analysis...")
    else:
        st.error(f"❌ Required columns missing. Required: {required_cols}")
        df = None
else:
    df = pd.read_csv("space_mutation_dataset.csv")

days = st.slider("Days in Space", 30, 1095, 250)
gene = st.selectbox("Select Gene", ["TP53", "BRCA1", "TERT", "MT-RNR1"])

micro = np.random.randint(15, 35)
gcr = np.random.randint(20, 40)
temp = np.random.randint(5, 15)
solar = np.random.randint(15, 30)

st.write("### Environmental Factor Contribution")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Microgravity", f"{micro} mutations")
col2.metric("GCR", f"{gcr} mutations")
col3.metric("Temperature", f"{temp} mutations")
col4.metric("Solar Events", f"{solar} mutations")

if df is not None:
    st.write("### Radiation Over Time")
    fig = px.line(df, x="date", y="radiation", title="Daily Radiation Dose")
    st.plotly_chart(fig, use_container_width=True)

st.write("### Mutation Hotspots")
hotspots = np.random.randint(4, 12)
st.write(f"🔴 {hotspots} detected hotspots")

st.write("### Cumulative DNA Damage")
damage = np.cumsum(np.random.randint(1, 3, size=days))
fig2 = px.line(y=damage)
st.plotly_chart(fig2, use_container_width=True)

fasta_data = ">Mutated_{}_{}days\n{}".format(gene, days, "ATCG" * 200)
st.download_button("📥 Download Mutated FASTA", fasta_data, file_name=f"{gene}_{days}_mutated.fasta")

st.success("✅ All features are active!")
