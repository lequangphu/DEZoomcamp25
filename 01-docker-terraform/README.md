# Module 1: Containerization and Infrastructure as Code
In this directory, there are 2 subdirectories: `01-docker-sql` and `02-terraform-gcp`.

## 01-docker-sql
There are 4 files in this directory:
- [Dockerfile](01-docker-sql/Dockerfile): This file contains the instructions to build the Docker image.
- [docker-compose.yml](01-docker-sql/docker-compose.yml): This file contains the configuration to run the Docker container.
- [ingest_data.py](01-docker-sql/ingest_data.py): This file contains the Python script to ingest data into the PostgreSQL database.
- [queries](01-docker-sql/queries): This directory contains the SQL queries to interact with the PostgreSQL database to answer the questions in the homework.

## 02-terraform-gcp
There are 2 files in this directory:
- [main.tf](02-terraform-gcp/main.tf): This file contains the Terraform configuration to create a Google Cloud Platform (GCP) project.
- [variables.tf](02-terraform-gcp/variables.tf): This file contains the variables used in the Terraform configuration.
