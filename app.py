import xml.etree.ElementTree as ET
import xmltodict
import nltk
from nltk.tokenize import sent_tokenize

text_file = open("input_text.txt", "r")

if text_file.mode == 'r':
    input_text = text_file.read()
    print(input_text)


def xml_input_handling():
    tree = ET.parse("input_xml.xml")
    root = tree.getroot()
    return root


def entity_combined_with_scenario():
    root = xml_input_handling()
    for entity in root.findall('entity'):
        find_entities(entity)


def find_entities(entity):
    entity = entity
    sentences = text_into_sentence()
    for sentence in sentences:
        for word in sentence:
            if word == entity:
                print(sentence)


def text_into_sentence():
    return sent_tokenize(input_text)
