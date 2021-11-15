import os
import io
import spacy
from spacy.matcher import Matcher
from . import toolkat_spaCy

class get_info_spaCy(object):
    def __init__( self, resume ):
        nlp = spacy.load('en_core_web_sm')
        self.__matcher = Matcher(nlp.vocab)
        self.__details = {
            'name': None,
            'email': None,
            'mobile_number': None,
            'Age': None,
            'skills': None,
            'domain1': None,
            'domain2': None,
            'domain3': None,
            'quef_d': None,
            'Adress': None,
            'Projet': None,
            'Langue': None,
        }

        self.__resume = resume
        if not isinstance(self.__resume, io.BytesIO):
            ext = os.path.splitext(self.__resume)[1].split('.')[1]
        else:
            ext = self.__resume.name.split('.')[1]
        self.__text_raw = toolkat_spaCy.lire_file(self.__resume)
        self.__text = ' '.join(self.__text_raw.split())
        self.__get_basic_details()

    def get_extracted_data(self):
        return self.__details

    def __get_basic_details(self):

        name,Adress,email,Age,skills,projet,mobile,Langue = toolkat_spaCy.extract_Information(self.__text)
        Domain_un,Domain_deux,Domain_trois,un,deux,trois = toolkat_spaCy.get_domain(skills)
        quef_domain=[]
        quef_domain.append(un)
        quef_domain.append(deux)
        quef_domain.append(trois)
        if name[0] == None:
            self.__details['name'] = "unknown"
        else:
            self.__details['name'] = name[0]
        if email[0] == None:
            self.__details['email'] = "unknown"
        else:
            self.__details['email'] = email[0]
        if mobile[0] == None:
            self.__details['mobile_number'] = "unknown"
        else:
            self.__details['mobile_number'] = mobile[0]
        if Age[0] == None:
            self.__details['Age'] = "unknown"
        else:
            self.__details['Age'] = Age[0]
        if skills == None:
            self.__details['skills'] = "unknown"
        else:
            self.__details['skills'] = skills
        if Domain_un == None:
            self.__details['domain1'] = "unknown"
        else:
            self.__details['domain1'] = Domain_un
        if Domain_deux == None:
            self.__details['domain2'] = "unknown"
        else:
            self.__details['domain2'] = Domain_deux
        if Domain_trois == None:
            self.__details['domain3'] = "unknown"
        else:
            self.__details['domain3'] = Domain_trois
        if quef_domain == None:
            self.__details['quef_d'] = "unknown"
        else:
            self.__details['quef_d'] = quef_domain
        if Adress[0] == None:
            self.__details['Adress'] = "unknown"
        else:
            self.__details['Adress'] = Adress[0]
        Pro = ""
        for a in projet:
            a = str(a)
            Pro += a + " , "
        if Pro == None:
            self.__details['Projet'] = "unknown"
        else:
            self.__details['Projet'] = Pro
        Lan = ""
        for a in Langue:
            a = str(a)
            Lan += a + " , "
        if Lan == None:
            self.__details['Langue'] = "unknown"
        else:
            self.__details['Langue'] = Lan
        return