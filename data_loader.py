import streamlit as st
import pandas as pd

@st.cache_data
def load_data(file: str, sep: str = ";") -> pd.DataFrame:
    df = pd.read_csv(file, sep = sep)
    return df