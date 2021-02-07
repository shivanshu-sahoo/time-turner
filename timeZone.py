
def UTC_offset(time_zone):
    time_zone= time_zone.lower()
    if (time_zone=="anat"):
        offset= "12"
    elif (time_zone=="aedt"): 
        offset= "11" 
    elif (time_zone=="aest"): 
        offset= "10"
    elif (time_zone=="jst"): 
        offset= "9"
    # elif (time_zone=="cst"): 
    #     offset= "8" 
    elif (time_zone=="wib"): 
        offset= '7'
    elif (time_zone=="bst"): 
        offset= '6'    
    elif (time_zone=="uzt"): 
        offset= '5'   
    elif (time_zone=="gst"): 
        offset= '4'
    elif (time_zone=="msk"): 
        offset= '3' 
    elif (time_zone=="eet"): 
        offset= '2'
    elif (time_zone=="cet"): 
        offset= '1'
    elif (time_zone=="gmt"): 
        offset= '0' 
    elif (time_zone=="cvt"): 
        offset= '-1' 
    elif (time_zone=="gst"): 
        offset= '-2' 
    elif (time_zone=="art"): 
        offset= '-3' 
    elif (time_zone=="vet"): 
        offset= '-4'
    elif (time_zone=="est"): 
        offset= '-5'
    elif (time_zone=="cst"): 
        offset= '-6'
    elif (time_zone=="mst"): 
        offset= '-7'
    elif (time_zone=="pst"): 
        offset= '-8'
    elif (time_zone=="akst"): 
        offset= '-9' 
    elif (time_zone=="mst"): 
        offset= '-10'
    elif (time_zone=="nut"): 
        offset= '-11'
    elif (time_zone=="aoe"): 
        offset= '-12'

    elif (time_zone=="lint"): 
        offset= '14'
    elif (time_zone=="nzdt"): 
        offset= '13'

    elif (time_zone=="acdt"): 
        offset= '10:30'
    elif (time_zone=="acst"): 
        offset= '9:30'
    elif (time_zone=="mmt"): 
        offset= '6:30'
    elif (time_zone=="ist"): 
        offset= '5:30'
    elif (time_zone=="aft"): 
        offset= '4:30'
    elif (time_zone=="irst"): 
        offset= '3:30' 
    elif (time_zone=="nst"): 
        offset= '-3:-30'  
    elif (time_zone=="mart"): 
        offset= '-9:-30' 

    elif (time_zone=="chadt"): 
        offset= '13:45'
    elif (time_zone=="acwst"): 
        offset= '8:45'
    elif (time_zone=="npt"): 
        offset= '5:45' 
    else:
        offset= '25'
                            
    return offset                                           
