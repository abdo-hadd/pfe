import os
import io
import spacy
from spacy.matcher import Matcher
from . import toolkat


class get_info(object):

    def __init__( self, resume, skills_file=None, custom_regex=None ):
        nlp = spacy.load('en_core_web_sm')
        self.__skills_file = skills_file
        self.__custom_regex = custom_regex
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
        }

        self.__resume = resume
        if not isinstance(self.__resume, io.BytesIO):
            ext = os.path.splitext(self.__resume)[1].split('.')[1]
        else:
            ext = self.__resume.name.split('.')[1]
        self.__text_raw = toolkat.lire_file(self.__resume)
        self.__text = ' '.join(self.__text_raw.split())
        self.__nlp = nlp(self.__text)
        self.__noun_chunks = list(self.__nlp.noun_chunks)
        self.__get_basic_details()

    def get_extracted_data(self):
        return self.__details

    def __get_basic_details(self):
        name = toolkat.extract_name(self.__nlp, matcher=self.__matcher)
        email = toolkat.extract_email(self.__text)
        Adress = toolkat.extract_Adress(self.__nlp,self.__noun_chunks,self.__text)
        mobile = toolkat.extract_mobile_number(self.__text, self.__custom_regex)
        Age = toolkat.extract_Age(self.__text)
        skills,Stats,Domain_un,Domain_deux,Domain_trois,Domain_quatre,un,deux,trois,quatre = toolkat.extract_skills(
                    self.__nlp,
                    self.__noun_chunks,
                    self.__skills_file
                )
        Domain = []
        Domain.append(Domain_un)
        Domain.append(Domain_deux)
        Domain.append(Domain_trois)
        Domain.append(Domain_quatre)
        quef_domain=[]
        quef_domain.append(un)
        quef_domain.append(deux)
        quef_domain.append(trois)
        quef_domain.append(quatre)
        if name == None:
            self.__details['name'] = "unknown"
        else:
            self.__details['name'] = name
        if email == None:
            self.__details['email'] = "unknown"
        else:
            self.__details['email'] = email
        if mobile == None:
            self.__details['mobile_number'] = "unknown"
        else:
            self.__details['mobile_number'] = mobile
        if Age == None:
            self.__details['Age'] = "unknown"
        else:
            self.__details['Age'] = Age
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
        if Adress == None:
            self.__details['Adress'] = "unknown"
        else:
            self.__details['Adress'] = Adress
        return


