import entity_from_huristics
import entity_from_tfidf


def find_entity():
    new_entity_list = []
    for entity in entity_from_huristics.entity_from_noun_list:
        for en in entity_from_tfidf.entity_tf_idf_model:
            if entity == en:
                new_entity_list.append(entity)
    print(new_entity_list)



find_entity()



