import utils
import read_csv
import charts

def run():
 
  continent_user = input('¿De qué continente desea conocer la información? ==> ')
 
  data = read_csv.read_csv('data.csv')
  
  data = list(filter(lambda item : item['Continent'] == continent_user,data))
  
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  
  '''
  country = input('Type Country => ')
  
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  '''

# Dualidad en python
if __name__ == '__main__':
  run()
'''
Sirve para hacer que el archivo también se pueda ejecutar como script directamente desde la terminal, pero también permite que nos sirva como módulo

if name == “main”:
run()

Se le llama: Entry point
'''

