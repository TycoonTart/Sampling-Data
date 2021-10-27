import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import pandas as pd
import csv
df=pd.read_csv("data.csv")
data=df["temp"].tolist()
def random_set_of_mean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()
def setup():
    mean_list=[]
    for i in range(0,1000):
        setOfMeans=random_set_of_mean(100)
        mean_list.append(setOfMeans)
    show_fig(mean_list)      
    mean=statistics.mean(mean_list)
    print("mean",mean)
setup()
population_mean=statistics.mean(data)
print("Population mean",population_mean)
def standard_division():
    mean_list=[]
    for i in range(0,1000):
        setOfMeans=random_set_of_mean(100)
        mean_list.append(setOfMeans)
    standard_division=statistics.stdev(mean_list)
    print("Standard division of sampling distribution",standard_division)
standard_division()
