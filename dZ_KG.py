import spacy
import re
import pandas as pd
import bs4
import requests
import spacy
from spacy import displacy
from spacy.matcher import Matcher
from spacy.tokens import Span
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
from spacy.lang.de.examples import sentences
import csv
import time

nlp = spacy.load('de_core_news_sm')
# nlp = spacy.load('de')

doc = nlp("Der Hund springt in ein Gebüsch.")
# dz_saetze = pd.read_csv("/Users/Fabi/PycharmProjects/Zeit1.csv",error_bad_lines=False, encoding='utf-8')

for token in doc:
  print(token.text, "...", token.tag_, "-", token.pos_, "--", token.dep_)

# df = open("/Users/Fabi/PycharmProjects/Zeit1.txt", encoding='utf-8').read()
df = pd.read_csv("/Users/Fabi/PycharmProjects/Zeit2.csv", error_bad_lines=False, encoding= "utf-8")
# for id, line in df:
#     doc = nlp(line)
# unicode_strings = [s.decode('utf8') for s in byte_strings]
# df = df.applymap(str)
# df['column'] = df['column'].astype('str')
# df['column'] = df['column'].astype('unicode')
# print(df['Hannover 96 verliert Absteigerduell gegen FC Nuernberg.'])
# print(df)
# for parsed_doc in nlp.pipe(iter(df['Hannover 96 verliert Absteigerduell gegen FC Nuernberg.']), batch_size=1, n_threads=4):
#   print (parsed_doc[0].text, parsed_doc[0].dep_)
# print(Zeit)
# df1 = open("/Users/Fabi/PycharmProjects/Zeit1.txt", encoding="latin-1").read()
print(type(df))
# print(type(df1))
df = nlp(doc)
print("Wir sind hier 0")
# print(df)
# for token in df:
#   print(token.text, "...", token.tag_, "-", token.pos_, "--", token.dep_)
def get_entities(sent):
  ## chunk 1
  ent1 = ""
  ent2 = ""

  prv_tok_dep = ""  # dependency tag of previous token in the sentence
  prv_tok_text = ""  # previous token in the sentence

  prefix = ""
  modifier = ""

  #############################################################

  for tok in nlp(sent):
    ## chunk 2
    # if token is a punctuation mark then move on to the next token
    if tok.dep_ != "punct":
      # check: token is a compound word or not
      if tok.dep_ == "nk":
        prefix = tok.text
        # if the previous word was also a 'compound' then add the current word to it
        if prv_tok_dep == "nk":
          prefix = prv_tok_text + " " + tok.text

      # check: token is a modifier or not
      if tok.dep_.endswith("b") == True:
        modifier = tok.text
        # if the previous word was also a 'compound' then add the current word to it
        if prv_tok_dep == "nk":
          modifier = prv_tok_text + " " + tok.text

      ## chunk 3
      if tok.dep_.find("sb") == True:
        ent1 = modifier + " " + prefix + " " + tok.text
        prefix = ""
        modifier = ""
        prv_tok_dep = ""
        prv_tok_text = ""

        ## chunk 4
      if tok.dep_.find("oa") == True:
        ent2 = modifier + " " + prefix + " " + tok.text

      ## chunk 5
      # update variables
      prv_tok_dep = tok.dep_
      prv_tok_text = tok.text
  #############################################################

  return [ent1.strip(), ent2.strip()]

entity_pairs = []

for i in tqdm(df["Hannover 96 verliert Absteigerduell gegen FC Nuernberg."]):
  entity_pairs.append(get_entities(i))

print(entity_pairs[10:20])
print("Wir sind hier 1")
# print(Zeit) # shape gibt die Anzahl der Zeilen wieder
#
# for token in Zeit:
#   print(token.text, "...", token.tag_, "-", token.pos_, "--", token.dep_)
#
# print("Wir sind hier 2")
#
# def get_entities(sent):
#   pass
#
# print("Funktion wurde gepassed.")
#
# # for token in doc:
# #   print(token.text, "...", token.lemma_, "...", token.pos_,"...", token.tag_, token.dep_)
#
# # pd.set_option('display.max_colwidth', 200)
# # # 'exec(%matplotlib inline)'
# #
# # dz_saetze = pd.read_csv("/Users/Fabi/PycharmProjects/Zeit1.csv",error_bad_lines=False, encoding='utf-8')
# #
# # # dz_saetze.shape
# # print(dz_saetze.shape)
# #
# # # dz_saetze['Hannover 96 verliert Absteigerduell gegen FC Nurnberg'].sample(5)
# # print(dz_saetze['Hannover 96 verliert Absteigerduell gegen FC Nuernberg'].sample(5))
#
#
# #
# # entity_pairs = []
# # print(entity_pairs[10:20])
# #
# # for i in tqdm(dz_saetze["Hannover 96 verliert Absteigerduell gegen FC Nuernberg"]):
# #   entity_pairs.append(get_entities(i))
# #
# # print(entity_pairs[10:20])
# #
# #
#
