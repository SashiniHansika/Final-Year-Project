import nltk
import inflect
from nltk.tokenize import word_tokenize, sent_tokenize

stopAttributes = ["no", "number", "date","code", "volume", "type", "name", "id", "address", "birth","s","'","location", "gender"]
visited = set()
p = inflect.engine()

input_text = open("input_text5.txt","r")
scenario = input_text.read()

postxt=[]
wordsFilter = []
commonNouns = []
attributeFilter = []
singularNouns = []
output = []


def preprocess_data(senario):
    lowertxt = word_tokenize(scenario.lower())
    postxt = nltk.pos_tag(lowertxt)
    word_filter(postxt)

def word_filter(postxt):
    stopWords = ["database", "information", "system", "record"]
    for w in postxt:
        if w[0] not in stopWords:
            wordsFilter.append(w)
    common_nouns(wordsFilter)

def common_nouns(wordsFilter):
    for w in wordsFilter:
        if w[1] == "NN" or w[1] == "NNS":
            commonNouns.append(w)
    stop_attributes(commonNouns)

def stop_attributes(commonNouns):
    for w in commonNouns:
        if w[0] not in stopAttributes:
            attributeFilter.append(w)
    convert_singular(attributeFilter)

def convert_singular(attributeFilter):
    for i in attributeFilter:
        if i[1] == "NNS":
            singularNouns.append((p.singular_noun(i[0]), i[1]))
        else:
            singularNouns.append(i)
    remove_duplicates(singularNouns)

def remove_duplicates(singularNouns):
    for a, b in singularNouns:
        if not a in visited:
            visited.add(a)
            output.append((a, b))

preprocess_data(scenario)
entity_from_noun_list = []
for i in output:
    entity_from_noun_list.append(i[0])

print(entity_from_noun_list)

'''(entity_from_noun_list)
sentence_list = sent_tokenize(scenario)

for sentece in sentence_list:
    word_list = word_tokenize(sentece)
    for word in word_list:
        index = word_list.index(word)
        next_index =  index+ 1
        print(word_list[next_index])'''