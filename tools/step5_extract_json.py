import os
import json

source_folder_path = "train_poseimg"
target_folder_path = "train_img"
source_dirs = os.listdir(source_folder_path)
target_dirs = os.listdir(target_folder_path)

json_list = []
source_image_paths = []
target_image_paths = []

for folder in source_dirs:
    folder_path = os.path.join(source_folder_path + "/" + folder)
    if os.path.isdir(folder_path):
        source_images = os.listdir(folder_path)
        for image_name in source_images:
            #source_image_paths.append(os.path.join(folder_path, image_name))
            source_image_paths.append(folder_path + "/" + image_name)

for folder in target_dirs:
    folder_path = os.path.join(target_folder_path + "/" + folder)
    if os.path.isdir(folder_path):
        target_images = os.listdir(folder_path)
        for image_name in target_images:
            #target_image_paths.append(os.path.join(folder_path, image_name))
            target_image_paths.append(folder_path + "/" + image_name)

if (len(source_image_paths) == len(target_image_paths)):
    print(f"len(source_image_paths) is {len(source_image_paths)}"
          f"len(target_image_paths) is {len(target_image_paths)}"
          f"Len are same")
    with open("prompt.json", "w") as f:
        for i in range(len(source_image_paths)):
            # Construct file path
            source_path = source_image_paths[i]
            target_path = target_image_paths[i]
            # Read picture information
            source_info = {"source": source_path}
            target_info = {"target": target_path}
            # Construct the JSON object and add it to the list
            json_obj = {**source_info, **target_info, "prompt": "A person demonstrates sign language in front of a green background, realistic"}
            f.write(json.dumps(json_obj) + "\n")

else:
    print(f"len(source_image_paths) is {len(source_image_paths)}"
          f"len(target_image_paths) is {len(target_image_paths)}"
          f"Len are not equal")
