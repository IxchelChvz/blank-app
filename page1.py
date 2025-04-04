import streamlit as st
import pandas as pd
import os

# Cargar datos desde CSV si existe
if 'bmi' not in st.session_state:
    if os.path.exists("BMI.csv"):
        st.session_state['bmi'] = pd.read_csv("BMI.csv", index_col=0)
    else:
        st.session_state['bmi'] = pd.DataFrame(columns=["weight", "height", "BMI"])

st.title("📏 BMI Tracker")

# Inputs
peso = st.number_input("Introduce tu peso (kg)", min_value=1, value=50)
altura = st.number_input("Introduce tu altura (cm)", min_value=1, value=100)

# Calcular y guardar BMI
if st.button("Calcula tu BMI", type="primary"):
    BMI = peso / ((altura / 100) ** 2)
    new_row = {"peso": peso, "altura": altura, "BMI": round(BMI, 2)}
    st.session_state['bmi'] = pd.concat([st.session_state['bmi'], pd.DataFrame([new_row])],ignore_index=True)
    st.session_state['bmi'].to_csv("BMI.csv")
    st.success(f"Tu BMI es: {round(BMI, 2)}")
    st.write("✅Tu BMI fue guardado")

# Progreso del BMI
st.subheader("📈 BMI Progreso")
st.line_chart(st.session_state['bmi'], y="BMI")