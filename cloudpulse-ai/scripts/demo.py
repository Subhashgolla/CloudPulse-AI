from app.config import settings
from app.generator import generate_transaction
from app.storage import append_local
from app.pipeline import raw_to_curated
from app.ml.train import train_model
from app.ml.predict import score_transactions

def main(count=1000):
    if settings.raw_data_path.exists(): settings.raw_data_path.unlink()
    for _ in range(count): append_local(generate_transaction())
    curated=raw_to_curated(); train_model(); scored=score_transactions()
    print(f"CloudPulse AI ready: {len(curated)} rows, {int(scored.is_anomaly.sum())} anomalies")
    print("Run: uvicorn app.api.main:app --reload")
if __name__=="__main__": main()
