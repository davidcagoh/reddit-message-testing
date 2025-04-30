import json, csv

with open('filtered_comments.json') as f:
    comments = json.load(f)

label_fields = [
    "Check and Balance", "PAP Conduct", "Policy Gaps",
    "Credible Opposition", "Political Pluralism", "Grounded Opposition"
]

with open('unlabeled_comments.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['text', 'upvotes', 'date', 'author'] + label_fields)
    writer.writeheader()

    for c in comments:
        row = {
            'text': c['text'],
            'upvotes': c['upvotes'],
            'date': c['date'],
            'author': c['author'],
            **{label: 0 for label in label_fields}
        }
        writer.writerow(row)