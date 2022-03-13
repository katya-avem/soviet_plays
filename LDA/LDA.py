import pandas as pd
import gensim
import os
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)
import nltk
nltk.download('wordnet')


path = "C:/Users/katya/Documents/PyCharmProjects/soviet_plays/LDA"
dirs = os.listdir(path)


def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(token)
    return result

with open(os.path.join(path, 'ALL_SPEECH_FIO.txt'), encoding="utf-8") as file:

    df = np.array([file.read().split('\n')])
    df = pd.DataFrame(df.T)
    print(df)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_df=0.95, min_df=2, stop_words=["и", "в", "во", "не", "что", "он", "оно", "на", "я", "с", "со", "как", "а", "то", "это", "все", "она", "так", "его", "весь", "но", "да", "ты", "к", "у", "же", "вы", "за", "бы", "по", "только", "ее", "мне", "меня", "мень", "было", "вот", "от", "меня", "еще", "нет", "о", "из", "ему", "теперь", "когда", "даже", "ну", "вдруг", "ли", "если", "уже", "или", "ни", "быть", "был", "него", "до", "вас", "опять", "уж", "вам", "ведь", "там", "потом", "себя", "ничего", "ей", "может", "они", "тут", "где", "есть", "надо", "ней", "для", "мы", "тебя", "их", "чем", "была", "сам", "чтоб", "без", "будто", "чего", "раз", "тоже", "себе", "под", "будет", "ж", "тогда", "кто", "этот", "того", "потому", "этого", "какой", "совсем", "ним", "здесь", "этом", "один", "почти", "мой", "тем", "чтобы", "нее", "сейчас", "были", "куда", "зачем", "всех", "никогда", "можно", "при", "наконец", "два", "об", "другой", "хоть", "после", "над", "больше", "тот", "через", "эти", "нас", "про", "всего", "них", "какая", "много", "разве", "три", "эту", "моя", "впрочем", "хорошо", "свою", "этой", "перед", "иногда", "лучше", "чуть", "том", "нельзя", "такой", "им", "более", "всю", "между"])
dtm = cv.fit_transform(df[0])
from sklearn.decomposition import LatentDirichletAllocation
LDA = LatentDirichletAllocation(n_components=6,random_state=42)
LDA.fit(dtm)

single_topic = LDA.components_[0]
top_10_words = single_topic.argsort()[-10:]

for index in top_10_words:
    print(cv.get_feature_names()[index])

for index,topic in enumerate(LDA.components_):
    print(f'THE TOP 15 WORDS FOR TOPIC #{index}')
    print([cv.get_feature_names()[i] for i in topic.argsort()[-15:]])
    print('\n')

topic_results = LDA.transform(dtm)
print(topic_results.shape)
print(topic_results[0])

print(topic_results[0].round(2))
df['Topic'] = topic_results.argmax(axis=1)
