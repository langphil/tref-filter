import pandas as pd
import glob

keywords = ['abortion']
df_filtered = []

# Opening multiple CSV's
files = glob.glob("./input/*.csv")
df_list = []

# Concat multiple CSV's into a single dataframe
for filename in sorted(files):
	df_list.append(pd.read_csv(filename))

df_full = pd.concat(df_list)

# Filter for keywords in the text column
for kw in keywords:
	df_full.text = df_full.text.str.lower()
	filtered = df_full.loc[df_full['text'].str.contains(kw, na=False)]
	df_filtered.append(filtered)

# Concatenate the array of datatables
df_res = pd.concat(df_filtered)

# Drop duplicate rows and unnecessary columns
df_res.drop_duplicates(subset=["text"], inplace=True)
df_res.drop(df_res.columns[[0]], inplace=True, axis=1)

# Save filtered dataframe to a CSV
print "CSV's filtered and saved to the output folder"
df_res.to_csv('./output/output.csv',  index = False)
