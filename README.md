# pinterest-data-pipeline363

Milestone 3: Batch Processing - Configure the EC2 Kafka Client

Table of Contents
Task 1: Create a .pem key file locally
Task 2: Connect to the EC2 instance
Task 3: Set up Kafka on the EC2 instance
Task 4: Create Kafka topics
Task 1: Create a .pem key file locally
Step 1:
Navigate to Parameter Store in your AWS account.
Using your KeyPairId, locate the key pair associated with your EC2 instance.
Copy the entire key pair value (including BEGIN and END headers).
Paste it into a new file in VSCode with the .pem extension.
Step 2:
Navigate to the EC2 console and identify the instance with your unique UserId.
Find the Key pair name under the Details section and save the file in VSCode as KeyPairName.pem.
Task 2: Connect to the EC2 instance
Follow the Connect instructions (SSH client) on the EC2 console to connect to your EC2 instance.
Task 3: Set up Kafka on the EC2 instance
Step 1:
Install Kafka on your client EC2 machine (version 2.12-2.8.1).
Step 2:
Install the IAM MSK authentication package on your client EC2 machine.
Step 3:
Navigate to the IAM console on your AWS account.
In the Roles section, find and copy the ARN of the <your_UserId>-ec2-access-role.
Edit trust policy, add IAM roles as the Principal type, and replace ARN with the copied ARN.
Step 4:
Configure your Kafka client to use AWS IAM authentication by modifying the client.properties file.
Task 4: Create Kafka topics
Step 1:
Retrieve Bootstrap servers string and Plaintext Apache Zookeeper connection string from the MSK Management Console.
Step 2:
Create the following three topics:
<your_UserId>.pin for Pinterest posts data
<your_UserId>.geo for post geolocation data
<your_UserId>.user for post user data
Ensure CLASSPATH is set properly before running Kafka commands.
Note: You have permission to create topics only with the specified names.

License
This project is licensed under the MIT License.
