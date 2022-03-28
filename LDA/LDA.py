import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.stem.porter import *

np.set_printoptions(suppress=True)
# nltk.download('wordnet')


if __name__ == '__main__':
    with open('./Speech_with_replaced_names.txt', encoding="utf-8") as file:
        texts = file.readlines()
        texts = [text.strip() for text in texts]
        texts = [re.sub("['\[\],]", "", text) for text in texts]

    stop_words = ["и", "в", "во", "не", "что", "он", "оно", "на", "я", "с", "со", "как", "а", "то", "это", "все", "она",
                  "так", "его", "весь", "но", "да", "ты", "к", "у", "же", "вы", "за", "бы", "по", "только", "ее", "мне",
                  "меня", "мень", "было", "вот", "от", "меня", "еще", "нет", "о", "из", "ему", "теперь", "когда",
                  "даже", "ну", "вдруг", "ли", "если", "уже", "или", "ни", "быть", "был", "него", "до", "вас", "опять",
                  "уж", "вам", "ведь", "там", "потом", "себя", "ничего", "ей", "может", "они", "тут", "где", "есть",
                  "надо", "ней", "для", "мы", "тебя", "их", "чем", "была", "сам", "чтоб", "без", "будто", "чего", "раз",
                  "тоже", "себе", "под", "будет", "ж", "тогда", "кто", "этот", "того", "потому", "этого", "какой",
                  "совсем", "ним", "здесь", "этом", "один", "почти", "мой", "тем", "чтобы", "нее", "сейчас", "были",
                  "куда", "зачем", "всех", "никогда", "можно", "при", "наконец", "два", "об", "другой", "хоть", "после",
                  "над", "больше", "тот", "через", "эти", "нас", "про", "всего", "них", "какая", "много", "разве",
                  "три", "эту", "моя", "впрочем", "хорошо", "свою", "этой", "перед", "иногда", "лучше", "чуть", "том",
                  "нельзя", "такой", "им", "более", "всю", "между"]

    cv = CountVectorizer(max_df=0.95, min_df=2, stop_words=stop_words)
    tf = cv.fit_transform(texts)

    n_components = 5
    LDA = LatentDirichletAllocation(n_components=n_components)
    LDA.fit(tf)

    top_words = []
    for i in range(n_components):
        component = LDA.components_[i]
        words_indices = component.argsort()[-10:]
        words = [cv.get_feature_names_out()[j] for j in words_indices]
        top_words.append(words)

    for item in top_words:
        print(item)

    topic_results = LDA.transform(tf).round(2)
    print()
    print(topic_results)

    topic_results = topic_results.argmax(axis=1)
    print()
    print(topic_results + 1)

