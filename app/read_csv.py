import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])

'''
¿Qué es un archivo CSV?

Un archivo CSV es un tipo de archivo que se utiliza para almacenar datos en una forma tabular estructurada (fila / columna). Es un archivo de texto plano y, como su nombre lo indica, almacena los valores separados por una coma.

En este artículo, tendremos una discusión detallada sobre cómo leer, escribir y analizar un archivo CSV en Python.

Fuente del archivo CSV

El concepto de tener un archivo CSV nació de la necesidad de exportar grandes cantidades de datos de un lugar a otro (programas). Por ejemplo, importando datos de una hoja de cálculo de gran tamaño y exportándolos a una base de datos. Asimismo, podemos exportar grandes cantidades de datos a programas.

Los diferentes lenguajes usan diferentes formatos para almacenar datos, por lo que cuando los programadores necesitan exportar datos de un programa a otro, sienten la necesidad de tener algún tipo de archivo universal con el cual transferir grandes cantidades de datos; Un tipo de archivo que cualquier programa puede leer y analizar en su propio formato.
'''