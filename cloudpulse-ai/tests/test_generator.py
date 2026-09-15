from app.generator import generate_transaction
def test_generator():
    e=generate_transaction()
    assert e.amount>0 and e.customer_id.startswith("CUST-")
