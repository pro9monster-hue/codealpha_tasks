import os
import shutil

SOURCE_DIR = "source_folder"
DEST_DIR = "destination_folder"

def move_jpg_files():
    print(f"Starting to move .jpg files from '{SOURCE_DIR}' to '{DEST_DIR}'...")
    
    if not os.path.isdir(SOURCE_DIR):
        print(f"Error: Source directory '{SOURCE_DIR}' does not exist.")
        return

    os.makedirs(DEST_DIR, exist_ok=True)
    
    files_moved_count = 0

    for item in os.listdir(SOURCE_DIR):
        source_path = os.path.join(SOURCE_DIR, item)
        
        if os.path.isfile(source_path) and item.lower().endswith(('.jpg', '.jpeg')):
            destination_path = os.path.join(DEST_DIR, item)
            
            try:
                shutil.move(source_path, destination_path)
                print(f"Moved: {item}")
                files_moved_count += 1
            except Exception as e:
                print(f"Failed to move {item}: {e}")

    print(f"\nProcess complete. Total files moved: {files_moved_count}")

if __name__ == "__main__":
    move_jpg_files()
