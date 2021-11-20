import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    student_attendance = []
    student_marks = []

    with open(data_path) as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            student_attendance.append(float(row['Marks In Percentage']))
            student_marks.append(float(row['Days Present']))
        
    return {'x' : student_attendance, 'y' : student_marks}

def correlation(data_source):
    corelation = np.corrcoef(data_source['x'], data_source['y'])
    print('Correlation between marks and attendance:', corelation[0, 1])

def scatterPlot(data_path):
    with open(data_path, newline = '') as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = 'Marks In Percentage', y = 'Days Present')
        fig.show()

def setUp():
    data_path = 'correlation-master\data\ProjectMarksandPresenty.csv'
    data_source = getDataSource(data_path)
    
    correlation(data_source)
    scatterPlot(data_path)

setUp()