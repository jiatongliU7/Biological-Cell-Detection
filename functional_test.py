from ultralytics import YOLO
import matplotlib.pyplot as plt
import shutil
import cv2
import os


model = YOLO("runs/detect/train/weights/best.pt")

# Directory for storing prediction results
predict_dir = "./functional_test_data/predict/"
if os.path.exists(predict_dir):
    shutil.rmtree(predict_dir)
    print("Delete previous predict_dir: ./functional_test_data/predict/")

results = model.predict(source="./functional_test_data/small_test_data", save=True, project="./functional_test_data", name="predict")

num_predictions = len(results)

class_names = model.names

print(f"\nTotal number of test data sets: {num_predictions}")
print(f"Class names: {class_names}")

# Go through each test img, print the prediction and display the picture
for i, result in enumerate(results):
    img_name = os.path.basename(result.path)
    pred_img_path = os.path.join(predict_dir, img_name)

    print(f"\ntest img {img_name}:")
    
    # Get prediction categories and confidence levels
    for box in result.boxes:
        class_id = int(box.cls)
        confidence = box.conf.item()
        print(f"Class prediction: {class_names[class_id]} (Confidence: {confidence:.2f})")

    # Display prediction
    if os.path.exists(pred_img_path):
        pred_img = cv2.imread(pred_img_path)
        pred_img = cv2.cvtColor(pred_img, cv2.COLOR_BGR2RGB)

        plt.figure(figsize = (6, 6))
        plt.imshow(pred_img)
        plt.axis("off")
        plt.title(f"Predicted Image: {img_name}")
        plt.show()
    else:
        print(f"Predicted image not found: {pred_img_path}")

    if i >= 4:
        print(f"Only the first 5 predicted images are shown... The completed test result images are saved in the directory '{predict_dir}'")
        break
