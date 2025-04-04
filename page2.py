import streamlit as st
import pandas as pd

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=[ "Date","Ejercicio", "Sets", "Reps", "Weight"])


with st.form("my_form", clear_on_submit=True):
    st.header("💪Workout Logger")
    
    ejercicio = st.text_input("Nombre del ejercicio", "Ejercicio")
    sets = st.number_input("Sets", min_value=1, max_value=100)
    reps = st.number_input("Reps", min_value=1, max_value=100)
    weight = st.number_input("Weight (kg)")
    date = st.date_input("Fecha")
    
    submit_button = st.form_submit_button("Log Workout")

    if submit_button:
        new_row = {"Date": date, "Ejercicio": ejercicio, "Sets": sets, "Reps": reps, "Weight": weight}
        st.session_state['data'] = pd.concat([st.session_state['data'], pd.DataFrame([new_row])], ignore_index=True)
        st.success(f"Rutina agregada correctamente!")

st.subheader("🏋️Workout History")
st.write(st.session_state['data'])





# data = pd.DataFrame({
#         "Date": [ p , "Valor2"],
#         "Exercise": ["Valor3", "Valor4"],
#         "Sets": ["Valor3", "Valor4"],
#         "Reps": ["Valor3", "Valor4"],
#         "Weight": ["Valor3", "Valor4"],
# })

# st.table(data)  