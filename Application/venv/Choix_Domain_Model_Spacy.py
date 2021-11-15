import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from PFE import function as fun
from PFE_spaCy import get_info_spaCy
from rdopdf import pdf_ex as pdfe
import datetime

def Choix_Domain_Model_Spacy(path,Domain1,Domain2,Domain3):
    mypath = path
    onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    for fileName in onlyfiles:
        if fileName.endswith(".pdf") or fileName.endswith(".docx") or fileName.endswith(".doc"):
            data = get_info_spaCy(fileName).get_extracted_data()
            if data['skills'] != []:
                if data['domain1'] == Domain1 and data['domain2'] == Domain2 and data['domain3'] == Domain3:
                    fun.NAME_1.append(data['name'])
                    Num_phone = ""
                    for aa in data['mobile_number']:
                        aa = str(aa)
                        Num_phone += aa + " "
                    fun.MOBILE_1.append(Num_phone)
                    if data['Age'] == None:
                        fun.AGE_1.append(22)
                    else:
                        fun.AGE_1.append(data['Age'])
                    fun.SEXE_1.append(fun.gender(data['name'],data['name']))
                    fun.EMAIL_1.append(data['email'])
                    fun.Adress_1.append(data['Adress'])
                    bzaf_maharat = ""
                    for maharat in data['skills']:
                        maharat = str(maharat)
                        bzaf_maharat = maharat + " , " + bzaf_maharat
                    fun.SKILLS_1.append(bzaf_maharat)
                    fun.Eta_1.append("BON")
                    domain_en_ligne = "" + data['domain1'] + "/" + data['domain2'] + "/" + data['domain3']
                    fun.DOMAIN1_1.append(data['domain1'])
                    fun.DOMAIN2_1.append(data['domain2'])
                    fun.DOMAIN3_1.append(data['domain3'])
                    fun.domain_1_pdf.append(data['domain1'])
                    fun.domain_1_pdf.append(data['domain2'])
                    fun.domain_1_pdf.append(data['domain3'])
                    fun.projet_1.append(data['Projet'])
                    fun.langue_1.append(data['Langue'])
                    if fileName.endswith(".pdf"):
                        fun.cnt_1_pdf += 1
                    if fileName.endswith(".docx"):
                        fun.cnt_1_docx += 1
                    if fileName.endswith(".doc"):
                        fun.cnt_1_doc += 1
                elif (data['domain1'] == Domain1 and data['domain2'] == Domain2) or (data['domain1'] == Domain1 and data['domain3'] == Domain3) or (data['domain2'] == Domain2 and data['domain3'] == Domain3) :
                    fun.NAME_2.append(data['name'])
                    Num_phone = ""
                    for aa in data['mobile_number']:
                        aa = str(aa)
                        Num_phone += aa + " "
                    fun.MOBILE_2.append(Num_phone)
                    if data['Age'] == None:
                        fun.AGE_2.append(22)
                    else:
                        fun.AGE_2.append(data['Age'])
                    fun.SEXE_2.append(fun.gender(data['name'], data['name']))
                    fun.EMAIL_2.append(data['email'])
                    fun.Adress_2.append(data['Adress'])
                    bzaf_maharat = ""
                    for maharat in data['skills']:
                        maharat = str(maharat)
                        bzaf_maharat = maharat + " , " + bzaf_maharat
                    fun.SKILLS_2.append(bzaf_maharat)
                    fun.Eta_2.append("MOYENNE")
                    domain_en_ligne = "" + data['domain1'] + "/" + data['domain2'] + "/" + data['domain3']
                    fun.DOMAIN1_2.append(data['domain1'])
                    fun.DOMAIN2_2.append(data['domain2'])
                    fun.DOMAIN3_2.append(data['domain3'])
                    fun.domain_2_pdf.append(data['domain1'])
                    fun.domain_2_pdf.append(data['domain2'])
                    fun.domain_2_pdf.append(data['domain3'])
                    fun.projet_2.append(data['Projet'])
                    fun.langue_2.append(data['Langue'])
                    if fileName.endswith(".pdf"):
                        fun.cnt_2_pdf += 1
                    if fileName.endswith(".docx"):
                        fun.cnt_2_docx += 1
                    if fileName.endswith(".doc"):
                        fun.cnt_2_doc += 1
                elif (data['domain1'] == Domain1) or (data['domain2'] == Domain2) or (data['domain3'] == Domain3) :
                    fun.NAME_3.append(data['name'])
                    Num_phone = ""
                    for aa in data['mobile_number']:
                        aa = str(aa)
                        Num_phone += aa + " "
                    fun.MOBILE_3.append(Num_phone)
                    if data['Age'] == None:
                        fun.AGE_3.append(22)
                    else:
                        fun.AGE_3.append(data['Age'])
                    fun.SEXE_3.append(fun.gender(data['name'], data['name']))
                    fun.EMAIL_3.append(data['email'])
                    fun.Adress_3.append(data['Adress'])
                    bzaf_maharat = ""
                    for maharat in data['skills']:
                        maharat = str(maharat)
                        bzaf_maharat = maharat + " , " + bzaf_maharat
                    fun.SKILLS_3.append(bzaf_maharat)
                    fun.Eta_3.append("FAIBLE")
                    domain_en_ligne = "" + data['domain1'] + "/" + data['domain2'] + "/" + data['domain3']
                    fun.DOMAIN1_3.append(data['domain1'])
                    fun.DOMAIN2_3.append(data['domain2'])
                    fun.DOMAIN3_3.append(data['domain3'])
                    fun.domain_3_pdf.append(data['domain1'])
                    fun.domain_3_pdf.append(data['domain2'])
                    fun.domain_3_pdf.append(data['domain3'])
                    fun.projet_3.append(data['Projet'])
                    fun.langue_3.append(data['Langue'])
                    if fileName.endswith(".pdf"):
                        fun.cnt_3_pdf += 1
                    if fileName.endswith(".docx"):
                        fun.cnt_3_docx += 1
                    if fileName.endswith(".doc"):
                        fun.cnt_3_doc += 1
                else:
                    fun.NAME_4.append(data['name'])
                    Num_phone = ""
                    for aa in data['mobile_number']:
                        aa = str(aa)
                        Num_phone += aa + " "
                    fun.MOBILE_4.append(Num_phone)
                    if data['Age'] == None:
                        fun.AGE_4.append(22)
                    else:
                        fun.AGE_4.append(data['Age'])
                    fun.SEXE_4.append(fun.gender(data['name'], data['name']))
                    fun.EMAIL_4.append(data['email'])
                    fun.Adress_4.append(data['Adress'])
                    bzaf_maharat = ""
                    for maharat in data['skills']:
                        maharat = str(maharat)
                        bzaf_maharat = maharat + " , " + bzaf_maharat
                    fun.SKILLS_4.append(bzaf_maharat)
                    fun.Eta_4.append("BON")
                    domain_en_ligne = "" + data['domain1'] + "/" + data['domain2'] + "/" + data['domain3']
                    fun.DOMAIN1_4.append(data['domain1'])
                    fun.DOMAIN2_4.append(data['domain2'])
                    fun.DOMAIN3_4.append(data['domain3'])
                    fun.domain_4_pdf.append(data['domain1'])
                    fun.domain_4_pdf.append(data['domain2'])
                    fun.domain_4_pdf.append(data['domain3'])
                    fun.projet_4.append(data['Projet'])
                    fun.langue_4.append(data['Langue'])
                    if fileName.endswith(".pdf"):
                        fun.cnt_4_pdf += 1
                    if fileName.endswith(".docx"):
                        fun.cnt_4_docx += 1
                    if fileName.endswith(".doc"):
                        fun.cnt_4_doc += 1
            else:
                if fileName.endswith(".pdf"):
                    fun.cnt_non_lue_pdf += 1
                if fileName.endswith(".docx"):
                    fun.cnt_non_lue_docx += 1
                if fileName.endswith(".doc"):
                    fun.cnt_non_lue_doc += 1
                fun.Non_lu.append(Full_name)

    # hna kanbda n7ssbe 3adad cv li tl3o f ay mra

    NombreCvNonLue = fun.cnt_non_lue_pdf + fun.cnt_non_lue_docx + fun.cnt_non_lue_doc
    NombreCvD1 = fun.cnt_1_pdf + fun.cnt_1_docx + fun.cnt_1_doc
    NombreCvD2 = fun.cnt_2_pdf + fun.cnt_2_docx + fun.cnt_2_doc
    NombreCvD3 = fun.cnt_3_pdf + fun.cnt_3_docx + fun.cnt_3_doc
    NombreCvD7 = fun.cnt_4_pdf + fun.cnt_4_docx + fun.cnt_4_doc
    NombreCvLue = NombreCvD1 + NombreCvD2 + NombreCvD3 + NombreCvD7
    NombreTotalCV = NombreCvNonLue + NombreCvLue

    # hna bache ndire histrique nta3 taritement cv
    Date = []
    Nb_CV = []
    try:
        aha = pd.read_csv('hist.csv')
        for a in aha['DATE']:
            Date.append(a)
        for a in aha['NBCV']:
            Nb_CV.append(a)
    except:
        pass
    a = datetime.datetime.now().strftime('%m/%d %H:%M')
    Date.append(a)
    Nb_CV.append(NombreTotalCV)

    df_hist = pd.DataFrame({
        'DATE': Date,
        'NBCV': Nb_CV})

    df_hist.to_csv('./hist.csv', index=False)

    # hna dok fichier li mat9rawche
    print("hadok li mat9rawche hhh :", fun.Non_lu)

    # hna safi nrdhom datafram bache lo7hom lficheir csv

    df_Domain1 = pd.DataFrame({
        'NAME': fun.NAME_1,
        'MOBILE': fun.MOBILE_1,
        'AGE': fun.AGE_1,
        'SEXE': fun.SEXE_1,
        'EMAIL': fun.EMAIL_1,
        'ADRESS': fun.Adress_1,
        'SKILLS': fun.SKILLS_1,
        'DOMAIN1': fun.DOMAIN1_1,
        'DOMAIN2': fun.DOMAIN2_1,
        'DOMAIN3': fun.DOMAIN3_1,
        'Etas': fun.Eta_1,
        'Projet': fun.projet_1,
        'Langue': fun.langue_1,})

    df_Domain2 = pd.DataFrame({
        'NAME': fun.NAME_2,
        'MOBILE': fun.MOBILE_2,
        'AGE': fun.AGE_2,
        'SEXE': fun.SEXE_2,
        'EMAIL': fun.EMAIL_2,
        'ADRESS': fun.Adress_2,
        'SKILLS': fun.SKILLS_2,
        'DOMAIN1': fun.DOMAIN1_2,
        'DOMAIN2': fun.DOMAIN2_2,
        'DOMAIN3': fun.DOMAIN3_2,
        'Etas': fun.Eta_2,
        'Projet': fun.projet_2,
        'Langue': fun.langue_2,})

    df_Domain3 = pd.DataFrame({
        'NAME': fun.NAME_3,
        'MOBILE': fun.MOBILE_3,
        'AGE': fun.AGE_3,
        'SEXE': fun.SEXE_3,
        'EMAIL': fun.EMAIL_3,
        'ADRESS': fun.Adress_3,
        'SKILLS': fun.SKILLS_3,
        'DOMAIN1': fun.DOMAIN1_3,
        'DOMAIN2': fun.DOMAIN2_3,
        'DOMAIN3': fun.DOMAIN3_3,
        'Etas': fun.Eta_3,
        'Projet': fun.projet_3,
        'Langue': fun.langue_3,})

    df_Domain4 = pd.DataFrame({
        'NAME': fun.NAME_4,
        'MOBILE': fun.MOBILE_4,
        'AGE': fun.AGE_4,
        'SEXE': fun.SEXE_4,
        'EMAIL': fun.EMAIL_4,
        'ADRESS': fun.Adress_4,
        'SKILLS': fun.SKILLS_4,
        'DOMAIN1': fun.DOMAIN1_4,
        'DOMAIN2': fun.DOMAIN2_4,
        'DOMAIN3': fun.DOMAIN3_4,
        'Etas': fun.Eta_4,
        'Projet': fun.projet_4,
        'Langue': fun.langue_4,})

    df_Domain1.to_csv('./Choix_Domain_Model_Spacy/Domain1.csv', index=False)
    df_Domain2.to_csv('./Choix_Domain_Model_Spacy/Domain2.csv', index=False)
    df_Domain3.to_csv('./Choix_Domain_Model_Spacy/Domain3.csv', index=False)
    df_Domain4.to_csv('./Choix_Domain_Model_Spacy/Domain4.csv', index=False)


    return fun.cnt_1_pdf,fun.cnt_1_docx,fun.cnt_1_doc,fun.cnt_2_pdf,fun.cnt_2_docx,fun.cnt_2_doc,fun.cnt_3_pdf,fun.cnt_3_docx,fun.cnt_3_doc,fun.cnt_4_pdf,fun.cnt_4_docx,fun.cnt_4_doc



