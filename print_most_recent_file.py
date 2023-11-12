import os
import glob

folder_path = "C:/Users/kg7481ty/Downloads/"  # Replace with the actual path to your folder

# Get a list of all files in the folder
files = glob.glob(os.path.join(folder_path, "*"))

# Sort the files by modification time (most recent first)
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)


# Check if there are any files in the folder
if files:
    most_recent_file = files[0]
    fileath = most_recent_file.replace(f'\\',"/" )
    print(fileath)
else:
    print("The folder is empty.")
