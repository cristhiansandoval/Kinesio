#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Importo las librerias necesrias para el programa

from flask import Flask
from flaskext.mysql import MySQL
import datetime

# Configuraciones de Python Flask
app = Flask(__name__)
mysql = MySQL()

# Configuraciones de MySQL
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345'
app.config['MYSQL_DATABASE_DB'] = 'kinesio'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

# Clase SQL
# Argumentos
#   No tiene
class Datos():
	# Función init:
    #   Define los atributos de la clase Datos, que son los mismos que
    #   se solicitan cuando se intancia la misma
    # Argumentos:
    #   self: Variable que indica que estamos en el ambito de la clase.
    #   Se omite a la hora de instanciar la clase.
	# Retorno:
    #   No tiene valores de retorno
    def __init__(self, id):
		self.numero = str(id)
		self.fecha = "%s-%s-%s" % (datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
		self.hora = "%s:%s:%s" % (datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second)
    def buscarPaciente(self):
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT nombre FROM pacientes WHERE id ="+self.numero)
        if cur:
            return cur.fetchone()
        else:
            return 'No se pudo encontrar al paciente'
    def buscarNumero(self, nombre):
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT id FROM pacientes WHERE nombre = %s", nombre)
        if cur:
            return cur.fetchone()
        else:
            return 'No se pudo encontrar al paciente'
    def agregarPaciente(self, nombre):
        argumentos = [self.numero, nombre]
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO  pacientes (`id`,`nombre`) VALUES (%s, %s)",argumentos)
        conn.commit()
        cur.execute("SELECT nombre FROM pacientes WHERE id ="+self.numero)
        if cur:
            return cur.fetchone()
        else:
            return 'Error en base de datos'
    def quitarPaciente(self):
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM pacientes WHERE id ="+self.numero)
        conn.commit()
        cur.execute("SELECT nombre FROM pacientes WHERE id ="+self.numero)
        if cur:
            return cur.fetchone()
        else:
            return 'Error en base de datos'
    def todosLosPacientes(self):
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT nombre FROM pacientes")
        if cur:
            return cur.fetchall()
        else:
            return 'No se pudo encontrar al paciente'
