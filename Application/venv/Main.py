from flask import Flask,render_template,request , json, send_from_directory
import os
import function
import pandas as pd
import Choix_skills_Notre_Model  as CSNM
import Choix_skills_Model_Spacy  as CSMS
import Choix_Domain_Notre_Model  as CDNM
import Choix_Domain_Model_Spacy  as CDMS
import Choix_Cluster_Notre_Model as CCNM
import Choix_Cluster_Model_Spacy as CCMS

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploade')


#---------------------------------------------------------------------
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		upload_path = '{}/{}'.format(UPLOAD_FOLDER, file.filename)
		if function.allowed_file(file.filename):
			file.save(upload_path)
			if function.allowed_file_filesize(os.stat('./uploade/'+file.filename).st_size):
				function.Extract('./uploade/'+file.filename)
			else :
				os.remove('./uploade/'+file.filename)
		return 'ok'

#---------------------------------------------------------------------
# hna bnsba l choix skill
# had page controle
@app.route('/Choix_Skills')
def erreur_404_Skills():
	return render_template("404.html")

@app.route('/Choix_Skills',methods=["GET","POST"])
def process_Skills():
	if request.method == 'POST':
		if len(os.listdir('./uploade')) == 0:
			return render_template("index.html", erreur=1)

		mypath = './Extraire'
		# hna kanhze skills mn l page html
		skills1 = request.form['skills1']
		skills2 = request.form['skills2']
		skills3 = request.form['skills3']
		skills4 = request.form['skills4']
		#domain1 = request.form['domain1']
		#domain2 = request.form['domain2']
		#domain3 = request.form['domain3']
		choix  = request.form['Rad']
		# ila maktbe walo lmskhote aykhsni n7bso hhhh b7al dkhol l7mam b7al khrojo ... ( wakha ma3ndha ta m3na hhh )
		s1 = str(skills1)
		s2 = str(skills2)
		s3 = str(skills3)
		s4 = str(skills4)
		s1 = s1.split(';')
		s2 = s2.split(';')
		s3 = s3.split(';')
		s4 = s4.split(';')
		key=[]
		for key_word in s1:
			key.append(key_word)
		for key_word in s2:
			key.append(key_word)
		for key_word in s3:
			key.append(key_word)
		for key_word in s4:
			key.append(key_word)
		# key fiha daba les mots khsni nzide ta domain
		if choix == "op1":
			# hna aykhsni n remplacih bkmala t programme  ----
			aaa,bbb,ccc,ddd,eee,fff,ggg,hhh,iii = CSNM.Choix_skills_Notre_Model(mypath, key)

			choix = 1
			df = pd.read_csv('./Choix_skills_Notre_Model/Inters.csv')
			df_non_inters = pd.read_csv('./Choix_skills_Notre_Model/Non_Inters.csv')
			# petite vérification
			if df.empty :
				Inters_vide = 1
			else:
				Inters_vide= 0
			if df_non_inters.empty:
				Non_Inters_vide = 1
			else :
				Non_Inters_vide = 0

			kolchi_Inters = []
			for a,b,c,d,e,f,g,h,i in zip(df['NAME'],df['EMAIL'],df['MOBILE'],df['DOMAIN1'],df['DOMAIN2'],df['DOMAIN3'],df['SEXE'],df['AGE'],df['Etas']):
				kolchi_Inters.append(a)
				kolchi_Inters.append(b)
				kolchi_Inters.append(c)
				kolchi_Inters.append(d)
				kolchi_Inters.append(e)
				kolchi_Inters.append(f)
				kolchi_Inters.append(g)
				kolchi_Inters.append(h)
				kolchi_Inters.append(i)


			hada_lskills = []
			for list in df['SKILLS']:
				list = str(list)
				hada_lskills.append('.')
				hada_lskills.append(list)
				for i in range(0,7):
					hada_lskills.append('.')

			hada_Adresse = []
			for list in df['ADRESS']:
				list = str(list)
				hada_Adresse.append('.')
				hada_Adresse.append(list)
				for i in range(0, 7):
					hada_Adresse.append('.')

			kolchi_Non_Inters = []
			for a,b,c,d,e,f,g,h,i in zip(df_non_inters['NAME'], df_non_inters['EMAIL'], df_non_inters['MOBILE'], df_non_inters['DOMAIN1'], df_non_inters['DOMAIN2'], df_non_inters['DOMAIN3'], df_non_inters['SEXE'], df_non_inters['AGE'],df_non_inters['Etas']):
				kolchi_Non_Inters.append(a)
				kolchi_Non_Inters.append(b)
				kolchi_Non_Inters.append(c)
				kolchi_Non_Inters.append(d)
				kolchi_Non_Inters.append(e)
				kolchi_Non_Inters.append(f)
				kolchi_Non_Inters.append(g)
				kolchi_Non_Inters.append(h)
				kolchi_Non_Inters.append(i)


			hada_lskills_non_inters = []
			for list in df_non_inters['SKILLS']:
				list = str(list)
				hada_lskills_non_inters.append('.')
				hada_lskills_non_inters.append(list)
				for i in range(0, 7):
					hada_lskills_non_inters.append('.')

			hada_Adresse_non_inters = []
			for list in df_non_inters['ADRESS']:
				list = str(list)
				hada_Adresse_non_inters.append('.')
				hada_Adresse_non_inters.append(list)
				for i in range(0, 7):
					hada_Adresse_non_inters.append('.')

			# hna nbda n7ma9 fm3a plot

			label_nom=[]
			label_age=[]
			for kok in df['NAME']:
				label_nom.append(kok)
			labels_nom = json.dumps( label_nom )
			for kok in df['AGE']:
					label_age.append(kok)
			labels_age = json.dumps( label_age )

			# fin nta3 choix

			# hna kan suprimiw uploid bache ikhwa l9ne

			mypath = './uploade'
			onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
			for a in onlyfiles:
				os.remove(a)

			# hna dakchi t char
			df_hist = pd.read_csv("./hist.csv")
			label_date = []
			label_nbcv = []
			for a in df_hist['DATE']:
				label_date.append(a)
			labels_date = json.dumps(label_date)
			for a in df_hist['NBCV']:
				label_nbcv.append(a)
			labels_nbcv = json.dumps(label_nbcv)

			# ila kolchi howa hadak rj3 lih pagge résultat
			return render_template("Resultat_Skills.html",
								   SKILLS_INTERS=hada_lskills,
								   KOLCHI_INTERS=kolchi_Inters,
								   SKILLS_NON_INTERS=hada_lskills_non_inters,
								   KOLCHI_NON_INTERS=kolchi_Non_Inters,
								   LABEL_NOM=labels_nom,
								   LABEL_AGE=labels_age,
								   LABEL_DATE=labels_date,
								   LABEL_NBCV=labels_nbcv,
								   CHOIX=choix,
								   ADRESS_INTERS=hada_Adresse,
								   ADRESS_NON_INTERS=hada_Adresse_non_inters,A=aaa,B=bbb,C=ccc,D=ddd,E=eee,F=fff,G=ggg,H=hhh,I=iii)

		elif choix == "op2":
			# hna aykhsni n remplacih bkmala t programme  ----
			aaa,bbb,ccc,ddd,eee,fff,ggg,hhh,iii = CSMS.Choix_skills_Model_Spacy(mypath, key)
			choix = 2
			df = pd.read_csv('./Choix_skills_Model_Spacy/Inters.csv')
			df_non_inters = pd.read_csv('./Choix_skills_Model_Spacy/Non_Inters.csv')
			# petite vérification
			if df.empty:
				Inters_vide = 1
			else:
				Inters_vide = 0
			if df_non_inters.empty:
				Non_Inters_vide = 1
			else:
				Non_Inters_vide = 0

			kolchi_Inters = []
			for a, b, c, d, e, f, g, h, i in zip(df['NAME'], df['EMAIL'], df['MOBILE'], df['DOMAIN1'], df['DOMAIN2'],
													df['DOMAIN3'], df['SEXE'], df['AGE'], df['Etas']):
				kolchi_Inters.append(a)
				kolchi_Inters.append(b)
				kolchi_Inters.append(c)
				kolchi_Inters.append(d)
				kolchi_Inters.append(e)
				kolchi_Inters.append(f)
				kolchi_Inters.append(g)
				kolchi_Inters.append(h)
				kolchi_Inters.append(i)


			hada_lskills = []
			for list in df['SKILLS']:
				list = str(list)
				hada_lskills.append('.')
				hada_lskills.append(list)
				for i in range(0, 7):
					hada_lskills.append('.')

			hada_Adresse = []
			for list in df['ADRESS']:
				list = str(list)
				hada_Adresse.append('.')
				hada_Adresse.append(list)
				for i in range(0, 7):
					hada_Adresse.append('.')

			hada_projet = []
			for list in df['Projet']:
				list = str(list)
				hada_projet.append('.')
				hada_projet.append(list)
				for i in range(0, 7):
					hada_projet.append('.')

			hada_langue = []
			for list in df['Langue']:
				list = str(list)
				hada_langue.append('.')
				hada_langue.append(list)
				for i in range(0, 7):
					hada_langue.append('.')

			kolchi_Non_Inters = []
			for a, b, c, d, e, f, g, h, i in zip(df_non_inters['NAME'], df_non_inters['EMAIL'],
													df_non_inters['MOBILE'], df_non_inters['DOMAIN1'],
													df_non_inters['DOMAIN2'], df_non_inters['DOMAIN3'],
													df_non_inters['SEXE'], df_non_inters['AGE'], df_non_inters['Etas']):
				kolchi_Non_Inters.append(a)
				kolchi_Non_Inters.append(b)
				kolchi_Non_Inters.append(c)
				kolchi_Non_Inters.append(d)
				kolchi_Non_Inters.append(e)
				kolchi_Non_Inters.append(f)
				kolchi_Non_Inters.append(g)
				kolchi_Non_Inters.append(h)
				kolchi_Non_Inters.append(i)


			hada_lskills_non_inters = []
			for list in df_non_inters['SKILLS']:
				list = str(list)
				hada_lskills_non_inters.append('.')
				hada_lskills_non_inters.append(list)
				for i in range(0, 7):
					hada_lskills_non_inters.append('.')

			hada_Adresse_non_inters = []
			for list in df_non_inters['ADRESS']:
				list = str(list)
				hada_Adresse_non_inters.append('.')
				hada_Adresse_non_inters.append(list)
				for i in range(0, 7):
					hada_Adresse_non_inters.append('.')

			hada_projet_non_inters = []
			for list in df_non_inters['Projet']:
				list = str(list)
				hada_projet_non_inters.append('.')
				hada_projet_non_inters.append(list)
				for i in range(0, 7):
					hada_projet_non_inters.append('.')

			hada_langue_non_inters = []
			for list in df_non_inters['Langue']:
				list = str(list)
				hada_langue_non_inters.append('.')
				hada_langue_non_inters.append(list)
				for i in range(0, 7):
					hada_langue_non_inters.append('.')
			# hna nbda n7ma9 fm3a plot

			label_nom = []
			label_age = []
			for kok in df['NAME']:
				label_nom.append(kok)
			labels_nom = json.dumps(label_nom)
			for kok in df['AGE']:
				label_age.append(kok)
			labels_age = json.dumps(label_age)

			# fin nta3 choix

			# hna kan suprimiw uploid bache ikhwa l9ne

			mypath = './uploade'
			onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
			for a in onlyfiles:
				os.remove(a)

			# hna dakchi t char
			df_hist = pd.read_csv("./hist.csv")
			label_date = []
			label_nbcv = []
			for a in df_hist['DATE']:
				label_date.append(a)
			labels_date = json.dumps(label_date)
			for a in df_hist['NBCV']:
				label_nbcv.append(a)
			labels_nbcv = json.dumps(label_nbcv)

			# ila kolchi howa hadak rj3 lih pagge résultat
			return render_template("Resultat_Skills.html",
								   SKILLS_INTERS=hada_lskills,
								   KOLCHI_INTERS=kolchi_Inters,
								   SKILLS_NON_INTERS=hada_lskills_non_inters,
								   KOLCHI_NON_INTERS=kolchi_Non_Inters,
								   LABEL_NOM=labels_nom,
								   LABEL_AGE=labels_age,
								   LABEL_DATE=labels_date,
								   LABEL_NBCV=labels_nbcv,
								   CHOIX=choix,
								   PROJET_INTERS=hada_projet,
								   LANGUE_INTERS=hada_langue,
								   PROJET_NON_INTERS=hada_projet_non_inters,
								   LANGUE_NON_INTERS=hada_langue_non_inters,
								   ADRESS_INTERS=hada_Adresse,
								   ADRESS_NON_INTERS=hada_Adresse_non_inters,A=aaa,B=bbb,C=ccc,D=ddd,E=eee,F=fff,G=ggg,H=hhh,I=iii)

