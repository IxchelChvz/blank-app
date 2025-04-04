import streamlit as st

pages = {
    "Resources": [
        st.Page("home.py", title="Home"),
        st.Page("page1.py", title="BMI Tracker"),
        st.Page("page2.py", title="Workout Logger"),
    ]
}

pg = st.navigation(pages)
pg.run()
