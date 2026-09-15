CREATE DATABASE IF NOT EXISTS cloudpulse;
CREATE EXTERNAL TABLE IF NOT EXISTS cloudpulse.transactions_curated (
 transaction_id string, customer_id string, amount double, merchant_category string,
 country string, device_type string, card_present boolean, event_time timestamp,
 transaction_velocity_1h int, customer_avg_amount double, event_date string,
 event_hour int, is_international int, card_present_int int, amount_to_customer_avg double
) STORED AS PARQUET LOCATION 's3://YOUR_BUCKET/curated/transactions/';
