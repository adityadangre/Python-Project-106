import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    coffee_consumption_in_ml = []
    sleeping_hours = []

    with open(data_path) as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            coffee_consumption_in_ml.append(float(row['Coffee in ml']))
            sleeping_hours.append(float(row['sleep in hours']))
        
    return {'x' : coffee_consumption_in_ml, 'y' : sleeping_hours}

def correlation(data_source):
    corelation = np.corrcoef(data_source['x'], data_source['y'])
    print('Correlation between marks and attendance:', corelation[0, 1])

def scatterPlot(data_path):
    with open(data_path, newline = '') as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = 'Coffee in ml', y = 'sleep in hours')
        fig.show()

def setUp():
    data_path = 'correlation-master\data\ProjectCoffeeSleep.csv'
    data_source = getDataSource(data_path)
    
    correlation(data_source)
    scatterPlot(data_path)

setUp()