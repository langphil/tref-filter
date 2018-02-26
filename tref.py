import pandas as pd
import glob

keywords = ['referendum']
files = []
df_concat = []
df_full = []
df_filtered = []

# Opening multiple CSV's
def open_file():
	files.extend(glob.glob("./input/*.csv"))

# Concat multiple CSV's into a single dataframe
def concat_files():
	for filename in sorted(files):
		df_concat.append(pd.read_csv(filename))
	df_full.extend(pd.concat(df_concat))

# Filter for keywords in the text column
def keyword_filter():
	print df_full
	for kw in keywords:
		df_full.text = df_full.text.str.lower()
		filtered = df_full.loc[df_full['text'].str.contains(kw, na=False)]
		df_filtered.append(filtered)

# Drop duplicate rows and unnecessary columns
def datatable_clean():
	df_res.drop_duplicates(subset=["text"], inplace=True)
	df_res.drop(df_res.columns[[0]], inplace=True, axis=1)

# Process
open_file()
concat_files()
keyword_filter()
df_res = pd.concat(df_filtered)
datatable_clean()
print "CSV's filtered and saved to the output folder"
df_res.to_csv('./output/output.csv',  index = False)
