import pandas as pd
import glob

keywords = ['referendum']
files = []
df_concat = []
df_filtered = []

# Opening multiple CSV's
def open_files():
	files.extend(glob.glob("./input/*.csv"))

# Concat multiple CSV's into a single dataframe
def concat_files():
	for filename in sorted(files):
		df_concat.append(pd.read_csv(filename))

# Filter for keywords in the text column
def keyword_filter():
	for kw in keywords:
		df_full.text = df_full.text.str.lower()
		filtered = df_full.loc[df_full['text'].str.contains(kw, na=False)]
		df_filtered.append(filtered)

# Drop duplicate rows and unnecessary columns
def datatable_clean():
	df_clean.drop_duplicates(subset=["text"], inplace=True)
	df_clean.drop(df_clean.columns[[0]], inplace=True, axis=1)

# Process
open_files()
concat_files()

df_full = pd.concat(df_concat)
keyword_filter()

df_clean = pd.concat(df_filtered)
datatable_clean()

df_clean.to_csv('./output/output.csv',  index = False)
print "CSV's filtered and saved to the output folder"
