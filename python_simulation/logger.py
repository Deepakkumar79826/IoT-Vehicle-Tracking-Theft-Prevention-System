import pandas as pd
from docs.config import *

def save_log(data):

    try:
        df = pd.read_csv(CSV_LOG_FILE)

        df = pd.concat(
            [df, pd.DataFrame([data])],
            ignore_index=True
        )

    except:
        df = pd.DataFrame([data])

    df.to_csv(CSV_LOG_FILE, index=False)