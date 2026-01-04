import wfdb
import pandas as pd
import numpy as np


def load_ecg_record(record_id="100", channel=0, db_name="mitdb"):
    """
    Load ECG record from MIT-BIH database using WFDB
    """

    record = wfdb.rdrecord(record_id, pn_dir=db_name)
    signal = record.p_signal[:, channel]
    fs = record.fs

    times = pd.to_timedelta(np.arange(len(signal)) / fs, unit="s")
    ecg_series = pd.Series(signal, index=times)

    return ecg_series, fs
