import xml.etree.ElementTree as ET
import nltk
from nltk.corpus import stopwords
import re

# from nltk.tokenize import sent_tokenize, word_tokenize
filtered_sentence_list = []

text_file = open("input_text.txt", "r")
stopWords = set(stopwords.words('english'))

if text_file.mode == 'r':
    input_text_load = text_file.read()
    input_text = input_text_load.lower()
    # print(input_text)

new_word_list = []


def xml_input_handling():
    tree = ET.parse("input_xml.xml")
    root = tree.getroot()
    return root


def find_entities(word):
    root = xml_input_handling()
    for entity_ref in root.findall('entity'):
        entity = entity_ref.get('name')
        if word == entity:
            return word


def entity_combined_with_scenario():
    sentences = text_into_sentence()
    for sentence in sentences:
        entity_list = []
        word_list = nltk.word_tokenize(sentence)
        # print(sentence)
        for word in word_list:
            word_new = find_entities(word)
            if word_new is not None:
                entity_list.append(word_new)

        # print(entity_list)
        if len(entity_list) >= 2:
            # if len(entity_list) == 3 :
            #     new_entity_list = list(dict.fromkeys(entity_list))
            # if len(entity_list) == 4 :
            #
            # print(entity_list, sentence)

            # entity_list_dic = []
            #
            # for entity in entity_list:
            #     index = entity.index()
            #     member_number = index + 1
            #     entity_name = "member" + member_number
            #     entity_list_dic.append({entity_name : entity})
            #     print(entity_list_dic)

            # print(sentence)
            find_relationship(entity_list, sentence)
            # index = word_list.index(word_new)
            # new_word = {'entity' : word_new}
            # print(sentence)

        # print(word_list)
        # sentences = ''.join(word_list)
        # print(sentences)


def find_relationship(entity_list, sentence):
    word_list = sentences_into_word(sentence)
    pos_tag_list = nltk.pos_tag(word_list)
    # print(entity_list)
    # print(sentence)
    test = []
    if len(entity_list) == 2 or len(entity_list) == 4:
        for data in pos_tag_list:
            for entity in entity_list:
                # print(data[0])
                # print(entity_list)
                if data[0] == entity:
                    # print(entity)
                    member_name = 'member' + str(entity_list.index(entity) + 1)
                    index = pos_tag_list.index(data)
                    test.append({member_name: entity, 'index': index})
                    # print(test)
                    if len(test) == 2:
                        first_index = test[0].get('index')
                        second_index = test[1].get('index') + 1
                        # print(first_index , second_index)
                        temp_list = pos_tag_list[first_index: second_index]
                        relationship_list = []
                        for data in temp_list:
                            # print(data[0])
                            if data[1] == 'VBG' or data[1] == 'VBD' or data[1] == 'VB' or data[1] == 'VBP' or data[
                                1] == 'VBN' or data[1] == 'VBZ':
                                relationship_list.append(data[0])
                                # print(sentence)
                        # print(relationship_list)
                        if relationship_list:
                            if len(relationship_list) > 1:
                                relationship = relationship_list[0]+'_'+relationship_list[1]
                            else:
                                relationship = relationship_list[0]
                            print(test[0].get('member1'))
                            print(relationship)
                            print(test[1].get('member2'))
                            print('######################################')

                        # print(test)
                        # print(sentence)

    # for data in pos_tag_list:
    #     if data[0] == entity:
    #         temp_entity = data[0]
    #         print(temp_entity)
    #     if re.match(r'VB.*', data[1]):
    #         # data[1] == 'VBZ':
    #         print(data[0])
    # print(pos_tag_list)
    # print(sentence)


def removing_stopwords(words):
    for w in words:
        if w not in stopWords:
            filtered_sentence_list.append(w)
            return filtered_sentence_list


def text_into_sentence():
    return nltk.sent_tokenize(input_text)


def sentences_into_word(sentence):
    word = nltk.word_tokenize(sentence)
    return word


# def text_pos_tagging():
#     sentences = text_into_sentence()
#     for sentence in sentences:
#         word = nltk.word_tokenize(sentence)
#         print(nltk.pos_tag(word))
#
#
# #
# # entity_combined_with_scenario()
# # text_pos_tagging()
#
# def sentences_into_word():
#     word = nltk.word_tokenize(input_text)
#     # for i in word:
#     #     print(i)
#
#     return word


# sentences_into_word()
# text_pos_tagging()
entity_combined_with_scenario()
