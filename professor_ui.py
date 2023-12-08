import streamlit as st
from storage import load_tasks, update_task

def show_professor_ui():
    st.title("教員用タスク一覧")
    
    if 'editing_task_id' not in st.session_state:
        st.session_state['editing_task_id'] = None

    tasks_df = load_tasks()
    tasks_df = tasks_df.sort_values(by='status', ascending=True)

    print(tasks_df)


    if not tasks_df.empty:
        for i, task in tasks_df.iterrows():
            completed = task.get('status')
            completed_label = "完了　" if completed else "未完了"

            # タスクカードのexpander
            with st.expander(f"{completed_label} | 締切日: {task['deadline']} | {task['title']}  (by {task['student_name']})"):
                st.markdown(f"--- 学生コメント ---")
                st.markdown(f"{task['content']}")
                st.markdown("</div>", unsafe_allow_html=True)
                
                # ボタンの配置
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.download_button(
                        label="資料ダウンロード",
                        data=task['file_path'],
                        file_name="dl.txt",
                        key=f"download_{task['task_id']}"
                    )
                with col2:
                    if st.button("編集", key=f"edit_{task['task_id']}"):
                        # 編集中のタスクIDを保存
                        st.session_state['editing_task_id'] = task['task_id']
                with col3:
                    if st.button("完了", key=f"complete_{task['task_id']}", disabled=completed):
                        update_task(task['task_id'], {'status': True})
                        st.success(f"タスク {task['task_id']} を完了済みとしてマークしました。")
                        st.experimental_rerun()
        
        # 編集フォームの表示
        if st.session_state['editing_task_id'] is not None:
            with st.form(key=f'edit_form_{st.session_state["editing_task_id"]}'):
                # 編集フォームの表示
                task_to_edit = tasks_df.loc[tasks_df['task_id'] == st.session_state['editing_task_id']].iloc[0]
                new_student_name = st.text_input("氏名", value=task_to_edit['student_name'])
                new_title = st.text_input("要件名", value=task_to_edit['title'])
                new_content = st.text_area("学生コメント", value=task_to_edit['content'])
                submit_button = st.form_submit_button("更新")

                if submit_button:
                    # フォームの送信が確認された場合のみ実行
                    update_task(st.session_state['editing_task_id'], {'student_name': new_student_name, 'content': new_content, 'title': new_title})
                    st.success(f"タスク {st.session_state['editing_task_id']} が更新されました。")
                    st.session_state['editing_task_id'] = None  # 編集状態をリセット
                    st.experimental_rerun()


    else:
        st.write("現在、表示するタスクはありません。")
