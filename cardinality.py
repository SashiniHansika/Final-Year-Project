from relationship import relationship_dic_list
from pattern.en import pluralize, singularize,conjugate, lemma, lexeme
import nltk


print(relationship_dic_list)
text_file = open("input_text.txt", "r")

if text_file.mode == 'r':
    # Read the scenario and covert that text file into lowercase
    input_text_load = text_file.read()
    input_text = input_text_load.lower()
    # print(input_text)


def text_into_sentence():
    return nltk.sent_tokenize(input_text)


def sentences_into_word(sentence):
    word = nltk.word_tokenize(sentence)
    return word


def get_sentences_match_with_entities(member1, member2):
    sentence_list = text_into_sentence()
    matching_sentences_list = []
    for sentence in sentence_list:
        # print(sentence)
        word_list = sentences_into_word(sentence)
        nouns_list = get_nouns_list(word_list)
        # print(nouns_list)
        # print(word_list)
        for noun in nouns_list:
            if noun == member1:
                index_of_first_member = nouns_list.index(noun)
                new_noun_list = nouns_list[index_of_first_member + 1:]
                for second_noun in new_noun_list:
                    if second_noun == member2:
                        matching_sentences_list.append(sentence)
                        # print(matching_sentences_list)
        for noun in nouns_list:
            if noun == member2:
                index_of_first_member = nouns_list.index(noun)
                new_noun_list = nouns_list[index_of_first_member + 1:]
                for second_noun in new_noun_list:
                    if second_noun == member1:
                        matching_sentences_list.append(sentence)
                        # print(matching_sentences_list)

    return matching_sentences_list


def get_nouns_list(sentence):
    pos_tag_list = nltk.pos_tag(sentence)
    noun_list = []
    # print(pos_tag_list)
    for data in pos_tag_list:
        if data[1] == 'NN' or data[1] == 'NNS':
            noun_list.append(data[0])
    # print(noun_list)
    return noun_list


def find_one_to_one():
    for dic in relationship_dic_list:
        # print(dic)

        member1 = dic.get('member1')
        member2 = dic.get('member2')
        print(member1, member2)

        singular_member1 = singularize(member1)
        singular_member2 = singularize(member2)
        # print(singular_member1, singular_member2)

        sentence_list = get_sentences_match_with_entities(member1, member2)
        print(sentence_list)

        relationship = dic.get('relationship')
        print(relationship)
        new_relationship_list = relationship.split('_')

        # pos_tag_relationship = nltk.pos_tag(new_relationship_list)
        # print(pos_tag_relationship)

        if len(new_relationship_list) > 1:
            correct_relationship =  new_relationship_list[1]

        else:
            correct_relationship = new_relationship_list[0]

        print(correct_relationship)
        print(conjugate('purred', '3sg'))
        # if singular_member1 == member1 and singular_member2 == member2:
        #     print(dic)



find_one_to_one()
