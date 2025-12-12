# LLaVA-1.5 VQA Replication (VL Course Project)

This repository contains a small-scale replication of LLaVA-1.5-7B on the
Visual Question Answering (VQA) task. The project reproduces reported performance
using the released model and official evaluation pipeline under limited
computational resources.

---

## Repository Contents

- **README.md**  
  Overview of the project, repository structure, and instructions to install
  dependencies and run the replication.

- **requirements.txt**  
  Python package dependencies required to run the evaluation scripts.

- **scripts/prepare_vqa_subset.py**  
  Samples a small subset of questions from the VQAv2 validation set and writes
  them in JSONL format expected by the LLaVA evaluation script.

- **scripts/run_llava_vqa.sh**  
  Runs the official LLaVA Visual Question Answering inference script on the
  prepared subset using the LLaVA-1.5-7B checkpoint.

- **scripts/evaluate_accuracy.py**  
  Computes a simplified accuracy metric by comparing model predictions against
  VQAv2 ground-truth answers.

- **notebooks/**  
  Contains documentation related to the Google Colab notebook used for
  replication.

- **results/**  

## Installation

This project was tested in a Google Colab environment.
