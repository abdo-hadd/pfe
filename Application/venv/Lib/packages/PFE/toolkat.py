import os
import re
import pandas as pd
from . import function as fun
from googletrans import Translator
from tika import parser
import phonenumbers
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def lire_file(file):
  raw = parser.from_file(file)
  text = raw['content']
  t = str(text)
  try:
      trans = Translator()
      t = trans.translate(text, dest='en', src='fr')
      t = str(t)
      t = t.split(', text=')[1]
      t = t.split(', pronunciation=')[0]
  except:
      return t
  return t

def extract_email(text):
    email = re.findall(r'([^@|\s]+@[^@]+\.[^@|\s]+)', text)
    if email:
        try:
            return email[0].split()[0].strip(';')
        except IndexError:
            return None



def extract_name(nlp_text, matcher):
    pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}]]
    matcher.add('NAME', None, *pattern)
    matches = matcher(nlp_text)
    for _, start, end in matches:
        span = nlp_text[start:end]
        if 'name' not in span.text.lower():
            return span.text


def extract_mobile_number(text, custom_regex=None):
    text = str(text)
    text = text.replace("\\n"," ")
    text = text.replace("-","")
    number =[]
    i=0
    for match in phonenumbers.PhoneNumberMatcher(text,'MA'):
        i=i+1
        number.append(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))
    return number

from datetime import date
def extract_Age(text):
  Y = date.today()
  Y = str(Y)
  Y = Y.split('-')
  Y = int(Y[0])
  tech1 = []
  tech2 = []
  tech3 = []
  tech4 = []
  tech5 = []
  pattern = re.compile(r'Age[\:\s](\d{1,3})')
  matches = pattern.finditer(text)
  for match in matches:
    tech1.append(match)
    if tech1 != None :
      tech1 = str(tech1)
      tech1 = tech1.split('Age ')
      tech1 = tech1[1]
      tech1 = str(tech1)
      tech1 = tech1.split('\'')
      tech1 = tech1[0]
      return tech1
  pattern = re.compile(r'\d{1,2} [AaYy][nge][sea]')
  matches = pattern.finditer(text)
  for match in matches:
    tech2.append(match)
    if tech2 != None :
      tech2 = str(tech2)
      tech2 = tech2.split('=\'')
      tech2 = tech2[1]
      tech2 = str(tech2)
      tech2 = tech2.split(' ')
      tech2 = tech2[0]
      return tech2
  pattern = re.compile(r'([2-9]|1[0-2]?)-[0-3][1-9]-[1-2][9|0][0-9]{2}[^0-9]*$')
  matches = pattern.finditer(text)
  for match in matches:
    tech3.append(match)
    if tech3 != None :
      tech3 = str(tech3)
      tech3 = tech3.split('=\'')
      tech3 = tech3[1]
      tech3 = str(tech3)
      tech3 = tech3.split('-')
      tech3 = tech3[2]
      tech3 = tech3.split(' ')
      tech3 = tech3[0]
      tech3 = int(tech3)
      return Y-tech3
  pattern = re.compile(r'([2-9]|1[0-2]?)/[0-3][1-9]/[0-1][9|0][0-9]{2}')
  matches = pattern.finditer(text)
  for match in matches:
    tech4.append(match)
    if tech4 != None :
      tech4 = str(tech4)
      tech4 = tech4.split('=\'')
      tech4 = tech4[1]
      tech4 = str(tech4)
      tech4 = tech4.split('/')
      tech4 = tech4[2]
      tech4 = tech4.split('\'')
      tech4 = int(tech4[0])
      return Y-tech4
  pattern = re.compile(r'[0-1][9|0][0-9]{2}/[0-3][1-9]/([2-9]|1[0-2]?)')
  matches = pattern.finditer(text)
  for match in matches:
    tech5.append(match)
    if tech5 != None :
      tech5 = str(tech5)
      tech5 = tech5.split('=\'')
      tech5 = tech5[1]
      tech5 = str(tech5)
      tech5 = tech5.split('\\')
      tech5 = int(tech5[0])
      return Y-tech5
  return None

def extract_Adress(nlp_text,noun_chunks,text):
    Adresse = ""
    lis_ad = []
    V = []
    #hada l vérifiecation bache nhze mdina w7da
    i=0
    # hna kmala
    tokens = [token.text for token in nlp_text if not token.is_stop]
    for token in tokens:
        token = token.lower()
        if token in fun.ville:
            V.append(token)
            i += 1
    tech1 = []
    pattern = re.compile(r'Address[ :] \d{1,7}( \w+){1,6}( \w+){1,6}[\., ]+.........')
    matches = pattern.finditer(text)
    for match in matches:
        tech1.append(match)
        tech1 = str(tech1)
        tech1 = tech1.split('Address')
        tech1 = tech1[1]
        tech1 = str(tech1)
        tech1 = tech1.split('\'')
        tech1 = tech1[0]
        tech1 = tech1[:-1]
        tech1 = tech1[1:]

    if i == 0:
        return tech1
    elif i >= 1 :
        lis_ad.append(V[0])
        lis_ad.append(tech1)
        for a in lis_ad:
            a = str(a)
            if not a == "[]":
             Adresse += a
        if Adresse == "[]":
            return "not found"
        return Adresse
    else:
        return "not found"


def extract_skills(nlp_text, noun_chunks, skills_file=None):
    tokens = [token.text for token in nlp_text if not token.is_stop]
    skillset = []
    Stats = []

    mypath = os.path.join(os.path.dirname(__file__),'./skills')
    onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    for fileName in onlyfiles:
        count = 0
        data = pd.read_csv(fileName)
        skills = list(data.columns.values)
        # check for one-grams
        for token in tokens:
            token = token.lower()
            if token in skills:
                skillset.append(token)
                count += 1
        # check for bi-grams and tri-grams
        for token in noun_chunks:
            token = token.text.lower().strip()
            if token in skills:
                skillset.append(token)
                count += 1
        Stats.append(count)
    i=0
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
    Stats[index_trois] = 0
    for ss in Stats:
        if ss == max(Stats):
            index_quatre = i
        i += 1
    temp4 = Stats[index_quatre]
    Stats[index] = temp1
    Stats[index_deux] = temp2
    Stats[index_trois] = temp3

    return [i.capitalize() for i in set([i.lower() for i in skillset])],Stats,fun.NAME_CLASTRE_SKILLS[index],fun.NAME_CLASTRE_SKILLS[index_deux],fun.NAME_CLASTRE_SKILLS[index_trois],fun.NAME_CLASTRE_SKILLS[index_quatre],temp1,temp2,temp3,temp4










