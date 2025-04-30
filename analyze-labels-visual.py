import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('comments_labeled.csv')

label_cols = [
    'Check and Balance', 'PAP Conduct', 'Policy Gaps',
    'Credible Opposition', 'Political Pluralism', 'Grounded Opposition'
]

comment_counts = df[label_cols].sum()
total_comments_labeled = comment_counts.sum()
comment_pct = (comment_counts / total_comments_labeled * 100).round(1)

upvote_counts = {label: df.loc[df[label] == 1, 'upvotes'].sum() for label in label_cols}
total_upvotes_labeled = sum(upvote_counts.values())
upvote_pct = {label: round(upvote_counts[label] / total_upvotes_labeled * 100, 1) for label in label_cols}

# Bar chart: Comment Counts with Percentages
plt.figure(figsize=(10, 5))
ax = comment_counts.sort_values(ascending=False).plot(kind='bar', color='skyblue')
for i, (count, pct) in enumerate(zip(comment_counts.sort_values(ascending=False), comment_pct.sort_values(ascending=False))):
    ax.text(i, count + 1, f'{pct}%', ha='center', va='bottom')
plt.title('Number of Comments per Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('comment_counts.png')
plt.close()

# Bar chart: Upvote Counts with Percentages
sorted_upvotes = pd.Series(upvote_counts).sort_values(ascending=False)
sorted_pct = {k: upvote_pct[k] for k in sorted_upvotes.index}
plt.figure(figsize=(10, 5))
ax = sorted_upvotes.plot(kind='bar', color='salmon')
for i, (count, pct) in enumerate(zip(sorted_upvotes, sorted_pct.values())):
    ax.text(i, count + 1, f'{pct}%', ha='center', va='bottom')
plt.title('Total Upvotes per Category')
plt.ylabel('Upvotes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('upvote_counts.png')
plt.close()

print("Charts with percentages saved.")