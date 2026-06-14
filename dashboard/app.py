import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Vehicle Tracking Dashboard",
    layout="wide"
)

st.title("🚗 IoT Vehicle Tracking Dashboard")

try:

    df = pd.read_csv(
        "data/vehicle_logs.csv"
    )

    st.dataframe(df.tail(20))

    st.subheader("Location Map")

    st.map(
        df[
            ["latitude","longitude"]
        ]
    )

    st.subheader("Vehicle Path")

    fig = px.line_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        zoom=10,
        height=500
    )

    fig.update_layout(
        mapbox_style="open-street-map"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Status Count")

    st.bar_chart(
        df["status"].value_counts()
    )

except Exception as e:

    st.error(str(e))