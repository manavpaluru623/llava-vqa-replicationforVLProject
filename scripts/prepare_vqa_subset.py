import json, random
random.seed(42)

with open("v2_OpenEnded_mscoco_val2014_questions.json") as f:
    qs = json.load(f)["questions"]

subset = random.sample(qs, 500)

with open("questions.jsonl", "w") as f:
    for q in subset:
        f.write(json.dumps({
            "question_id": q["question_id"],
            "image": f"COCO_val2014_{q['image_id']:012d}.jpg",
            "text": q["question"]
        }) + "\n")
