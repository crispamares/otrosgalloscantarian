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

class Provincia:
    def __init__(self):
        self.poblacion = 0
        self.censoTotal = 0

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

    votos = {}

    for sigla in siglas[13:]:
        id = siglas.index(sigla)
        partidos[id] = (nombres[id],sigla)

    for row in voteReader:
        # Actualizar Informacion Provincia
        comunidad = row[COMUNIDAD].strip()
        provincia = row[PROVINCIA].strip()
        municipio = row[MUNICIPIO].strip()
        poblacionMunicipio = eval(row[POBLACION].strip().replace(",",""))
        censoMunicipio = eval(row[CENSOTOTAL].strip().replace(",",""))
        totalVotosMunicipio = eval(row[VOTOSTOTALES].strip().replace(",",""))
        validosMunicipio = eval(row[VOTOSVALIDOS].strip().replace(",",""))
        candidaturasMunicipio = eval(row[VOTOSCANDIDATURA].strip().replace(",",""))
        blancoMunicipio = eval(row[VOTOSBLANCO].strip().replace(",",""))
        nulosMunicipio = eval(row[VOTOSNULO].strip().replace(",",""))
        if (not comunidad in votos):
            votos[comunidad] = {}
        if (not provincia in votos[comunidad]):
            votos[comunidad][provincia] = {'Poblacion':0,'Censo':0,'TotalVotos':0,'Validos':0,'Candidaturas':0,'Blanco':0,'Nulos':0,'Votos':{}}
        votos[comunidad][provincia]['Poblacion'] += poblacionMunicipio
        votos[comunidad][provincia]['Censo'] += censoMunicipio
        votos[comunidad][provincia]['TotalVotos'] += totalVotosMunicipio
        votos[comunidad][provincia]['Validos'] += validosMunicipio
        votos[comunidad][provincia]['Candidaturas'] += candidaturasMunicipio
        votos[comunidad][provincia]['Blanco'] += blancoMunicipio
        votos[comunidad][provincia]['Nulos'] += nulosMunicipio

        # Actualizar votos partidos
        for idPartido in range(13,len(row)):
            sigla = siglas[idPartido]
            votosMunicipio = eval(row[idPartido].replace(",",""))
            if (votosMunicipio > 0):
                if (not sigla in votos[comunidad][provincia]['Votos']):
                    votos[comunidad][provincia]['Votos'][sigla] = votosMunicipio
                else:
                    votos[comunidad][provincia]['Votos'][sigla] += votosMunicipio

    # El ano es el mismo para todos
    i = filepath.find('/')
    ano = filepath[i+1:i+5]

    WriteToDataStore(ano, votos)


def WriteToDataStore(ano, votos):
    for comunidad in votos:
        for provincia in votos[comunidad]:
            censo = CensoElectoral()
            censo.ano = ano
            censo.comunidad = comunidad
            censo.provincia = provincia
            censo.poblacion = votos[comunidad][provincia]['Poblacion']
            censo.censoTotal = votos[comunidad][provincia]['Censo']
            censo.votosTotales = votos[comunidad][provincia]['TotalVotos']
            censo.votosValidos = votos[comunidad][provincia]['Validos']
            censo.votosCandidatura = votos[comunidad][provincia]['Candidaturas']
            censo.votosBlanco = votos[comunidad][provincia]['Blanco']
            censo.votosNulo = votos[comunidad][provincia]['Nulos']
            censo.put()

            for partido in votos[comunidad][provincia]['Votos']:
                escrutinio = Escrutinio()
                escrutinio.censo = censo
                escrutinio.partido = partido
                escrutinio.votos = votos[comunidad][provincia]['Votos'][partido]
                escrutinio.put()
