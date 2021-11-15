import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from PFE import function as fun
from PFE_spaCy import get_info_spaCy
from rdopdf import pdf_ex as pdfe
import datetime

def Choix_skills_Model_Spacy(path,cherche):
    mypath = path
    onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    for fileName in onlyfiles:
        if fileName.endswith(".pdf") or fileName.endswith(".docx") or fileName.endswith(".doc"):
            data = get_info_spaCy(fileName).get_extracted_data()
            if data['skills'] != []:
                if fun.Skills_in_list(fun.synonyms_mot_cle(cherche), data['skills']) != 0:
                    fun.NAME_Intres.append(data['name'])
                    Num_phone = ""
                    for aa in data['mobile_number']:
                        aa = str(aa)
                        Num_phone += aa + " "
                    fun.MOBILE_Intres.append(Num_phone)
                    if data['Age'] == None:
                        fun.AGE_Intres.append(22)
                    else:
                        fun.AGE_Intres.append(data['Age'])
                    fun.SEXE_Intres.append(fun.gender(data['name'],data['name']))
                    fun.EMAIL_Intres.append(data['email'])
                    fun.Adress_inter.append(data['Adress'])
                    bzaf_maharat = ""
                    for maharat in data['skills']:
                        maharat = str(maharat)
                        bzaf_maharat = maharat + " , " + bzaf_maharat
                    fun.SKILLS_Intres.append(bzaf_maharat)
                    fun.Eta.append("Acc")
                    domain_en_ligne = "" + data['domain1'] + "/" + data['domain2'] + "/" + data['domain3']
                    fun.DOMAIN1_Intres.append(data['domain1'])
                    fun.DOMAIN2_Intres.append(data['domain2'])
                    fun.DOMAIN3_Intres.append(data['domain3'])
                    fun.domain_Intres_pdf.append(data['domain1'])
                    fun.domain_Intres_pdf.append(data['domain2'])
                    fun.domain_Intres_pdf.append(data['domain3'])
                    fun.projet_inter.append(data['Projet'])
                    fun.langue_inter.append(data['Langue'])
                    if fileName.endswith(".pdf"):
                        fun.cnt_int_pdf += 1
                    if fileName.endswith(".docx"):
                        fun.cnt_int_docx += 1
                    if fileName.endswith(".doc"):
                        fun.cnt_int_doc += 1
                else:
                    fun.NAME_Non_Intres.append(data['name'])
                    Num_phone = ""
                    for aa in data['mobile_number']:
                        aa = str(aa)
                        Num_phone += aa + " "
                    fun.MOBILE_Non_Intres.append(Num_phone)
                    if data['Age'] == None:
                        fun.AGE_Non_Intres.append(22)
                    else:
                        fun.AGE_Non_Intres.append(data['Age'])
                    fun.SEXE_Non_Intres.append(fun.gender(data['name'], data['name']))
                    fun.EMAIL_Non_Intres.append(data['email'])
                    fun.Adress_Non_inter.append(data['Adress'])
                    bzaf_maharat = ''
                    for maharat in data['skills']:
                        maharat = str(maharat)
                        bzaf_maharat = maharat + ',' + bzaf_maharat
                    fun.SKILLS_Non_Intres.append(bzaf_maharat)
                    fun.Eta_Non_inters.append("Ref")
                    domain_en_ligne = "" + data['domain1'] + "/" + data['domain2'] + "/" + data['domain3']
                    fun.DOMAIN1_Non_Intres.append(data['domain1'])
                    fun.DOMAIN2_Non_Intres.append(data['domain2'])
                    fun.DOMAIN3_Non_Intres.append(data['domain3'])
                    fun.domain_Non_Intres_pdf.append(data['domain1'])
                    fun.domain_Non_Intres_pdf.append(data['domain2'])
                    fun.domain_Non_Intres_pdf.append(data['domain3'])
                    fun.projet_Non_inter.append(data['Projet'])
                    fun.langue_Non_inter.append(data['Langue'])
                    if fileName.endswith(".pdf"):
                        fun.cnt_non_int_pdf += 1
                    if fileName.endswith(".docx"):
                        fun.cnt_non_int_docx += 1
                    if fileName.endswith(".doc"):
                        fun.cnt_non_int_doc += 1
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
    NombreCvNonInt = fun.cnt_non_int_pdf + fun.cnt_non_int_docx + fun.cnt_non_int_doc
    NombreCvInt = fun.cnt_int_pdf + fun.cnt_int_docx + fun.cnt_int_doc
    NombreTotalCV = NombreCvNonLue + NombreCvNonInt + NombreCvInt

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

    df_Intres = pd.DataFrame({
        'NAME': fun.NAME_Intres,
        'MOBILE': fun.MOBILE_Intres,
        'AGE': fun.AGE_Intres,
        'SEXE': fun.SEXE_Intres,
        'EMAIL': fun.EMAIL_Intres,
        'ADRESS': fun.Adress_inter,
        'SKILLS': fun.SKILLS_Intres,
        'DOMAIN1': fun.DOMAIN1_Intres,
        'DOMAIN2': fun.DOMAIN2_Intres,
        'DOMAIN3': fun.DOMAIN3_Intres,
        'Etas': fun.Eta,
        'Projet': fun.projet_inter,
        'Langue': fun.langue_inter,})

    df_Non_Intres = pd.DataFrame({
        'NAME': fun.NAME_Non_Intres,
        'MOBILE': fun.MOBILE_Non_Intres,
        'AGE': fun.AGE_Non_Intres,
        'SEXE': fun.SEXE_Non_Intres,
        'EMAIL': fun.EMAIL_Non_Intres,
        'ADRESS': fun.Adress_Non_inter,
        'SKILLS': fun.SKILLS_Non_Intres,
        'DOMAIN1': fun.DOMAIN1_Non_Intres,
        'DOMAIN2': fun.DOMAIN2_Non_Intres,
        'DOMAIN3': fun.DOMAIN3_Non_Intres,
        'Etas': fun.Eta_Non_inters,
        'Projet': fun.projet_Non_inter,
        'Langue': fun.langue_Non_inter,})

    df_Intres.to_csv('./Choix_skills_Model_Spacy/Inters.csv', index=False)
    df_Non_Intres.to_csv('./Choix_skills_Model_Spacy/Non_Inters.csv', index=False)
    
    
    return fun.cnt_int_pdf,fun.cnt_int_docx,fun.cnt_int_doc,fun.cnt_non_int_pdf,fun.cnt_non_int_docx,fun.cnt_non_int_doc,fun.cnt_non_lue_pdf,fun.cnt_non_lue_docx,fun.cnt_non_lue_doc
