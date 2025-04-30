import pandas as pd

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

# Build DataFrame
summary_df = pd.DataFrame({
    'Comment Count': comment_counts,
    'Comment %': comment_pct,
    'Upvote Total': pd.Series(upvote_counts),
    'Upvote %': pd.Series(upvote_pct)
}).sort_values(by='Comment Count', ascending=False)

summary_df.to_csv('summary_table.csv')
summary_df.to_markdown('summary_table.md')

print(summary_df)