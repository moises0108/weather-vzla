import request,graphic
if __name__=='__main__':
    clean_data,temp_min,temp_max=request.get_data()
    print("temp min: "+str(temp_min))
    print("temp max: "+str(temp_max))
    graphic.graphic_temp(clean_data)