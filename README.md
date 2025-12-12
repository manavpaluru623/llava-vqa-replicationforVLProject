# llava-vqa-replicationforVLProject
This repository contains a small-scale replication of LLaVA-1.5-7B on the
Visual Question Answering (VQA) task.

The goal is to reproduce reported performance using the released model and
official evaluation pipeline under limited computational resources.

## Task
Visual Question Answering (VQA): given an image and a natural-language question,
generate a textual answer grounded in the image.

## Model
- LLaVA-1.5-7B
- Official pretrained checkpoint
- Official LLaVA evaluation scripts

## Dataset
- VQAv2 (validation split)
- COCO val2014 images
- Small-scale subset (200–500 samples)

## Results
- Reported VQAv2 accuracy: ~78%
- Replicated subset accuracy: ~73%
- Evaluation uses a simplified string-matching metric

## Notes
Evaluation was performed on a reduced subset due to hardware constraints.
