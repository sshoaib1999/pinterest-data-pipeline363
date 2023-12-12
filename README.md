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



# Batch Processing with MSK Connect

## Overview

This project creates an MSK Connect connector to sync Kafka cluster data from an IAM authenticated MSK cluster to an S3 bucket, enabling automated ingestion pipelines.

**Key Components:**

- EC2 Kafka client
- IAM authenticated MSK cluster
- S3 bucket for storage  
- Custom connector plugin/connector

**Learnings:**

- MSK Connect architecture
- Building custom plugins and connectors
- Kafka to S3 stream ingestion pipelines  

## Prerequisites

- EC2 instance with Kafka client
- IAM authenticated MSK cluster 
- S3 bucket with appropriate permissions 
- IAM roles for access

## Connector Setup 

**Plugin Configuration**

1. Identify S3 bucket name
2. Download Confluent connector 
3. Build `<user_id>-plugin` plugin in MSK Connect

**Connector Configuration**  

1. Name connector `<user_id>-connector`
2. Point to correct S3 bucket  
3. Set `topics.regex` to `<user_id>.*` 
4. Choose IAM role for access  

Once built, the connector automatically syncs Kafka data to the S3 bucket.

## Additional Resources

- MSK Connect Guide
- IAM Permissions
- S3 Bucket for Storage

- [IAM Authentication](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html)


# Batch Processing with Configuring API in API Gateway

## Introduction

This project implements an end-to-end streaming data pipeline by integrating API Gateway, Kafka, and S3 services on AWS.  

Data is ingested via a REST API built in API Gateway. The API passes data to an MSK Kafka cluster using a Kafka REST proxy hosted on EC2. Finally, an MSK Connect connector streams the Kafka data into an S3 bucket for storage and analysis.  

## Overview   

This project builds an end-to-end streaming data pipeline by integrating:  

- API Gateway with Kafka REST proxy
- MSK Kafka cluster 
- S3 storage via MSK Connect connector  

**Key Components:**   

- API Gateway with proxy integration 
- EC2 Kafka client
- IAM authenticated MSK cluster
- Custom connector and plugin
- S3 bucket  

**Learnings:**  

- Implementing streaming data pipelines   
- Building APIs and Kafka connectors  
- Moving and processing data across services

## Prerequisites  


- API Gateway API  
- EC2 instance with Kafka    
- IAM authenticated MSK cluster
- S3 bucket    
- Appropriate IAM roles and policies  

## Installation    

**REST Proxy Integration**   

1. Create proxy resource in API Gateway 
2. Set up ANY method with EC2's Public DNS  
3. Deploy API and note invoke URL   

**Kafka REST Proxy**    

1. Install Confluent REST proxy package   
2. Modify properties for IAM authentication
3. Start proxy on EC2   

**Connector Setup**   

1. Create plugin in MSK Connect  
2. Build connector using cluster permissions
3. Configure regex to capture data

