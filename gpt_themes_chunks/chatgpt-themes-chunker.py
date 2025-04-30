import json

with open('../filtered_comments.json') as f:
    comments = json.load(f)

chunks = []
chunk_size = 40
for i in range(0, len(comments), chunk_size):
    chunk = comments[i:i+chunk_size]
    chunk_text = "\n\n".join(f"{i+1}. {c['text']}" for i, c in enumerate(chunk))
    chunks.append(chunk_text)

for i, chunk in enumerate(chunks):
    filename = f'chunk_{i+1}.txt'
    with open(filename, 'w') as f:
        f.write("Here are 40 Reddit comments explaining why Singaporeans support the opposition. "
                "Group them into 4–6 distinct motivations. For each group, give a short descriptive name, "
                "a 1–2 sentence summary, and 2–3 representative quotes (no need to clean grammar). "
                "Focus on themes, values, or frustrations expressed.\n\n")
        f.write(chunk)
    print(f"Saved {filename}")