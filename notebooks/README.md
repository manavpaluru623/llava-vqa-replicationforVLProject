The Google Colab notebook used for this project contains the following steps:

1. Environment setup and dependency installation  
2. Downloading and preparing VQAv2 and COCO validation data  
3. Loading the LLaVA-1.5-7B pretrained checkpoint  
4. Running official LLaVA VQA inference  
5. Collecting predictions and computing subset accuracy  

Due to environment-specific paths and large model dependencies, the notebook
is not fully automated when run outside Colab. The structure and commands
closely follow the official LLaVA repository instructions.
Evaluation was performed on a reduced subset due to hardware constrainst
