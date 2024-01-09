from pathlib import Path
import shutil


COLOR_BLUE = "\u001b[34m"
COLOR_GREEN = "\u001b[32m"
COLOR_RED = "\u001b[31m"


def pars_input(user_input1, user_input2):
    source_path = user_input1
    destination_path = user_input2
    return source_path, destination_path


def file_sorter(source_path, destination_path):
    source_path = Path(source_path)
    if destination_path == "":
        destination_path = Path(source_path/"dist")
    else:
        destination_path = Path(destination_path)

    for child in source_path.iterdir(): 
        if child.is_dir():
            file_sorter(child, destination_path)
        elif child.is_file():
            copy_file(child, destination_path)


def copy_file(file, destination_path):
    destination_path.mkdir(parents=False, exist_ok=True)
    destination_file = destination_path/file.suffix
    destination_file.mkdir(parents=True, exist_ok=True)

    try:
        shutil.copy(file, destination_file)
        print(COLOR_BLUE + f"Copied {file.name} to {destination_file}.")
    except Exception as e:
        print(COLOR_RED + f"Error copying {file.name}: {e}")


def main():
    user_input1 = input("Enter the source path: ")
    user_input2 = input("Enter the destination path(optional): ")
    source_path, destination_path = pars_input(user_input1, user_input2)
    try:
        file_sorter(source_path, destination_path)
        print(COLOR_GREEN + "Sorting files into folders has been completed successfully.")
    except Exception as e:
        print(COLOR_RED + f"Error: {e}")


if __name__ == "__main__":
    main()
