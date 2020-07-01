from pprint import pprint
import pandas as pd
import json

# reading the html file
with open('New Lead .html', 'r') as f:
    data = f.read()

df = pd.read_html(data, flavor="lxml")[0]

new_header = df.iloc[0]
df = df[1:]
df.columns = new_header

#using pandas to extract data
details_dict = df.to_dict('records')
result_list = [v for k,v in details_dict[1].items()]

#converting list to string extracting required data fields
str1 = ''.join(result_list[0])
li = list(str1.split("  "))
stringname = li[5]
name = stringname.split(' ', 1)[1]

#converting into json
json_dict = {
    'name': name,
    'phone': li[13],
    'email': li[14]
}

#output to json file
with open('output.json', 'w') as f:
  json.dump(json_dict, f, ensure_ascii=False)
  pprint("output data in output.json file")

