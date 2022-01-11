import collections
import csv
from collections import namedtuple
import statistics
from datetime import datetime
import parser


Info = namedtuple('Info','id,sex,birth_date,age,country,department,illness,group,infection_cause,arrival_date,infected_by,confirmation_date,recovery_date,status,need_ICU,other_pathologies,different_treatments_given,maximum_temperature,average_temperature,daily_medications,daily_medical_examinations')

#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 1
#----------------------------------------------------------------------------------------------------------------------------
def lee_fichero(fichero):

    with open(fichero, encoding='utf-8') as f:
        
        lector = csv.reader(f)
        next(lector)
        res=[]
        for id, sex, birth_date, age, country, department, illness, group, infection_cause, arrival_date, infected_by, confirmation_date, recovery_date, status, need_UCI, other_pathologies, different_treatments_given, maximum_temperature, average_temperature, daily_medications, daily_medical_examinations in lector:
                         
            tupla = Info(int(id), str(sex), datetime.strptime(birth_date), int(age), str(country), 
                         str(department), str(illness), int(group), str(infection_cause), 
                         datetime.strptime(arrival_date), str(infected_by), str(confirmation_date),
                         str(recovery_date),int(status), bool(need_UCI),bool(other_pathologies),int(different_treatments_given), float(maximum_temperature),
                         float(average_temperature), int(daily_medications), int(daily_medical_examinations))
            res.append(tupla)
    return res   

#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 2
#----------------------------------------------------------------------------------------------------------------------------

#----- BLOQUE 1 -------------------------------------------------------------------------------------------------------------
def filtra_por_genero(fichero, sex='m'):
#input: los registros de la funcion sex
#output: filtro de los registros por genero
    res = [t for t in fichero if t.sex==sex]
    return res
 

#----- BLOQUE 2 -------------------------------------------------------------------------------------------------------------
def conjunto_registros(registros, filtro = None):
#Divide a todos los ingresados en dos conjuntos segun su id
    if filtro == None:
        res = {e.id for e in registros}
    else:
            res = {e.id for e in registros if e.sex == filtro}
    return res

def calcula_porcentaje_de_guatemaltecos(registros, country='guatemala'):
#input: los registros de la funcion country
#output: el porcentaje de los ingresados guatemaltecos
    cont_guatemaltecos = 0
    cont_ingresados = 0

    for e in registros:
        cont_ingresados = cont_ingresados + 1
        if e.country == country:
            cont_guatemaltecos = cont_guatemaltecos + 1 
    res = None
    if cont_ingresados > 0: 
        res = cont_guatemaltecos*100/cont_ingresados
    return res
#----- BLOQUE 3 -------------------------------------------------------------------------------------------------------------
def calcula_id_pocos_tratamientos_dados(registros):
#Calcula los pacientes que han recibido menos de 3 tratamientos distintos
    res = sorted([(e.id, e.different_treatments_given) for e in registros if e.different_treatments_given < 3], key = lambda x:x[1])
    return res

def calcula_promedio_de_temperatura_maxima(registros):
#Calcula el promedio de la temperatura máxima de los pacientes
    res=[e.average_temperature for e in registros]
    promedio= sum(res)/len(res)
    return promedio

#----------------------------------------------------------------------------------------------------------------------------
#-- ENTREGA 3
#----------------------------------------------------------------------------------------------------------------------------


#----- BLOQUE 4 -------------------------------------------------------------------------------------------------------------

def calcula_id_con_mas_tratamientos_diferentes(registros):
#Obtiene el id de la persona que ha recibido más tratamientos diferentes
        maximo =  max(registros, key = lambda x:x.different_treatments_given)
        res = [e for e in registros if e.different_treatments_given == maximo.different_treatments_given]
        return res

#----- BLOQUE 5-------------------------------------------------------------------------------------------------------------
def obtener_lista_de_registros(registros,n):
#Obtiene los tres primeros pacientes de la lista ordenados según su id
    res = sorted([e.age for e in registros ])
    return res[:n]
#----- BLOQUE 6-------------------------------------------------------------------------------------------------------------

def agrupa_por_pais (registros):
#Agrupa a los pacientes sengún su nacionalidad
    res = dict()
    for t in registros:
        if t.country in res:
            res[t.country].append(t)
        else:
            res[t.country]= [t]
    return res

def obten_media_edad_por_pais(registros):
#Calcula la media de edad por país
    dicc=agrupa_por_pais(registros)
    res = {clave:calcula_media_edad(lista_valores) for clave, lista_valores in dicc.items()}
    return res

def calcula_media_edad(registros):
#Calcula la media de edad
    return statistics.mean(t.age for t in registros)


def agrupa_por_distinto_tratamiento(registros):
    res = dict()
    for h in registros:
        if h in res:
            res[h.different_treatments_given].append(h)
        else:
            res[h.different_treatments_given]= [h]
    return res

def obten_media_revisiones_diarias_segun_distintos_tratamientos(registros):
    dicc= agrupa_por_distinto_tratamiento(registros)
    res = {clave: calcula_media_revisiones_diarias(lista_valores) for clave, lista_valores in dicc.items()}
    return res
def contar_hombres(registros):
    res[counter(sex=='m') in registros]

def calcula_media_revisiones_diarias(registros):
    return statistics.mean(t.daily_medical_examinations for t in registros)

def muestra_revisiones_diarias_por_tratamientos_recividos(registros):
    dicc=obten_media_revisiones_diarias_segun_distintos_tratamientos(registros)
    X, Y = zip(*sorted(dicc.items()))    
    titulo ='Revisiones diarias según la cantidad de tratamientos distintos'
    etiqueta_eje_x = 'Tratamientos distintos'
    etiqueta_eje_y = 'Revisiones diarias'  
        

