# GitHub Issues Classification Script

This repository contains a script that uses a fine-tuned BERT model to classify GitHub issues into four categories: **Bug**, **Improvement**, **New Feature**, and **Task**.

## Model
The script uses a pre-trained BERT model, fine-tuned on a custom dataset, and is available on Hugging Face under the model name:


## Requirements

Before running the script, make sure you have Python installed along with the following packages:

- `transformers`
- `torch`

You can install them using the following command:

```bash
pip install transformers torch
```

## Usage

### 1. clone and get in the repository
### 2. Use the classification function
The script contains a function classify_issue(title, description) that takes the title and description of a GitHub issue as input and returns a category from the following labels:

- Bug
- Improvement
- New Feature
- Task
To use the function, you can modify the provided issue_title and issue_description in the script or pass your own values.
Example:
```
issue_title = "the compression format requested when saving a dataset in json format is not respected"
issue_description = "Describe the bug in the `to_json` method..."

print(classify_issue(issue_title, issue_description))
```
The model will return the predicted label for the issue based on its title and description.

### Example Output
```
Bug
```
### How It Works
1. The AutoTokenizer converts the input (title and description) into a format the model can process.
2. The AutoModelForSequenceClassification generates the predictions for the input data.
3. The label is mapped back to one of the four classes: Bug, Improvement, New Feature, or Task.


