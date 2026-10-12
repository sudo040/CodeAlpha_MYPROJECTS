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