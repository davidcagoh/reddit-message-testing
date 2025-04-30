import json
from keybert import KeyBERT
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

with open('filtered_comments.json') as f:
    comments = json.load(f)

texts = [c['text'].lower() for c in comments]

kw_model = KeyBERT()
results = []

for i, text in enumerate(texts):
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=3)
    results.append({
        'text': text,
        'upvotes': comments[i]['upvotes'],
        'keywords': keywords
    })

with open('comment_keywords.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"Extracted keywords for {len(results)} comments.")