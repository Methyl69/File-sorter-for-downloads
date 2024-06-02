import os ,shutil
path = r"C:\Users\User\Downloads\\"  #edit path if your path to download is different
file_name  = os.listdir(path)
folder_names = ["vids", "pics", "gifs", "pdfs"]
for folder in folder_names:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        print(folder_path)
        os.makedirs(folder_path)

for file in file_name:
    file_path = os.path.join(path, file)
    if file.endswith(".mp4") and not os.path.exists(os.path.join(path, "vids", file)):
        shutil.move(file_path, os.path.join(path, "vids", file))
    elif (file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".webp")) and not os.path.exists(os.path.join(path, "pics", file)):
        shutil.move(file_path, os.path.join(path, "pics", file))
    elif file.endswith(".gif") and not os.path.exists(os.path.join(path, "gifs", file)):
        shutil.move(file_path, os.path.join(path, "gifs", file))
    elif (file.endswith(".pdf") or file.endswith(".xlsx") or file.endswith(".pptx") or file.endswith(".docx")) and not os.path.exists(os.path.join(path, "pdfs", file)):
        shutil.move(file_path, os.path.join(path, "pdfs", file))
