import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from PFE import function as fun
from PFE_spaCy import get_info_spaCy
from rdopdf import pdf_ex as pdfe
import datetime

def Choix_Cluster_Model_Spacy(path,K_cluster):
    mypath = path
    onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    for fileName in onlyfiles:
        if fileName.endswith(".pdf") or fileName.endswith(".docx") or fileName.endswith(".doc"):
            data = get_info_spaCy(fileName).get_extracted_data()
            if data['skills'] != []:
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
                    fun.SEXE_Intres.append(fun.gender(data['name'], data['name']))
                    fun.EMAIL_Intres.append(data['email'])
                    fun.Adress_inter.append(data['Adress'])
                    bzaf_maharat = ""
                    for maharat in data['skills']:
                        maharat = str(maharat)
                        bzaf_maharat = maharat + "," + bzaf_maharat
                    fun.SKILLS_Intres.append(bzaf_maharat)
                    bzaf_maharat = ""
                    for maharat in data['skills']:
                        bzaf_maharat = maharat + "," + bzaf_maharat
                    lista_skills = [bzaf_maharat]
                    Domain, prec = fun.get_domain(lista_skills)
                    prec = prec * 100
                    prec = str(prec)
                    prec = prec[:-12]
                    prec = prec + "%"
                    if prec == None:
                        fun.similarite_domain.append("unknown")
                    else:
                        fun.similarite_domain.append(prec)
                    domain_en_ligne = "" + str(Domain)
                    if Domain == None:
                        fun.DOMAIN1_Intres.append("unknown")
                    else:
                        fun.DOMAIN1_Intres.append(Domain)
                    fun.projet_inter.append(data['Projet'])
                    fun.langue_inter.append(data['Langue'])
                    if fileName.endswith(".pdf"):
                        fun.cnt_int_pdf += 1
                    if fileName.endswith(".docx"):
                        fun.cnt_int_docx += 1
                    if fileName.endswith(".doc"):
                        fun.cnt_int_doc += 1

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
    NombreCvInt = fun.cnt_int_pdf + fun.cnt_int_docx + fun.cnt_int_doc
    NombreTotalCV = NombreCvNonLue  + NombreCvInt

    # hna fin njbde cluster

    fun.cluster, fun.similarite_cluster = fun.get_cluster(fun.SKILLS_Intres, K_cluster=K_cluster)

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
        'Projet': fun.projet_inter,
        'Langue': fun.langue_inter,
        'DOMAIN1': fun.DOMAIN1_Intres,
        'Sim_Dom': fun.similarite_domain,
        'Cluster': fun.cluster,
        'Sim_Clu': fun.similarite_cluster, })


    df_Intres.to_csv('./Choix_Cluster_Model_Spacy/Cluster.csv', index=False)

    return fun.cnt_int_pdf,fun.cnt_int_docx,fun.cnt_int_doc,fun.cnt_non_lue_pdf,fun.cnt_non_lue_docx,fun.cnt_non_lue_doc


