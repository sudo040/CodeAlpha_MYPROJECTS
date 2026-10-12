# JPG File Mover

A small Python script that moves all `.jpg` files from one folder into another. It's a simple example of task automation with the `os` and `shutil` modules.

## Features

- Moves every `.jpg` file from a source folder to a destination folder
- Matches both `.jpg` and `.JPG` (case-insensitive)
- Skips subfolders and non-JPG files
- Creates the destination folder automatically if it doesn't exist
- Avoids overwriting existing files by renaming duplicates (e.g., `photo_1.jpg`)
- Prints a summary of how many files were moved

## Requirements

- Python 3.6 or newer
- No third-party packages needed (uses only the standard library)

## Installation

No installation is required. Save the script as `move_jpgs.py`:

```python
import os
import shutil


def move_jpg_files(source_folder, destination_folder):
    """Move all .jpg files from source_folder into destination_folder."""
    if not os.path.isdir(source_folder):
        print(f"Error: source folder '{source_folder}' does not exist.")
        return

    # Create the destination folder if it doesn't exist yet
    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Skip subfolders and non-jpg files
        if not os.path.isfile(source_path):
            continue
        if not filename.lower().endswith(".jpg"):
            continue

        destination_path = os.path.join(destination_folder, filename)

        # Avoid overwriting: if a file with the same name exists, add a number
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(destination_path):
            destination_path = os.path.join(destination_folder, f"{base}_{counter}{ext}")
            counter += 1

        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")
        moved_count += 1

    print(f"\nDone. Moved {moved_count} .jpg file(s) to '{destination_folder}'.")


if __name__ == "__main__":
    source = input("Enter the source folder path: ").strip()
    destination = input("Enter the destination folder path: ").strip()
    move_jpg_files(source, destination)
```

## Usage

Run the script from the terminal:

```bash
python move_jpgs.py
```

You'll be prompted for two paths:

```
Enter the source folder path: /home/user/Pictures/Downloads
Enter the destination folder path: /home/user/Pictures/Sorted
```

Example output:

```
Moved: vacation.jpg
Moved: sunset.JPG
Moved: vacation_1.jpg

Done. Moved 3 .jpg file(s) to '/home/user/Pictures/Sorted'.
```

## How It Works

1. `os.listdir()` lists the contents of the source folder.
2. `os.path.isfile()` filters out subfolders.
3. `filename.lower().endswith(".jpg")` selects JPG files regardless of case.
4. `os.makedirs(..., exist_ok=True)` creates the destination folder if needed.
5. A `while` loop checks for name collisions and appends a counter when a file already exists.
6. `shutil.move()` moves each file to its new location.

## Notes

- Files are **moved**, not copied, so they are removed from the source folder.
- Only files directly inside the source folder are processed. Subfolders are not searched recursively.
- Only the `.jpg` extension is matched. Files ending in `.jpeg` are not moved.

## Possible Extensions

- Add `.jpeg` support by checking `filename.lower().endswith((".jpg", ".jpeg"))`
- Add a dry-run mode that prints what would move without moving anything
- Accept folder paths as command-line arguments using `sys.argv` or `argparse`

## License

This project is free to use for learning and personal purposes.
