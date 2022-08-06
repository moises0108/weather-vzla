import matplotlib.pyplot as plt
def graphic_temp(clean_data:dict):
    fig,ax = plt.subplots() 

    ax.plot(list(clean_data.keys()),list(clean_data.values()));  
    plt.show()