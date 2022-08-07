import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
def graphic_temp(clean_data:dict,temp_min:float,temp_max:float):
    fig,ax = plt.subplots(figsize = (9, 9))

    ax.scatter(temp_min[1],temp_min[0], s=60, alpha=0.7, edgecolors="k")
    ax.scatter(temp_max[1],temp_max[0], s=60, alpha=0.7, edgecolors="k")
    ax.set_title("Temperature Valencia Vzla Next 15 days")
    ax.set_xlabel('Days')
    ax.set_ylabel('Temperature °C')
    ax.text(temp_min[1],temp_min[0]," temp min: "+str(temp_min[0])+"°C")
    ax.text(temp_max[1],temp_max[0]," temp max "+str(temp_max[0])+"°C")

    x = [d for d in clean_data]
    y=list(clean_data.values())

    ax.plot_date(x,y,"-",label='temperature avg',color='m');  
    ax.legend(loc='upper left')
    plt.show()