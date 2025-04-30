import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('comments_labeled.csv')

label_cols = [
    'Check and Balance', 'PAP Conduct', 'Policy Gaps',
    'Credible Opposition', 'Political Pluralism', 'Grounded Opposition'
]

# Total unique comments
total_comments = len(df)

# Compute comment counts and percentage (unique comments per label)
comment_counts = df[label_cols].sum()
comment_pct = (comment_counts / total_comments * 100).round(1)

# Total unique upvotes (from all comments)
total_upvotes = df['upvotes'].sum()

# Compute upvotes per label (overlapping OK), then use total unique upvotes for percentage
upvote_counts = {label: df.loc[df[label] == 1, 'upvotes'].sum() for label in label_cols}
upvote_pct = {label: round(upvote_counts[label] / total_upvotes * 100, 1) for label in label_cols}

# Bar chart: Comment Counts with Percentages
plt.figure(figsize=(10, 5))
sorted_comments = comment_counts.sort_values(ascending=False)
sorted_pct_comments = comment_pct[sorted_comments.index]
ax = sorted_comments.plot(kind='bar', color='skyblue')
for i, (count, pct) in enumerate(zip(sorted_comments, sorted_pct_comments)):
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