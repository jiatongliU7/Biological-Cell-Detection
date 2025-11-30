Bio-cell Detection with YOLOv8 on TXL-PBC Dataset

## **Project Goal**

The primary objective of this project is to train and evaluate a **YOLOv8n** model for detecting and classifying different blood cell types within the **TXL-PBC dataset**. The model is optimized for **bounding box detection**, aiming to achieve high **precision, recall, and mean Average Precision (mAP)**.

## Dataset

The TXL-PBC dataset, introduced by **Lu Gan and Xi Li** (TXL-PBC: a freely accessible labeled peripheral blood cell dataset, arXiv:2407.13214), provides high-quality annotated images of peripheral blood cells, enabling precise cell detection and classification. The dataset is split as follows:

+ Training set: 1,008 images
+ Validation set: 288 images
+ Test set: 144 images

Each image contains labeled bounding boxes representing different types of blood cells.


## Functional Test Data Instructions

The functional test script (functional_test.py) runs object detection using a trained YOLO model on a small test dataset. The results, including predictions and confidence scores, are saved and displayed.

**1\. Installation Requirements**

Before running the script, ensure you have the required dependencies installed:

    pip install ultralytics matplotlib opencv-python shutil

You may also need to install:

    pip install opencv-python-headless

**2\. Directory Structure**

Make sure you have functional_test_data/ directory with structure as follows:

```
Final Project/
│── functional_test_data/
│   ├── small_test_data/      # Small test dataset (images)
│── runs/detect/train/weights/
│   ├── best.pt               # Trained YOLO model weights
│── functional_test.py        # The test script
│── README.md                 # Instructions (this file)
│── etc....
```

**3\. Running the Functional Test Script**

To run the functional test, execute the following command in the terminal: `python functional_test.py`. Or, you can click the run button in any python-supported IDE, like Pycharm.app

This script will:

- Load the trained YOLO model from `runs/detect/train/weights/best.pt`
- Run predictions on images in `functional_test_data/small_test_data/`
- Save predicted images in `functional_test_data/predict/`
- Print predicted class labels and confidence scores
- Display the first 5 processed images

If the `predict/` folder already exists, it will be deleted and replaced to avoid duplicate folders (`predict2`, `predict3`, etc.).

**4\. Expected Output**

After running the script, you should see:

1. Text output in the terminal, showing:

    ```
    Total number of test data sets: 10
    Class names: {0: 'WBC', 1: 'RBC', 2: 'Platelet'}
    
    test img 1:
    Class prediction: RBC (Confidence: 0.97)
    Class prediction: RBC (Confidence: 0.97)
    ...
    ```

2. Processed images in `functional_test_data/predict/` with bounding boxes around detected objects.

3. Displayed images for the first 5 test cases.

## Important Files

```
Final Project/
│── functional_test_data/
│   ├── small_test_data/      # Small test dataset (images)
│   ├── predict/              # Directory where predictions will be saved
│── runs/
│── ├── detect/
│── ├── ├── train/            # training evaluation
│── ├── ├── val/              # validation evaluation
│── ├── ├── test/             # test evaluation
│── ├── ├── predict/          # test results for all test data
│── functional_test.py        # The functional test script for a small test data set
│── data-preprocess.py        # Containing code for pre-processing the dataset
│── train_test.ipynb          # Containing code of the process for training, validation, and testing
│── train_test.pdf            # The pdf version of train_test.ipynb, containg all the outputs
│── README.md                 # Instructions (this file)
│── yolov8n.pt
│── etc....
```

## Contributors

Qizhi Tian, Jiatong Liu, Sijie Guo, Yifei Sun

