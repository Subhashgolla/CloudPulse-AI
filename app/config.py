from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_mode: str = "local"
    aws_region: str = "us-east-1"
    kinesis_stream_name: str = "cloudpulse-events"
    s3_bucket_name: str = ""
    raw_data_path: Path = Path("data/raw/transactions.jsonl")
    curated_data_path: Path = Path("data/curated/transactions.parquet")
    scored_data_path: Path = Path("data/scored/transactions_scored.parquet")
    model_path: Path = Path("models/isolation_forest.joblib")
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
settings = Settings()
