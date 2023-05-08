import os
import requests
import hashlib

# Create the 'files' sub-directory if it doesn't exist
if not os.path.exists("files"):
    os.makedirs("files")

# Get the data from the application
response = requests.get("http://localhost:5000/data")
data = response.json()

# Parse and save the data
for sample in data["samples"]:
    file_name = f"files/{sample['id']}.txt"
    content = sample["name"]

    # Verify that the SHA256 hash of the content matches the id
    content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
    if content_hash == sample["id"]:
        with open(file_name, "w") as file:
            file.write(content)
    else:
        print(f"Hash mismatch: expected {sample['id']}, got {content_hash}")

