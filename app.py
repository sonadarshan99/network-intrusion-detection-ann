from flask import Flask, render_template
import os

app = Flask(__name__)


def load_metrics():

    metrics = {
        "Accuracy": "N/A",
        "Precision": "N/A",
        "Recall": "N/A",
        "F1 Score": "N/A"
    }

    metrics_file = "results/metrics.txt"

    if os.path.exists(metrics_file):

        with open(metrics_file, "r") as f:

            for line in f:

                if ":" in line:

                    key, value = line.strip().split(":", 1)

                    metrics[key.strip()] = value.strip()

    return metrics


@app.route("/")
def home():

    metrics = load_metrics()

    print("Loaded Metrics:", metrics)

    return render_template(
    "index.html",
    accuracy=f"{float(metrics['Accuracy'])*100:.2f}%",
    precision=f"{float(metrics['Precision'])*100:.2f}%",
    recall=f"{float(metrics['Recall'])*100:.2f}%",
    f1=f"{float(metrics['F1 Score'])*100:.2f}%"
)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )