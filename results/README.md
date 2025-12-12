According to the original paper, LLaVA-1.5-7B achieves approximately 78% accuracy on the VQAv2 test-standard benchmark. In my replication, the model achieves an accuracy of 73% on a validation subset.

Model	Evaluation Setting	Accuracy
LLaVA-1.5-7B (reported)	VQAv2 test-std	~78%
LLaVA-1.5-7B (replicated)	VQAv2 validation subset	~73%

The difference between reported and replicated results is attributed to subset evaluation, the use of a simplified metric, and limited hardware resources. Despite this gap, the replicated performance remains consistent with expected behavior.
