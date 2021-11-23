# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  2021/2022)
Autor/a: Germán Lamela Núñez   uvus:gerlamnun

Este dataset registra los pacientes ingresados por covid en Guatemala.


## Estructura de las carpetas del proyecto

* **/src**: Contiene  los diferentes módulos de Python que conforman el proyecto.
  * **\<patients.py\>**: Contiene funciones para explotar los datos de los pacientes de Guatemala.
  * **\<patients_test.py\>**: Contiene funciones de test para probar las funciones del módulo patients.py. En este módulo está el main. 
* **/data**: Contiene el dataset.
    * **\<patients_guatemala_covid.csv\>**: Archivo con los datos de los pacientes de covid en Guatemala.
    
    
## Estructura del *dataset*

Contiene los datos de los pacientes de covid en Guatemala.

El dataset está compuesto por \<21\> columnas, con la siguiente descripción:

* **\<id>**: de tipo \<int\>, representa el número de columnas.
* **\<sex>**: de tipo \<str\>, representa el sexo.
* **\<birth_date>**: de tipo \<str\>, representa la fecha de nacimiento.
* **\<edad>**: de tipo \<int\>, representa la edad.
* **\<country>**: de tipo \<str\>, representa el país de procedencia.
* **\<department>**: de tipo \<str\>, representa el departamento.
* **\<illness>**: de tipo \<str\>, representa la enfermedad.
* **\<group>**: de tipo \<int\>, representa el grupo.
* **\<infection_cause>**: de tipo \<str\>, representa la causa de la infección.
* **\<arrival_date>**: de tipo \<str\>, representa la fecha de llegada.
* **\<infected_by>**: de tipo \<str\>, representa el medio por el que se infectó.
* **\<confirmation_date>**: de tipo \<str\>, representa la fecha de la confirmación de la enfermedad.
* **\<recovery_date>**: de tipo \<str\>, representa la fecha de recuperación.
* **\<status>**: de tipo \<int\>, representa el status.
* **\<need_UCI>**: de tipo \<boolean\>, representa la necesidad de cuidados intensivos.
* **\<other_pathologies>**: de tipo \<boolean\>, representa otras patologías.
* **\<different_treatments_given>**: de tipo \<int\>, representa los distintos tratamientos.
* **\<maximum_temperature>**: de tipo \<float\>, representa la temperatura máxima.
* **\<average_temperature>**: de tipo \<float\>, representa la media de temperatura.
* **\<daily_medications>**: de tipo \<int\>, representa el la medicación diaria.
* **\<daily_medical_examinations>**: de tipo \<int\>, representa la examinación de las medicaciones previas.



## Tipos implementados

Para trabajar con los datos del dataset se ha definido la siguiente tupla con nombre: 

Info = namedtuple('Info','id,sex,birth_date,age,country,department,illness,group,infection_cause,arrival_date,infected_by,confirmation_date,recovery_date,status,need_ICU,other_pathologies,different_treatments_given,maximum_temperature,average_temperature,daily_medications,daily_medical_examinations')

Siendo: int(id), str(sex), str(birth_date), int(age), str(country), str(department), str(illness), int(group), str(infection_cause), 
        str(arrival_date), str(infected_by), str(confirmation_date), str(recovery_date),int(status), bool(need_UCI), bool(other_pathologies),int(different_treatments_given), float(maximum_temperature),float(average_temperature), int(daily_medications), int(daily_medical_examinations.



## Funciones implementadas
En este proyecto se han implementado las siguientes funciones, que están clasificadas según el módulo en el que se encuentren.

### \<patients_guatemala_covid\>

* **<lee_fichero>**: Hace una lectura del fichero.


### \<patients_guatemala_covid_test\>

* **<test_lee_fichero>**: Prueba de la lectura del fichero.

