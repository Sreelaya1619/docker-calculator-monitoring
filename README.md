# Docker Calculator Monitoring & Logging Project

## Overview

This project demonstrates a complete observability setup for a containerized Calculator application using Docker, Prometheus, Grafana, Elasticsearch, Logstash, and Kibana (ELK Stack).

The application is built with Python and Streamlit, exposes Prometheus metrics for monitoring, and sends application logs to Logstash for centralized log management and visualization in Kibana.

---

## Architecture

```text
Calculator Application
│
├── Metrics
│     └── Prometheus
│            └── Grafana
│
└── Logs
      └── Logstash
             └── Elasticsearch
                    └── Kibana
```

---

## Tech Stack

* Python 3.11
* Streamlit
* Docker
* Docker Compose
* Prometheus
* Grafana
* Elasticsearch
* Logstash
* Kibana

---

## Features

### Application

* Basic Calculator Operations

  * Addition
  * Subtraction
  * Multiplication
  * Division

### Monitoring

* Prometheus Metrics Collection
* Custom Application Metrics
* Real-Time Monitoring
* Grafana Dashboards

### Logging

* Structured Application Logging
* Log Collection using Logstash
* Log Storage in Elasticsearch
* Log Visualization in Kibana

---

## Project Structure

```text
docker-calculator/
│
├── calculator.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── prometheus.yml
├── logstash.conf
├── README.md
└── .gitignore
```

---

## Setup and Run

### Clone Repository

```bash
git clone https://github.com/Sreelaya1619/docker-calculator-monitoring.git
cd docker-calculator-monitoring
```

### Start All Services

```bash
docker compose up -d --build
```

### Verify Running Containers

```bash
docker ps
```

Expected Containers:

* calculator
* prometheus
* grafana
* elasticsearch
* logstash
* kibana

---

## Access URLs

| Service          | URL                           |
| ---------------- | ----------------------------- |
| Calculator       | http://localhost:8501         |
| Metrics Endpoint | http://localhost:8000/metrics |
| Prometheus       | http://localhost:9090         |
| Grafana          | http://localhost:3006         |
| Elasticsearch    | http://localhost:9200         |
| Kibana           | http://localhost:5601         |

---

## Monitoring Workflow

1. Perform calculator operations.
2. Metrics are exposed on:

```text
http://localhost:8000/metrics
```

3. Prometheus scrapes the metrics.
4. Grafana visualizes application metrics.

Example Metric:

```text
calculator_operations_total
```

---

## Logging Workflow

1. Calculator generates logs.
2. Logs are sent to Logstash.
3. Logstash forwards logs to Elasticsearch.
4. Kibana visualizes logs.

Example Log:

```text
Operation=add Num1=4.0 Num2=17.0 Result=21.0
```

---

## Docker Hub Image

```bash
docker pull sreelaya1619/docker-calculator-monitoring:latest
```

Docker Hub Repository:

https://hub.docker.com/r/sreelaya1619/docker-calculator-monitoring

---

## Screenshots

### Calculator UI

<img width="1355" height="670" alt="image" src="https://github.com/user-attachments/assets/f4b938f9-5c66-4df8-b289-ac532c6a3e55" />

### Prometheus Metrics

Add Prometheus screenshot here.

### Grafana Dashboard

Add Grafana screenshot here.

### Kibana Logs

Add Kibana Discover screenshot here.

---

## Learning Outcomes

This project helped in understanding:

* Docker Containerization
* Docker Compose Orchestration
* Application Monitoring
* Prometheus Metrics Collection
* Grafana Dashboard Creation
* Centralized Logging
* ELK Stack Integration
* Observability Fundamentals
* DevOps Troubleshooting

---

## Author

**Sreelaya R**

GitHub:
https://github.com/Sreelaya1619

Docker Hub:
https://hub.docker.com/u/sreelaya1619
