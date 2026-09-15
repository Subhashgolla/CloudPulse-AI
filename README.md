# CloudPulse AI

CloudPulse AI is a data engineering and machine learning project built to process transaction data and detect unusual transaction patterns.

The project uses Python for data processing, Isolation Forest for anomaly detection, and FastAPI to provide access to the processed results. It also includes Docker support and AWS infrastructure files.

## Technologies Used

- Python
- FastAPI
- Pandas
- Scikit-learn
- AWS Kinesis
- Amazon S3
- AWS Glue
- Amazon Athena
- Docker
- GitHub Actions

## Project Structure

```text
app/        - Application and API code
data/       - Raw, processed, and scored data
infra/      - AWS infrastructure files
models/     - Trained ML models
scripts/    - Scripts for running the pipeline
tests/      - Application tests
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/Subhashgolla/CloudPulse-AI.git
cd CloudPulse-AI
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create the environment file:

```cmd
copy .env.example .env
```

Run the demo pipeline:

```bash
python scripts/demo.py
```

## Run the API

```bash
uvicorn app.api.main:app --reload
```

Open the API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Testing

Run the tests using:

```bash
pytest -q
```

## Docker

Build the Docker image:

```bash
docker build -t cloudpulse-ai .
```

Run it:

```bash
docker run -p 8000:8000 cloudpulse-ai
```

## Author

Subhash Krishna Golla

GitHub: https://github.com/Subhashgolla  
LinkedIn: https://www.linkedin.com/in/subhashkrishna

## License

MIT