#---------------------------------------------------------------------
#hna lchoix domain
# had page l controle
@app.route('/Choix_Domain')
def erreur_404_Domain():
	return render_template("404.html")

@app.route('/Choix_Domain',methods=["GET","POST"])
def process_Domain():
	if request.method == 'POST':
		if len(os.listdir('./uploade')) == 0:
			return render_template("index.html", erreur=1)
		# hna kanhze domain mn l page html
		domain1 = request.form['domain1']
		domain2 = request.form['domain2']
		domain3 = request.form['domain3']
		choix  = request.form['Rad']
		mypath = './Extraire'
		# hna nhze domain f recherche
		#print(domain1+"/"+domain2+"/"+domain3)
		# key fiha daba les mots khsni nzide ta domain
		if choix == "op1":
			aaa,bbb,ccc,ddd,eee,fff,ggg,hhh,iii,jjj,kkk,lll = CDNM.Choix_Domain_Notre_Model(mypath,domain1,domain2,domain3)
			choix = 1
			d1 = pd.read_csv('./Choix_Domain_Notre_Model/Domain1.csv')
			d2 = pd.read_csv('./Choix_Domain_Notre_Model/Domain2.csv')
			d3 = pd.read_csv('./Choix_Domain_Notre_Model/Domain3.csv')
			d4 = pd.read_csv('./Choix_Domain_Notre_Model/Domain4.csv')

			# petite vérification miwamiwa hinhinhinhinhinhinhin
			if d1.empty and d2.empty and d3.empty and d4.empty :
				cont_vide = 1
			else:
				cont_vide = 0

			kolchi_d1 = []
			for a,b,c,d,e,f,g,h,i in zip(d1['NAME'],d1['EMAIL'],d1['MOBILE'],d1['DOMAIN1'],d1['DOMAIN2'],d1['DOMAIN3'],d1['SEXE'],d1['AGE'],d1['Etas']):
				kolchi_d1.append(a)
				kolchi_d1.append(b)
				kolchi_d1.append(c)
				kolchi_d1.append(d)
				kolchi_d1.append(e)
				kolchi_d1.append(f)
				kolchi_d1.append(g)
				kolchi_d1.append(h)
				kolchi_d1.append(i)


			d1_skills = []
			for list in d1['SKILLS']:
				list = str(list)
				d1_skills.append('.')
				d1_skills.append(list)
				for i in range(0,7):
					d1_skills.append('.')

			d1_Adresse = []
			for list in d1['ADRESS']:
				list = str(list)
				d1_Adresse.append('.')
				d1_Adresse.append(list)
				for i in range(0, 7):
					d1_Adresse.append('.')

			kolchi_d2 = []
			for a, b, c, d, e, f, g, h, i in zip(d2['NAME'], d2['EMAIL'], d2['MOBILE'], d2['DOMAIN1'], d2['DOMAIN2'],
												 d2['DOMAIN3'], d2['SEXE'], d2['AGE'], d2['Etas']):
				kolchi_d2.append(a)
				kolchi_d2.append(b)
				kolchi_d2.append(c)
				kolchi_d2.append(d)
				kolchi_d2.append(e)
				kolchi_d2.append(f)
				kolchi_d2.append(g)
				kolchi_d2.append(h)
				kolchi_d2.append(i)

			d2_skills = []
			for list in d2['SKILLS']:
				list = str(list)
				d2_skills.append('.')
				d2_skills.append(list)
				for i in range(0, 7):
					d2_skills.append('.')

			d2_Adresse = []
			for list in d2['ADRESS']:
				list = str(list)
				d2_Adresse.append('.')
				d2_Adresse.append(list)
				for i in range(0, 7):
					d2_Adresse.append('.')

			kolchi_d3 = []
			for a, b, c, d, e, f, g, h, i in zip(d3['NAME'], d3['EMAIL'], d3['MOBILE'], d3['DOMAIN1'], d3['DOMAIN2'],
												 d3['DOMAIN3'], d3['SEXE'], d3['AGE'], d3['Etas']):
				kolchi_d3.append(a)
				kolchi_d3.append(b)
				kolchi_d3.append(c)
				kolchi_d3.append(d)
				kolchi_d3.append(e)
				kolchi_d3.append(f)
				kolchi_d3.append(g)
				kolchi_d3.append(h)
				kolchi_d3.append(i)

			d3_skills = []
			for list in d3['SKILLS']:
				list = str(list)
				d3_skills.append('.')
				d3_skills.append(list)
				for i in range(0, 7):
					d3_skills.append('.')

			d3_Adresse = []
			for list in d3['ADRESS']:
				list = str(list)
				d3_Adresse.append('.')
				d3_Adresse.append(list)
				for i in range(0, 7):
					d3_Adresse.append('.')

			kolchi_d4 = []
			for a, b, c, d, e, f, g, h, i in zip(d4['NAME'], d4['EMAIL'], d4['MOBILE'], d4['DOMAIN1'], d4['DOMAIN2'],
												 d4['DOMAIN3'], d4['SEXE'], d4['AGE'], d4['Etas']):
				kolchi_d4.append(a)
				kolchi_d4.append(b)
				kolchi_d4.append(c)
				kolchi_d4.append(d)
				kolchi_d4.append(e)
				kolchi_d4.append(f)
				kolchi_d4.append(g)
				kolchi_d4.append(h)
				kolchi_d4.append(i)

			d4_skills = []
			for list in d4['SKILLS']:
				list = str(list)
				d4_skills.append('.')
				d4_skills.append(list)
				for i in range(0, 7):
					d4_skills.append('.')

			d4_Adresse = []
			for list in d4['ADRESS']:
				list = str(list)
				d4_Adresse.append('.')
				d4_Adresse.append(list)
				for i in range(0, 7):
					d4_Adresse.append('.')



			# hna nbda n7ma9 fm3a plot

			label_nom=[]
			label_age=[]
			for a,b,c,d  in zip(d1['NAME'],d2['NAME'],d3['NAME'],d4['NAME']):
				label_nom.append(a)
				label_nom.append(b)
				label_nom.append(c)
				label_nom.append(d)
			labels_nom = json.dumps( label_nom )
			for a,b,c,d  in zip(d1['AGE'],d2['AGE'],d3['AGE'],d4['AGE']):
				label_age.append(a)
				label_age.append(b)
				label_age.append(c)
				label_age.append(d)
			labels_age = json.dumps( label_age )

			# fin nta3 choix

			# hna kan suprimiw uploid bache ikhwa l9ne

			mypath = './uploade'
			onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
			for a in onlyfiles:
				os.remove(a)

			# hna dakchi t char
			df_hist = pd.read_csv("./hist.csv")
			label_date = []
			label_nbcv = []
			for a in df_hist['DATE']:
				label_date.append(a)
			labels_date = json.dumps(label_date)
			for a in df_hist['NBCV']:
				label_nbcv.append(a)
			labels_nbcv = json.dumps(label_nbcv)

			# ila kolchi howa hadak rj3 lih pagge résultat
			return render_template("Resultat_Domain.html",
								   LABEL_NOM=labels_nom,
								   LABEL_AGE=labels_age,
								   LABEL_DATE=labels_date,
								   LABEL_NBCV=labels_nbcv,
								   CHOIX=choix,
								   KOLCHI_D1 = kolchi_d1,
								   SKILLS_D1 = d1_skills,
								   ADRESS_D1 = d1_Adresse,
								   KOLCHI_D2=kolchi_d2,
								   SKILLS_D2=d2_skills,
								   ADRESS_D2=d2_Adresse,
								   KOLCHI_D3=kolchi_d3,
								   SKILLS_D3=d3_skills,
								   ADRESS_D3=d3_Adresse,
								   KOLCHI_D4=kolchi_d4,
								   SKILLS_D4=d4_skills,
								   ADRESS_D4=d4_Adresse,A=aaa,B=bbb,C=ccc,D=ddd,E=eee,F=fff,G=ggg,H=hhh,I=iii,J=jjj,K=kkk,L=lll)

		elif choix == "op2":
			aaa,bbb,ccc,ddd,eee,fff,ggg,hhh,iii,jjj,kkk,lll = CDMS.Choix_Domain_Model_Spacy(mypath,domain1,domain2,domain3)
			choix = 2
			d1 = pd.read_csv('./Choix_Domain_Model_Spacy/Domain1.csv')
			d2 = pd.read_csv('./Choix_Domain_Model_Spacy/Domain2.csv')
			d3 = pd.read_csv('./Choix_Domain_Model_Spacy/Domain3.csv')
			d4 = pd.read_csv('./Choix_Domain_Model_Spacy/Domain4.csv')

			# petite vérification miwamiwa hinhinhinhinhinhinhin
			if d1.empty and d2.empty and d3.empty and d4.empty:
				cont_vide = 1
			else:
				cont_vide = 0

			kolchi_d1 = []
			for a, b, c, d, e, f, g, h, i in zip(d1['NAME'], d1['EMAIL'], d1['MOBILE'], d1['DOMAIN1'], d1['DOMAIN2'],
												 d1['DOMAIN3'], d1['SEXE'], d1['AGE'], d1['Etas']):
				kolchi_d1.append(a)
				kolchi_d1.append(b)
				kolchi_d1.append(c)
				kolchi_d1.append(d)
				kolchi_d1.append(e)
				kolchi_d1.append(f)
				kolchi_d1.append(g)
				kolchi_d1.append(h)
				kolchi_d1.append(i)

			d1_skills = []
			for list in d1['SKILLS']:
				list = str(list)
				d1_skills.append('.')
				d1_skills.append(list)
				for i in range(0, 7):
					d1_skills.append('.')

			d1_Adresse = []
			for list in d1['ADRESS']:
				list = str(list)
				d1_Adresse.append('.')
				d1_Adresse.append(list)
				for i in range(0, 7):
					d1_Adresse.append('.')

			d1_projet = []
			for list in d1['Projet']:
				list = str(list)
				d1_projet.append('.')
				d1_projet.append(list)
				for i in range(0, 7):
					d1_projet.append('.')

			d1_langue = []
			for list in d1['Langue']:
				list = str(list)
				d1_langue.append('.')
				d1_langue.append(list)
				for i in range(0, 7):
					d1_langue.append('.')

			kolchi_d2 = []
			for a, b, c, d, e, f, g, h, i in zip(d2['NAME'], d2['EMAIL'], d2['MOBILE'], d2['DOMAIN1'], d2['DOMAIN2'],
												 d2['DOMAIN3'], d2['SEXE'], d2['AGE'], d2['Etas']):
				kolchi_d2.append(a)
				kolchi_d2.append(b)
				kolchi_d2.append(c)
				kolchi_d2.append(d)
				kolchi_d2.append(e)
				kolchi_d2.append(f)
				kolchi_d2.append(g)
				kolchi_d2.append(h)
				kolchi_d2.append(i)

			d2_skills = []
			for list in d2['SKILLS']:
				list = str(list)
				d2_skills.append('.')
				d2_skills.append(list)
				for i in range(0, 7):
					d2_skills.append('.')

			d2_Adresse = []
			for list in d2['ADRESS']:
				list = str(list)
				d2_Adresse.append('.')
				d2_Adresse.append(list)
				for i in range(0, 7):
					d2_Adresse.append('.')

			d2_projet = []
			for list in d2['Projet']:
				list = str(list)
				d2_projet.append('.')
				d2_projet.append(list)
				for i in range(0, 7):
					d2_projet.append('.')

			d2_langue = []
			for list in d2['Langue']:
				list = str(list)
				d2_langue.append('.')
				d2_langue.append(list)
				for i in range(0, 7):
					d2_langue.append('.')

			kolchi_d3 = []
			for a, b, c, d, e, f, g, h, i in zip(d3['NAME'], d3['EMAIL'], d3['MOBILE'], d3['DOMAIN1'], d3['DOMAIN2'],
												 d3['DOMAIN3'], d3['SEXE'], d3['AGE'], d3['Etas']):
				kolchi_d3.append(a)
				kolchi_d3.append(b)
				kolchi_d3.append(c)
				kolchi_d3.append(d)
				kolchi_d3.append(e)
				kolchi_d3.append(f)
				kolchi_d3.append(g)
				kolchi_d3.append(h)
				kolchi_d3.append(i)

			d3_skills = []
			for list in d3['SKILLS']:
				list = str(list)
				d3_skills.append('.')
				d3_skills.append(list)
				for i in range(0, 7):
					d3_skills.append('.')

			d3_Adresse = []
			for list in d3['ADRESS']:
				list = str(list)
				d3_Adresse.append('.')
				d3_Adresse.append(list)
				for i in range(0, 7):
					d3_Adresse.append('.')

			d3_projet = []
			for list in d3['Projet']:
				list = str(list)
				d3_projet.append('.')
				d3_projet.append(list)
				for i in range(0, 7):
					d3_projet.append('.')

			d3_langue = []
			for list in d3['Langue']:
				list = str(list)
				d3_langue.append('.')
				d3_langue.append(list)
				for i in range(0, 7):
					d3_langue.append('.')

			kolchi_d4 = []
			for a, b, c, d, e, f, g, h, i in zip(d4['NAME'], d4['EMAIL'], d4['MOBILE'], d4['DOMAIN1'], d4['DOMAIN2'],
												 d4['DOMAIN3'], d4['SEXE'], d4['AGE'], d4['Etas']):
				kolchi_d4.append(a)
				kolchi_d4.append(b)
				kolchi_d4.append(c)
				kolchi_d4.append(d)
				kolchi_d4.append(e)
				kolchi_d4.append(f)
				kolchi_d4.append(g)
				kolchi_d4.append(h)
				kolchi_d4.append(i)

			d4_skills = []
			for list in d4['SKILLS']:
				list = str(list)
				d4_skills.append('.')
				d4_skills.append(list)
				for i in range(0, 7):
					d4_skills.append('.')

			d4_Adresse = []
			for list in d4['ADRESS']:
				list = str(list)
				d4_Adresse.append('.')
				d4_Adresse.append(list)
				for i in range(0, 7):
					d4_Adresse.append('.')

			d4_projet = []
			for list in d4['Projet']:
				list = str(list)
				d4_projet.append('.')
				d4_projet.append(list)
				for i in range(0, 7):
					d4_projet.append('.')

			d4_langue = []
			for list in d4['Langue']:
				list = str(list)
				d4_langue.append('.')
				d4_langue.append(list)
				for i in range(0, 7):
					d4_langue.append('.')

			# hna nbda n7ma9 fm3a plot

			label_nom = []
			label_age = []
			for a, b, c, d in zip(d1['NAME'], d2['NAME'], d3['NAME'], d4['NAME']):
				label_nom.append(a)
				label_nom.append(b)
				label_nom.append(c)
				label_nom.append(d)
			labels_nom = json.dumps(label_nom)
			for a, b, c, d in zip(d1['AGE'], d2['AGE'], d3['AGE'], d4['AGE']):
				label_age.append(a)
				label_age.append(b)
				label_age.append(c)
				label_age.append(d)
			labels_age = json.dumps(label_age)

			# fin nta3 choix

			# hna kan suprimiw uploid bache ikhwa l9ne

			mypath = './uploade'
			onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
			for a in onlyfiles:
				os.remove(a)

			# hna dakchi t char
			df_hist = pd.read_csv("./hist.csv")
			label_date = []
			label_nbcv = []
			for a in df_hist['DATE']:
				label_date.append(a)
			labels_date = json.dumps(label_date)
			for a in df_hist['NBCV']:
				label_nbcv.append(a)
			labels_nbcv = json.dumps(label_nbcv)

			# ila kolchi howa hadak rj3 lih pagge résultat
			return render_template("Resultat_Domain.html",
								   LABEL_NOM=labels_nom,
								   LABEL_AGE=labels_age,
								   LABEL_DATE=labels_date,
								   LABEL_NBCV=labels_nbcv,
								   CHOIX=choix,
								   KOLCHI_D1=kolchi_d1,
								   SKILLS_D1=d1_skills,
								   ADRESS_D1=d1_Adresse,
								   PROJET_D1=d1_projet,
								   LANGUE_D1=d1_langue,
								   KOLCHI_D2=kolchi_d2,
								   SKILLS_D2=d2_skills,
								   ADRESS_D2=d2_Adresse,
								   PROJET_D2=d2_projet,
								   LANGUE_D2=d2_langue,
								   KOLCHI_D3=kolchi_d3,
								   SKILLS_D3=d3_skills,
								   ADRESS_D3=d3_Adresse,
								   PROJET_D3=d3_projet,
								   LANGUE_D3=d3_langue,
								   KOLCHI_D4=kolchi_d4,
								   SKILLS_D4=d4_skills,
								   ADRESS_D4=d4_Adresse,
								   PROJET_D4=d4_projet,
								   LANGUE_D4=d4_langue,A=aaa,B=bbb,C=ccc,D=ddd,E=eee,F=fff,G=ggg,H=hhh,I=iii,J=jjj,K=kkk,L=lll
								   )
