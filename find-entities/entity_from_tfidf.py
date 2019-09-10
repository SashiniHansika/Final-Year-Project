from sklearn.feature_extraction.text import CountVectorizer
import re

sentences = list()
with open("input_text5.txt") as file:
    for line in file:
        for l in re.split(r"\.\s|\?\s|\!\s|\n",line):
            if l:
                sentences.append(l)
cvec = CountVectorizer(stop_words='english', min_df=2, max_df=0.9, ngram_range=(0,1))
sf = cvec.fit_transform(sentences)

entity_tf_idf_model = []
entity_tf_idf_model = cvec.get_feature_names()

print(entity_tf_idf_model)