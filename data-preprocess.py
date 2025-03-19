# 1. Name the imgs and labels
import os


def match_img_lbl(image_dir, label_dir):
    image_names = sorted(
        [f.replace(".jpg", "") for f in os.listdir(image_dir) if
         f.endswith(".jpg")])
    label_names = sorted(
        [f.replace(".txt", "") for f in os.listdir(label_dir) if
         f.endswith(".txt")])

    extra_labels = set(label_names) - set(image_names)
    extra_images = set(image_names) - set(label_names)

    # Prints and remove files that do not match
    if extra_labels:
        print(
            f"{len(extra_labels)} additional label/txt files (no corresponding picture) in {label_dir}: {extra_labels}")
        for file in extra_labels:
            remove_file = os.path.join(label_dir, f"{file}.txt")
            os.remove(remove_file)
            print(f"Removed extra label files: {remove_file}")
    if extra_images:
        print(
            f"{len(extra_images)} additional image/jpg files (without corresponding labels) in {image_dir}: {extra_images}")
        for file in extra_images:
            remove_file = os.path.join(image_dir, f"{file}.jpg")
            os.remove(remove_file)
            print(f"Removed extra label files: {remove_file}")

    if len(os.listdir(image_dir)) == len(os.listdir(label_dir)):
        print(
            f"Now directories {image_dir} and {label_dir} matched - {len(image_names)} items.\n")


def rename_files(image_dir, label_dir):
    image_files = sorted(
        [f for f in os.listdir(image_dir) if f.endswith(".jpg")])
    label_files = sorted(
        [f for f in os.listdir(label_dir) if f.endswith(".txt")])

    if len(image_files) != len(label_files):
        print(
            f"The number of pictures and labels does not match: {len(image_files)} vs {len(label_files)}")
        match_img_lbl(image_dir, label_dir)
        return

    for i, (img_file, lbl_file) in enumerate(zip(image_files, label_files),
                                             start = 1):
        new_img_name = f"img{i}.jpg"
        new_lbl_name = f"img{i}.txt"

        os.rename(os.path.join(image_dir, img_file),
                  os.path.join(image_dir, new_img_name))
        os.rename(os.path.join(label_dir, lbl_file),
                  os.path.join(label_dir, new_lbl_name))

    print(
        f"{image_dir} ({len(image_files)} items) and {label_dir} ({len(label_files)} items) directory rename complete!")


dataset_path = "./TXL_PBC"
splits = ["train", "val", "test"]

for split in splits:
    print(split)
    image_dir = os.path.join(dataset_path, "images", split)
    label_dir = os.path.join(dataset_path, "labels", split)
    rename_files(image_dir, label_dir)
    # print(f"{split} - img: {len(os.listdir(image_dir))}, label: {len(os.listdir(label_dir))}\n")

print("All data set files have been renamed!")


# 2. Read classes.txt and print the classes information
classes_file_path = "./TXL_PBC/labels/classes.txt"

with open(classes_file_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

print("Classes of the dataset:")
for i, class_name in enumerate(classes):
    print(f"{i}: {class_name}")
