import os
from os.path import isfile, join
from googletrans import Translator
from tika import parser
import pandas as pd
import spacy
from PFE import function as fun


def lire_file(file):
  raw = parser.from_file(file)
  text = raw['content']
  t = str(text)
  try:
      trans = Translator()
      t = trans.translate(text, dest='fr', src='en')
      t = str(t)
      t = t.split(', text=')[1]
      t = t.split(', pronunciation=')[0]
  except:
      return t
  return t

def extract_Information(test_text):
    Nom = []
    Adresse = []
    email = []
    Age = []
    skills = []
    projet = []
    Numéro = []
    Langue = []
    nlp2 = spacy.load(os.path.join(os.path.dirname(__file__),'./hna'))
    ner = nlp2.get_pipe("ner")
    move_names = list(ner.move_names)
    assert nlp2.get_pipe("ner").move_names == move_names
    doc2 = nlp2(test_text)
    for ent in doc2.ents:
        if ent.label_ == "Nom":
            Nom.append(ent.text)
        if ent.label_ == "Adresse":
            Adresse.append(ent.text)
        if ent.label_ == "Email":
            email.append(ent.text)
        if ent.label_ == "Age":
            Age.append(ent.text)
        if ent.label_ == "Skills":
            skills.append(ent.text)
        if ent.label_ == "Projet":
            projet.append(ent.text)
        if ent.label_ == "Numéro":
            Numéro.append(ent.text)
        if ent.label_ == "Langue":
            Langue.append(ent.text)
    if len(Nom) == 0:
        Nom.append("None")
    if len(Adresse) == 0:
        Adresse.append("None")
    if len(email) == 0:
        email.append("None")
    if len(Age) == 0:
        Age.append("None")
    if len(skills) == 0:
        skills.append("None")
    if len(projet) == 0:
        projet.append("None")
    if len(Numéro) == 0:
        Numéro.append("None")
    if len(Langue) == 0:
        Langue.append("None")
        
    return Nom,Adresse,email,Age,skills,projet,Numéro,Langue

def get_domain(lista):
    Stats = []
    mypath = os.path.join(os.path.dirname(__file__),'./skills')
    onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    for fileName in onlyfiles:
        count = 0
        data = pd.read_csv(fileName)
        skills = list(data.columns.values)
        for a in lista:
            a = str(a)
            a = a.lower()
            if a in skills:
                count += 1
        Stats.append(count)

    i = 0
    for ss in Stats:
        if ss == max(Stats):
            index = i
        i += 1
    temp1 = Stats[index]
    Stats[index] = 0
    i = 0
    for ss in Stats:
        if ss == max(Stats):
            index_deux = i
        i += 1
    temp2 = Stats[index_deux]
    Stats[index_deux] = 0
    i = 0
    for ss in Stats:
        if ss == max(Stats):
            index_trois = i
        i += 1
    i = 0
    temp3 = Stats[index_trois]
    Stats[index] = temp1
    Stats[index_deux] = temp2

    return fun.NAME_CLASTRE_SKILLS[index],fun.NAME_CLASTRE_SKILLS[index_deux],fun.NAME_CLASTRE_SKILLS[index_trois],temp1,temp2,temp3