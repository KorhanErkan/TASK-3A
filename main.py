import pandas as pd

population_dict = {'Bursa': 3186291,
                   'İzmir': 4455294,
                   'Ankara': 5747325,
                   'Aydın': 1134031,
                   'Antalya': 2619832,
                   'İstanbul': 16034511,
                   'Eskişehir': 907353}


area_dict = {'Bursa': 10820000, 
             'İzmir': 11891000, 
             'Ankara': 24521000,
             'Aydın': 1582000, 
             'Antalya': 1417000,
             'İstanbul': 5343000,
             'Eskişehir': 2678000}


sehirler = pd.DataFrame({'population': population_dict,
                       'area(m2)': area_dict})

sehirler