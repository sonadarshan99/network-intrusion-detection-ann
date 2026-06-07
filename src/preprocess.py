import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


def load_data():

    columns = [
        'duration','protocol_type','service','flag',
        'src_bytes','dst_bytes','land','wrong_fragment',
        'urgent','hot','num_failed_logins',
        'logged_in','num_compromised','root_shell',
        'su_attempted','num_root','num_file_creations',
        'num_shells','num_access_files',
        'num_outbound_cmds','is_host_login',
        'is_guest_login','count','srv_count',
        'serror_rate','srv_serror_rate',
        'rerror_rate','srv_rerror_rate',
        'same_srv_rate','diff_srv_rate',
        'srv_diff_host_rate','dst_host_count',
        'dst_host_srv_count',
        'dst_host_same_srv_rate',
        'dst_host_diff_srv_rate',
        'dst_host_same_src_port_rate',
        'dst_host_srv_diff_host_rate',
        'dst_host_serror_rate',
        'dst_host_srv_serror_rate',
        'dst_host_rerror_rate',
        'dst_host_srv_rerror_rate',
        'label',
        'difficulty'
    ]

    train = pd.read_csv(
        "data/KDDTrain+.txt",
        names=columns
    )

    test = pd.read_csv(
        "data/KDDTest+.txt",
        names=columns
    )

    return train, test


def preprocess(train, test):

    for col in [
        "protocol_type",
        "service",
        "flag"
    ]:

        encoder = LabelEncoder()

        train[col] = encoder.fit_transform(
            train[col]
        )

        test[col] = encoder.transform(
            test[col]
        )

    train["label"] = train["label"].apply(
        lambda x: 0 if x == "normal" else 1
    )

    test["label"] = test["label"].apply(
        lambda x: 0 if x == "normal" else 1
    )

    X_train = train.drop(
        ["label", "difficulty"],
        axis=1
    )

    y_train = train["label"]

    X_test = test.drop(
        ["label", "difficulty"],
        axis=1
    )

    y_test = test["label"]

    scaler = StandardScaler()

    X_train = scaler.fit_transform(
        X_train
    )

    X_test = scaler.transform(
        X_test
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )