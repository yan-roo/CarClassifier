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
```
```
CarClassifier
  +- training_data
  +- testing_data
  +- cs-t0828-2020-hw1.zip
```