#---------------------------------------------------------------------
#hna lchoix cluster
# had page l controle
@app.route('/Choix_Cluster')
def erreur_404_Cluster():
	return render_template("404.html")

@app.route('/Choix_Cluster',methods=["GET","POST"])
def process_Cluster():
	if request.method == 'POST':
		if len(os.listdir('./uploade')) == 0:
			return render_template("index.html", erreur=1)
		# hna kanhze domain mn l page html
		cluster = request.form['cluster']
		choix  = request.form['Rad']
		cluster = int(cluster)
		mypath = './Extraire'
		if choix == "op1":
			aaa,bbb,ccc,ddd,eee,fff = CCNM.Choix_Cluster_Notre_Model(mypath,K_cluster=cluster)
			choix = 1
			Clu = pd.read_csv('./Choix_Cluster_Notre_Model/Cluster.csv')
			# petite vérification miwamiwa hinhinhinhinhinhinhin
			if Clu.empty:
				cont_vide = 1
			else:
				cont_vide = 0

			kolchi_Clu = []
			for a,b,c,d,e,f,g,h,i in zip(Clu['NAME'],Clu['EMAIL'],Clu['MOBILE'],Clu['SEXE'],Clu['AGE'],Clu['DOMAIN1'],Clu['Sim_Dom'],Clu['Cluster'],Clu['Sim_Clu']):
				kolchi_Clu.append(a)
				kolchi_Clu.append(b)
				kolchi_Clu.append(c)
				kolchi_Clu.append(d)
				kolchi_Clu.append(e)
				kolchi_Clu.append(f)
				kolchi_Clu.append(g)
				kolchi_Clu.append(h)
				kolchi_Clu.append(i)


			Clu_skills = []
			for list in Clu['SKILLS']:
				list = str(list)
				Clu_skills.append('.')
				Clu_skills.append(list)
				for i in range(0,7):
					Clu_skills.append('.')

			Clu_Adresse = []
			for list in Clu['ADRESS']:
				list = str(list)
				Clu_Adresse.append('.')
				Clu_Adresse.append(list)
				for i in range(0, 7):
					Clu_Adresse.append('.')

			# hna nbda n7ma9 fm3a plot

			label_nom=[]
			label_age=[]
			for a in Clu['NAME']:
				label_nom.append(a)
			labels_nom = json.dumps( label_nom )
			for a in Clu['AGE']:
				label_age.append(a)
			labels_age = json.dumps( label_age )

			# fin nta3 choix

			# hna kan suprimiw uploid bache ikhwa l9ne

			mypath = './uploade'
			onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
			for a in onlyfiles:
				os.remove(a)

			# hna dakchi t char
			df_hist = pd.read_csv("./hist.csv")
			label_date = []
			label_nbcv = []
			for a in df_hist['DATE']:
				label_date.append(a)
			labels_date = json.dumps(label_date)
			for a in df_hist['NBCV']:
				label_nbcv.append(a)
			labels_nbcv = json.dumps(label_nbcv)

			# ila kolchi howa hadak rj3 lih pagge résultat
			return render_template("Resultat_Cluster.html",
								   LABEL_NOM=labels_nom,
								   LABEL_AGE=labels_age,
								   LABEL_DATE=labels_date,
								   LABEL_NBCV=labels_nbcv,
								   CHOIX=choix,
								   KOLCHI_CLU = kolchi_Clu,
								   SKILLS_CLU = Clu_skills,
								   ADRESS_CLU = Clu_Adresse,A=aaa,B=bbb,C=ccc,D=ddd,E=eee,F=fff)

		elif choix == "op2":
			aaa,bbb,ccc,ddd,eee,fff = CCMS.Choix_Cluster_Model_Spacy(mypath,K_cluster=cluster)
			choix = 2
			Clu = pd.read_csv('./Choix_Cluster_Model_Spacy/Cluster.csv')

			# petite vérification miwamiwa hinhinhinhinhinhinhin
			if Clu.empty:
				cont_vide = 1
			else:
				cont_vide = 0

			kolchi_Clu = []
			for a, b, c, d, e, f, g, h, i in zip(Clu['NAME'], Clu['EMAIL'], Clu['MOBILE'], Clu['SEXE'], Clu['AGE'],
												 Clu['DOMAIN1'], Clu['Sim_Dom'], Clu['Cluster'], Clu['Sim_Clu']):
				kolchi_Clu.append(a)
				kolchi_Clu.append(b)
				kolchi_Clu.append(c)
				kolchi_Clu.append(d)
				kolchi_Clu.append(e)
				kolchi_Clu.append(f)
				kolchi_Clu.append(g)
				kolchi_Clu.append(h)
				kolchi_Clu.append(i)

			Clu_skills = []
			for list in Clu['SKILLS']:
				list = str(list)
				Clu_skills.append('.')
				Clu_skills.append(list)
				for i in range(0, 7):
					Clu_skills.append('.')

			Clu_Adresse = []
			for list in Clu['ADRESS']:
				list = str(list)
				Clu_Adresse.append('.')
				Clu_Adresse.append(list)
				for i in range(0, 7):
					Clu_Adresse.append('.')

			Clu_projet = []
			for list in Clu['Projet']:
				list = str(list)
				Clu_projet.append('.')
				Clu_projet.append(list)
				for i in range(0, 7):
					Clu_projet.append('.')

			Clu_langue = []
			for list in Clu['Langue']:
				list = str(list)
				Clu_langue.append('.')
				Clu_langue.append(list)
				for i in range(0, 7):
					Clu_langue.append('.')


			# hna nbda n7ma9 fm3a plot

			label_nom = []
			label_age = []
			for a in Clu['NAME']:
				label_nom.append(a)
			labels_nom = json.dumps(label_nom)
			for a in Clu['AGE']:
				label_age.append(a)
			labels_age = json.dumps(label_age)

			# fin nta3 choix

			# hna kan suprimiw uploid bache ikhwa l9ne

			mypath = './uploade'
			onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
			for a in onlyfiles:
				os.remove(a)

			# hna dakchi t char
			df_hist = pd.read_csv("./hist.csv")
			label_date = []
			label_nbcv = []
			for a in df_hist['DATE']:
				label_date.append(a)
			labels_date = json.dumps(label_date)
			for a in df_hist['NBCV']:
				label_nbcv.append(a)
			labels_nbcv = json.dumps(label_nbcv)

			# ila kolchi howa hadak rj3 lih pagge résultat
			return render_template("Resultat_Cluster.html",
								   LABEL_NOM=labels_nom,
								   LABEL_AGE=labels_age,
								   LABEL_DATE=labels_date,
								   LABEL_NBCV=labels_nbcv,
								   CHOIX=choix,
								   KOLCHI_CLU=kolchi_Clu,
								   SKILLS_CLU=Clu_skills,
								   ADRESS_CLU=Clu_Adresse,
								   PROJET_CLU=Clu_projet,
								   LANGUE_CLU=Clu_langue,A=aaa,B=bbb,C=ccc,D=ddd,E=eee,F=fff)
#---------------------------------------------------------------------

#had page l téléchargment t rapport
@app.route('/RapportCv/<path:filename>')
def custom_static(filename):
    return send_from_directory('./RapportCv', filename)

#---------------------------------------------------------------------
# ohan lmain hahahha
if __name__ == '__main__':
	app.run(debug=True , port= 2020)

