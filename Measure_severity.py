import os
import librosa
import numpy as np

# Paths
snoring_path = "Snoring Dataset/1"
non_snoring_path = "Snoring Dataset/0"


def calculate_severity(audio, sr):
    # Loudness
    rms = np.mean(librosa.feature.rms(y=audio))

    # Frequency
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=audio, sr=sr))

    # Normalize (important)
    rms_score = min(rms * 1000, 100)
    freq_score = min(spectral_centroid / 50, 100)

    # Weighted score
    severity = 0.6 * rms_score + 0.4 * freq_score

    return round(min(severity, 100), 2)


# Store results
severity_scores = []

# Process Snoring (Label = 1)
for file in os.listdir(snoring_path):
    file_path = os.path.join(snoring_path, file)

    audio, sr = librosa.load(file_path, duration=1)
    severity = calculate_severity(audio, sr)

    severity_scores.append((file, 1, severity))

# Process Non-Snoring (Label = 0)
for file in os.listdir(non_snoring_path):
    file_path = os.path.join(non_snoring_path, file)

    audio, sr = librosa.load(file_path, duration=1)
    severity = calculate_severity(audio, sr)

    severity_scores.append((file, 0, severity))

# Print sample output
for i in range(10):
    print(severity_scores[i])

def severity_level(score):
    if score < 20:
        return "No Snoring"
    elif score < 40:
        return "Mild"
    elif score < 60:
        return "Moderate"
    elif score < 80:
        return "High"
    else:
        return "Severe"

for file, label, score in severity_scores[:10]:
    print(file, score, severity_level(score))

features = []
labels = []
severity_list = []


def extract_all(file_path, label):
    audio, sr = librosa.load(file_path, duration=1)

    # MFCC
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    mfcc_scaled = np.mean(mfcc.T, axis=0)

    # Severity
    severity = calculate_severity(audio, sr)

    return mfcc_scaled, label, severity


# Snoring
for file in os.listdir(snoring_path):
    file_path = os.path.join(snoring_path, file)
    mfcc, label, severity = extract_all(file_path, 1)

    features.append(mfcc)
    labels.append(label)
    severity_list.append(severity)

# Non-snoring
for file in os.listdir(non_snoring_path):
    file_path = os.path.join(non_snoring_path, file)
    mfcc, label, severity = extract_all(file_path, 0)

    features.append(mfcc)
    labels.append(label)
    severity_list.append(severity)

X = np.array(features)
y_class = np.array(labels)
y_severity = np.array(severity_list)

X = np.array(features)
y_class = np.array(labels)
y_severity = np.array(severity_list)



from sklearn.ensemble import RandomForestRegressor

reg_model = RandomForestRegressor()
reg_model.fit(X, y_severity)

# Predict severity
y_pred_sev = reg_model.predict(X)


from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_severity, y_pred_sev)
print("MAE:", mae)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y_severity, test_size=0.2, random_state=42
)

reg_model.fit(X_train, y_train)
y_pred = reg_model.predict(X_test)
