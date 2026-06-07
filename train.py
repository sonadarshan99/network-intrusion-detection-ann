from src.preprocess import load_data
from src.preprocess import preprocess

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

import matplotlib.pyplot as plt


print("Loading dataset...")

train, test = load_data()

X_train, X_test, y_train, y_test = preprocess(
    train,
    test
)

print("Dataset loaded successfully")


model = Sequential()

model.add(
    Dense(
        64,
        activation="relu",
        input_shape=(X_train.shape[1],)
    )
)

model.add(
    Dense(
        32,
        activation="relu"
    )
)

model.add(
    Dense(
        16,
        activation="relu"
    )
)

model.add(
    Dense(
        1,
        activation="sigmoid"
    )
)


model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


early_stop = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)

print("Training ANN model...")

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=20,
    batch_size=32,
    callbacks=[early_stop]
)

print("Training completed")


loss, accuracy = model.evaluate(
    X_test,
    y_test
)

print("\nFinal Accuracy:", accuracy)


model.save(
    "models/ann_model.keras"
)

print("Model saved successfully")


plt.figure(figsize=(8,5))

plt.plot(
    history.history["accuracy"],
    label="Training Accuracy"
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
)

plt.legend()

plt.title("ANN Accuracy")

plt.savefig(
    "results/training_accuracy.png"
)

plt.close()


plt.figure(figsize=(8,5))

plt.plot(
    history.history["loss"],
    label="Training Loss"
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss"
)

plt.legend()

plt.title("ANN Loss")

plt.savefig(
    "results/training_loss.png"
)

plt.close()

print("Graphs saved successfully")