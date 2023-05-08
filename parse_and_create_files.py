import hashlib

def sha256sum(filename):
    with open(filename, "rb") as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()

for file in os.listdir("files"):
    filepath = os.path.join("files", file)
    hash_value = sha256sum(filepath)
    print(f"File: {file}, SHA256: {hash_value}")
