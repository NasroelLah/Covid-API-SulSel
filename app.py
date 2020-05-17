import flask
from flask import request, jsonify

app = flask.Flask(__name__)
import json
import requests as req
import re
import ssl
import certifi
from bs4 import BeautifulSoup
import urllib.request as urllib3
ssl._create_default_https_context = ssl._create_unverified_context

page = urllib3.urlopen('https://covid19.sulselprov.go.id/')
soup = BeautifulSoup(page, 'html.parser')

name_box = soup.findAll('h4', attrs={'class':'text-danger'})
cleaner = re.compile('<.*?>')
waktu = []
for a in name_box:
    clean = re.sub(cleaner, '', str(a))
    waktu.append(clean.strip())

name_box = soup.findAll('span', attrs={'style':'display: inline-block; line-height:1; font-size: 100px; font-weight:bold; margin:0px'})
cleaner = re.compile('<.*?>')
angkaBig = []
for a in name_box:
    clean = re.sub(cleaner, '', str(a))
    angkaBig.append(clean.strip())

name_box = soup.findAll('span', attrs={'style':'font-size: 18px'})
cleaner = re.compile('<.*?>')
angkaSmall = []
for a in name_box:
    clean = re.sub(cleaner, '', str(a))
    angkaSmall.append(clean.strip())

name_box = soup.findAll('span', attrs={'style':'font-size: 16px'})
cleaner = re.compile('<.*?>')
angkaSmalll = []
for a in name_box:
    clean = re.sub(cleaner, '', str(a))
    angkaSmalll.append(clean.strip())

odp = angkaBig[0]
odp1 = angkaSmall[0].split(" ")
odp2 = angkaSmall[1].split(" ")
pdp = angkaBig[1]
pdp2 = angkaSmall[2].split(" ")
pdp3 = angkaSmall[3].split(" ")
positif = angkaBig[2]
isolasi1 = angkaSmall[4]
isolasi2 = angkaSmall[5]
pos1 = angkaSmall[6]
pos2 = angkaSmall[7].split(" ")
pos3 = angkaSmall[8].split(" ")

data = {'odp':odp, 'tOdp':odp1[0], 'sOdp':odp2[0], 'pdp':pdp, 'tPdp':angkaSmalll[0], 'nPdp':pdp2[0], 'mPdp':pdp3[0], 'positif':positif, 'tPos':pos1, 'mIso':isolasi1, 'rIso':isolasi2, 'sembuh':pos2[0], 'die':pos3[0]}

@app.route('/', methods=['GET'])
def home():
    return jsonify(data)
app.run()