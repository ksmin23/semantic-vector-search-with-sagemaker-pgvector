
# Semantic Vector Search in PostgreSQL using Amazon SageMaker and pgvector

This project is a search solution using [pgvector](https://github.com/pgvector/pgvector) for an online retail store product catalog. We’ll build a search system that lets customers provide an item description to find similar items.

For more information, check this blog post, [Building AI-powered search in PostgreSQL using Amazon SageMaker and pgvector (2023-05-03)](https://aws.amazon.com/blogs/database/building-ai-powered-search-in-postgresql-using-amazon-sagemaker-and-pgvector/)

The overall architecture is like this:

![semantic-vector-search-with-sagemaker-pgvector](./semantic-vector-search-with-sagemaker-pgvector.svg)

### Overall Workflow

1. Deploy the cdk stacks (For more information, see [here](./cdk_stacks/README.md)).
  - A SageMaker Studio in a private VPC.
  - An Amazon Aurora Postgresql cluster for storing embeddings.
  - Aurora Postgresql cluster's access credentials (username and password) stored in AWS Secrets Mananger as a name such as `VSPgVectorStackAuroraPostgr-xxxxxxxxxxxx`.
2. Open SageMaker Studio and then open a new **System terminal**.
3. Run the following commands on the terminal to clone the code repository for this project:
   ```
   git clone https://github.com/ksmin23/semantic-vector-search-with-sagemaker-pgvector.git
   ```
4. Open `data_ingestion_to_pgvector.ipynb` notebook and Run it. (For more information, see [here](./data_ingestion_to_vectordb/data_ingestion_to_pgvector.ipynb))
5. Run Streamlit application. (For more information, see [here](./app/README.md))

### References

  * [Building AI-powered search in PostgreSQL using Amazon SageMaker and pgvector (2023-05-03)](https://aws.amazon.com/blogs/database/building-ai-powered-search-in-postgresql-using-amazon-sagemaker-and-pgvector/)
     * [aws-samples/rds-postgresql-pgvector](https://github.com/aws-samples/rds-postgresql-pgvector)
  * [Extension versions for Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Extensions.html)
  * [Build Streamlit apps in Amazon SageMaker Studio (2023-04-11)](https://aws.amazon.com/blogs/machine-learning/build-streamlit-apps-in-amazon-sagemaker-studio/)
  * [Streamlit](https://streamlit.io/) - A faster way to build and share data apps
