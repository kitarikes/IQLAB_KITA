import streamlit as st
from storage import add_task
from file_manager import save_file
import uuid

st.title("学生用資料アップロードフォーム")


def show_student_ui():
    with st.form("upload_form"):
        student_name = st.text_input("名前")
        title = st.text_input("タイトル")
        content = st.text_area("内容")
        deadline = st.date_input("締切日（発表日）")
        file = st.file_uploader("資料をアップロード", type=['pdf', 'docx', 'pptx'])
        submit_button = st.form_submit_button("アップロード")

        if submit_button and file is not None:
            file_path = save_file(file)
            task_id = str(uuid.uuid4())
            task_data = {
                'task_id': task_id,
                'student_name': student_name,
                'title': title,
                'content': content,
                'deadline': deadline,
                'file_path': file_path,
                'status': False
            }
            add_task(task_data)
            st.success("資料がアップロードされました！")
