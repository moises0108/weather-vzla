import request,graphic
if __name__=='__main__':
    clean_data,temp_min,temp_max=request.get_data()
    graphic.graphic_temp(clean_data,temp_min,temp_max)