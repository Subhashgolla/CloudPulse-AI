import boto3
from app.config import settings

def append_local(event):
    settings.raw_data_path.parent.mkdir(parents=True,exist_ok=True)
    with settings.raw_data_path.open("a",encoding="utf-8") as f:
        f.write(event.model_dump_json()+"\n")

def put_kinesis(events):
    client=boto3.client("kinesis",region_name=settings.aws_region)
    failed=0
    for start in range(0,len(events),500):
        batch=events[start:start+500]
        response=client.put_records(StreamName=settings.kinesis_stream_name,
            Records=[{"Data":e.model_dump_json().encode(),"PartitionKey":e.customer_id} for e in batch])
        failed += response.get("FailedRecordCount",0)
    return failed
