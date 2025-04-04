import streamlit as st

pages = {
    "Resources": [
        st.Page("home.py", title="Home"),
        st.Page("page1.py", title="BMI Tracker"),
        st.Page("page2.py", title="Workout Logger"),
        st.Page("page3.py", title="Progess Tracker"),
    ]
}

pg = st.navigation(pages)
pg.run()
