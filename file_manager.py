from pathlib import Path
import shutil
import argparse


COLOR_BLUE = "\u001b[34m"
COLOR_GREEN = "\u001b[32m"
COLOR_RED = "\u001b[31m"


def file_sorter(source_path, destination_path):
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
    parser = argparse.ArgumentParser(description="Copy and organize files based on file extensions.")
    parser.add_argument("source_path", type=Path, help="Source directory path")
    parser.add_argument("destination_path", nargs="?", type=Path, default=None, help="Destination directory path (default: 'dist' in the source directory)")
    args = parser.parse_args()

    if args.destination_path is None:
        args.destination_path = args.source_path / "dist"

    try:
        file_sorter(args.source_path, args.destination_path)
        print(COLOR_GREEN + "Sorting files into folders has been completed successfully.")
    except Exception as e:
        print(COLOR_RED + f"Error: {e}")


if __name__ == "__main__":
    main()
