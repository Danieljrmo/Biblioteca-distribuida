# Biblioteca-distribuida
Uso de esquema maestro esclavo para distribuir la carga de trabajo (busqueda) en una biblioteca.
Integrantes: Rodrigo Vergara y Daniel Matamala

## Requisitos
- Python 3.9+
- Flask
- Pyro5

## Estructura
- Maestro en `maestro/`
- Esclavos en `esclavo/` (libros, videos, revistas, tesis)
- Servidor RMI en `rmi_server/`
- Logs centralizados en `logs/central_log.csv`

## Despliegue
- Ejecutar ./runSystem y esperar a que encienda todo el sistema, una vez listo ya puedes usar el navegador para las búsquedas.

## Busquedas:
 Tenemos las siguientes búsquedas en el sistema:

    1.- Por titulo de documento (broadcast): http://localhost:5000/query?titulo=ecuaciones

    2.- Por tipo de documento (sin título): http://localhost:5000/query?tipo_doc=libro+tesis
        Entrega todos los libros y tesis

    4.- Para ver el uso del ranking podemos buscar 
                http://localhost:5000/query?titulo=ecuaciones
        y se verá que existe "ecuaciones diferenciales" y "ecuaciones de primer grado" pero si se busca:
                http://localhost:5000/query?titulo=ecuaciones diferenciales
        el resultado dejará como último "ecuaciones de primer grado" ya que se prioríza "ecuaciones diferenciales" primero.
        
    5. Si queremos una búsqueda con edad para utilizar el ranking, podemos  hacer las búsquedas:
                http://localhost:5000/query?titulo=viaje&edad=12
        nos entregará primero el archivo del género Ciencia ficción con "viaje al centro de la tierra" para la edad entre 10 a 
        15 años, si cambiamos a 
                http://localhost:5000/query?titulo=viaje&edad=20
        nos entregará primero el género de Tecnología con "viaje en carretera con un programador" por estar entre 16 y 25 años.

## log_rmi
- Sistema funcionando y se puede ver todo lo que ha buscado desde que inició el sistema con los parámetros: 
        inicio,fin,maquina,tipo_maquina,query,tiempo
    en la carpeta "logs"