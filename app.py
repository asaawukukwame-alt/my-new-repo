import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Vehicle Explorer")

# Load data in the project folder
df = pd.read_csv("vehicles_us.csv")

st.write("Rows:", len(df))

# Checkbox to filter prices
max50k = st.checkbox("Show only cars priced ≤ 50,000")
df_show = df[df["price"] <= 50_000] if max50k and "price" in df.columns else df

# Histogram
if "price" in df_show.columns:
    st.subheader("Price distribution")
    st.plotly_chart(px.histogram(df_show, x="price", nbins=50))

# Scatter
if {"odometer", "price"}.issubset(df_show.columns):
    st.subheader("Price vs Odometer")
    st.plotly_chart(px.scatter(df_show, x="odometer", y="price", opacity=0.5))
else:
    st.info("Add columns named 'price' and 'odometer' to see the scatter plot.")
