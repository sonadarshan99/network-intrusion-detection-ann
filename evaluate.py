from src.preprocess import load_data
from src.preprocess import preprocess

from tensorflow.keras.models import load_model

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

import matplotlib.pyplot as plt


print("Loading model...")

model = load_model(
    "models/ann_model.keras"
)

train, test = load_data()

X_train, X_test, y_train, y_test = preprocess(
    train,
    test
)

predictions = model.predict(X_test)

predictions = (
    predictions > 0.5
).astype(int)

accuracy = accuracy_score(
    y_test,
    predictions
)

precision = precision_score(
    y_test,
    predictions
)

recall = recall_score(
    y_test,
    predictions
)

f1 = f1_score(
    y_test,
    predictions
)

print("\n========== RESULTS ==========")

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1)

with open("results/metrics.txt", "w") as f:

    f.write(f"Accuracy:{accuracy}\n")
    f.write(f"Precision:{precision}\n")
    f.write(f"Recall:{recall}\n")
    f.write(f"F1 Score:{f1}\n")
    
cm = confusion_matrix(
    y_test,
    predictions
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot()

plt.savefig(
    "results/confusion_matrix.png"
)

plt.close()

print("\nConfusion matrix saved.")