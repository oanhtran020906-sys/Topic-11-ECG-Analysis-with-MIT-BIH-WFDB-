# Tải dữ liệu WFDB
import wfdb
import pandas as pd
import numpy as np

record = wfdb.rdrecord("100", pn_dir="mitdb")
signal = record.p_signal[:, 0]  # first channel
fs = record.fs

times = pd.to_timedelta(np.arange(len(signal)) / fs, unit="s")
ecg_series = pd.Series(signal, index=times)
