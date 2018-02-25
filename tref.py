import pandas as pd
import glob

keywords = ['referendum']
df_filtered = []

# Concat multiple files into a single file
files = glob.glob("./data/*.csv")
df_list = []

for filename in sorted(files):
	df_list.append(pd.read_csv(filename))

full_df = pd.concat(df_list)
full_df.to_csv('./temp/output.csv')

# Open the single file, turn into a DataFrame and filter for keywords
data = pd.read_csv('./temp/output.csv')
df = pd.DataFrame(data)

for kw in keywords:
	filtered = df.loc[df['text'].str.contains(kw, na=False)]
	df_filtered.append(filtered)

df_res = pd.concat(df_filtered)

# Save filtered dataframe to a CSV
df_res.to_csv('./output/output.csv')
