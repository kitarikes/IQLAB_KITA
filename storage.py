import pandas as pd

CSV_FILE_PATH = 'storage.csv'

def load_tasks():
    try:
        return pd.read_csv(CSV_FILE_PATH)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return pd.DataFrame(columns=['task_id', 'student_name', 'title', 'content', 'deadline', 'file_path'])

def add_task(task_data):
    df = load_tasks()
    new_df = pd.DataFrame([task_data])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv(CSV_FILE_PATH, index=False)

def update_task(task_id, updated_data):
    df = load_tasks()
    index = df.index[df['task_id'] == task_id]
    if not index.empty:
        for key, value in updated_data.items():
            df.at[index[0], key] = value
    df.to_csv(CSV_FILE_PATH, index=False)
