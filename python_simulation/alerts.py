from datetime import datetime
import pandas as pd
from docs.config import *

def generate_alert(alert_type):

    alert = {
        "timestamp": datetime.now(),
        "alert": alert_type
    }

    try:
        df = pd.read_csv(ALERT_FILE)
        df = pd.concat(
            [df, pd.DataFrame([alert])],
            ignore_index=True
        )

    except:
        df = pd.DataFrame([alert])

    df.to_csv(ALERT_FILE, index=False)

    print(f"🚨 {alert_type}")