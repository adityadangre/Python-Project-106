import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []

    with open(data_path) as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            ice_cream_sales.append(float(row['Ice-cream Sales']))
            cold_drink_sales.append(float(row['Cold drink sales']))
        
    return {'x' : ice_cream_sales, 'y' : cold_drink_sales}

def correlation(data_source):
    corelation = np.corrcoef(data_source['x'], data_source['y'])
    print('Correlation between temperature and sales:', corelation[0, 1])

def scatterPlot(data_path):
    with open(data_path, newline = '') as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = 'Ice-cream Sales', y = 'Cold drink sales')
        fig.show()

def setUp():
    data_path = 'correlation-master\data\SalesData.csv'
    data_source = getDataSource(data_path)
    
    correlation(data_source)
    scatterPlot(data_path)

setUp()