# Batch Processing - Configure EC2 Kafka Client and Connect MSK to S3

## Project Aim

The aim of this project is to:

- Set up a Kafka client on an EC2 instance
- Connect the client to an Amazon MSK cluster 
- Create Kafka topics to capture streaming data
- Sync the topics with an S3 bucket for storage

## Milestone 3 - Configure EC2 Kafka Client

### Tasks 

1. **Create Pem Key File** 
    - Retrieve key pair from Parameter Store
    - Save key pair locally as .pem file

2. **Connect to EC2 Instance**
    - Use SSH client 
    - Authenticate with .pem key 

3. **Install Kafka**
    - Install Kafka version 2.12-2.8.1
    - Install IAM auth package
    - Configure IAM role for access
    - Connect Kafka client using IAM

4. **Create Kafka Topics** 
    - Retrieve MSK connection details
    - Create `<userId>.pin` topic
    - Create `<userId>.geo` topic 
    - Create `<userId>.user` topic

## Milestone 4 - Connect MSK to S3

### Tasks

1. **Identify S3 Bucket**
    - Note user-specific S3 bucket 

2. **Download S3 Connector**
    - Download Confluent S3 connector

3. **Create MSK Connect**
    - Create <userId>-plugin  
    - Create <userId>-connector
    - Configure connector
