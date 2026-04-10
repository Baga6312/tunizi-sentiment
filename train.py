import os
import json
import gzip

output = []

# Process Barcha files (same as before)
for root, dirs, files in os.walk("dataset"):
    for file in files:
        if file.endswith(".txt") and "TUNIZI" not in file:
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        output.append({
                            "text": line,
                            "source": file,
                            "label": None
                        })
        elif file.endswith(".gz"):
            path = os.path.join(root, file)
            with gzip.open(path, "rt", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        output.append({
                            "text": line,
                            "source": file,
                            "label": None
                        })

# Process TUNIZI file
tunizi_path = "dataset/TUNIZI-Dataset.txt"
with open(tunizi_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        # Split label and text
        if ';' in line:
            parts = line.split(';', 1)
            label = parts[0].strip()
            text = parts[1].strip()
            
            # Convert % label to "neutral"
            if label == '%':
                label = "neutral"
            
            output.append({
                "text": text,
                "source": "TUNIZI-Dataset.txt",
                "label": label
            })

# Save
with open("dataset/all_lines_labeled.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Total lines: {len(output)}")
print("Saved to: dataset/all_lines_labeled.json")