import justpy as jp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime

# <div class="container px-5 py-24 mx-auto flex flex-col">
#     <div class="lg:w-4/6 mx-auto">
#       <div class="rounded-lg h-64 overflow-hidden">
#         <img alt="content" class="object-cover object-center h-full w-full" src="https://dummyimage.com/1200x500">
#       </div>
class ScoreSeries(jp.Section):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_classes('container px-5 mx-auto flex flex-col')
        self.div1 = jp.Div(a=self, classes = 'rounded-lg overflow-hidden')
        # create dataframe
 
        dataframe = pd.DataFrame({'date_of_week': np.array([datetime.datetime(2021, 11, i+1)
                                                            for i in range(7)]),
                                'classes': [5, 6, 8, 2, 3, 7, 4]})
        
        # Plotting the time series of given dataframe
        plt.plot(dataframe.date_of_week, dataframe.classes)
        
        # Giving title to the chart using plt.title
        plt.title('ESG time series')
        
        # rotating the x-axis tick labels at 30degree
        # towards right
        plt.xticks(rotation=30, ha='right')
        
        # Providing x and y label to the chart
        plt.xlabel('Date')
        plt.ylabel('ESG score')
        jp.Matplotlib(a=self.div1,classes='object-cover object-center h-full w-full')
        plt.close()
