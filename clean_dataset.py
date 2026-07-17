import pandas as pd
import re

csv_path = "/Users/cemkaya/Developer/PDF-to-InstructionDatasetPipeline/pipeline_workspace/exports/dataset.csv"
df = pd.read_csv(csv_path)

def is_junk(text):
    if not isinstance(text, str):
        return True
    
    # 1. Too short
    words = text.split()
    if len(words) < 5:
        return True
        
    # 2. TOC/Index pattern: high density of numbers
    num_count = sum(1 for w in words if any(c.isdigit() for c in w))
    if num_count / len(words) > 0.20: # If more than 20% of "words" contain numbers, likely TOC/Index
        return True
        
    # 3. Repeated sequences or very long words (junk)
    if max((len(w) for w in words), default=0) > 40:
        return True
        
    return False

initial_len = len(df)
df['is_junk'] = df['text'].apply(is_junk)

print("\nExamples of junk being dropped:")
for idx, row in df[df['is_junk']].head(5).iterrows():
    print(f"--- Junk ---")
    print(row['text'][:200])

df_clean = df[~df['is_junk']].copy()
df_clean.drop(columns=['is_junk'], inplace=True)

print(f"\nRemoved {initial_len - len(df_clean)} junk rows out of {initial_len}.")
print(f"Clean shape: {df_clean.shape}")

df_clean.to_csv("/Users/cemkaya/Developer/PDF-to-InstructionDatasetPipeline/pipeline_workspace/exports/dataset_cleaned.csv", index=False)
print("Saved to dataset_cleaned.csv")
