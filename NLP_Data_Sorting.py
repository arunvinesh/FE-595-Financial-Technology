import pandas as pd
import glob

path = r"C:\Users\Arun vinesh\Documents\Arun\MS\Financial Services Analytics\FE-595-Financial Technology\Assignment\Assignment_3"
all_files = glob.glob(path + "/*.csv")

f = open("output_nlp_data_sorting.txt", "w")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame = frame.reset_index()
frame.drop("index", axis=True, inplace=True)
frame.drop_duplicates(subset="Name")


result = []
for row in frame["Purpose"]:
    pol_score = SIA().polarity_scores(row)
    pol_score["Purpose"] = row
    result.append(pol_score)

frame["Score"] = pd.DataFrame(result)["compound"]
df = frame.sort_values(by="Score", ascending=False)