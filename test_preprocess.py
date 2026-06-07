from src.preprocess import load_data
from src.preprocess import preprocess

train, test = load_data()

X_train, X_test, y_train, y_test = preprocess(
    train,
    test
)

print("Train Shape:", X_train.shape)
print("Test Shape:", X_test.shape)