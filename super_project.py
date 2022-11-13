from transformers import pipeline

classifire = pipeline("sentiment-analysis")

result = classifire("I hate somebady")
print(result)