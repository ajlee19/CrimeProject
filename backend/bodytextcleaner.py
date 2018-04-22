import re
import pandas as pd
import numpy as np

dataset = pd.read_excel('data/parsed_crime_data.xlsx')
dataset
x = 0
dataset["Body_Text"] = dataset["Body_Text"].astype(str)
while (x < 4213):
    if dataset["Body_Text"][x] == None:
        x = x + 1 
        continue
    text = str(re.sub(r'<.*?>', '', dataset["Body_Text"][x])) 
    dataset["Body_Text"][x] = text
    x = x + 1

dataset = dataset[dataset["Body_Text"] != 'nan']
dataset.index = range(0, len(dataset))


dataset["Body_Text"][0]
writer = pd.ExcelWriter('cleaned_crime_data.xlsx')
dataset.to_excel(writer, 'Sheet1')
writer.save()
