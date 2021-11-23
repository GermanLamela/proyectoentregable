# -*- coding: utf-8 -*-

# Importaciones:

import csv
from collections import namedtuple

from patients_guatemala_covid import calcula_porcentaje_con_diferentes_tratamientos,calcula_porcentaje_con_diferentes_tratamientos, cuenta_revisiones_diarias, lee_fichero, obten_registros_mas_tratamientos_recibidos, selecciona_registros_genero_y_pais

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

def test_selecciona_registros_de_genero_y_pais(fichero,  sex='m', country='guatemala'):
    print (f"pais={country} genero={sex}")
    res=selecciona_registros_genero_y_pais(fichero,sex, country)
    print (f"Hay {len(res)} registros del genero y pais dados como parámetros. Son los siguientes:")
    

def test_cuenta_revisiones_diarias (fichero, sex='m' ):
    res = cuenta_revisiones_diarias(fichero, sex) 
    print (f"Hay {res} revisiones diarias al género {sex}")

def test_calcula_porcentaje_con_diferentes_tratamientos(fichero, sex='m'):
    res = calcula_porcentaje_con_diferentes_tratamientos(fichero, sex)
    print(f"El porcentaje de ingresados en UCI de genero {sex} es {res:.2f}")

def test_obten_registros_mas_tratamientos_recibidos(fichero):
    res = obten_registros_mas_tratamientos_recibidos(fichero)
    print (f"Hay {len(res)} registros con la cantidad máxima de tratamientos recibidos. Son los siguientes:")
    mostrar_fichero(res)

def main():

    test_lee_fichero('./data/patients_guatemala_covid.csv')

    REGISTROS = lee_fichero('./data/patients_guatemala_covid.csv')


    print ("test_selecciona_registros_de_genero_y_pais" +"="*25)     
    test_selecciona_registros_de_genero_y_pais(REGISTROS, 'm')
    test_selecciona_registros_de_genero_y_pais(REGISTROS, 'f')

    print ("\ntest_cuenta_revisiones_diarias" +"="*25)
    test_cuenta_revisiones_diarias(REGISTROS)
    test_cuenta_revisiones_diarias(REGISTROS, 'm')

    print ("\ntest_calcula_porcentaje_en_ICU" +"="*25)
    test_calcula_porcentaje_con_diferentes_tratamientos(REGISTROS)
    test_calcula_porcentaje_con_diferentes_tratamientos(REGISTROS, 'f')

    print ("\ntest_obten_registros_mas_dinero_banco" +"="*25)     
    test_obten_registros_mas_tratamientos_recibidos(REGISTROS)
    (REGISTROS[:100])
    (REGISTROS[:100])





if __name__ == '__main__':
    main()
