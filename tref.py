import pandas as pd
import glob

keywords = ['abortion']
df_filtered = []

# Concat multiple files into a single file
files = glob.glob("./data/*.csv")
df_list = []

for filename in sorted(files):
	df_list.append(pd.read_csv(filename))

full_df = pd.concat(df_list)
full_df.to_csv('./temp/output.csv')

# Open the single file, turn into a DataFrame, filter for keywords and append
# to the array of datatables
data = pd.read_csv('./temp/output.csv')
df = pd.DataFrame(data)

for kw in keywords:
	df.text = df.text.str.lower()
	filtered = df.loc[df['text'].str.contains(kw, na=False)]
	df_filtered.append(filtered)

# Concatenate the array of datatables and drop duplicate rows
df_res = pd.concat(df_filtered)
df_res.drop_duplicates(subset=["text"], inplace=True)
df_res.drop(df_res.columns[[0]], inplace=True, axis=1)

# Save filtered dataframe to a CSV
print "CSV's filtered and saved to the outputs folder"
df_res.to_csv('./output/output.csv',  index = False)
