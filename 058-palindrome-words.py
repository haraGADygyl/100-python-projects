import re

text = 'LOL, My interview went good. My Mom will be so happy.'

clean_text = re.sub(r'[^a-zA-Z ]', '', text)

for i in clean_text.split():
    if i.lower() == i[::-1].lower():
        print(i)
