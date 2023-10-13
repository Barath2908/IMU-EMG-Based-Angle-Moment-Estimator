# IMU-EMG-Based-Angle-Moment-Estimator
Description:
This project presents a comprehensive analysis of gait patterns using a combination of Xsens IMU (Inertial Measurement Unit) sensors and Delsys sEMG (surface electromyography) data collected from a cohort of 25 healthy subjects across three different walking speeds. The primary goal of this research is to provide insights into the fusion of sensor modalities for improved gait analysis.

Key Steps:

Data Collection: We collected a rich dataset containing 14 Xsens IMU sensor measurements and sEMG data using XsenseMVN and Delsys equipment. This dataset encompasses a wide range of walking conditions, making it a valuable resource for gait analysis.

Data Preprocessing: The sEMG data underwent extensive preprocessing, including a 20-450 Hz bandpass filter, 50 Hz notch filter to remove power line interference, differentiation for signal enhancement, and normalization for consistency.

Neural Network Models: To extract meaningful insights from this multimodal dataset, we employed a variety of neural network architectures, including Convolutional Neural Networks (CNN), Recurrent Neural Networks (RNN), Long Short-Term Memory networks (LSTM), Bidirectional LSTM (Bi-LSTM), Multilayer LSTM (MLSTM), Attention LSTM (ALSTM), and Multimodal Attention LSTM (MALSTM).

Results: Our efforts led to remarkable achievements in gait analysis. The LSTM model emerged as the most promising, achieving the highest accuracy and low variance. Specifically, we attained an impressive R2 (Coefficient of Determination) of 97.45% with a small variance of ±1.46%. Furthermore, the Normalized Root Mean Square Error (NRMSE) reached an exceptionally low 5.01% with a variance of ±1.1%. These results demonstrate the power of LSTM in modeling and understanding gait patterns using multimodal sensor data.
