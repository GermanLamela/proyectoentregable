# -*- coding: utf-8 -*-

# Importaciones:

import csv
from collections import namedtuple

from patients_guatemala_covid import calcula_media_edad, obten_media_edad_por_pais, calcula_porcentaje_de_guatemaltecos, conjunto_registros, filtra_por_genero, lee_fichero, calcula_id_pocos_tratamientos_dados, filtra_por_genero,calcula_id_con_mas_tratamientos_diferentes, muestra_revisiones_diarias_por_tratamientos_recividos, obtener_lista_de_registros, calcula_promedio_de_temperatura_maxima

Info = namedtuple('Info','id,sex,birth_date,age,country,department,illness,group,infection_cause,arrival_date,infected_by,confirmation_date,recovery_date,status,need_ICU,other_pathologies,different_treatments_given,maximum_temperature,average_temperature,daily_medications,daily_medical_examinations')


# Funciones:



def test_lee_fichero(fichero):
    lista_tuplas = lee_fichero(fichero)
    print('Leídos', len(lista_tuplas),'registros.')
    print('Los tres primeros registros son:',lista_tuplas[:3])
    print('Los tres últimos registros son:',lista_tuplas[-3:])


def mostrar_fichero (fichero):
    for indx, fichero in enumerate(fichero):
        print(f"{indx+1}-{fichero}")

def mostrar_diccionario(dicc):
    for clave, valor in dicc.items():
        print(f"{clave}-->{valor}")    

 
#----- BLOQUE 1 -------------------------------------------------------------------------------------------------------------

def test_filtrar_por_genero(fichero,  sex='m'):
    print (f"genero={sex}")
    res=filtra_por_genero(fichero,sex)
    print (f"Hay {len(res)} registros del género dado como parámetros.")
    
#----- BLOQUE 2 -------------------------------------------------------------------------------------------------------------


def test_conjunto_registros (fichero, sex='m' ):
    res = conjunto_registros(fichero, sex) 
    print (f"Hay {len(res)} personas del sexo {sex}, los cuales son: {res}")

def test_calcula_porcentaje_de_guatemaltecos(fichero, country='guatemala'):
    res = calcula_porcentaje_de_guatemaltecos(fichero, country)
    print(f"El porcentaje de ingresados con  {country} es {res:.2f}")

#----- BLOQUE 3 -------------------------------------------------------------------------------------------------------------


def test_calcula_id_pocos_tratamientos_dados(registros):
    res = calcula_id_pocos_tratamientos_dados(registros)
    print(f"Hay {len(res)} personas que tienen pocos de  tratamientos diferentes, los cuales son:")
    print((res))

def test_calcula_promedio_de_temperatura_maxima(registros):
    res=calcula_promedio_de_temperatura_maxima(registros)
    print(f"El promedio de temperatura máxima de los pacientes es:")
    print(res)
#----- BLOQUE 4-------------------------------------------------------------------------------------------------------------

def test_calcula_id_con_mas_tratamientos_diferentes(registros):
    res = calcula_id_con_mas_tratamientos_diferentes(registros)
    print (f"La persona que mas tratamientos distintos es el {res[0][16]}")

#----- BLOQUE 5-------------------------------------------------------------------------------------------------------------

def test_obtener_lista_de_registros(registros,n):
    res= obtener_lista_de_registros(registros,4)
    print(f"Los primeros 4 registros ordenados de menor a mayor según su id son:")
    print(res)

#----- BLOQUE 6-------------------------------------------------------------------------------------------------------------

def test_calcula_media_de_edad(registros):
    res= calcula_media_edad(registros)
    print(f'La media de edad es:')
    print(res)

def test_obten_media_edad_por_pais (registros):
    res = obten_media_edad_por_pais(registros)
    print("La media de edad según el nivel de educación es la siguiente:")
    mostrar_diccionario(res)




def main():

    test_lee_fichero('./data/patients_guatemala_covid.csv')

    REGISTROS = lee_fichero('./data/patients_guatemala_covid.csv')


    print ("test_filtrar_por_genero" +"="*25)     
    test_filtrar_por_genero(REGISTROS, 'm')
    test_filtrar_por_genero(REGISTROS, 'f')

    print ("\ntest_conjunto_registro" +"="*25)
    test_conjunto_registros(REGISTROS)
    test_conjunto_registros(REGISTROS, 'f')

    print ("\ntest_calcula_porcentaje_de_guatemaltecos" +"="*25)
    test_calcula_porcentaje_de_guatemaltecos(REGISTROS)
    
    print ("\ntest_calcula_id_menos_tratamientos_dados" +"="*25)
    test_calcula_id_pocos_tratamientos_dados(REGISTROS)

    print ("\ntest_calcula_id_pocos_tratamientos_dados" +"="*25)
    test_calcula_promedio_de_temperatura_maxima(REGISTROS)

    print ("\ntest_calcula_id_con_mas_tratamientos_dados" +"="*25)
    test_calcula_id_con_mas_tratamientos_diferentes(REGISTROS)

    print ("\ntest_obtener_lista_de_registros" +"="*25)
    test_obtener_lista_de_registros(REGISTROS,3)


    print ("\ntest_calcula_media_de_edad" +"="*25)
    test_calcula_media_de_edad(REGISTROS)





if __name__ == '__main__':
    main()
