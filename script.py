from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


model_name = "peler1nl1kelt0s/github-issues-classification-final"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def classify_issue(title, description):
    inputs = tokenizer(f"{title} {description}", return_tensors="pt")
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
    label_mapping = {0: "Bug", 1: "Improvement", 2: "New_feature", 3: "Task"}
    return label_mapping[predictions.item()]

issue_title = "the compression format requested when saving a dataset in json format is not respected"
issue_description = "Describe the bug In the documentation of the `to_json` method, it is stated in the parameters that > **to_json_kwargs  Parameters to pass to pandass pandas.DataFrame.to_json. however when we pass for example `compression=gzi`, the saved file is not compressed. Would you also have expected compression to be applied? :relaxed: ## Steps to reproduce the bug ```python my_dict = a: [1, 2, 3], : [1, 2, 3]}  ### Result with datasets ```python from datasets import Dataset dataset = Dataset.from_dict(my_dict) dataset.to_json dic_with_datasets.jsonl.gz, compression=gzip) !cat dic_with_datasets.jsonl.gz ``` output  a:1,b:1} a:2,b:2} a:3,b:3}  Note: I would expected to see binary data here ### Result with pandas ```python import pandas as pd df = pd.DataFrame(my_dict)"
print(classify_issue(issue_title, issue_description))
