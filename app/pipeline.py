import pandas as pd
from app.config import settings

def raw_to_curated():
    df=pd.read_json(settings.raw_data_path,lines=True)
    df["event_time"]=pd.to_datetime(df["event_time"],utc=True)
    df["event_date"]=df["event_time"].dt.strftime("%Y-%m-%d")
    df["event_hour"]=df["event_time"].dt.hour.astype(int)
    df["is_international"]=(df["country"]!="US").astype(int)
    df["card_present_int"]=df["card_present"].astype(int)
    df["amount_to_customer_avg"]=(df["amount"]/df["customer_avg_amount"]).clip(0,100)
    df=df.drop_duplicates("transaction_id").sort_values("event_time")
    settings.curated_data_path.parent.mkdir(parents=True,exist_ok=True)
    df.to_parquet(settings.curated_data_path,index=False)
    return df
