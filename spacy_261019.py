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
doc  = pd.read_csv("/Users/Fabi/PycharmProjects/Zeit2.csv", error_bad_lines=False, encoding= "ISO-8859-1") # utf-8
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
# print(type(df))
# print(type(df1))
# df = nlp(doc)
print("Wir sind hier 0")
# print(df)
# for token in df:
#   print(token.text, "...", token.tag_, "-", token.pos_, "--", token.dep_)
def get_entities(sent):

  ent1 = ""
  ent2 = ""
  ent3 = ""
  # ent4 = ""

  #############################################################

  for tok in nlp(sent):

    if tok.dep_ != "punct":
      if tok.dep_.startswith("s") == False:
        ent1 = tok.text

      if tok.dep_.startswith("o") == False:
        ent2 = tok.text

      if tok.dep_.find("oa") == False:
        ent3 = tok.text

      # if tok.dep_.find("ROOT") == False:
      #   ent4 = tok.text


  #############################################################

  return [ent1.strip(), ent2.strip(), ent3.strip()] # ent4.strip()

entity_pairs = []

for i in tqdm(doc["Sentence"]):
  entity_pairs.append(get_entities(i))

print(entity_pairs[10:20])

print(entity_pairs)

print("********************")

source = [i[0] for i in entity_pairs]

target = [i[1] for i in entity_pairs]

edge_attr = [i[2] for i in entity_pairs]

# root = [i[3] for i in entity_pairs]


kg_df = pd.DataFrame({'source':source, 'target':target, 'edge_attr':edge_attr}) # 'root':root
print("    **************   ")
print(kg_df)
G = nx.from_pandas_edgelist(kg_df, "source", "target", "edge_attr") #[kg_df['edge']=="composed by"] ////      edge_attr=True
print(type(G))
print("Hier: +++++++++++")
print(G)

plt.figure(figsize=(6,6))
pos = nx.spring_layout(G, k = 0.5) # k regulates the distance between nodes
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, pos = pos) # edge_cmap=plt.cm.Blues, pos = pos
plt.show()
