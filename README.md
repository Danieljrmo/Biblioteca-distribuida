# Biblioteca-distribuida
Uso de esquema maestro esclavo para distribuir la carga de trabajo (busqueda) en una biblioteca.
Para este programa estamos utilizando Python y Flask para las consultas HTTP
Para desplegarlo se debe ingresar a la carpeta /esclavos y ejecutar ./runEsclavos.py para correr los esclavos de cada tipo de documento.
Luego se debe ejecutar en un terminal aparte en la carpeta /maestro ./app.py
Con esto estaremos listos para realizar una búsqueda en un navegador
Tenemos los siguientes tipos de búsquedas
    1.- Por titulo de documento (broadcast): http://localhost:5000/query?titulo=ecuaciones

    2.- Por tipo de documento (sin título): http://localhost:5000/query?tipo_doc=libro+tesis
        Entrega todos los libros y tesis

    3.- Por tipo de documento y título : http://localhost:5000/query?titulo=ecuaciones&tipo_doc=libro+tesis 
        Solo libros y tesis que contengan “ecuaciones”

    4.- Para ver como se usa el rankin podemos buscar http://localhost:5000/query?titulo=ecuaciones y se verá que existe "ecuaciones
        diferenciales" y "ecuaciones de primer grado" pero si se busca: http://localhost:5000/query?titulo=ecuaciones diferenciales, el resultado
        dejará como último "ecuaciones de primer grado" ya que se prioríza "ecuaciones diferenciales" primero.
        
    5. Si queremos una búsqueda con edad para utilizar el ranking, podemos  hacer las búsquedas:
        http://localhost:5000/query?titulo=viaje&edad=12  -> nos entregará primero el archivo del género Ciencia ficción con "viaje al centro de la tierra",
        para la edad entre 10 a 15 años, si cambiamos a http://localhost:5000/query?titulo=viaje&edad=20  -> nos entregará primero
        el género de Tecnología con "viaje en carretera con un programador"