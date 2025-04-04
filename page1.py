import streamlit as st
import pandas as pd

if "bmi_data" not in st.session_state:
        st.session_state["bmi_data"] = []

st.title("📏MBI Tracker")

altura = st.number_input("Enter your height (cm)", min_value=1)
peso = st.number_input("Enter your weight (kg)", min_value=1, max_value=100)

resultado = None

calcular = st.button("Calcular", type="primary")
if calcular:
    resultado = peso / ((altura / 100) ** 2) 
    st.success("Tu BMI es: " + str(round(resultado, 2)))  


st.write("✅Tu BMI fue guardado")

st.subheader("📊BMI Progress")

if resultado is not None:
    data_df = pd.DataFrame({"BMI": [resultado]}) 
    st.session_state["bmi_data"].append({"BMI": resultado})
    data_df = pd.DataFrame(st.session_state["bmi_data"])
    st.data_editor(
        data_df,
        column_config={
            "BMI": st.column_config.AreaChartColumn("BMI", width="medium",help="Tus BMI", y_min=0,y_max=100,),
        },
        hide_index=True,
    )

    


