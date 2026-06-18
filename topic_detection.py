import pandas as pd
import json
import re

print("Loading CSV...")

df = pd.read_csv(
    "data/conversations.csv",
    engine="python"
)

print("CSV Loaded")

all_messages = []

for conversation in df.iloc[:,0]:

    msgs = str(conversation).split("\\n")

    for msg in msgs:

        msg = msg.strip()

        if msg:
            all_messages.append(msg)

print("Total Messages:", len(all_messages))

# Save messages
with open("output/messages.json","w",encoding="utf-8") as f:
    json.dump(all_messages,f,indent=4)

print("Done")