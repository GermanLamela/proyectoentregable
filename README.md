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
* **<filtra_por_genero>**: Divide el fichero según el género.
* **<conjunto_registros>**: Divide a todos los ingresados en dos conjuntos segun su id.
* **<calcula_porcentaje_de_guatemaltecos>**: Calcula el porcentaje de personas cuya nacionalidad es guatemalteca.
* **<calcula_id_pocos_tratamientos_dados>**: Calcula los pacientes que han recibido menos de 3 tratamientos distintos.
* **<calcula_promedio_de_temperatura_maxima>**: Calcula el promedio de la temperatura máxima de los pacientes.
* **<calcula_id_con_mas_tratamientos_diferentes>**: Obtiene el id de la persona que ha recibido más tratamientos diferentes
* **<obtener_lista_de_registros>**: Obtiene los tres primeros pacientes de la lista ordenados según su id
* **<agrupa_por_pais>**: Agrupa a los pacientes sengún su nacionalidad.
* **<obten_media_edad_por_pais>**: Calcula la media de edad por país.
* **<calcula_media_edad>**: Calcula la media de edad.
* **<agrupa_por_distinto_tratamiento>**: Agrupa a los pacientes sengún su nacionalidad.
* **<obten_media_revisiones_diarias_segun_distintos_tratamientos>**: Obtiene la media de las revisiones diarias según la cantidad de distintos tratamientos.
* **<calcula_media_revisiones_diarias>**: Calcula la media de las revisiones médicas diarias.


### \<patients_guatemala_covid_test\>

* **<test_lee_fichero>**: Prueba de la lectura del fichero.
* **<mostrar_fichero>**: Muestra el fichero del archivo csv.
* **<mostrar_diccionario>**: Muestra el diccionaro.
* **<test_filtrar_por_genero>**: Prueba del filtrado por género.
* **<test_conjunto_registros>**: Prueba de la división de los ingresados en dos conjuntos.
* **<test_calcula_porcentaje_de_guatemaltecos>**: Prueba del porcentaje de guatemaltecos.
* **<test_calcula_id_pocos_tratamientos_dados>**: Prueba del calculo de los pacientes con menos tratamientos distintos
* **<test_calcula_promedio_de_temperatura_maxima>**: Pueba del calculo del promedio de la temperatura máxima.
* **<est_calcula_id_con_mas_tratamientos_diferentes>**: Prueba del calculo del paciente con más tratamientos diferentes.
* **<test_obtener_lista_de_registros>**: Prueba de la obtención de los 3 primeros pacientes de la lista según su id.
* **<test_calcula_media_de_edad>**: Prueba del calculo de la media de edad.
* **<test_obten_media_edad_por_pais>**: Prueba del calculo de la media de edad según su país.
