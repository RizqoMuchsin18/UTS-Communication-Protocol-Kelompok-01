import json
import pandas as pd

with open("users.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

print(df[["id", "name", "username", "email","address","phone"]])

df.to_csv("users.csv", index=False)

print("File users.csv berhasil dibuat")