import os
import shutil

# Source and Destination folder paths
source_f = "source_folder"
destination_f = "Destination_folder"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_f):
    os.makedirs(destination_f)

# Move all .jpg files
for file in os.listdir(source_f):
    if file.endswith(".jpg"):
        source_path = os.path.join(source_f, file)
        destination_path = os.path.join(destination_f, file)

        shutil.move(source_path, destination_path)
        print(file, " \n moved successfully.")

print("\nAll JPG files moved successfully.")