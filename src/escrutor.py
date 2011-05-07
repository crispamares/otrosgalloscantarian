# -*- coding: utf-8 -*-

import csv
import sys
from model import *

COMUNIDAD = 0
PROVINCIA = 2
MUNICIPIO = 4
POBLACION = 5
CENSOTOTAL = 7
VOTOSTOTALES = 8
VOTOSVALIDOS = 9
VOTOSCANDIDATURA = 10
VOTOSBLANCO = 11
VOTOSNULO = 12


def LoadFile(filepath):
    voteReader = csv.reader(open(filepath,'rb'),delimiter=",")
    # Cargar todos los partidos existentes y asociarlos con su numero de col
    voteReader.next()
    voteReader.next()
    voteReader.next()
    voteReader.next()
    nombres = voteReader.next()
    siglas = voteReader.next()
    partidos = {}
    for sigla in siglas[13:]:
        id = siglas.index(sigla)
        partidos[id] = (nombres[id],sigla)

    for row in voteReader:
        censo = CensoElectoral()
        i = filepath.find('/')
        censo.ano = filepath[i+1:i+5]
        censo.comunidad = row[COMUNIDAD].strip()
        censo.provincia = row[PROVINCIA].strip()
        censo.municipio = row[MUNICIPIO].strip()
        censo.censoTotal = row[CENSOTOTAL].strip()
        censo.votosTotales = row[VOTOSTOTALES].strip()
        censo.votosValidos = row[VOTOSVALIDOS].strip()
        censo.votosCandidatura = row[VOTOSCANDIDATURA].strip()
        censo.votosBlanco = row[VOTOSBLANCO].strip()
        censo.votosNulo = row[VOTOSNULO].strip()
        censo.put()

        for idPartido in range(13,len(row)):
            escrutinio = Escrutinio()
            escrutinio.censo = censo
            escrutinio.partido = partidos[idPartido][0]
            escrutinio.votos = row[idPartido]
            escrutinio.put()



