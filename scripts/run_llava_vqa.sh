python -m llava.eval.model_vqa \
  --model-path checkpoints/llava-v1.5-7b \
  --question-file questions.jsonl \
  --image-folder coco/val2014 \
  --answers-file preds.jsonl \
  --temperature 0 \
  --conv-mode llava_v1 \
  --max_new_tokens 32
