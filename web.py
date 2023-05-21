import streamlit as st
from functions import get_todos,create_file,write_todo


#FILEPATH = "udemy_python/files/todoss.txt"
FILEPATH = "todoss.txt"
create_file(FILEPATH)

todos = get_todos(FILEPATH)

#st.set_page_config(layout='wide')

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    write_todo(todos, FILEPATH)
    st.session_state["new_todo"] = ""


st.title("My ToDo App")
st.subheader("This is My Todo App")
st.write("This app is for you to help <b>record</b> of things to do.",)
#For html use unsafe_allow_html=True in st.write
for index, todo in enumerate(todos):
    Checkbox = st.checkbox(todo, key=todo)
    if Checkbox:
        todos.pop(index)
        write_todo(todos, FILEPATH)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input('todo_add', label_visibility='hidden', placeholder="Add new todo....",
              on_change=add_todo, key='new_todo')
