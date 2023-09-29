FROM quay.io/astronomer/astro-runtime:9.1.0

COPY requirements.txt .

RUN pip install -r requirements.txt