
# ECSE3058
# Lab 1
# Daniel Robertson 
# 620139653

import math

#Question 1
def parallel(resistor_values):
    #Initializing Variable
    Res_Total=0

    for resistor in resistor_values:
        Res_Total = Res_Total + 1/resistor
    
    parallel_res = round((1/Res_Total),3)
    return(parallel_res)
    
resistor_values = [2000,1500,3000]
print(parallel(resistor_values), "Ohms")

    
#Question 2


def potential_divider(Voltage_Supply, Resistors): 
    Res_Total= 0
    for Res in Resistors:
        Res_Total = Res_Total + Res
    
    i= Voltage_Supply/ Res_Total
    
    for Res in Resistors:
        Voltage_Drop = round((Res * i),2)
        print(Voltage_Drop,"V")
#Assign values
potential_divider(9,[3000,1000])



#Question 3
def temperature_check(temp,unit):
    match unit:
        case "C":
            #Hypothermia Temperature in Celcius is below 35C
            if temp < 35: 
                print ("the patient is hypothermic")

            elif temp >= 35:
                print ("the patient's temperature is normal")

        case "F":
            #Hypothermia Temperature in Farenheit is below 95F
            if temp >= 95: 
                print ("the patient is hypothermic")

            elif temp < 95:
                print ("the patient's temperature is normal")


#Assign Values & Unit      
temperature_check(36,"F")