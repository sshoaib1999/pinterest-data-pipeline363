
# Batch Processing - Configure EC2 Kafka Client and Connect MSK to S3

## Table of Contents

- [Milestone 3: Configure EC2 Kafka Client](#milestone-3-configure-ec2-kafka-client)
  - [Task 1: Create a .pem key file locally](#task-1-create-a-pem-key-file-locally)
  - [Task 2: Connect to the EC2 instance](#task-2-connect-to-the-ec2-instance)
  - [Task 3: Set up Kafka on the EC2 instance](#task-3-set-up-kafka-on-the-ec2-instance)
  - [Task 4: Create Kafka topics](#task-4-create-kafka-topics)
- [Milestone 4: Connect MSK Cluster to S3 Bucket](#milestone-4-connect-msk-cluster-to-s3-bucket)
  - [Step 1: Identify S3 Bucket](#step-1-identify-s3-bucket)
  - [Step 2: Download S3 Connector](#step-2-download-s3-connector)
  - [Step 3: Create MSK Connect Plugin & Connector](#step-3-create-msk-connect-plugin--connector)

## Milestone 3: Configure EC2 Kafka Client

### Task 1: Create a .pem key file locally

#### Step 1:  

Navigate to Parameter Store in your AWS account.  

Using your KeyPairId, locate the key pair associated with your EC2 instance.   

Copy the entire key pair value (including BEGIN and END headers).   

Paste it into a new file in VSCode with the .pem extension.

#### Step 2:

Navigate to the EC2 console and identify the instance with your unique UserId.

Find the Key pair name under the Details section and save the file in VSCode as KeyPairName.pem.  

### Task 2: Connect to the EC2 instance

Follow the Connect instructions (SSH client) on the EC2 console to connect to your EC2 instance.

### Task 3: Set up Kafka on the EC2 instance  

#### Step 1:

Install Kafka on your client EC2 machine (version 2.12-2.8.1).  

#### Step 2:

Install the IAM MSK authentication package on your client EC2 machine.

#### Step 3:

Navigate to the IAM console on your AWS account.  

In the Roles section, find and copy the ARN of the `<your_UserId>-ec2-access-role`.  

Edit trust policy, add IAM roles as the Principal type, and replace ARN with the copied ARN.

#### Step 4:  

Configure your Kafka client to use AWS IAM authentication by modifying the client.properties file.

### Task 4: Create Kafka topics  

#### Step 1:  

Retrieve Bootstrap servers string and Plaintext Apache Zookeeper connection string from the MSK Management Console.

#### Step 2:

Create the following three topics:
<your_UserId>.pin for Pinterest posts data

<your_UserId>.geo for post geolocation data
<your_UserId>.user for post user data


Ensure CLASSPATH is set properly before running Kafka commands.  

**Note:** You have permission to create topics only with the specified names.

## Milestone 4: Connect MSK Cluster to S3 Bucket   

### Step 1: Identify S3 Bucket

Go to the S3 console and find the bucket that contains your UserId. The bucket name should have the following format: user-`<your_UserId>`-bucket. Make a note of the bucket name, as you will need it in the next steps.

### Step 2: Download S3 Connector  

On your EC2 client, download the Confluent.io Amazon S3 Connector and copy it to the S3 bucket you have identified in the previous step.  

### Step 3: Create MSK Connect Plugin & Connector

Create your custom plugin in the MSK Connect console. For this project your AWS account only has permissions to create a custom plugin with the following name: `<your_UserId>`-plugin. Make sure to use this name when creating your plugin.  

For this project your AWS account only has permissions to create a connector with the following name: `<your_UserId>`-connector. Make sure to use this name when creating your connector.

Make sure to use the correct configurations for your connector, specifically your bucket name should be user-`<your_UserId>`-bucket.  

You should also pay attention to the topics.regex field in the connector configuration. Make sure it has the following structure: `<your_UserId>.*`. This will ensure that data going through all the three previously created Kafka topics will get saved to the S3 bucket.

When building the connector, make sure to choose the IAM role used for authentication to the MSK cluster in the Access permissions tab. Remember the role has the following format `<your_UserId>`-ec2-access-role. This is the same role you have previously used for authentication on your EC2 client, and contains all the necessary permissions to connect to both MSK and MSK Connect.

Now that you have built the plugin-connector pair, data passing through the IAM authenticated cluster, will be automatically stored in the designated S3 bucket.
