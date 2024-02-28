import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"]
    todos = functions.get_todos()
    todos.append(todo + "\n")
    functions.write_todos(todos)


todos = functions.get_todos()
st.title("My TODO App")
st.subheader("this is my to do app")
st.write("some text here to test")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,  key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="Add new todo...",on_change=add_todo,key="new_todo")
st.session_state
print("Hello1")
