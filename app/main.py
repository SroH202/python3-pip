import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = list(filter(lambda item : item['Continent'] == continent_user,data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''
  continent_user = input('¿De qué continente desea conocer la información? ==> ')
  
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == continent_user]
  
  country_name = continent_user
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(country_name,countries, percentages)
  
  data = read_csv.read_csv('data.csv')

  country = input('Type Country => ')
  
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  

# Dualidad en python
if __name__ == '__main__':
  run()

'''
Sirve para hacer que el archivo también se pueda ejecutar como script directamente desde la terminal, pero también permite que nos sirva como módulo

if name == “main”:
run()

Se le llama: Entry point
'''

