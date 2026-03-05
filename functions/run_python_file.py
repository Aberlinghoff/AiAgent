import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, file_path))
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path

        if not valid_target_dir:
            error_str = f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            return error_str
        elif not os.path.isfile(target_dir):
            error_str = f'Error: "{file_path}" does not exist or is not a regular file'
            return error_str
        elif not target_dir.endswith(".py"):
            error_str = f'Error: "{file_path}" is not a Python file'
            return error_str
        else:
            command = ["python", target_dir]
            if args:
                command.extend(args)
            result = subprocess.run(
                command,
                cwd=abs_path,
                capture_output=True,
                text=True,
                timeout=30)
            output = []
            if result.returncode != 0:
                output.append(f"Process exited with code {result.returncode}")
            if not result.stdout and not result.stderr:
                output.append("No output produced")
            if result.stdout:
                output.append(f"STDOUT:\n{result.stdout}")
            if result.stderr:
                output.append(f"STDERR:\n{result.stderr}")

            new_output ="\n".join(output)
            return new_output




    except Exception as e:
        return f"Error: executing Python file: {e}"
