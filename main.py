import plotly.figure_factory as ff
import statistics 
import random
import pandas as pd
import csv
df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
fig=ff.create_distplot([data],["reading_time"],show_hist=False)
fig.show()
print("POPULATION MEAN:",statistics.mean(data))
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
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.show()
def setup():
    mean_list=[]
    for i in range(0,100):
        setOfMeans=random_set_of_mean(10)
        mean_list.append(setOfMeans)
    show_fig(mean_list)      
    print("sampling mean",statistics.mean(mean_list))
setup()