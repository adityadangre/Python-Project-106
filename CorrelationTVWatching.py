import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    size_of_tv = []
    average_time_spend = []

    with open(data_path) as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            size_of_tv.append(float(row['Size of TV']))
            average_time_spend.append(float(row['\tAverage Time']))
        
    return {'x' : size_of_tv, 'y' : average_time_spend}

def correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print('The correlation between Size of TV and Average watching time:', correlation[0, 1])

def scatterPlot(data_path):
    with open(data_path, newline = '') as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = 'Size of TV', y = '\tAverage Time')
        fig.show()

def setup():
    data_path = 'correlation-master\data\TVWatchingTime.csv'
    data_source = getDataSource(data_path)

    correlation(data_source)
    scatterPlot(data_path)

setup()