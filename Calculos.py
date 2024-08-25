import numpy as np
import math
import random as rd
import pandas as pd

#=========================Functions to generate the variables============================

#Function to calculate variables associated with forces
def calcular_fuerzas():
    fuerzas=[]
    fuerzas = [rd.randint(10,300) for _ in range(16)]
    return fuerzas

#Functions to calculate variables associated with angles
def calcular_angulos(num_angulos=16, rangos=None):
    if rangos is None:
        # Ranges
        rangos = [(2, 88), (91, 180), (181, 270), (271, 360)]
    
    angulos = []
    
    for i in range(num_angulos):
        rango = rangos[i % len(rangos)]
        angulo = rd.randint(rango[0], rango[1])
        angulos.append(angulo)
    
    if angulos[0] >= angulos[4]:
        angulos[4] = rd.randint(rangos[0][0]+1, rangos[0][1])
        angulos[0] = rd.randint(rangos[0][0], angulos[4] - 1)

    return angulos

def calcular_coordenadas():
    while True:
        coordenadas = [rd.randint(-100, 100) for _ in range(9)]#x_0,y_0,z_0,x_1,y_1,z_1
        if coordenadas[0] < coordenadas[3] and coordenadas[1] < coordenadas[4] and coordenadas[2] < coordenadas[5]:
            return coordenadas

def calcular_dimensiones(num_dimensiones = 28, rangos = None):
    values = [(1, 10), (-10, -1), (-10, 10)]
    
    dimensiones = []
    
    for i in range(num_dimensiones):
        value = values[i % len(values)]
        dimension = rd.randint(value[0], value[1])
        dimensiones.append(dimension)
    
    if dimensiones[0] >= dimensiones[3]:
        dimensiones[3] = rd.randint(values[0][0]+1, values[0][1])
        dimensiones[0] = rd.randint(values[0][0], dimensiones[3] - 1)

    return dimensiones

def calcular_momentos():
    momentos=[]
    momentos = [rd.randint(10,100) for _ in range(4)]
    return momentos

#=========================
class Calculations:
    def cosine(angle):
        cos=math.cos(math.radians(angle))
        return cos
    
    def sine(angle):
        sin=math.sin(math.radians(angle))
        return sin
    
    def tangent(angle):
        tan=math.tan(math.radians(angle))
        return tan
    
    def magnitude(fx,fy):
        magnitude=math.sqrt(fx**2 + fy**2)
        return magnitude
    
    def magnitude3D(fx,fy,fz):
        magnitude3D=math.sqrt(fx**2 + fy**2 + fz**2)
        return magnitude3D
    
    def define_angle(fx,fy):
        if fx>0 and fy>0: #Primer cuadrante
            angle = math.degrees(math.atan(abs(fy)/abs(fx)))
        if fx<0 and fy>0: #Segundo cuadrante
            angle = 180-math.degrees(math.atan(abs(fy)/abs(fx)))
        if fx<0 and fy<0: #Tercer cuadrante
            angle = 180+math.degrees(math.atan(abs(fy)/abs(fx)))
        if fx>0 and fy<0: #Cuarto cuadrante
            angle = 360-math.degrees(math.atan(abs(fy)/abs(fx)))
        return angle
    
    def arccosine(fc,mag):
        arccosine = math.degrees(math.acos(fc/mag))
        return arccosine