import streamlit as st
import data_loader as dl
import data_cleaning as dc
import graphics as gr
import os

st.set_page_config(layout="wide")

def main():
    path = os.path.dirname(__file__)
    file = os.path.join(path, "data", "Construction_investment_amount_in_japan.csv")
        
    df_raw = dl.load_data(file,",")

    df_clean = dc.clean_data(df_raw)

    gr.generate_graphics(df_clean)
    
if __name__ == "__main__":
    main()