import random

# Read the source (incorrect) and target (correct) files
with open("data/source.txt", "r", encoding="utf-8") as f:
    source_lines = f.readlines()

with open("data/target.txt", "r", encoding="utf-8") as f:
    target_lines = f.readlines()

# Combine into "incorrect correct" format
combined = [s.strip() + " " + t.strip() + "\n" for s, t in zip(source_lines, target_lines)]

# Shuffle the combined lines
random.shuffle(combined)

# Split into train (80%) and dev (20%)
split_index = int(0.8 * len(combined))
train_lines = combined[:split_index]
dev_lines = combined[split_index:]

# Write files
with open("data/train.txt", "w", encoding="utf-8") as f:
    f.writelines(train_lines)

with open("data/dev.txt", "w", encoding="utf-8") as f:
    f.writelines(dev_lines)

print("train.txt and dev.txt created in data/ folder")
