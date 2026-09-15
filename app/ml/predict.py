import joblib, pandas as pd
from app.config import settings

def score_transactions():
    bundle=joblib.load(settings.model_path)
    df=pd.read_parquet(settings.curated_data_path)
    pred=bundle["model"].predict(df[bundle["features"]])
    score=bundle["model"].decision_function(df[bundle["features"]])
    df["is_anomaly"]=(pred==-1).astype(int)
    df["anomaly_score"]=(-score).round(6)
    settings.scored_data_path.parent.mkdir(parents=True,exist_ok=True)
    df.to_parquet(settings.scored_data_path,index=False)
    return df
if __name__=="__main__": score_transactions()
