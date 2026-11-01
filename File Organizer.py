from pathlib import Path
import shutil
print("~~~~~~~~~ File Organizer~~~~~~~~~ ")
path = input("Enter the file path here: ")

file_list = []
if Path(path).exists():
    exist = True

else:
    exist = False

if exist == True:
    for file in Path(path).iterdir():
        if file.is_file():
            file_list.append(file)
        else:
            pass


filedata = []
for file in file_list:
    filedata.append(
        {"Name": file.name, "Extension": file.suffix, "path": file})


categories = {
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".mp4": "Videos",
    ".mp3": "Audio",
    ".py": "Programs"
}

for file in filedata:
    extension = file["Extension"]
    category = categories.get(extension, "Others")
    file["Category"] = category


print(filedata)

destination = Path(path) / "Organized"
destination.mkdir(parents=True, exist_ok=True)

available_categories = []
for type in filedata:

    file_category = type["Category"]
    if file_category not in available_categories:
        available_categories.append(file_category)
    else:
        pass

print(available_categories)

for folder in available_categories:
    location = Path(path) / "Organized" / folder
    location.mkdir(parents=True, exist_ok=True)

for file in filedata:
    source = file["path"]
    target = destination / file["Category"] / file["Name"]
    shutil.move(str(source), str(target))
