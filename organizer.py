import shutil
import os

target_folder = "path"
extensions = {
    item.split(".")[-1]
    for item in os.listdir(target_folder)
    if os.path.isfile(os.path.join(target_folder, item))
}
# print(extensions)

for exten in extensions:
    if not os.path.exists(os.path.join(target_folder, exten)):
        os.mkdir(os.path.join(target_folder, exten))


for item in os.listdir(target_folder):
    if os.path.isfile(os.path.join(target_folder, item)):
        file_exten = item.split(".")[-1]
        shutil.move(
            os.path.join(target_folder, item),
            os.path.join(target_folder, file_exten, item),
        )
