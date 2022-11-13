from transformers import pipeline

classifire = pipeline("sentiment-analysis")

classifire1 = pipeline("sentiment-analysis", model = "blanchefort/rubert-base-cased-sentiment")

result = classifire("I hate somebady")

result1  = classifire1("Я ненавижу тебя")

print(result, result1)
