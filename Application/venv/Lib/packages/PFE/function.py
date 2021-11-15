import os
from sklearn.feature_extraction.text import CountVectorizer     # hadi bache ndrdo dak fichier li fih nom drari o bnat l liste
import pandas as pd
import nltk
from nltk.corpus import wordnet  # hadi bache njbdo sysnony bnsba les mots li ktbe f recherche
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import random

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def get_gender(prenom,nom):
  url = '{0}{1}{2}{3}'.format('https://api.namsor.com/onomastics/api/json/gender/',prenom,'/',nom)
  r = requests.get(url,verify=False)
  return r.json()['gender']

def gender(prenom,nom):
  url = '{0}{1}{2}{3}'.format('https://v2.namsor.com/NamSorAPIv2/api2/json/gender/',prenom,'/',nom)
  headers = {'content-type': 'application/json', 'X-API-KEY': 'bde2470a4d296a4fcd4633a9da0a81da'}
  r = requests.get(url, headers=headers)
  return r.json()['likelyGender']


cnt_int_pdf = 0
cnt_int_docx = 0
cnt_int_doc = 0
cnt_non_int_pdf = 0
cnt_non_int_docx = 0
cnt_non_int_doc = 0
cnt_non_lue_pdf = 0
cnt_non_lue_docx = 0
cnt_non_lue_doc = 0

'''Nom_clastre =[]
mypath = 'C:\\Users\\tatim\\Desktop\\Skills'
onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
for aha in onlyfiles:
    aha = str(aha).split('\\')
    aha = aha[5]
    aha = str(aha)
    aha = aha[:-4]
    Nom_clastre.append(aha)

NAME_CLASTRE = Nom_clastre'''


Nom_clastre_skills =[]
mypath = os.path.join(os.path.dirname(__file__),'.\\skills')
onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
for aha in onlyfiles:
    aha = str(aha).split('\\')
    aha = aha[11]
    aha = str(aha)
    aha = aha[:-4]
    Nom_clastre_skills.append(aha)

NAME_CLASTRE_SKILLS = Nom_clastre_skills

# hna l choix par skills
NAME_Intres =[]
MOBILE_Intres =[]
AGE_Intres =[]
SEXE_Intres = []
EMAIL_Intres =[]
SKILLS_Intres =[]
DOMAIN1_Intres =[]
DOMAIN2_Intres =[]
DOMAIN3_Intres =[]
NAME_Non_Intres =[]
MOBILE_Non_Intres =[]
AGE_Non_Intres =[]
SEXE_Non_Intres = []
EMAIL_Non_Intres =[]
SKILLS_Non_Intres =[]
DOMAIN1_Non_Intres =[]
DOMAIN2_Non_Intres =[]
DOMAIN3_Non_Intres =[]
Non_lu = []
Eta = []
Eta_Non_inters = []
Adress_inter = []
Adress_Non_inter = []
domain_Intres_pdf = []
domain_Non_Intres_pdf = []
projet_inter = []
projet_Non_inter = []
langue_inter = []
langue_Non_inter = []
ga3_skills = []

# hna l choix par domain


NAME_1 = []
NAME_2 = []
NAME_3 = []
NAME_4 = []
MOBILE_1 = []
MOBILE_2 = []
MOBILE_3 = []
MOBILE_4 = []
AGE_1 = []
AGE_2 = []
AGE_3 = []
AGE_4 = []
SEXE_1 = []
SEXE_2 = []
SEXE_3 = []
SEXE_4 = []
EMAIL_1 = []
EMAIL_2 = []
EMAIL_3 = []
EMAIL_4 = []
Adress_1 = []
Adress_2 = []
Adress_3 = []
Adress_4 = []
SKILLS_1 = []
SKILLS_2 = []
SKILLS_3 = []
SKILLS_4 = []
Eta_1 = []
Eta_2 = []
Eta_3 = []
Eta_4 = []
DOMAIN1_1 = []
DOMAIN2_1 = []
DOMAIN3_1 = []
DOMAIN1_2 = []
DOMAIN2_2 = []
DOMAIN3_2 = []
DOMAIN1_3 = []
DOMAIN2_3 = []
DOMAIN3_3 = []
DOMAIN1_4 = []
DOMAIN2_4 = []
DOMAIN3_4 = []
domain_1_pdf = []
domain_2_pdf = []
domain_3_pdf = []
domain_4_pdf = []
cnt_1_pdf = 0
cnt_2_pdf = 0
cnt_3_pdf = 0
cnt_4_pdf = 0
cnt_1_docx = 0
cnt_2_docx = 0
cnt_3_docx = 0
cnt_4_docx = 0
cnt_1_doc = 0
cnt_2_doc = 0
cnt_3_doc = 0
cnt_4_doc = 0
projet_1 = []
langue_1 = []
projet_2 = []
langue_2 = []
projet_3 = []
langue_3 = []
projet_4 = []
langue_4 = []

#hna la cluster

cluster = []
similarite_domain = []
similarite_cluster = []

def synonyms_mot_cle(cherche):
    synonyms = []
    for Query in cherche:
        for syn in wordnet.synsets(Query):
            for l in syn.lemmas():
                synonyms.append(l.name())
        synonyms.append(Query)
    return synonyms

#bache nchof ch7al mn klma ktbe kayna f dok skills li jbna mn cv

def Skills_in_list(cherche,skills_in_list):
    skills_lower = []
    for e in skills_in_list:
        e=str(e).lower()
        skills_lower.append(e)
    Rank = 0
    for a in cherche:
        a=str(a)
        if a.lower() in skills_lower:
            Rank = Rank+1
    return Rank

def get_Full_name(path):
    smya_kamla = str(path)
    smya_kamla = smya_kamla.split('\\')
    smya_kamla = smya_kamla[len(smya_kamla) - 1]
    smya_kamla = str(smya_kamla)
    smya_kamla = smya_kamla[:-4]
    smya_kamla = smya_kamla.split('_')
    knya = smya_kamla[0]
    smya = "pass"
    try:
        smya = smya_kamla[1]
    except:
        pass
    smya_kamla_maj = knya+' '+smya
    knya = str(knya).lower()
    smya = str(smya).lower()
    return knya,smya,smya_kamla_maj

#hna njbde smya tlmdone

cv = CountVectorizer()
data_ville = pd.read_csv(os.path.join(os.path.dirname(__file__),'Villes/Villes.csv'))
X_ville = data_ville['ville']
X_v = cv.fit_transform(X_ville)
ville = cv.get_feature_names()



#hna kanrde smya t drari obnat l liste sa3a mab9itche khdam biha daba namesor 7sne

