import json

with open("preds.jsonl") as f:
    preds = [json.loads(line) for line in f]

with open("v2_OpenEnded_mscoco_val2014_annotations.json") as f:
    ann = json.load(f)["annotations"]

gt = {a["question_id"]: a["multiple_choice_answer"].lower() for a in ann}

correct = 0
for p in preds:
    if gt[p["question_id"]] in p["text"].lower():
        correct += 1

print("Accuracy:", correct / len(preds))
