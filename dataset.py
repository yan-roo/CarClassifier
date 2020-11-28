import pandas as pd
import os
import cv2


df = pd.read_csv('training_labels.csv')
for index, row in df.iterrows():
    img = cv2.imread(f"training_data/{row['id']:06}.jpg")
    if not os.path.exists(f"tmp/{row['label']}"):
        os.makedirs(f"tmp/{row['label']}")
    print(f"{row['label']}")
    cv2.imwrite(f"tmp/{row['label']}/{row['id']:06}.jpg", img)
    

# file_list = []
# for file in os.listdir('testing_data'):
#     file_list.append(file[1:])

    
# for d in os.listdir('car_data/train'):
#     for f in os.listdir(f'car_data/train/{d}/'):
#         if f in file_list:
#             file_list.remove(f)
#             img = cv2.imread(f"car_data/train/{d}/{f}")
#             if not os.path.exists(f"tmp_test/{d}"):
#                 os.makedirs(f"tmp_test/{d}/")
#             cv2.imwrite(f"tmp_test/{d}/0{f}", img)


            