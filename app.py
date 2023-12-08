import streamlit as st
from student_ui import show_student_ui
from professor_ui import show_professor_ui

st.title("タスク管理アプリ")

# ユーザーのロールを選択させる
role = st.radio("あなたは？", ('学生', '教員'))

if role == '学生':
    show_student_ui()
elif role == '教員':
    show_professor_ui()
