import joblib, pandas as pd
from sklearn.ensemble import IsolationForest
from app.config import settings
FEATURES=["amount","event_hour","is_international","card_present_int","transaction_velocity_1h","amount_to_customer_avg"]

def train_model():
    df=pd.read_parquet(settings.curated_data_path)
    model=IsolationForest(n_estimators=250,contamination=0.035,random_state=42,n_jobs=-1)
    model.fit(df[FEATURES])
    settings.model_path.parent.mkdir(parents=True,exist_ok=True)
    joblib.dump({"model":model,"features":FEATURES},settings.model_path)
    return model
if __name__=="__main__": train_model()
