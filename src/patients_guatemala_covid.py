import csv
from collections import namedtuple




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
                         
            tupla = Info(int(id), str(sex), str(birth_date), int(age), str(country), 
                         str(department), str(illness), int(group), str(infection_cause), 
                         str(arrival_date), str(infected_by), str(confirmation_date),
                         str(recovery_date),int(status), bool(need_UCI),bool(other_pathologies),int(different_treatments_given), float(maximum_temperature),
                         float(average_temperature), int(daily_medications), int(daily_medical_examinations))
            res.append(tupla)
    return res   


def selecciona_registros_genero_y_pais(fichero, sex='m',country='guatemala'):
    res = [t for t in fichero if t.sex==sex and t.country==country]
    return res
 
def cuenta_revisiones_diarias(fichero, sex='m'):
    res=0
    for t in fichero:
        if t.sex==sex and t.daily_medical_examinations !=0:
            res=res+1
    return res

def calcula_porcentaje_con_diferentes_tratamientos(fichero,sex='m'):
    cont_infectados_con_diferentes_tratamientos=0
    cont_infectados=0
    
    for t in fichero:
        if t.sex==sex:
            cont_infectados+=1
            if t.different_treatments_given!=0:
                cont_infectados_con_diferentes_tratamientos+=1
    
        res=None            
        if cont_infectados >0: 
         res=cont_infectados_con_diferentes_tratamientos*100/cont_infectados 
    return res

def obten_registros_mas_tratamientos_recibidos(fichero):
    maximo =  max(fichero, key = lambda x:x.different_treatments_given)
    res = [t for t in fichero if t.different_treatments_given == maximo.different_treatments_given]
    return res

def obten_registros_mas_temperatura_maxima(fichero):
    maximo =  max(fichero, key = lambda x:x.maximum_temperature)
    res = [t for t in fichero if t.maximum_temperature== maximo.maximum_temperature]
    return res