#cv = CountVectorizer()
#data_drari = pd.read_csv(os.path.join(os.path.dirname(__file__),'Nom/drari.csv'))
#X_drari = data_drari['NAME']
#X_d = cv.fit_transform(X_drari)
#drari = cv.get_feature_names()
#data_bnat = pd.read_csv(os.path.join(os.path.dirname(__file__),'Nom/bnat.csv'))
#X_bnat= data_bnat['NAME']
#X_b = cv.fit_transform(X_bnat)
#bnat = cv.get_feature_names()



def similarity(corpus,skills,vect):
    skills_vect= vect.transform(skills)
    corpus_vect= vect.transform(corpus)
    similarity_values = cosine_similarity(corpus_vect, skills_vect)
    idx=np.argmax(similarity_values)
    max_value=np.amax(similarity_values)
    if(max_value < 0.4):
        domain_r = "UNKNOWN"
    else:
        domain_r = Nom_clastre_skills[idx+1]
    return domain_r,max_value



def get_domain(skills):
    corpus = [
                'academic,administration,campus,learning,teaching,manuscript,writing,linguistics,literature,journals,textbooks,libraries,ebooks,advising,tutoring,courses,ecole,school,student financial aid,admissions counseling,classroom,workshops,historical interpretation,teaching,curriculum,psychological,elearning,captivate,entretiens,salle de classe,administration,droit du travail,gestion dentreprise,formation continue,veille juridique',
               'adobe,microsoft office,symantec,photoshop,corel,macromedia,nero,winzip,apple,avg,autodesk,adobe acrobat,pitstop,enfocus pitstop,quarkxpress,preflight,preps,prepress,prinergy,catalogs,structured authoring,mac,adobe acrobat pro,adobe acrobat,adobe indesign,adobe photoshop cs5,adobe photoshop,adobe illustrator,camtasia studio,microsoft onenote,adobe illustrator cs5',
               'aerial cinematography,aerial photography,aerial surveys,cinematography,video production,video editing,underwater video,videography,steadicam,photography,timelapse,aerial lifts,boom lift,scissor lift,general industry safety,fall protection,excavation safety,osha trainer,safety meetings,job safety,skid steer,work at height,aerospace,aircraft,space systems,overhaul,air filtration,damage tolerance,orbital mechanics,spacecraft,flight,aeronavegabilidad,aeronaves,vuelos,aeropuertos,air force,military,security clearance,forwarding,freight,environmental management',
               'agricultural economics,agribusiness,production,sustainable,tractor,food policy,rural development,agricultural production,plant nutrition,plant protection,soil fertility,agriculture,contract farming,seed production,crop,animal behavior,animal welfare,animal husbandry,animal work,dogs,pets,animal nutrition,euthanasia,soft tissue surgery,veterinary,nutrition,swine,animal nutrition,poultry,pigs,beef,dairy science,livestock,cattle,agriculture,animal handling,pets,dogs,zoo,cats,pet sitting'
               'analyse,ecoute,formidling,rigueur,autonomie,projektledelse,organisation,dynamisme,relationnel,gestion,onderzoek,analyse des besoins,cahier des charges fonctionnel,gestion de projet,analyse fonctionnelle,appel doffres,relations clients,animation datelier,amoa,accompagnement,gestion des litiges,ecoute,analyse des causes,amdec,manufacture,gestion de la maintenance,lean manufacturing,usine,gestion de projet,conception de produit,analyse des risques,six sigma,kaizen,analyse des exigences,gestion de projet logiciel,analyste,analytical approach,analytical skills,detail orientation,results focused,stress resistant,influential,highly adaptable,innovative problem solver,quality oriented,innovative thinking,attention to detail,analytical',
                'galleries,public art,contemporary,glass painting,glassblowing,glass,mirrors,glazing,craft,art handling,art history,museums,art exhibitions,curating,museum collections,history of art,preventive conservation,museum education,galleries,art criticism,art history,curating,art handling,museums,art exhibitions,history of art,art education,contemporary art,galleries,art criticism,museum collections,art installation,ibujo,museos,exposiciones de arte,patrimonio cultural,redes sociales,artesanato,artes visuais,belas artes,artes,desenho,pintura,escultura,modelagem,fotografia,design de moda,escrita criativa,arthritis,migraine,menopause,fibromyalgia,insomnia,infertility,chronic pain,music,artist booking,record labels,music publishing,music management,artist management,artist development,artist booking,music industry,aandr,artist relations,booking,concert promotion,music,record labels,music management,artist relations,artist development,artist booking,artist management,aandr,music industry,concert promotion,booking,talent booking,promoting,music,artistic,creative,imaginative,versatile,compassionate,detailed,assertive,musical,friendly,passionate,logical,artistic abilities,artistic eye,artistic vision,artistic ,creativity',
                'audio,sound,audio mixing,onair,production,audio design,digidesign pro tools,hd,audio engineering,promos,composing,audio books,voice over,narrator,voicing,voice acting,promo,narration,commercials,narrative,voiceovers,oncamera,audio codecs,video codec,codecs,audio processing,h264,mpeg4,psychoacoustics,digital signal processors,rtp,digital signal processing,arm,audio conferencing,video conferencing,tandberg,extron,crestron,telepresence,amx,digital signage,av,projectors,streaming media,audio design,sound design,audio mixing,digidesign pro tools,sfx,audio engineering,audio post production,field recording,dialogue editing,audio editing,audio,audio editing,audio post production,music scheduling,audio restoration,audio engineering,pro tools,audiovault,sound design,sound editing,dialogue editing,sound,audio engineering,mastering,audio post production,recording,live sound,sound design,sound,studio recording,pro tools,professional audio,sound reinforcement,audio equipment,audio engineering,audio editing,microphone placement,video systems,microphones,professional audio,live sound',
                'automotive,vehicles,automotive aftermarket,dealers,automobile,parts,powertrain,dealer management,warranty,chassis,automotive engineering,automotive aftermarket,automobile,vehicles,dealers,parts,automotive,warranty,dealer management,automotive repair,tires,automotive parts,automotive design,class a surfacing,alias studio tools,clay modelling,automotive engineering,alias automotive,teamcenter,icem surf,product design,interior trim,biw,automotive electrical systems,engine performance,onboard diagnostics,electrical diagnosis,engine rebuilding,automotive electronics,fuel injection,engine management systems,oil changes,automotive repair,automotive safety,automotive electronics,brake,steering,suspension,ase certified,onboard diagnostics,powertrain,automotive repair,tires,chassis,infotainment,automotive engineering,powertrain,automotive,chassis,dfmea,hev,vehicle dynamics,vehicles,nvh,automotive design,automotive electronics',
                'anaerobic microbiology,microbiology,environmental microbiology,microbial ecology,molecular biology,pcr,anaerobic digestion,molecular microbiology,industrial microbiology,environmental biotechnology,medical microbiology,biologia,ecologia,microbiologia,biologia molecolare,genetica,biologia molecular,biochimica,biologia celular,biologia cellulare,scienza,scienze ambientali,biologia cellulare,biologia molecolare,coltura cellulare,biochimica,genetica,scienze naturali,western blot,bioinformatica,biotecnologia,scienza,immunologia,biologia celular,biologia molecular,cultura celular,biotecnologia,imunologia,microbiologia,microscopia,pesquisa,biologia,western blot,farmacologia,biologia molecolare,biologia cellulare,coltura cellulare,biochimica,genetica,bioinformatica,scienze naturali,scienza,biotecnologia,bioinformatics,bioconductor,microarray analysis,functional genomics,computational genomics,conservation biology,ecology,wildlife biology,wildlife conservation,conservation issues,biodiversity,ornithology,zoology,wildlife,wildlife management,environmental science,developmental biology,molecular biology,cell biology,genetics,confocal microscopy,zebrafish,cell culture,in situ hybridization,fluorescence microscopy,embryology,molecular cloning,environmental microbiology,microbial ecology,microbiology,industrial microbiology,anaerobic microbiology,soil microbiology,pharmaceutical microbiology,molecular microbiology,food microbiology,bioremediation,environmental biotechnology,evolutionary biology,phylogenetics,molecular evolution,population genetics,evolution,biology,ecology',
                'body care,skin care,skin care products,body wraps,facials,sensitive skin,cosmetics,body weight training,antiaging,acne treatment,body massage,body composition,exercise physiology,personal training,nutrition,sports nutrition,special populations,medical exercise,exercise prescription,fitness,muscular endurance,functional movement screen,body contouring,tummy tuck,liposuction,facelift,breast augmentation,restylane,rhinoplasty,fillers,juvederm,radiesse,blepharoplasty,body image,treatment of depression,selfesteem,life transitions,post traumatic stress,young adults,mindfulness,psychotherapy,panic disorder,anger management,trauma therapy,body language,nonverbal communication,presentation skills coaching,diction,etiquette,separation anxiety,corporate etiquette,confidence building,personality development,puppies,dining etiquette,body massage,holistic massage,therapeutic massage,deep tissue massage,body wraps,pedicures,scrubs,chair massage,manicures,pregnancy massage,facials,body sculpting,muscle tone,cardio kickboxing,cardiovascular training,high intensity interval training,bronze sculpture,bodybuilding,body weight training,weight loss,muscular endurance,weight training,body shop,collision,auto body,paintless dent repair,automotive,automotive repair,ccc pathways,automobile,vehicles,parts,automotive aftermarket,body weight training,weight training,weight loss,weight gain,weight loss coaching,fitness training,high intensity interval training,personal training,weightlifting,muscular endurance,cardiovascular fitness,body wraps,scrubs,brazilian ',
                'agrochemicals,crop protection,agronomy,corn,agribusiness,agriculture,crop,rural marketing,plant protection,vegetables,soybean,biochemical engineering,fermentation,fermentation technology,downstream processing,biotechnology,bioprocessing,metabolic engineering,bioprocess,fermentation process development,chemical engineering,bioreactor,chemical,specialty chemicals,chemicals,additives,polymers,coatings,adhesives,fine chemicals,resin,pigments,raw materials,chemical analysis,analytical chemistry,instrumental analysis,chemical synthesis,aas,chemistry,environmental analysis,japanese language,aquatic toxicology,metallography,water analysis,chemical biology,medicinal chemistry,organic synthesis,biochemistry,organic chemistry,peptide synthesis,chemistry,nmr,mass spectrometry,drug design,synthetic organic chemistry,chemical dependency,dual diagnosis,addiction recovery,cooccurring disorders,group therapy,mental health,mental health counseling,behavioral health,relapse prevention,crisis intervention,motivational interviewing,chemical engineering,reaction engineering,aspen plus,aspen hysys,process simulation,process optimization,equipment sizing,distillation,process engineering,pfd,pro ii,chemical formulation,formulation chemistry,chemistry,formulation,chemical sales,randd,analytical chemistry,polymer chemistry,coatings technology,raw materials,rheology,chemical handling,chemical safety,emergency spill response,sds,hazardous chemicals,msds,tank farms,hazard communications,chemical processing,chemical research,bleaching,chemical industry,polyurethane,additives,chemical processing,resin,pigments,adhesives,raw materials,chemical plants,coatings,polymers,chemical peels,microdermabrasion,hyperpigmentation,acne,microcurrent,rosacea,laser hair removal,acne treatment,skin care,laser resurfacing,obagi,chemical plants,chemical processing,chemical process engineering,chemical industry,chemical safety,chemical engineering,unit operations,process safety,petrochemical,refinery,petroleum refining,chemical process engineering,chemical engineering,chemical processing,mass transfer,chemical plants,unit operations,aspen plus,aspen hysys,mass and energy balance,reaction engineering,process engineering,chemical processing,chemical engineering,chemical plants,distillation,reaction engineering,chemical industry,pilot plant,chemical process engineering,process safety,psm,process optimization,chemical research,inorganic synthesis,inorganic chemistry',
                'management development,executive coaching,executive development,personal development,outplacement,mbti,coaching de dirigeants,personal coaching,nlp,action learning,coaching baseball,baseball,sports coaching,athletic recruiting,basketball coaching,softball,athletics,sports management,intercollegiate athletics,sports,athlete development,coaching de dirigeants,formation de leader,consulting en management,formation,coaching,coaching professionnel,gestion des talents,gestion des performances,change management,offre de formation,ressources humaines,coaching empresarial,coaching personal,coaching laboral,desarrollo del liderazgo,desarrollo personal,liderazgo de equipos,inteligencia emocional,estrategia empresarial,conferencias,liderazgo empresarial,desarrollo organizacional,coaching executivo,coaching pessoal,desenvolvimento organizacional,desenvolvimento pessoal,consultoria de rh,palestras motivacionais,treinamento,executive coaching,coaching,planejamento empresarial,recrutamento,coaching for excellence,driving operational excellence,business excellence,driving profitability,center of excellence,credibility,exceeding expectations,residential treatment,process excellence,seven habits of highly effective people,passion for success,coaching laboral,coaching personal,coaching empresarial,liderazgo de equipos,desarrollo del liderazgo,inteligencia emocional,liderazgo,liderazgo empresarial',
                'commercial,industrial,juridique,gestion,achat,grande distribution,grands comptes,new construction,relationnel,residential,relation client,commercial architecture,residential architecture,architectural design,commercial projects,residential projects,consultant coordination,residential design,design development,construction documents,detailing,sustainable design,commercial aviation,flights,aviation,civil aviation,airlines,flight safety,flight planning,airports,type rating,charter,aircraft,commercial awareness,employer engagement,welfaretowork,cv,private sector,employability,training delivery,ptlls,bid writing,a1 assessor,job coaching,commercial banking,banking,small business lending,commercial lending,credit,retail banking,credit analysis,sba,loans,credit risk,lines of credit,commercial buildings,industrial buildings,residential buildings,office buildings,construction,building codes,construction management,residential homes,building design,tenant improvements,renovation,commercial business development,data transmission,international business development,male grooming,residential land development,european,languages,business development,digital business development,team restructuring,strategic manda,tender development,commercial cleaning,office cleaning,janitorial services,carpet cleaning,professional cleaning,window cleaning,upholstery cleaning,post construction cleaning,floor cleaning,industrial cleaning,green cleaning,commercial construction,residential construction,construction,construction management,residential additions,general contracting,renovation,contractors,kitchen remodeling,bathroom remodeling,historical renovations,commercial contracts,corporate law,legal advice,intellectual property,shareholder agreements,contract law,corporate governance,data protection,joint ventures,commercial litigation,real estate contracts,commercial conveyancing,enduring powers of attorney,conveyancing,court of protection,lasting powers of attorney,legal research,appeals,legal writing,courts,commercial management,cost planning,pfi,jct,refurbishing,quantity surveying,cost management,fitout,cost reporting,nec3,refurbishments,commercial mortgages,loans,sba,commercial lending,mortgage lending,construction loans,second mortgages,debt consolidation,credit,loan origination,lines of credit,commercial moving,residential moving,long distance moving,movers,corporate relocation,international relocations,move management,packing,certified relocation professional,destination services,removals,commercial music,music production,computer music,composition,music,sound design,film scoring,studio recording,songwriting,music theory,jingles,commercial operation,developments,expansion strategies,operations control,business operations,sales force alignment,tandd,chartering,prayer,service operation,inclusive leadership,commercial paper,money market,covered bonds,print estimating,repos,interest rate swaps,liquidity management,fx hedging,bindery,foil stamping,government bonds,commercial photography,portrait photography,headshots,portraits,event photography,studio photography,on location,photos,lifestyle photography,environmental portraiture,fine art photography,commercial pilot,flight operations,commercial aviation,aviation operations,aviation,piloting,cfi,flight instructor,aviation industry,aircraft,flights,commercial piloting,instrument rated pilot,multiengine land,piloting,aviation,private piloting,commercial aviation,helicopter piloting,single engine land,flight training,aircraft,commercial planning,customer marketing,trade marketing,channel strategy development,planning appeals,planning applications,business planning,field force management,promotional analysis,customer value,campaign performance analysis,commercial product photography,portrait photography,commercial photography,environmental portraiture,food photography,wedding photojournalism,studio photography,lifestyle photography,boudoir,editorial photography,model portfolios,commercial production,affiliate marketing,affiliate networks,online gambling,affiliate relations,bingo,cpl,igaming,poker,sportsbook,egaming,affiliate marketing,affiliate networks,affiliate management,ppc,conversion optimization,cpl,sem,online marketing,performance based marketing,online advertising,marketing de afiliados,affiliate networks,affiliate marketing,affiliate management,affiliate relations,cpl,performance based marketing,affiliates,online lead generation,ppc,conversion optimization,online marketing,affiliate relations,affiliate networks,affiliate management,affiliate marketing,affiliates,cpl,affiliation,performance based marketing,online marketing,igaming,online lead generation,affiliates,affiliate networks,affiliate marketing,affiliate relations,affiliate management,affiliation,ppc,online advertising,online casino,online marketing,online lead generation,affiliation,marketing en ligne,emailing,display,seo,marketing par email,affiliates,statistiques web,retargeting,marketing digital,sem,advertising agency,advertising,digital marketing,agency relationship management,advertising management,online advertising,local advertising,marketing communications,above the line,marketing,managing agency relationships,agency agreements,agency coordination,agency relations,agency relationship management,managing agency relationships,franchise agreements,nondisclosure agreements,general commercial agreements,distributorships,shareholder disputes,purchase agreements,agency coordination,agency agreements,agency relationship management,managing agency relationships,economics,business education,executive education,engineering education,faculty training,faculty development,entrepreneurship education,ecollege,academic administration,career education,webct,desire2learn,business efficiency,cost efficiency,process efficiency,operational efficiency,business process efficiency,production efficiency,increase productivity,resource efficiency,efficiency improvement,streamlining work processes,efficiency,business engineering,industrial equipment,requirements engineering,strategy mapping,purchasing negotiations,process architecture,avaloq,dymola,application engineering,project management,spacecraft design,business english,english for specific purposes,pronunciation,ielts,tesol,toefl,tefl,applied linguistics,teaching english as a second language,academic english,language teaching,business ethics,professional ethics,code of ethics,ethical leadership,ethics,code of conduct,government ethics,legal ethics,uk bribery act,anticorruption,medical ethics,business excellence,efqm excellence model',
                'electric,grip,electric power,ledit,ltspice,electrical,production assistant,gaffer,hydraulic,mechanical,electrical testing,electric cars,muscle cars,electric vehicles,battery management systems,preowned,hybrids,automotive,electric drives,charging systems,lithiumion batteries,hydrogen fuel cells,electric drives,power electronics,power converters,electrical machines,electric motors,motor drives,electrical engineering,simulink,matlab,digital control,power electronics design,electric guitar,acoustic guitar,lead guitar,rhythm guitar,bass guitar,classical guitar,blues guitar,guitar repair,jazz guitar,hard rock,guitarist,electric motors,motor control,electric drives,motor drives,variable frequency drives,dc drives,gearboxes,ac drives,circuit breakers,electrical machines,servo drives,electric power,nerc,power systems,outage management,power generation,smart grid,power distribution,electricity,substation,reactor,demand response,electric utility,utility regulation,utility industry,electric power,power utilities,smart grid,demand response,ferc,nerc,outage management,demandside management,electric vehicles,hev,hybrid,batteries,powertrain,automotive engineering,hybrids,vehicle dynamics,battery management systems,battery,lithiumion batteries,electrical,electricians,controllogix,industrial controls,vfd,electrical maintenance,motor controls,control system design,industrial networks,plant,mechanical,electrical code,national electrical code,electrical work,electrical estimating,licensed master electrician,electrical contracting,electricians,electrical repairs,electrical safety,wiring,generator installation,electrical contracting,electrical estimating,electrical safety,electrical industry,electrical design,wiring,electrical controls,electricians,electrical equipment,electrical troubleshooting,electrical code,electrical controls,electrical safety,electrical troubleshooting,motor control,wiring,variable frequency drives,electricians,electrical equipment,allen bradley,electricity,plc,electrical controls design,electrical panel design,electrical distribution design,plc programming,electrical engineering,electrical design,hmi programming,electrical controls,electrical troubleshooting,plc,control systems design,electrical design,electrical engineering,short circuit,power distribution,lightning protection,electrical estimating,switchgear,grounding,electrical contracting,electrical controls,electricians,electrical diagnosis,engine performance,automotive electrical systems,oil changes,onboard diagnostics,engine rebuilding,fuel injection,engine management systems,automotive safety,automotive repair,steering,electrical distribution design,electrical panel design,electrical engineering,electrical controls design,electrical design',
                'engineer,producer,music producer,technician,spc charts,field,manager,composer,fault diagnosis,mechanical engineer,ug,engineered wood products,truss,plywood,wood,timber,forest products,laminate flooring,timber frame,millwork,building materials,timber structures,engineering,project engineering,mechanical engineering,engineering design,commissioning,engineering management,power plants,epc,electrical engineering,design for manufacturing,power generation,engineering analysis,mechanical engineering,proandmechanica,finite element analysis,engineering,dfma,algor,engineering leadership,solidworks,machine design,sdrc ideas,engineering change control,engineering change management,bom management,bom creation,bill of materials,boms,engineering documentation,iec 60601,first article inspection,epdm,fishbone,engineering change management,engineering change control,bom management,bill of materials,bom creation,pdm,product lifecycle management,oracle agile plm,teamcenter,plm tools,product data management,engineering design,plant design,pds,feed,pdms,project engineering,engineering,smart plant review,autoplant,pandid,epc,engineering documentation,procedural documentation,technical documentation,documentation practices,engineering change control,engineering drawings,assembly drawings,user documentation,bom management,bill of materials,bom creation,engineering drawings,mechanical drawings,solid modeling,design for assembly,design engineering,assemblies,mechanism design,assembly drawings,autocad mechanical,mechanical product design,solidworks,engineering economics,engineering statistics,operations research,arena simulation software,time study,simio,matlab,statics,industrial engineering,mechanics of materials,discrete event simulation,engineering education,ecollege,faculty development,university teaching,webct,critical pedagogy,faculty training,lecturing,educational research,theory,academic administration,engineering geology,slope stability,geotechnics,rock mechanics,geotechnical engineering,site investigation,geology,ground investigation,slope stability analysis,geological mapping,ground improvement,engineering leadership,engineering management,engineering analysis,engineering,systems engineering,trade studies,flight test engineering,system of systems engineering,lean engineering,umbilicals,concurrent engineering,engineering management,trade studies,systems engineering,engineering,spacecraft,space systems,telelogic doors,earned value management',
                'enterprise,service providers,cloud marketing,employability,cloud,yahoo,smb,imis,enterprise software,network infrastructure architecture,rpas,enterprise 20,social business,social software,enterprise collaboration,enterprise social networking,web 20,social collaboration,collaboration tools,knowledge management,portals,enterprise content management,enterprise account management,enterprise solution sales,enterprise technology sales,software solution sales,solution selling,vars,sales cycle management,isv,channel account management,it sales,clevel sales,enterprise application integration,eai,soa,unified modeling language,servizi web,integrazione,tibco,architettura delle soluzioni,tibco rendezvous,integration,analisi dei requisiti,enterprise architect,uml,rational rose,scrum,rup,levantamento de requisitos,java,sql,oracle,eclipse,bpmn,enterprise architecture,togaf,solution architecture,it strategy,zachman,soa,integration,application architecture,architecture frameworks,eai,business architecture,enterprise asset management,architecture management,maximo,eam,actuate report,birt,cmms,it asset management,erp,business process,oracle scm,enterprise backup,enterprise storage,tape libraries,virtualization,san,disaster recovery,disk arrays,server virtualisation,storage area networks,storage consolidation,vtl,enterprise collaboration,enterprise 20,collaboration solutions,collaboration tools,social business,enterprise social networking,social software,enterprise software,social technologies,enterprise content management,quickr,enterprise content management,document capture,ecm,webtop,filenet,document management,kofax,wdk,captiva,enterprise search,documentum,enterprise data modeling,logical data modeling,data warehousing,data architecture,data modeling,relational data modeling,physical data modeling,data warehouse architecture,erwin,business intelligence,star schema,enterprise development,value chain analysis,sme development,private sector development,microfinance,local economic development,livelihood,rural development,social protection,food security,capacity building,enterprise gis,arcgis server,esri,gis,arcsde,spatial databases,arcims,geodatabase,arcgis,web mapping,spatial data management,enterprise information systems,enterprise systems implementation,information systems project management,enterprise integration,computer information systems,it and business strategy alignment,enterprise it strategy,internetandintranet technologies,information technology audit,data governance,ict governance,enterprise integration,soa,integration architecture',
                'food,recipes,gourmet,frozen food,culinary skills,food cost,food service,menu development,sauces,ingredients,sanitation,food allergies,celiac disease,heart disease,clinical nutrition,renal nutrition,nutrition education,nutritional counseling,nutritional analysis,medical nutrition therapy,cholesterol,enteral nutrition,food chemistry,food science,food microbiology,food technology,sensory evaluation,food processing,haccp,flavors,food safety,ingredients,food industry,food cost,menu design,menu creation,culinary,menu development,fine dining,catering,cuisine,food,restaurants,guest satisfaction,food cost analysis,food cost management,menu costing,culinary management,menu engineering,recipe testing,menu development,culinary education,sauces,labor control,food quality,food cost management,food cost analysis,menu costing,culinary management,labor control,menu engineering,menu development,recipe testing,sauces,new restaurant openings,culinary skills,food demonstrations,american cuisine,international cuisines,culinary education,recipe testing,personal chef services,culinary travel,cooking,food styling,saute,product demonstration,food distribution,foodservice distribution,food marketing,retail food,frozen,frozen food,vehicle routing,kosher,food policy,cold chain,food industry,food engineering,food technology,food science,food processing,food chemistry,food microbiology,food preservation,food safety,haccp,functional foods,food law,food hygiene,food safety,manual handling,fire marshall,food production,menu planning,haccp,coshh,unit operations,food law,personnel training,food industry,food processing,food manufacturing,food technology,ingredients,frozen food,food science,haccp,food safety,meat,flavors,food labelling,allergens,food law,ssop,gfsi,food technology,food science,food safety,haccp,brc,food microbiology,food law,food labelling,food safety,food science,haccp,food technology,ghp,allergens,food microbiology,food industry,food engineering,food management,certified food manager,food marketing,food cost management,food safety,food safety management system,food service operations,food preparation,american cuisine,food service sanitation,international cuisines,food manufacturing,food processing,food industry,haccp,food safety,food technology,sqf,food science,brc,ingredients,gfsi,food marketing,food management,food industry,retail food,foodservice distribution,natural foods,food demonstrations,food writing,food distribution,food law,communication development,food microbiology,food science,food technology,food chemistry,sensory evaluation,food processing,haccp,gfsi,food safety,iso 22000,ssop,food packaging,corrugated,folding cartons,retail packaging,packaging engineering,packaging,flexo,paperboard,flexible films,artioscad,rotogravure,food pairing,wineries,champagne,wine tasting,alcoholic beverages,winemaking,wine,beer,beverage industry,viticulture,wine lists,food photography,still life,commercial photography,architectural photography,lifestyle photography,environmental portraiture,portrait photography,studio photography,studio lighting,on location,editorial photography,food policy,food systems,agricultural policy,sustainable agriculture,urban agriculture,food security,food law,local food,food labelling,farmers markets,trade policy,food preparation,sanitation,sauces,recipe testing,culinary management,recipes,food cost management,menu costing,servsafe,cooking,gourmet,food preservation,canning,food engineering',
                'geologia,geofisica,ouro,setor de minerais,processamento mineral,ingegneria geotecnica,geology,valutazione di impatto ambientale,ambientalismo,scienze ambientali,acqua,geological mapping,geology,structural geology,economic geology,geochemistry,earth science,mineral exploration,sedimentology,field mapping,stratigraphy,geostatistics,geologists,exploration geologists,geology,geological mapping,environmental geology,engineering geology,geophysics,structural geology,petroleum geology,mud logging,geolocation,geology,geological mapping,structural geology,earth science,stratigraphy,sedimentology,sequence stratigraphy,geochemistry,geophysics,economic geology,petroleum geology',
                'graphic,graphic design,photo,logo,graphics,vector design,batik,organizational project management,fashion designer,vector,prestampa,graphic arts,proof,inkjet,color management,print on demand,wide format printing,prepress,bindery,labels,variable data printing,offset printing,graphic communication,print solutions,graphic design,graphic presentations,kodak,foil stamping,finishing,prinergy,offset,print production management,indesign,graphic design,logos,typography,logo design,posters,corporate identity,graphics,business cards,flyers,layout,brochures,graphic design software,graphic design,computer graphics design,graphic designers,illustrator,adobe creative suite,graphic presentations,photoshop,graphic illustrations,indesign,logo design,graphic designer,web designer,art director,photographer,web developer,creative director,production manager,interior designer,graphic design,cataloghi,artist,graphic designers,design logos,designers,graphic design software,graphic design,web designer,banner designing,logo design,illustrator,corporate stationary,web design,graphic designing,web designing,label design,graphic illustrations,inpage,filming,animation,graphic design,ecommerce solutions,batik,vfx,graphic facilitation,visual thinking,workshop facilitation,facilitators,design workshops,facilitation,executive facilitation,appreciative inquiry,systems thinking,strategic planning facilitation,design thinking,graphic illustrations,graphic design,illustrator,editorial illustrations,photoshop,vector illustration,book illustration,logo design,illustration,icons,indesign,graphic novels,comic books,comics,inking,sequential art,comic art,cartoons,comic book illustration,storyboarding,visual storytelling,cover art,graphic presentations,graphic communication,packaging graphics,graphic design,color renderings,su podium,brand strengthening,graphic illustrations,sketchup,presentation design,model homes,graphics,posters,graphic design,logo',
                'patient registration,medical billing,employee health,occupational health nursing,workplace health,spirometry,audiometry,sickness absence management,travel medicine,health assessment,occupational medicine,occupational rehabilitation,health promotion,environmental health,exposure assessment,outbreak investigation,industrial hygiene,public health,disease surveillance,public health surveillance,public health emergency preparedness,epidemiology,occupational health,environmental awareness,global health,international health,public health,reproductive health,epidemiology,health systems,hiv prevention,health services research,community health,malaria,health equity,group health,health insurance,group benefits,dental,supplemental insurance,health plans,medicare supplements,insurance,disability insurance,term life insurance,employee benefits,health,pain,natural health,conditioning,corporate wellness,sports performance,athletes,stress reduction,healthy lifestyle,group exercise,treatments,health advocacy,public health education,health literacy,health program planning,environmental advocacy,government advocacy,social determinants of health,public health,health equity,child advocacy,community health,health assessment,employee health,occupational health nursing,spirometry,therapeutic communication,health promotion,health education,medication administration,workplace health,health program planning,audiometry,health benefits administration,employee benefits,health services administration,retirement benefits,human resources,benefits administration,disability benefits,open enrollment,benefit plan administration,peo,adp payroll,health care fraud,health law,fraud,public corruption,medical compliance,health care regulation,internal investigations,certified fraud examiner,fraud claims,medicaid,antifraud,health care professionals,health care regulation,health care systems,physician assistants,medical staffing,primary health care,healthcare,health care fraud,residential care,community hospitals,healthcare staffing,health care reform,selffunded,health savings accounts,group medical,health insurance,cobra,flexible spending accounts,group insurance,employee benefits,cafeteria plans,disability insurance,health care regulation,health care reform,health care fraud,health law,health insurance exchanges,health care professionals,health care systems,affordable care act,hospital reimbursement,accountable care,healthcare compliance,health care systems',
                'commercial,office,multifamily,domestic,transformers,fire alarm systems,foreman,offices,marine,residential,industrial automation,plc programming,automation,scada,hmi,plc,plc siemens,plc allen bradley,hmi programming,ac drives,iec 611313,industrial buildings,commercial buildings,office buildings,residential buildings,steel buildings,preengineered metal buildings,dynamic analysis,steel structures,industrial real estate,structural engineers,steel design,industrial chemicals,fine chemicals,hazardous chemicals,chemical sales,chemical industry,specialty chemicals,biocides,chemical safety,industrial cleaning,chemical research,lubricants,industrial cleaning,floor cleaning,professional cleaning,green cleaning,window cleaning,commercial cleaning,construction cleanup,office cleaning,post construction cleaning,carpet cleaning,home cleaning,industrial coatings,protective coatings,coatings technology,coatings,powder coating,epoxy,epoxy flooring,corrosion protection,nace,paint,uv coating,industrial control,motion control,servo,automation,hmis,industrial ethernet,variable frequency drives,plc,process automation,control logic,allen bradley,industrial controls,controllogix,vfd,industrial networks,control system design,industrial control,plc,automation,ethernetandip,hmis,allen bradley,industrial design,hypershot,design strategy,concept generation,alias studio tools,product design,design thinking,strategic design,concept development,sketching,rapid prototyping,industrial distribution,fluid power,bearings,industrial markets,outside sales,industrial supplies,motion control,power transmission,key account management,sales management,seals,industrial ecology,life cycle assessment,simapro,sustainable development,sustainability,carbon footprinting,environmental impact assessment',
                'javascript,php,c#,c++,ruby,css,c,objective-c,shell,scala,swift,matlab,clojure,octave,machine learning,data analytics,predictive analytics,html,js,accounts payable,receivables,inventory controls,payroll,deposits,bank reconciliation,planning and enacting cash-flows,report preparation,financial models,financial controls,documentation,time management,schedules,benchmarking,future state assessment,business process re-engineering,as-is analysis,defining solutions and scope,gap analysis,role change,wireframing,prototyping,user stories,financial analysis/modeling,swot analysis,quickbooks,quicken,erp,enterprise resource planning,spanish,german,rest,soap,json,website,ui,ux,design,crm,cms,communication,coding,windows,servers,unix,linux,redhat,solaris,java,perl,vb script,xml,database,oracle,microsoft sql,sql,microsoft word,microsoft powerpoint,powerpoint,word,excel,visio,microsoft visio,microsoft excel,adobe,photoshop,hadoop,hbase,hive,zookeeper,openserver,auto cad,pl/sql,ruby on rails,asp,jsp,operations,technical,training,sales,marketing,reporting,compliance,strategy,research,analytical,engineering,policies,budget,finance,project management,health,customer service,content,presentation,brand,presentations,safety,certification,seo,digital marketing,accounting,regulations,legal,engagement,analytics,distribution,coaching,testing,vendors,consulting,writing,contracts,inventory,retail,healthcare,regulatory,scheduling,construction,logistics,mobile,c�(programming language),correspondence,controls,human resources,specifications,recruitment,procurement,partnership,partnerships,management experience,negotiation,hardware,programming,agile,forecasting,advertising,business development,audit,architecture,supply chain,governance,staffing,continuous improvement,product development,networking,recruiting,product management,sap,troubleshooting,computer science,budgeting,electrical,customer experience,economics,information technology,transportation,social ,analysis,datasets,alliances,solidworks,prototype,lan,sci,budget management,rfps,flex,gaap,experimental,cpg,information system,customer facing,process development,web services,international,travel,revenue growth,software development life cycle,operations management,computer applications,risk assessments,sales operations,raw materials,internal audit,physical security,sql server,affiliate,computer software,manage projects,business continuity,litigation,it infrastructure,cost reduction,small business,annual budget,ios,html5,real-time,consulting experience,circuits,risk assessment,cross-functional team,public policy,analyzing data,consulting services,google drive,ad words,pay per click,email,db2,expense tracking,reports,wordpress,yoast,ghostwriting,corel draw,automated billing,system,customer management,debugging,system administration,network configuration,software installation,security,tech support,updates,tci/ip,dhcp,wan/lan,ubuntu,virtualized networks,network automation,cloud management,ai,salesforce,mango db,arduino',
                'literary,literature,fiction,nonfiction,short stories,fiction writing,novels,manuscripts,books,creative writing,stories,literary criticism,literary theory,literary editing,american literature,literature,literary writing,english literature,literary fiction,comparative literature,british literature,creative writing,literary editing,literary writing,literary criticism,literary theory,literary fiction,creative writing,comparative literature,british literature,literature,poetics,poetry,literary fiction,prose,memoir,creative nonfiction,fiction writing,science fiction,rewriting,novels,manuscript,book reviews,fiction,literary theory,literary criticism,literary editing,literary writing,comparative literature,american literature,literature,english literature,british literature,cultural studies,critical theory,literary translation,translation,technical translation,legal translation,subtitling,proofreading,language services,linguistics,literature,sdl trados,medical translation,literary writing,literary editing,literary theory,literary criticism,literary fiction,comparative literature,creative writing,english literature,poetry,british literature,literature',
                'management,leadership,strategy,business development,planification commerciale,training,crm,executive management,consulting en management,sales,outsourcing,management accounting,financial accounting,financial reporting,accounting,cima,cash flow,statutory accounting,year end accounts,cash flow forecasting,management accounts,vat,management accounts,vat returns,management accounting,vat,year end accounts,accounting,paye,prepayment,sage,sage line50,self assessment tax returns,management buyouts,private equity,buyouts,mergers and acquisitions,corporate finance,restructuring,growth capital,business valuation,exit strategies,shareholder agreements,manda experience,management by objectives,meeting objectives,kpi implementation,objectivity,cost of quality,staff appraisal,development coaching,driven by results,customer value management,challenging environment,milestones,management coaching,performance management,executive coaching,change management,organizational development,management development,human resources,personal coaching,employee engagement,succession planning,talent management,management consulting,market entry,operating models,business transformation,change management,business strategy,strategy,executive development,strategic consulting,executive coaching,interim management,management contracts,management engineering,contracts administrators,sales contracts,compliance oversight,procurement contracts,vendor contracts,real estate contracts,operations audit,certified hotel administrator,contract management,management control,business control,audit financier,audit interne,management engineering,financial controlling,management contracts,project management office,information system,reporting financier,balanced scorecard,management de la direction,gestion de projet,management des processus,leadership organisationnel,coaching de dirigeants,expertise informatique,gestion de la relation avec les partenaires,consulting en management',
                'math,ethical,selfmanagement,physics,basic accounting,macros,physical sciences,theoretical computer science,unsupervised learning,socorrista,puns,mathcad,risa,finite element analysis,aisc,risa 3d,structural analysis,structural dynamics,autocad,matlab,steel design,sacs,mathematica,matlab,latex,mathematical modeling,theoretical physics,physics,numerical analysis,scientific computing,computational physics,quantum optics,fortran,mathematical analysis,mathematical programming,computational mathematics,applied mathematics,mathematical physics,discrete mathematics,linear algebra,mathematical modeling,abstract algebra,differential equations,mathematical statistics,mathematical economics,econometrics,microeconomics,mathematical statistics,macroeconomics,economics,economic statistics,econometric modeling,economic modeling,stata,applied economics,mathematical logic,theoretical computer science,formal languages,discrete mathematics,model checking,number theory,combinatorics,formal methods,complexity theory,abstract algebra,theory of computation,mathematical modeling,numerical analysis,scientific computing,latex,applied mathematics,numerical simulation,partial differential equations,physics,computational physics,simulations,matlab,mathematical physics,theoretical physics,physics,general relativity,applied mathematics,quantum mechanics,computational physics,partial differential equations,quantum field theory,statistical physics,mathematical modeling,mathematical programming,combinatorial optimization,mathematical modeling,cplex,linear programming,applied mathematics,operations research,integer programming,mathematical analysis,computational mathematics,optimization,mathematical statistics,mathematical economics,probability theory,economic statistics,mathematical analysis,applied probability,bayesian statistics,stochastic processes,multivariate statistics,r,stochastic calculus,mathematics,abstract algebra,number theory,algebra,calculus,geometry,differential geometry,combinatorics,mathematical physics,physics,linear algebra,mathematics education,algebra,precalculus,geometry,trigonometry,curriculum mapping,tutoring,lesson planning,smartboard,classroom,classroom management,mathlab,mathcad,microsoft office,autocad,polymath,mathematical analysis,solidworks,maple,mathematics,working model,multisim,maths,employability,question answering,makeup,tuition,eftpos,sen,behaviour management,assessing,physics,computing',
                'mechanical,electrical,structural,operation monitoring,industrial equipment,electric,hydraulics,pneumatics,hydraulic,repairing,machine operatormechanical analysis,dynamic analysis,mechanical testing,mechanical engineering,mechanical product design,mechanism design,mechanical drawings,finite element analysis,mechanical systems,solid mechanics,stress analysis,mechanical aptitude,hand tools,equipment repair,power tools,electrical troubleshooting,equipment maintenance,mechanics,mig welding,hydraulic systems,arc welding,pneumatics,mechanical assembly,soldering,assembly drawings,mechanical inspection,electromechanical troubleshooting,mechanical drawings,mechanical troubleshooting,assembly processes,wiring diagrams,surface grinding,manufacturing,mechanical design,mechanical engineering,solidworks,piping design,cad,electromechanical design,structural design,finite element analysis,engineering,fea,sheet metal design,mechanical desktop,autocad,inventor,solidworks,autodesk vault,autocad mechanical,mechanical drawings,sdrc ideas,mechanism design,cad,mechanical product design,mechanical drawings,mechanical product design,engineering drawings,autocad mechanical,mechanical engineering,mechanical analysis,mechanical systems,assembly drawings,mechanical desktop,solidworks,solid modeling,mechanical engineer,mechanical engineering,electrician,engineering,engineer,project manager,welder,plant commissioning,sheet metal design,biomems,accountable,mechanical engineering,engineering,pro engineer,finite element analysis,solidworks,machine design,solid modeling,ptc creo,design engineering,tolerance analysis,ansys,mechanical inspection,visual inspection,mechanical systems,b313,hydrostatic testing,welding inspection,third party inspection,mechanical testing,risk based inspection,api 510,nde,mechanical maintenance,electrical maintenance,mechanical engineering,preventive maintenance,vibration analysis,psychological operations,civil affairs,cbm,commissioning,pressure testing,lubrication,mechanical product design,mechanical engineering,mechanical drawings,solidworks,mechanical analysis,mechanism design',
                'mobile,mobile devices,mobile software,mobile solutions,cellular,mobile applications,product strategy,mobile internet,mobile technology,mobile content,mobile communications,mobile advertising,ad networks,mobile marketing,ad serving,rich media,behavioral targeting,online advertising,display advertising,doubleclick,ad exchanges,digital marketing,mobile analytics,mobile advertising,web analytics,mobile applications,mobile marketing,mobile strategy,aandb testing,web analytics implementation,analytics,google analytics,digital analytics,mobile application design,mobile application development,user interface design,web design,mobile applications,user experience,user experience design,desktop application design,mobile design,interaction design,web application design,mobile application development,mobile application design,web application development,android development,ios development,javascript,java,web development,xamarin,mobile game development,swift,mobile application testing,manual testing,regression testing,mobile testing,test planning,functional testing,test cases,black box testing,web testing,test automation,smoke testing,mobile applications,mobile software,mobile internet,mobile content,mobile strategy,mobile devices,mobile technology,brew,s60,ios development,symbian,mobile architecture,mobile applications,mobile strategy,mobility strategy,mobile technology,enterprise mobility,mobile security,project architecture,ios development,agile methodologies,mobile product development,mobile banking,internet banking,mobile payments,payment cards,debit cards,cards,acquiring,emv,payment systems,mobile commerce,payment services,mobile broadband,telecommunications,lte,mobile communications,mobile devices,gsm,wireless,mobile telephony,wireless broadband,mobile technology,broadband networks,mobile commerce,mobile payments,epayments,mobile content,acquiring,payment gateways,payment industry,payment services,nfc,cards,mobile internet,mobile communications,mobile devices,telecommunications,handsets,mobile technology,wireless,gsm,lte,umts,comunicazioni mobili,mobile telephony,mobile computing,barcode,enterprise mobility,rfid,mobility,solutions marketing,wlan,windows mobile,ubiquitous computing,mobile devices,mobile device management,mobile content',
    ]
    vect = CountVectorizer(analyzer='char_wb', ngram_range=(2, 2),token_pattern=r'\w{1,}')
    vect.fit(corpus)
    terms = vect.get_feature_names()
    return similarity(corpus,skills,vect)


