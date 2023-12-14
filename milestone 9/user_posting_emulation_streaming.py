import requests
import json 
import pandas as pd
from time import sleep 

# Original user posting emulation script 
import user_posting_emulation as upe

# Kinesis stream names
users_stream = "users"
boards_stream = "boards"
pins_stream = "pins"

# API Gateway endpoints
users_url = "<users-api-invoke-url>"
boards_url = "<boards-api-invoke-url>" 
pins_url = "<pins-api-invoke-url>"

# Generate sample data
users = upe.generate_users(10) 
boards = upe.generate_boards(20)
pins = upe.generate_pins(30)

# Send users data 
for index, row in users.iterrows():
    payload = {"Data": row.to_json(), "PartitionKey": str(row["user_id"])}
    response = requests.put(users_url, json=payload)
    print(response.status_code)
    sleep(1)

# Send boards data
for index, row in boards.iterrows(): 
    payload = {"Data": row.to_json(), "PartitionKey": str(row["board_id"])}  
    response = requests.put(boards_url, json=payload)
    print(response.status_code)
    sleep(1)

# Send pins data 
for index, row in pins.iterrows():
    payload = {"Data": row.to_json(), "PartitionKey": str(row["pin_id"])}   
    response = requests.put(pins_url, json=payload)
    print(response.status_code)
    sleep(1)
