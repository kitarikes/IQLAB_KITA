import os
import uuid

def save_file(uploaded_file):
    if uploaded_file is not None:
        file_name = f"{uuid.uuid4()}_{uploaded_file.name}"
        file_path = os.path.join('./storage/', file_name)

        if not os.path.exists('./storage/'):
            os.makedirs('./storage/')

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        return file_path
    return None
