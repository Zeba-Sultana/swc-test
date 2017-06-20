import sys
def temprature_check(temprature):
    if temprature > 25 :
        print("too hot")
    elif temprature >15 & temprature <= 25:
        print("Good")
    else:
        print("too cold")
    
    
#for temprature in range(5,30,5):
 # print("temprature is %d : %s" % (temprature,temprature_check(temprature)))

temprature = int(sys.argv[1])
temprature_check(temprature)   
