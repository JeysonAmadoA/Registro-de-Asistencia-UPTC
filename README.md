
# Registro-de-Asistencia-UPTC

El propósito principal de este proyecto es establecer una base de datos mediante el procesamiento de archivos CSV, con el fin de llevar un registro de la asistencia a eventos en la Universidad Pedagógica y Tecnológica de Colombia, además de permitir su visualización a través de un módulo web.

  

Para la implementación de este proyecto, se emplearon las siguientes tecnologías:

* Angular
* Postgres
* Docker
* Python

	* Para la manipulación de los archivos CSV, se optó por la librería Pandas

	* Para la implementación del servicio de API REST, se eligió Flask como la plataforma principal, aprovechando su versatilidad y eficiencia.

## Ejecutar proyecto

Para ejecutar el proyecto se debe usar el siguiente comando en la carpeta raíz del proyecto


```shell

docker-compose -f .devops/docker/develop/docker-compose.yml -f .devops/docker/develop/docker-compose.override.yml up --build

```