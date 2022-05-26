import statistics as st 
import plotly.graph_objects as pgo
import plotly.figure_factory as pff
import pandas as pd
import random

df = pd.read_csv("Project/medium_data.csv")
data = df["reading_time"].tolist()
fig = pff.create_distplot([data], ["Reading Time"], show_hist = False)
population_mean = st.mean(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean



mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)



std_deviation = st.stdev(mean_list)
mean = st.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)


fig = pff.create_distplot([mean_list], ["Reading Time"], show_hist=False)
fig.add_trace(pgo.Scatter(x=[mean, mean], y=[0, 1.00], mode="lines", name="MEAN"))
fig.show()



first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)



fig = pff.create_distplot([mean_list], ["Reading Time"], show_hist=False)
fig.add_trace(pgo.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
fig.add_trace(pgo.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 1], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(pgo.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(pgo.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 1], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(pgo.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 1], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(pgo.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,1], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(pgo.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,1], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()



df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean_of_sample1 = st.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = pff.create_distplot([mean_list], ["Reading time"], show_hist=False)
fig.add_trace(pgo.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
fig.add_trace(pgo.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 1], mode="lines", name="MEAN OF SAMPLE"))
fig.add_trace(pgo.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.show()

z_score=(mean_of_sample1-mean)/std_deviation

print('Z-Score is =',z_score)

