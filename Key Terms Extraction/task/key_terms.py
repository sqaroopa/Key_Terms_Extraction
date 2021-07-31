import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from lxml import etree
from collections import Counter
from nltk.corpus import stopwords
import string

wnl = WordNetLemmatizer()
xml_path = "news.xml"
tree = etree.parse(xml_path)
root = etree.parse(xml_path).getroot()
news = root[0]
stop_words = set(stopwords.words('english'))
stop_words.update(string.punctuation)
punct = set(string.punctuation)

for topic in news:
    header = topic[0].text
    body = topic[1].text
    body_tokenized = word_tokenize(body.lower())
    filtered_body = []
    for w in body_tokenized:
        filtered_body.append(wnl.lemmatize(w))

    sorted_body = []
    for w in filtered_body:
        if w not in stop_words:
            sorted_body.append(w)

    sorted_nouns_wrong = []
    sorted_nouns = []
    for i in nltk.pos_tag(sorted_body):
        if i[1] == 'NN':
            sorted_nouns_wrong.append(i[0])

    for word in sorted_body:
        if nltk.pos_tag([word])[0][1] == "NN":
            sorted_nouns.append(word)

    freq_counter = Counter(sorted(sorted_nouns, reverse=True))
    out_list = []
    for i in freq_counter.most_common(5):
        out_list.append(i[0])
    out = " ".join(out_list)
    print(f'{header}:\n{out}')


# import nltk
# poem = ['Twinkle', ',', 'twinkle', ',', 'little', 'star', ',',
#         'How', 'I', 'wonder', 'what', 'you', 'are', '.',
#         'Up', 'above', 'the', 'world', 'so', 'high', ',',
#         'Like', 'a', 'diamond', 'in', 'the', 'sky', '.']
# out = []
# for i in nltk.pos_tag(poem):
#     if i[1] == 'NN':
#         # print(f'{i[0]}\n')
#         out.append(i[0])
# print(out)
# from nltk.stem import SnowballStemmer
#
#
# # the following line reads a text from the input and converts it into a list
# # sent = input().split()
# sent = 'Allen Leuten recht getan ist eine Kunst die niemand kann'.split()
# snowball = SnowballStemmer('german')
# for i in sent:
#     snowball.stem(f'{i}')

# from nltk.stem import SnowballStemmer
# snowball = SnowballStemmer('english')
# print(snowball.stem('playing')) # play
# print(snowball.stem('played'))   # play