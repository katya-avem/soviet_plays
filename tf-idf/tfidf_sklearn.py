import glob
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
import os

directory_path = "../speech_of_characters (replaced name)"


text_files = glob.glob(f"{directory_path}/*.txt")
text_files = [Path(file_path) for file_path in text_files]
text_titles = [path.stem for path in text_files]
text_files = [path.read_text(encoding='utf-8') for path in text_files]

tfidf_vectorizer = TfidfVectorizer(input='content', smooth_idf=False, norm=None, use_idf=False)
tf_matrix = tfidf_vectorizer.fit_transform(text_files)
tf_matrix = tf_matrix.toarray()

document_total_words_count = [text_file.count(' ') for text_file in text_files]
document_total_words_count = np.array(document_total_words_count)

tf_matrix = (tf_matrix.T / document_total_words_count).T

idf_matrix = (tf_matrix > 0)
idf_matrix = np.sum(idf_matrix, axis=0)
idf_matrix = 13 / idf_matrix
idf_matrix = np.log(idf_matrix)

tfidf_matrix = tf_matrix * idf_matrix
tfidf_df = pd.DataFrame(tfidf_matrix, index=text_titles, columns=tfidf_vectorizer.get_feature_names_out())
tfidf_df = tfidf_df.stack().reset_index()
tfidf_df = tfidf_df.rename(columns={0: 'tf_idf', 'level_0': 'document', 'level_1': 'term', 'level_2': 'term'})

result_df = tfidf_df.sort_values(by=['document', 'tf_idf'], ascending=[True, False]).groupby(['document']).head(30)
result_df.to_excel('./tf_idf.xlsx')

with pd.option_context('display.max_rows', 100):
    print(result_df)

