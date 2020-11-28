# CarClassifier
This repository gathers the code for Stanford car image classification from the [in-class Kaggle challenge](https://www.kaggle.com/c/cs-t0828-2020-hw1).

Using __EfficientNetB7 (noisy-student) with AutoAugmentation + MixUp and SGD + Lookahead optimizer + 1 cycle cosine annealing learning rate scheduler__.
Without any ensemble models or extra training data.

Final submission score of __0.95920__ which places me __second on the final leaderboard__.


## Hardware
- Ubuntu 18.04.4 LTS
- Intel(R) Xeon(R) Gold 6154 CPU @ 3.00GHz
- 1x NVIDIA Tesla V100


## Getting Started
### Enviornment
```
virtualenv .
source bin/activate
pip3 install -r requirements.txt
```

### Dataset Preparation
[Join the competition and download the dataset](https://www.kaggle.com/c/cs-t0828-2020-hw1/data).
```
cd CarClassifier
kaggle competitions download -c cs-t0828-2020-hw1
unzip cs-t0828-2020-hw1
python dataset.py
```
```
CarClassifier
  +- training_data/
  +- testing_data/
  +- training_labels.csv
  +- tmp/
  +- log/
  +- cutmix_keras.py
  +- dataset.py
  +- EfficientNetB7.ipynb
  +- Normalization_testing.ipynb
  +- panda.jpg
  +- ResNet50.ipynb
```

## Results

|               Model               | Size | Batch |     Methods     | Testing Accuracy |
| --------------------------------- | ---- | ----- |---------------- | ---------------- |
|       ResNet50                    |  256 |  16   |   Hflip only    |       0.89       |
|   EfficientNetB3                  |  456 |  16   |   + Rotate 10   |       0.915      |
|   EfficientNetB7                  |  456 |  4    |                 |       0.932      |
|   EfficientNetB7                  |  456 |  4    |   AutoAugment   |       0.944      |
|   EfficientNetB7                  |  456 |  4    | wd1e-3 to 1e-4  |       0.949      |
|   EfficientNetB7                  |  456 |  4    | wd1e-4 to 1e-5  |       0.951      |
|   EfficientNetB7                  |  456 |  4    |   + RAdam       |       0.952      |
|   EfficientNetB7                  |  456 |  4    | + SGD_Lookahead |       0.954      |
|   EfficientNetB7                  |  600 |  4    |  + Cutout       |       0.956      |
|   EfficientNetB7 (noisy-student)  |  600 |  4    |- Cutout + Mixup |       0.959      |
|   EfficientNetB7 (noisy-student)  |  600 |  4    | + Dropout 0.5   |       0.9594     |


