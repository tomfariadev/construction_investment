import streamlit as st
import plotly.express as px
from i18n import get_translations

def generate_graphics(df):
    # translations config
    if "lang" not in st.session_state:
        st.session_state.lang = "en"

    lang = st.sidebar.selectbox(
        "Language / Idioma", 
        ["en", "pt"],
        index=["en","pt"].index(st.session_state.lang),
        key="lang_selector"
    )
    st.session_state.lang = lang
    t = get_translations(lang)

    st.title(t["title"])

    with st.expander(f"ℹ️ {t["about_title"]}"):
        st.markdown(t["about_text"])

    # sidebar
    st.sidebar.markdown("---")
    # year
    if "year" not in st.session_state:
        st.session_state.year = df["year"].max()

    year = st.sidebar.selectbox(
        t["year"], 
        sorted(df["year"].unique()),
        key="year"
    )
    st.sidebar.markdown("---")
    # construction investment
    if "construction_filter" not in st.session_state:
        st.session_state.construction_filter = list(df["construction_investment"].unique())

    construction_investment = st.sidebar.multiselect(
        label=t["construction_type"],
        options=sorted(df["construction_investment"].unique()),
        key="construction_filter")
    st.sidebar.markdown("---")

    # value
    if "value_filter" not in st.session_state:
        st.session_state.value_filter = list(df["value"].unique())

    value = st.sidebar.multiselect(
        label=t["value"],
        options=sorted(df["value"].unique()),
        key="value_filter")
    st.sidebar.markdown("---")

    ### Filters ###
    df_filtered = df[
        (df["year"] == year) &
        (df["construction_investment"]).isin(construction_investment) &
        (df["value"].isin(value))
    ]

    if df_filtered.empty:
        st.warning(t["no_data"])
        st.stop()
    
    ### Metrics ###
    with st.container(border=True):
        met1,met2,met3,met4 = st.columns(4)

        # 1
        total_sales = df_filtered["total"].sum()
        
        with met1:
            st.metric(f"{t["total_investment"]} {t["in"]} {year}", f"${total_sales:,.2f}")

        # 2
        last_year_total = df[df["year"] == year - 1]["total"].sum()
        
        if last_year_total > 0:
            growth = (total_sales - last_year_total) / last_year_total * 100
        else:
            growth = 0

        with met2:
            st.metric(f"{t["growth"]}", f"{growth:.2f}%", delta=f"{growth:.2f}%")

        # 3
        architecture = df_filtered["architecture_total"].sum()
        perc_arch = (architecture / total_sales * 100) if total_sales else 0

        with met3:
            st.metric(f"{t["architecture"]}",f"{perc_arch:.2f}%")

        # 4
        civil = df_filtered["civil_engineering_total"].sum()
        perc_civil = (civil / total_sales * 100) if total_sales else 0
        with met4:
            st.metric(f"{t["civil_engineering"]}",f"{perc_civil:.2f}%")

    ### Graphics ###
    # 1
    with st.container(border=True):
        fig_gov = px.bar(
            df,
            x="year",
            y=["repeated_total_government", "repeated_total_private"],
            labels={
                "year": "Year",
                "repeated_total_government": "Government",
                "repeated_total_private": "Private",
                "value": "Investment ($)" 
            },
            title=f"1. {t["gov_vs_private"]}"
        )
        fig_gov.update_layout(
            legend_title_text="Sector",
            xaxis_title="Year",
            yaxis_title="Investment ($)"
        )
        fig_gov.for_each_trace(
            lambda t: t.update(name=t.name.replace("repeated_total_", "").capitalize())
        )
        st.plotly_chart(fig_gov, width="stretch")
    

    with st.container(border=True):
        col1, col2 = st.columns(2)
        # 2
        fig_res = px.bar(
            df,
            x="year",
            y=["architecture_residential", "architecture_non_residential"],
            barmode="group",
            labels={"architecture_residential":"Residential","architecture_non_residential":"Non Residential"},
            title=f"2. {t["res_vs_nonres"]}"
        )
        fig_res.update_layout(
            legend_title_text="Type",
            xaxis_title="Year",
            yaxis_title="Investment ($)"
        )
        fig_res.for_each_trace(
            lambda t: t.update(name=t.name.replace("architecture_", "").capitalize())
        )
        col1.plotly_chart(fig_res, width="stretch")

        # 3
        fig_invest = px.line(
            df,
            x="year",
            y="architecture_non_residential_private_mining_and_industry",
            labels={
                "year":"Year",
                "architecture_non_residential_private_mining_and_industry": ""
            },
            title=f"3. {t["industry"]}"
        )
        col2.plotly_chart(fig_invest, width="stretch")

    # 4
    with st.container(border=True):
        fig_repair = px.area(
            df,
            x="year",
            y=[
                "architecture_building_repairs(renovation or remodeling)",
                "architecture_total"
            ],        
            labels={
                "year":"Year",
                "architecture_building_repairs(renovation or remodeling)":"Renovation",
                "architecture_total":"Total"
            },
            title=f"4. {t["repairs"]}"
        )
        fig_repair.update_layout(
            legend_title_text="Type",
            xaxis_title="Year",
            yaxis_title=""
        )
        fig_repair.for_each_trace(
            lambda t: t.update(name=t.name.replace("_", " ").capitalize())
        )
        st.plotly_chart(fig_repair, width="stretch")