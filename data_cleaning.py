import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.replace(",", "", regex=True)
    df = df.apply(pd.to_numeric, errors="ignore")
    df.columns = df.columns.str.lower().str.strip()
    df["year"] = df["year"].astype(int)

    return df