#-------------------------

def similarity_cluster(corpus,skills,vect):
    skills_vect= vect.transform(skills)
    corpus_vect= vect.transform(corpus)
    similarity_values = cosine_similarity(corpus_vect, skills_vect)
    idx=np.argmax(similarity_values)
    max_value=np.amax(similarity_values)
    return idx,max_value

def get_cluster(list, K_cluster):
    corpus = []
    for a in range(0,K_cluster):
        zhre = random.randint(0, len(list)-1)
        ligne_skills = str(list[zhre])
        corpus.append(ligne_skills)
    vect = CountVectorizer(analyzer='char_wb', ngram_range=(2, 2), token_pattern=r'\w{1,}')
    vect.fit(corpus)
    terms = vect.get_feature_names()
    cluster = []
    similarite_cluster = []
    for skills in list:
        bzaf_maharat = ""
        for maharat in skills:
            bzaf_maharat = maharat + "," + bzaf_maharat
        lista_skills = [bzaf_maharat]
        clu,sim_clu = similarity_cluster(corpus, lista_skills, vect)
        if clu == None:
            cluster.append("unknown")
        else:
            cluster.append(clu)
        prec = sim_clu * 100
        prec = str(prec)
        prec = prec[:-12]
        prec = prec + "%"
        if prec == None:
            similarite_cluster.append("unknown")
        else:
            similarite_cluster.append(prec)

    return cluster,similarite_cluster
