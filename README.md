# ECE575-OSA-Acoustic-Screening
Group project of ECE575 on OSA-Acoustic-Screening topic.

# ECE575 - Acoustic Screening for OSA

## 1. Project Overview
Obstructive Sleep Apnea (OSA) is a serious sleep disorder where the airway repeatedly becomes blocked during sleep, causing breathing interruptions and reduced oxygen levels. These episodes create distinct acoustic patterns, including irregular snoring, high-frequency gasps, and prolonged silences lasting over 10 seconds.
The goal of this project is to build an automated acoustic screening system that can distinguish between harmless snoring and apneic snoring, which indicates potential OSA. By analyzing overnight audio recordings, the system will generate a preliminary risk assessment that could help identify individuals who should seek formal clinical evaluation.


## 2. Problem Statement
Primary Goal:
Develop a machine-learning classifier that detects apneic snoring events in audio recordings.
Additional Goals:

Identify breathing pauses exceeding 10 seconds in duration.
Extract acoustic features associated with airway obstruction.
Calculate a nightly OSA risk score based on detected events.
Compare traditional machine learning approaches with deep learning methods.
Create an interactive visualisation dashboard for results.

## 3. Motivation

## 4. Dataset Description
We're planning to work with  Kaggle datasets:
Kaggle Snoring Dataset - Includes 500 snore samples and 500 non-snore samples for balanced training. This dataset will be used primarily for initial model development and testing the basic classification pipeline.

## 5. Proposed Methodology
- Audio preprocessing
- Feature extraction
- Classification models
- Risk scoring system

## 6. Tools and Technologies

## 7. Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

## 8. Timeline
Weeks 1-2: Dataset collection and preparation, feature extraction implementation.
Weeks 3-4: Model training, hyperparameter tuning, and evaluation.
Week 5: Risk scoring algorithm and visualisation dashboard development.
Week 6: Final testing, documentation, and presentation preparation.

## 9. Related Work

(Discussion of 15–20 papers)

## 10. Individual Objectives

### Abhishek Kumar Singh
Abhishek Kumar Singh
Objective 1: Implement a robust feature extraction pipeline for acoustic OSA detection

PI1 (basic): Load and preprocess audio files from all three datasets (Munich-Passau, Kaggle, MIT-BIH), including resampling to 16 kHz and noise reduction
PI2 (basic): Extract basic MFCC features (13 coefficients) and save them in a structured format for model training
PI3 (expected): Implement extraction of multiple feature types (MFCCs, spectral centroid, rolloff, ZCR, RMS energy) and create a unified feature matrix
PI4 (expected): Add delta and delta-delta features to capture temporal dynamics, conduct feature correlation analysis to identify redundant features
PI5 (advanced): Implement feature selection using mutual information or recursive feature elimination, compare model performance with different feature subsets, document optimal feature combinations

Objective 2: Develop and evaluate silence detection algorithm for apnea event identification

PI1 (basic): Implement energy-based endpoint detection to identify low-energy segments in audio recordings
PI2 (basic): Detect and flag silence intervals exceeding 10 seconds duration
PI3 (expected): Calculate precision and recall for silence detection against ground truth annotations from MIT-BIH database
PI4 (expected): Tune detection threshold parameters using validation data, compare multiple silence detection approaches (energy-based vs. spectral-based)
PI5 (advanced): Incorporate temporal context using sliding windows, implement false positive reduction using spectral characteristics, achieve >75% sensitivity for detecting actual apnea events

Objective 3: Train and compare classical ML models for apnea classification

PI1 (basic): Implement and train a baseline Random Forest classifier on extracted features
PI2 (basic): Train SVM and Logistic Regression models, save trained models for deployment
PI3 (expected): Perform hyperparameter tuning using grid search or random search for all three classifiers, document optimal parameters
PI4 (expected): Conduct 5-fold cross-validation for each model, calculate and compare accuracy, precision, recall, F1-score, and ROC-AUC, generate confusion matrices
PI5 (advanced): Implement ensemble methods (stacking or voting) combining multiple classifiers, analyze feature importance across models, achieve F1-score ≥85% on validation set


### Nikhil Kumar Mukkuamala
Nikhil
Objective 1: Implement a deep learning architecture for apnea detection from audio

PI1 (basic): Design and implement a basic 1D CNN architecture with 2-3 convolutional layers for raw waveform processing
PI2 (basic): Prepare training data pipeline with appropriate batching and data loading for neural network training
PI3 (expected): Implement both 1D CNN (raw audio) and 2D CNN (mel-spectrogram) architectures, train both models and document training curves
PI4 (expected): Apply regularisation techniques (dropout, batch normalisation, L2 regularisation) to prevent overfitting, compare performance with and without regularisation
PI5 (advanced): Implement data augmentation strategies (pitch shifting, time stretching, adding noise) to improve model robustness, achieve performance comparable to or better than classical ML approaches

Objective 2: Develop and validate the OSA risk scoring system

PI1 (basic): Implement a simple counting-based risk score that tallies detected apnea events per recording
PI2 (basic): Calculate events per hour (analogous to AHI) and classify into Low/Moderate/High risk categories
PI3 (expected): Incorporate event duration and severity metrics into the risk score calculation, weight different types of events appropriately
PI4 (expected): Validate risk scores against clinical annotations from the MIT-BIH database, calculate correlation between computed scores and actual AHI values
PI5 (advanced): Implement confidence intervals for risk predictions, create calibration curves to assess reliability of risk estimates, and achieve correlation ≥0.7 with clinical AHI scores

Objective 3: Build an interactive visualisation dashboard for system demonstration

PI1 (basic): Create a basic Streamlit application that can load and display audio waveforms
PI2 (basic): Add spectrogram visualisation with time and frequency axes properly labelled
PI3 (expected): Implement timeline view showing detected apnea events overlaid on the audio, add audio playback functionality for selected segments
PI4 (expected): Display risk score with visual indicators (colour-coded risk levels), show summary statistics (total events, average duration, distribution), create comparison views for different models
PI5 (advanced): Add interactive filtering and zooming capabilities for detailed event inspection, implement export functionality for reports, and create a user-friendly interface suitable for demonstration to non-technical users


## 11. References
Janott, C., Kurscheid, H., Heiser, C., Rohrmeier, C., Herzog, M., & Eilers, K. (2019). "Snoring classified: The Munich-Passau Snore Sound Corpus." Computers in Biology and Medicine, 94, 106-118.
Khan, M. M., & Choi, K. S. (2018). "Automated detection of sleep apnea using hidden Markov model from audio features." Expert Systems with Applications, 115, 161-172.
