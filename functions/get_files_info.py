import os

def get_files_info(working_directory, directory=None):
    if directory == ".":
        absolute_dir_path = os.path.abspath(working_directory)
    else:
        absolute_dir_path = os.path.abspath(os.path.join(working_directory, directory))
    absolute_pwd_path = os.path.abspath(working_directory)
    if not absolute_dir_path.startswith(absolute_pwd_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    elif not os.path.isdir(absolute_dir_path): 
        return f'Error: "{directory}" is not a directory'
    
    else:
        try:
            result = []
            directory_items = os.listdir(absolute_dir_path)

            for item in directory_items:
                item_path = os.path.join(absolute_dir_path,item)
                get_size = os.path.getsize(item_path)
                if os.path.isfile(item_path):
                    is_dir = False
                else:
                    is_dir = True
                result.append(f"- {item}: file_size={get_size} bytes, is_dir={is_dir}")
        except Exception as e:
            return f"Error: {e}"

    return "\n".join(result)

