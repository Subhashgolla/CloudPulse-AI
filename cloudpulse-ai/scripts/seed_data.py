import argparse
from app.config import settings
from app.generator import generate_transaction
from app.storage import append_local, put_kinesis
p=argparse.ArgumentParser(); p.add_argument("--count",type=int,default=100); a=p.parse_args()
events=[generate_transaction() for _ in range(a.count)]
if settings.app_mode.lower()=="aws":
    print(f"failed={put_kinesis(events)}")
else:
    for e in events: append_local(e)
    print(f"Wrote {len(events)} events")
