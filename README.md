# cell_recognize

Use YOLO or Fast-RCNN network to recognize the adherent cells in test images.

A tmp sample parasitized cell image dataset can be accessed from:
# 链接：https://pan.baidu.com/s/1sFFgJfrpEVHxdcClCzrCYA 
# 提取码：2uz0

And we can also get a red-blood-cell dataset from https://github.com/cosmicad/dataset

Use this dataset the train a demo to recognize red-blood-cell, and changed to adherent cell dataset
to re-train the model in the future if the dataset is ready.

How to get the result of detecting:
1. In application/redcell_detect/, python3 redcell_detect.py;
2. The red blood cell image is specified to "Bloodimage_00003.jpg" just for demo;
3. We will integrate redcell_detect.py into a service; 
