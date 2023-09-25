# Lenguajes Formales y de Programación
## Proyecto 1 
### Semestre 2 2023
```js
Universidad San Carlos de Guatemala
Programador: Miguel Ricardo Galicia Urrutia
Carne: 202201117
Correo: galiciar319@gmail.com
```
---
## Descripción del Proyecto
El proposito de la aplicacion es la de un analizador lexico que resuelva problemas matematicos por medio de intrucciones que deben ser importadas por medio de un Archivo JSON
#### Cinta de opciones ####

Se creo un cinta de opciones la cual cuenta con las pestañas de archivo, analizar, ver reporte y ver errores. En la pestaña de archivo se encuentran las opciones de Agregar archivo, guardar archivo


![Cinta de opciones](opciones.png)


##### Pestaña Archivo #####

Para empezar con el funcionamiento de la aplicacion el usuario debera ir a la pestaña archivo y seleccionar la opcion de abrir documento para que este pueda ser analizado, al darle click a esa opcion este abrira un pestaña emergente en la cual el usuario debera seleccionar su archivo de entrada, este archivo debera ser un archivo JSON, si el usuario selecciona un archivo que no sea JSON se mostrara un mensaje de error y se le pedira que seleccione un archivo valido, si el usuario selecciona un archivo valido este se cargara en la aplicacion y se mostrara en la pestaña de analizar.

La opcion de guardar generara un archivo json derivado del original a excepcion que este mostrara las respuestas de las operaciones realizadas en el archivo original, si el usuario selecciona la opcion de guardar se le abrira una pestaña emergente en la cual debera seleccionar la ruta donde se guardara el archivo, si el usuario no selecciona una ruta se mostrara un mensaje de error y se le pedira que seleccione una ruta valida, si el usuario selecciona una ruta valida se guardara el archivo en la ruta seleccionada.

##### Analizar #####

iniciara con el analisis del archivo seleccionado por 
##### Salir #####
La cuarta opción, "Salir", muestra un mensaje de despedida y termina la ejecución del programa.

#### Analizar ####
Analizara el archivo seleccionado por el usuario, si el archivo es valido se mostrara el resultado de las operaciones en la pestaña de ver reporte, si el archivo no es valido se mostrara el error en la pestaña de ver errores.