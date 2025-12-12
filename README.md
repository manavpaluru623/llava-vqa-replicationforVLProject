# llava-vqa-replicationforVLProject
Small-scale replication of **LLaVA-1.5-7B** on the Visual Question Answering (VQA) task.

## Task
Visual Question Answering (VQA): given an image and a natural-language question, generate an answer grounded in the image.

## Model
- LLaVA-1.5-7B (released checkpoint)
- Official LLaVA evaluation scripts

## Dataset
- VQAv2 (validation split)
- COCO val2014 images
- Small-scale subset (200–500 samples)

## Results
- Reported VQAv2 accuracy (paper): ~78%
- Replicated subset accuracy: ~73%
- Simplified string-matching metric

## How to run (high level)
- Prepare subset questions JSONL
- Run `python -m llava.eval.model_vqa ...`
- Compute subset accuracy from predictions
