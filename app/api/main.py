import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from app.config import settings
app=FastAPI(title="CloudPulse AI API",version="1.0.0")

def load_data():
    if not settings.scored_data_path.exists():
        raise HTTPException(503,"Run python scripts/demo.py first.")
    return pd.read_parquet(settings.scored_data_path)

@app.get("/")
def root(): return {"project":"CloudPulse AI","docs":"/docs"}
@app.get("/health")
def health(): return {"status":"ok"}
@app.get("/api/v1/analytics/summary")
def summary():
    df=load_data(); n=int(df["is_anomaly"].sum())
    return {"total_transactions":len(df),"total_amount":round(float(df.amount.sum()),2),
            "average_amount":round(float(df.amount.mean()),2),"anomaly_count":n,
            "anomaly_rate":round(n/len(df),4) if len(df) else 0}
@app.get("/api/v1/transactions")
def transactions(limit:int=Query(20,ge=1,le=200)):
    return load_data().sort_values("event_time",ascending=False).head(limit).astype(str).to_dict("records")
@app.get("/api/v1/anomalies")
def anomalies(limit:int=Query(20,ge=1,le=200)):
    df=load_data(); df=df[df.is_anomaly==1].sort_values("anomaly_score",ascending=False).head(limit)
    return df.astype(str).to_dict("records")
