import os


def get_files_info(working_directory, directory="."):
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
        if not valid_target_dir:
            error_str = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            return error_str

        if not os.path.isdir(target_dir):
            error_str = f'Error: "{directory}" is not a directory'
            return error_str

        string_list = []

        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)
            string_list.append(f"- {filename}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
        return "\n".join(string_list)
    except Exception as e:
        return F"Error: {e}"