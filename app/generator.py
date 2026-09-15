import random
from app.schemas import TransactionEvent
CATEGORIES=["grocery","travel","electronics","restaurant","fuel","retail","entertainment"]
COUNTRIES=["US","US","US","US","CA","GB","IN","DE"]
DEVICES=["mobile","web","pos"]

def generate_transaction():
    avg=round(random.uniform(25,350),2)
    spike=random.random()<0.035
    amount=avg*random.uniform(5.5,14) if spike else random.lognormvariate(4.1,0.7)
    return TransactionEvent(customer_id=f"CUST-{random.randint(1000,1999)}",
        amount=round(max(1,min(amount,10000)),2), merchant_category=random.choice(CATEGORIES),
        country=random.choice(COUNTRIES), device_type=random.choice(DEVICES),
        card_present=random.random()>0.35,
        transaction_velocity_1h=random.randint(8,30) if spike else random.randint(0,7),
        customer_avg_amount=avg)
