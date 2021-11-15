# coding: utf-8

#-----------------------------------------------------------------------------
# Name:		  function.py
# Purpose:	  Automatic CV/Resumé analysis Using Natural Language Processing
#
# Author:	  ana hhhhhh ... maty9touch ????
#
# Created:	  February 2020
# Version:	  mohim kansayi tayjib lah version final
# dyalmn :	  gte likom ma3tah liya ta7de


from zipfile import ZipFile
from flask import Flask, request , redirect , url_for , render_template


app = Flask(__name__, instance_relative_config=True)
app.config["ALLOWED_FILE_EXTENSIONS"] = ["ZIP"]
app.config["MAX_FILE_FILESIZE"] = 200 * 1024 * 1024



def Extract(path):
    file_name = path
    with ZipFile(file_name, 'r') as zipe:
        zipe.extractall(path='./Extraire')

#-----------------------------------------------------------------


def allowed_file(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False

#-----------------------------------------------------------------

def allowed_file_filesize(filesize):

    if int(filesize) <= app.config["MAX_FILE_FILESIZE"]:
        return True
    else:
        return False


#------------------------------------------------------------------

def nom_fichier(name):
    return name[:-4]