import json
import matplotlib.pyplot as plt
import numpy as np

with open('comments.json', 'r') as f:
    comments = json.load(f)

upvotes = [c['upvotes'] for c in comments]

print(f"Total comments: {len(upvotes)}")
print(f"Min: {min(upvotes)}, Max: {max(upvotes)}")
print(f"Median: {np.median(upvotes)}")
print(f"25th percentile: {np.percentile(upvotes, 25)}")
print(f"75th percentile: {np.percentile(upvotes, 75)}")

plt.hist(upvotes, bins=30, edgecolor='black')
plt.title('Distribution of Comment Upvotes')
plt.xlabel('Upvotes')
plt.ylabel('Number of Comments')
plt.yscale('log')  # optional: log scale if skewed
plt.show()

filtered = [c for c in comments if c['upvotes'] >= 2]

with open('filtered_comments.json', 'w') as f:
    json.dump(filtered, f, indent=4)

print(f"Filtered to {len(filtered)} comments with ≥2 upvotes.")