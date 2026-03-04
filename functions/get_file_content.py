import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
     try:
          abs_path = os.path.abspath(working_directory)
          target_dir = os.path.normpath(os.path.join(abs_path,file_path))
          valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
          if not valid_target_dir:
              error_str = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
              return error_str
          elif not os.path.isfile(target_dir):
              error_str = f'Error: File not found or is not a regular file: "{file_path}"'
              return error_str

          with open(target_dir, "r") as f:
              file_content_string = f.read(MAX_CHARS)
              if f.read(1):
                  file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                  return file_content_string
              return file_content_string
     except Exception as e:
          error_str = f'Error: {e}'
          return error_str