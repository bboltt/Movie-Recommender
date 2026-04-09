# 🎬 Movie Recommender Portfolio Project

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PySpark](https://img.shields.io/badge/PySpark-MLlib-E25A1C?logo=apachespark&logoColor=white)](https://spark.apache.org/docs/latest/api/python/)
[![Elasticsearch](https://img.shields.io/badge/Elasticsearch-Vector%20Search-005571?logo=elasticsearch&logoColor=white)](https://www.elastic.co/)
[![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](#license)

A production-style movie recommendation workflow that combines **collaborative filtering in PySpark** with **Elasticsearch retrieval** for fast, explainable movie discovery.

---

## Why this project matters

Recommendation systems sit at the center of many consumer products. This repository demonstrates practical machine learning engineering patterns used by data science teams:

- Building implicit-feedback recommendations with Spark MLlib.
- Converting model outputs into search-friendly representations.
- Serving recommendations with Elasticsearch-backed querying.
- Supporting reproducibility through tests and dependency pinning.

---

## Repository structure

```text
.
├── notebooks/
│   ├── movie-recommendation.ipynb
│   ├── elasticsearch-spark-recommender.ipynb
│   └── fig_*.png
├── src/
│   └── movie_recommender/
│       ├── __init__.py
│       └── features.py
├── tests/
│   └── test_features.py
├── requirements.txt
├── README.md
└── readme.md
```

---

## End-to-end architecture

```mermaid
flowchart LR
    A[Raw Ratings + Movie Metadata] --> B[PySpark ETL]
    B --> C[ALS Collaborative Filtering Model]
    C --> D[Latent User/Movie Vectors]
    D --> E[Feature Engineering in Python]
    E --> F[Elasticsearch Index]
    F --> G[Top-N Recommendation API / Notebook Query]
    G --> H[Ranked Movies + Poster URLs]
```

---

## Core capabilities

- **Modeling**: Collaborative filtering with matrix factorization patterns from Spark ML workflows.
- **Retrieval**: Candidate lookup and similarity-inspired ranking in Elasticsearch.
- **Feature utilities**: Reusable helper functions for year parsing, vector conversion, and recommendation ranking.
- **Testing**: Pytest suite for deterministic, CI-friendly validation.

---

## Getting started

### 1) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run tests

```bash
pytest -q
```

### 4) Explore notebooks

Open the notebooks in JupyterLab or VS Code:

- `notebooks/movie-recommendation.ipynb`
- `notebooks/elasticsearch-spark-recommender.ipynb`

---

## Selected visual output

![Recommendation preview](png/test.PNG)

---

## Professional roadmap

- Add a reproducible training pipeline with tracked experiments (MLflow).
- Add API serving with FastAPI and request-level telemetry.
- Add offline ranking metrics (MAP@K, NDCG@K, coverage).
- Containerize local deployment with Docker Compose (Spark + Elasticsearch + API).

---

## License

MIT (recommended for portfolio reuse and extension).
