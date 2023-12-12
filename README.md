# Batch Processing with Kafka on EC2

## Table of Contents 

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started) 
- [Configuration](#configuration)
- [Usage](#usage)
- [Additional Resources](#additional-resources)


## Introduction  

This project sets up a Kafka client on an EC2 instance to ingest and process streaming data using an AWS MSK Kafka cluster with IAM authentication.

## Prerequisites  

* EC2 instance
    
* IAM authenticated MSK Kafka cluster

* IAM roles and policies for access

* Key pair for SSH access to EC2
    

## Getting Started  

Follow these steps to set up the Kafka client on EC2:

1. Create key pair for EC2 access   
2. Connect to EC2 instance  
3. Install Kafka and IAM authentication packages   
4. Configure IAM role for authentication   
5. Modify Kafka configuration

## Configuration   

The main configuration files:

- **client.properties**: Kafka client configuration for IAM authentication

- **server.properties**: Kafka server properties like listener settings

Relevant environment variables:  

- `CLASSPATH`: Needs to contain Kafka jar files  

- `KAFKA_OPTS`: Kafka runtime options  


## Usage

With Kafka set up on EC2, you can:  

- Produce and consume streaming data  

- Use Kafka for batch data ingestion

- Build stream processing applications  

**Creating Topics**  

Make sure to create topics with correct bootstrap servers and permissions.

## Additional Resources  

- [Kafka Documentation](https://kafka.apache.org/documentation/)

- [AWS MSK Guide](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html)  

- [IAM Authentication](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html)

