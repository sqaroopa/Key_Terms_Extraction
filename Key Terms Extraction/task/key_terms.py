from nltk.tokenize import word_tokenize
from lxml import etree
from collections import Counter

xml_path = "news.xml"
tree = etree.parse(xml_path)
root = etree.parse(xml_path).getroot()

news = root[0]
for topic in news:
    header = topic[0].text
    text = topic[1].text
    freq_counter = Counter(sorted(word_tokenize(text.lower()), reverse=True))
    out_list = []
    for i in freq_counter.most_common(5):
        out_list.append(i[0])

    out = " ".join(out_list)

    print(f'{header}:\n{out}\n')
