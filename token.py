import secrets
import json
import os
import re

def generate_token():
    return secrets.token_hex(32)

def save_token(node_id, token, folder="credentials"):
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f"node_{node_id}_token.json")
    with open(filepath, "w") as f:
        json.dump({"node_id": node_id, "token": token}, f)
    print(f"[INFO] Token za node {node_id} spremljen u {filepath}")

def extract_node_ids(folder="."):
    node_ids = set()
    pattern = re.compile(r"node_(\d+)")
    for filename in os.listdir(folder):
        match = pattern.match(filename)
        if match:
            node_ids.add(int(match.group(1)))
    return sorted(node_ids)

if __name__ == "__main__":
    detected_nodes = extract_node_ids(".")  # traži po trenutnom direktoriju
    if not detected_nodes:
        print("[WARN] Nema node_ fajlova u trenutnom direktoriju. Prekida se.")
        exit(0)

    for node_id in detected_nodes:
        token = generate_token()
        save_token(node_id=node_id, token=token)
