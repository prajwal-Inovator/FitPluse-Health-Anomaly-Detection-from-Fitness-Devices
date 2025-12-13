import pandas as pd
import io
from typing import Optional


def load_file(contents: bytes, filename: str) -> pd.DataFrame:
    name = filename.lower()

    if name.endswith(".csv"):
        return pd.read_csv(io.BytesIO(contents))

    if name.endswith(".json"):
        try:
            # normal JSON array
            return pd.read_json(io.BytesIO(contents))
        except:
            # newline-delimited JSON
            return pd.read_json(io.BytesIO(contents), lines=True)

    raise ValueError("Unsupported file format (only CSV or JSON allowed)")



def normalize_timestamps(
    df: pd.DataFrame,
    timestamp_col: Optional[str] = "timestamp",
    timezone_from: Optional[str] = None,
    to_utc: bool = True
) -> pd.DataFrame:

    if timestamp_col not in df.columns:
        raise ValueError("Timestamp column not found")

    df = df.copy()
    df[timestamp_col] = pd.to_datetime(df[timestamp_col], errors="coerce")

    if df[timestamp_col].isna().all():
        raise ValueError("Timestamp parsing failed")

    if timezone_from:
        try:
            df[timestamp_col] = df[timestamp_col].dt.tz_localize(timezone_from)
        except:
            pass

    if to_utc:
        try:
            df[timestamp_col] = df[timestamp_col].dt.tz_convert("UTC")
        except:
            df[timestamp_col] = df[timestamp_col].dt.tz_localize("UTC")

    return df.set_index(timestamp_col).sort_index()



def extract_health_metrics(df: pd.DataFrame) -> pd.DataFrame:

    data = {}

    if "heart_rate_avg" in df.columns:
        data["heart_rate"] = pd.to_numeric(
            df["heart_rate_avg"], errors="coerce"
        )

    if "steps" in df.columns:
        data["steps"] = pd.to_numeric(
            df["steps"], errors="coerce"
        )

    if "sleep_hours" in df.columns:
        data["sleep_minutes"] = (
            pd.to_numeric(df["sleep_hours"], errors="coerce") * 60
        )

    if not data:
        raise ValueError("No valid health metrics found")

    return pd.DataFrame(data, index=df.index)


def handle_missing(df: pd.DataFrame) -> pd.DataFrame:

    if "heart_rate" in df.columns:
        df["heart_rate"] = df["heart_rate"].fillna(df["heart_rate"].mean())

    if "steps" in df.columns:
        df["steps"] = df["steps"].fillna(0)

    if "sleep_minutes" in df.columns:
        df["sleep_minutes"] = df["sleep_minutes"].fillna(0)

    return df



def preprocess_fitpulse_pipeline(
    contents: bytes,
    filename: str,
    timestamp_col="timestamp",
    timezone_from=None,
    to_utc=True
):

    df = load_file(contents, filename)
    df = normalize_timestamps(df, timestamp_col, timezone_from, to_utc)
    df = extract_health_metrics(df)
    df = handle_missing(df)

    out_csv = df.reset_index().to_csv(index=False)
    return df, out_csv
