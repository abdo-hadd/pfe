
from __future__ import unicode_literals
from __future__ import print_function
import re
import plac
import random
from pathlib import Path
import spacy
import json
import logging


LABEL = "COL_NAME"




def trim_entity_spans(data: list) -> list:
    invalid_span_tokens = re.compile(r'\s')

    cleaned_data = []
    for text, annotations in data:
        entities = annotations['entities']
        valid_entities = []
        for start, end, label in entities:
            valid_start = start
            valid_end = end
            while valid_start < len(text) and invalid_span_tokens.match(
                    text[valid_start]):
                valid_start += 1
            while valid_end > 1 and invalid_span_tokens.match(
                    text[valid_end - 1]):
                valid_end -= 1
            valid_entities.append([valid_start, valid_end, label])
        cleaned_data.append([text, {'entities': valid_entities}])

    return cleaned_data


def convert_dataturks_to_spacy(dataturks_JSON_FilePath):
    try:
        training_data = []
        lines = []
        with open(dataturks_JSON_FilePath, 'r', encoding="utf8") as f:
            lines = f.readlines()

        for line in lines:
            data = json.loads(line)
            text = data['content']
            entities = []
            if data['annotation'] is not None:
                for annotation in data['annotation']:
                    # only a single point in text annotation.
                    point = annotation['points'][0]
                    labels = annotation['label']
                    # handle both list of labels or a single label.
                    if not isinstance(labels, list):
                        labels = [labels]

                    for label in labels:
                        # dataturks indices are both inclusive [start, end]
                        # but spacy is not [start, end)
                        entities.append((
                            point['start'],
                            point['end'] + 1,
                            label
                        ))

            training_data.append((text, {"entities": entities}))
        return training_data
    except Exception:
        logging.exception("Unable to process " + dataturks_JSON_FilePath)
        return None

#Four-Loco
TRAIN_DATA= trim_entity_spans(convert_dataturks_to_spacy("./JsonTraine/data1.json"))
#TRAIN_DATA = []
#for a in range(0,24):
    #TRAIN_DATA.append(TRAIN_DATAA[a])

