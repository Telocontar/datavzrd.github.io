import pandas as pd


data_df = pd.read_csv("data/perimyo_sample.csv")

smaller_data_df = data_df.head(500)
smaller_data_df.to_csv("data/perimyo_sample_small.csv", index=False)

super_small_data_df = data_df.head(500).sample(n=100, axis="columns", random_state=42)
super_small_data_df.to_csv("data/perimyo_sample_500x100.csv", index=False)
print(super_small_data_df.columns)

# we want to filter for lab values
lab_data_df = data_df.head(500).filter(regex="lab_.+?_(2|7)day_(min|max|mean|std)")
ops_data_df = data_df.head(500).filter(regex="OPS-5-(3[0-9]|4[0-9]|50)")
icd_data_df = data_df.head(500).filter(regex="^ICD-I.*$")
other_data_df = data_df.head(500)[["age_at_OP", "TROP", "gender_female", "condition_main"]]

combined_df = pd.concat([lab_data_df, ops_data_df, icd_data_df, other_data_df], axis=1)
print(combined_df.shape)
combined_df = combined_df.dropna(how="all", axis=1)
combined_df.to_csv("data/perimyo_combined.csv", index=False)
