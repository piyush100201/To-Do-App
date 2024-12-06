import streamlit as st
import functions


st.title("My Todo App")
st.subheader("This is my todo app.")

st.checkbox("Buy grocery")

todos = functions.read_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label = "", placeholder = "Add a new todo..." )