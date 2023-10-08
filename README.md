# Abnormal EEG Detection

## Overview
This project is focused on the detection of abnormal EEG (Electroencephalogram) signals using the TUH abnormal dataset. We employ a 1D-CNN (Convolutional Neural Network) model for classification, implemented in Python with the TensorFlow library. The dataset used in this project is publicly available, making it easy for others to reproduce and extend our work.

## Dataset
The TUH (Temple University Hospital) abnormal dataset is used as the input data for this project. This dataset contains a collection of EEG signals, including both normal and abnormal patterns. You can find more information about the dataset and access it [here](https://doi.org/10.3389/fnins.2016.00196).

## Model
We utilize a 1D-CNN model for the classification of EEG signals. Convolutional Neural Networks are well-suited for analyzing sequential data like EEG signals, and the 1D-CNN architecture allows us to capture important temporal patterns in the data.

## Getting Started
To get started with this project, follow these steps:

1. Clone the repository:
git clone https://github.com/mrezamostafavi/abnormal-eeg-detection.git
2. Install the necessary dependencies:
pip install tensorflow
3. Run the code:
python abnormal_eeg_detection.py

## References
Please refer to the original paper for more details about the methodology and findings of this project. You can find the original paper [here](https://doi.org/10.1007/s00521-018-3889-z).

## Contact
If you have any questions or suggestions, feel free to contact us at [mrezamostafavi98@gmail.com](mailto:mrezamostafavi98@gmail.com).

Happy coding!