@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int),
)
def main(
    model=None,
    new_model_name="training",
    output_dir='./',
    n_iter=30
):
    
    random.seed(0)
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank("en")  # create blank Language class
        print("Created blank 'en' model")
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy

    if "ner" not in nlp.pipe_names:
        print("Creating new pipe")
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner, last=True)

    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe("ner")

    # add labels
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    # if model is None or reset_weights:
    #     optimizer = nlp.begin_training()
    # else:
    #     optimizer = nlp.resume_training()
    move_names = list(ner.move_names)
    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        # batch up the examples using spaCy's minibatch
        for itn in range(n_iter):
            print("Starting iteration " + str(itn))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update(
                    [text],  # batch of texts
                    [annotations],  # batch of annotations
                    drop=0.2,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            print("Losses", losses)

    # test the trained model
    print("\n\n")
    test_text = """Lahcen ELMOUDNI\nBorn: 10/09/1996\nTel: +212 6 20 96 54 52\nEmail: elmoudni.lehcen.mp@gmail.com\nLinkedIn: linkedin.com/in/lahcenelmoudni\n204a77150\nState Engineering-Engineering\nOf Industrial Processes\nAbout me :\nQuick adaptation, total mobility, hardworking,\nautonomous worker, I want to invest\nmy theoretical and practical knowledge\nin favor of an innovative company in order\nexpand my interpersonal and\ndeveloping my knowledge\nACADEMIC TRAINING\n2016/2019: Cycle State Engineer, Process Engineering Industrial, Mohammadia School of Engineers, Rabat\n2014/2016: Preparatory classes for engineering schools MPSI / MP, center Mohammed V, Casablanca\nJune 2014: Bachelor of Mathematical Sciences A class honors, Lycée Hassan II, Casablanca\nPROFESSIONAL EXPERIENCES\nFebruary-June 2019: Project Graduation at AKWA GROUP-Pole fuel and lubricant, Casablanca\nSubject: Improving energy efficiency in the industrial site and within SALUB\nAFRIQUIA service stations.\n- Data analysis of energy consumption and production on the site SALUB.\n- Diagnosis of energy-intensive facilities.\n- Proposal and project business case for improvement of energy performance.\n- Design of a wash water recycling station in service stations\n- Design of a photovoltaic park to meet the need of electricity to the station\nrecycling, and part of the need of the service station.\nAugust 2018: Engineer Internship at OCP Jorf Lasfar JFC-IV\nTopic: Optimizing the quality of production performance DAP EURO workshop production of fertilizers.\nJuly 2018: Training engineer at the SNEP, Mohammedia.\nSubject: Evaluation of the efficiency of the boiler with water pipes and proposal of improvement actions\nJuly 2017: Introductory course to COSUMAR-refinery Casablanca.\nSubject: Energy balance and study of the evaporation station.\nACADEMIC KNOWLEDGE\nmanagerial strengths:\n Analysis and Project Management\n Production management and maintenance\n General and analytical compatibility\n Security management and industrial risks\n(Standards ISO 45001 and OHSAS 18001).\n Environmental management (ISO 14001)\n Quality Management (ISO 9001)\nComputer skills :\n Office: Microsoft Office (PowerPoint, Word,\nExcel, Visio)\n Programming: Python, SQL, Visual Basic\n Software: Aspen Plus, Ansys, Statgraphics, Catia, Matlab,\nDwsim, Retscreen, PVsyst, Hint, CES\nFINALISED PROJECT\nTechnical skills :\n Unit operations\n Energetic efficiency\n Mass transfer and heat\n Analysis of balance sheets\n Modeling, simulation and optimization of processes\n Calculation of reactors and\nheat exchangers\n Engineering Chemistry\n Dynamics and Control processes\n Water treatment\n Hydraulic machines\n Fluid mechanics\n Energy Integration\n Basic Electronics and electrical engineering.\n Plant Project: Design of the recovery boiler of a production unit of a maleic anhydride\ncapacity of 5000 t / year.\n Design of a seawater treatment plant using reverse osmosis.\n Sizing and technical and economic evaluation of an absorption column.\n Valorisation of lignocellulosic biomass to bioethanol: implementation of the process of investment and calculation\nprofitability.\n Selection of the material of the tubes of a heat exchanger.\nLANGUAGE SKILLS\nArab / Amazigh: Native languages ??French: Fluent English: Good level\nVARIOUS\n Teacher tutoring in mathematics.\n Extracurricular Activities: cell leader workshops cultural club EMINENCE.\n Military training: Reserve officer of the Royal Armed Forces.\n Entertainment: Latest news, football, travel\nState Engineer - Engineering Of\nIndustrial processes\nAbout me :\nQuick adaptation, total mobility, hardworking,\nautonomous worker, I want to invest\nmy knowledge and skills to\nadvantage of an innovative company in order\nexpand my interpersonal and\ndeveloping my technical knowledge.\nLahcen ELMOUDNI\nBorn: 10/09/1996 (23 years)\nAddress: Lamkanssa 5 Block B Street 22 No. 12 Ain Chok, Casablanca\nTel: +212 6 20 96 54 52\nEmail: lahcen.elmoudni96@gmail.com\nLinkedIn: linkedin.com/in/lahcenelmoudni204a77150\nmailto: abdennacersabri@gmail.com\nmailto: lahcen.elmoudni96@gmail.com\n"""

    doc = nlp(test_text)
    #print("Entities in '%s'" % test_text)
    for ent in doc.ents:
        print(ent.label_, ent.text)

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta["name"] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
"""print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        # Check the classes have loaded back consistently
        assert nlp2.get_pipe("ner").move_names == move_names
        doc2 = nlp2(test_text)
        for ent in doc2.ents:
            print(ent.label_, ent.text)"""



main(model='./hna',
    new_model_name="training",
    output_dir='./hna',
    n_iter=30)
