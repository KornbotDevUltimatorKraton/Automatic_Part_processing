from audioop import reverse
from numbers import Complex
import os 
import math
import json
from tabnanny import check 
import pandas as pd
import subprocess 
import psycopg2 # Getting the data from the postgres database and insert the json file into the list of the data
from PyPDF2 import PdfFileWriter, PdfFileReader
import difflib
username = str(subprocess.check_output("uname -a",shell=True)) # Get the the username of the computer reading from the client computer 
Getusername = username.split("-")[0].split(" ")[1]  #Get the username
EXTRACT  = "/home/"+str(Getusername)+"/Automaticsoftware/tempolarydocextract" #Tempolary read the file extraction from the pdf specification function
PATHMAIN = "/home/"+str(Getusername)+"/Automaticsoftware/ComponentDoc"   # Getting the document page 
CONFIG   = "/home/"+str(Getusername)+"/Automaticsoftware/Configuresearch" # Config file

inputcomp = "bq25616" #Testlist={'drv8873','drv8846','bq25616','bq25731','drv8320','tps62750'}

#Getting the pins name data 
PinsNamepack = []
PinsNumpack  = []
IONamepack = [] # Getting the io name pack 
Packagingdata = {} 
PackagewithIO = {} 
completepack = {} 
completeioname = {} 
check_datatype = {}
Check_Packagename = []  # Checking the list of the package name inside the list 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
#For multipackages
Generate_Pinspack = []
Generate_Numpack = [] 
Generate_iopack = [] 
completeNumpack = {} # Getting the new pins name append into the dictionary 
completePinspack = {} #Getting the complete pins pack data
check_pack_order = {}   
check_pins_table = {} #Getting the pins table inside the list 
#Static parameters 
n = 1
n1 = 0
n2 = 2
n3 = 3

Classified_package = {'Multipackage':['NAME', 'NO.', 'nan', 'nan', 'nan'],'Singlepackage':['NAME', 'NO.', 'nan', 'nan']}
False_package_check = {'True':'Singlepackage','False':'Multiplepackage'} # Getting the True Single package data ad false multipackage

listConfig = os.listdir(CONFIG)
def Configure(configfile): 
     try: 
       data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
       datas = data.readline()
       transfer = json.loads(datas)
       return transfer
     except:
        print("Not found the configure file please check again")

def intersection(lst1, lst2):   # Fidning the intersection of 2 list 
    lst3 = [value for value in lst1 if value in lst2]
    return lst3 

config_data = Configure(listConfig[0])
print(config_data.get('pinsconfig').get('Pins')) # Finding the matching of the list in percentage using sequence matcher

Getting_pins_page = {} 
Packagename_Package_pins = {}
def Matchingdata_cal(checkpackage,listheader): 
                percent=difflib.SequenceMatcher(None,checkpackage,listheader)
                print("Match found:"+str(percent.ratio()*100)+"%") #Getting the percent matching 
                prob = percent.ratio()*100 # Calculate the percentage inside the list to find the max value in possibility detection 
                return  prob

#Checking if the package is only one package in the datasheet in the list  devices 


def max_index_cal(dictdatakeys,dictdatavav):
         cal_max = list(dictdatavav)
         keys_cal_max = list(dictdatakeys)
         max_index = max(cal_max)
         print(max_index,'Choosing',keys_cal_max[cal_max.index(max_index)])
         return max_index,keys_cal_max[cal_max.index(max_index)]  # Getting the value out from the max index calculation and the keys ca max data from the matching search from the index 
def SinglePackagecomponent(): 
                 for il in range(1,len(df[df.columns.values[n1]])):
                              print(str(il),df[df.columns.values[n1]].values[il]) #Getting the list if the pins testing 
                              PinsNamepack.append(df[df.columns.values[n1]].values[il])
                 for il in range(1,len(df[df.columns.values[n]])):
                              print(str(il),df[df.columns.values[n]].values[il]) #Getting the list if the pins testing 
                              PinsNumpack.append(df[df.columns.values[n]].values[il])

                 for il in range(1,len(df[df.columns.values[n2]])):
                              print(str(il),df[df.columns.values[n2]].values[il]) #Getting the list if the pins testing 
                              IONamepack.append(df[df.columns.values[n2]].values[il])

                 print(PinsNamepack)
                 print(PinsNumpack)
                 print(IONamepack)
                 for match in range(0,len(PinsNamepack)):
                           Packagingdata[PinsNamepack[match]] = PinsNumpack[match]
                 for re in range(0,len(PinsNamepack)):
                           PackagewithIO[PinsNamepack[re]] = IONamepack[re] # Mapping the gpio name  
                 completepack[inputcomp] = Packagingdata 
                 completeioname[inputcomp] =  PackagewithIO 
                 print(completepack)
                 print(completeioname) 
def MultiplePackagecomponent():
             pass
def Get_fullPinpage_cal(configdata):
#Calculate the number of page 
                       Orderableoackage = configdata.get("Orderablepackage").get("Orderable") #Getting the package data from the search intersection                  
                       print(Orderableoackage) 
                       Pinstable = configdata.get("Specific_pins").get("Pins_header") 
                       list_pack = os.listdir(EXTRACT+"/"+inputcomp+"/") 
                       
                       for t in range(0,total_page): 
                                  try: 
                                       print("Found file")
                                       getpage = t  
                                       df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(getpage)+".csv")
                                       print(df)
                                       print(df.values.tolist()[0]) # Getting the header of each table list to calculate the matching data               
                                       #Checking the pins order 
                                       probpinsdata = Matchingdata_cal(Pinstable,df.columns) # checking the columns matching data of the pins table inside the list 
                                       print("Matching prob",probpinsdata) # Checking the matching prob of the pins datatable 
                                       if probpinsdata >=83.33 and probpinsdata <= 100: # Checking if the data pins correct 100 percent inside the list
                                                check_pins_table[inputcomp+"_"+str(t)] = probpinsdata # Getting the data of the page to calculate the right page to extract all pins to concatinate data together
                                       #Checking the orderlist
                                       probdata = Matchingdata_cal(Orderableoackage,df.columns)  
                                       print("Matching prob ",probdata)
                                       check_pack_order[inputcomp+"_"+str(t)] = probdata # Getting the data of the page to calculate the right page matching probability 
                                                                              

                                  except: 
                                      print("File not found")     
                                                  
                       print(check_pack_order) #using the matching dicision to calculate the data possibility of detection 
                       print(check_pins_table)
                       #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                       print(Pinstable)
                       try:
                          #checking pins data inside the table 
                          detect_pins_vavs = check_pins_table.values() # Getting the value of the package type to make the csv page search automatically from the data detection function 
                          detect_pins_keys = check_pins_table.keys() # Getting the keys of the package type to make the data selection from the maximum order in the list 
                          percen_cal,filematched = max_index_cal(detect_pins_keys,detect_pins_vavs)  
                          print('Selecte Page ',filematched," % ",percen_cal) 
                          df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+filematched+".csv") # Getting the 
                          print(df.values.tolist()[0]) # Getting the header of each table list to calculate the matching data 
                       except: 
                              print("The matching function is empty")
                       try:
                             #checking order data in the table 
                             detect_order_vavs = check_pack_order.values() # Getting the value of the package type to make the csv page search automatically from the data detection function 
                             detect_order_keys = check_pack_order.keys() # Getting the keys of the package type to make the data selection from the maximum order in the list 
                             percen_cal,filematched = max_index_cal(detect_order_keys,detect_order_vavs) 
                             print('Selecte Page ',filematched," % ",percen_cal) 
                             df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+filematched+".csv") # Getting the 
                             print(df.values.tolist()[0]) # Getting the header of each table list to calculate the matching data               
                             #print("Getting the package name and amount of pins",df.values.tolist()[0][0],df.values.tolist()[0][2]) 
                       except: 
                            print("The matching function is empty")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Search the file and page of the data search to running in the loop and calculate pins page
#Getting the csv file and dataframe 
input1 = PdfFileReader(open(PATHMAIN+"/"+inputcomp+".pdf", "rb"))  #using oslist dir readding the file and extract all the value in the loop 
print(inputcomp+".pdf has %d pages." % input1.getNumPages())  # Getting the total pins of th page component 
total_page = input1.getNumPages() # Getting the total page of the document to running the search system on the list 

#Getting the pins name data                        
Get_fullPinpage_cal(config_data)
print(check_pins_table)
print(check_pack_order)
for p in range(0,len(check_pins_table)):
      numberpage = list(check_pins_table)[p].split("_")[1]
      print(numberpage)
      getpage = numberpage
      df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(getpage)+".csv")
      print(df) #Getting the data frame before extracting the name from the columns into the list and starte to running the editor in xml file
      print("Header name",df.values.tolist()[0])  # Specify the 2 difference package from component using second row of first column you will found nan on the list
      print(df.columns.values[n1]) #Getting the the columns 0 of the data frame testing getting name from the detected dataframe 
      for il in range(1,len(df[df.columns.values[n2]])):
                              print(str(il),df[df.columns.values[n2]].values[il]) #Getting the list if the pins testing 
                              IONamepack.append(df[df.columns.values[n2]].values[il])                        
      print("Header name",df.values.tolist()[0])  # Specify the 2 difference package from component using second row of first column you will found nan on the list
      print("Second name",df.values.tolist()[1])  # Specify the 2 difference package from component using second row of first column you will found nan on the list
      headerpackage = df.values.tolist()[0] 
      Secondpackage = df.values.tolist()[1]
      #Calculate the percentage of the classified package
      for i in list(Classified_package):
               probdata = Matchingdata_cal(Classified_package.get(i),headerpackage) 
               check_datatype[i] =  int(probdata) # 
               print(check_datatype)
      print(check_datatype)
      cal_max = list(check_datatype.values())
      keys_cal_max = list(check_datatype.keys())
      max_index = max(cal_max)
      print(max_index,'Choosing',keys_cal_max[cal_max.index(max_index)])
      #Decision making from the search package data 
      search_type = keys_cal_max[cal_max.index(max_index)] # Getting the search type data to make the dicision of package selection 

      if Secondpackage[1].isnumeric() == True: 
                 print('Check package Single package') 
                 print('Checking the number of pins to calculate the page protocol ........')
                 for il in range(1,len(df[df.columns.values[n1]])):
                              print(str(il),df[df.columns.values[n1]].values[il]) #Getting the list if the pins testing 
                              PinsNamepack.append(df[df.columns.values[n1]].values[il])
                 for il in range(1,len(df[df.columns.values[n]])):
                              print(str(il),df[df.columns.values[n]].values[il]) #Getting the list if the pins testing 
                              PinsNumpack.append(df[df.columns.values[n]].values[il])

                 for il in range(1,len(df[df.columns.values[n2]])):
                              print(str(il),df[df.columns.values[n2]].values[il]) #Getting the list if the pins testing 
                              IONamepack.append(df[df.columns.values[n2]].values[il])

                 print(PinsNamepack)
                 print(PinsNumpack)
                 print(IONamepack)
                 for match in range(0,len(PinsNamepack)):
                           Packagingdata[PinsNamepack[match]] = PinsNumpack[match]
                 for re in range(0,len(PinsNamepack)):
                           PackagewithIO[PinsNamepack[re]] = IONamepack[re] # Mapping the gpio name  
                 completepack[inputcomp] = Packagingdata 
                 completeioname[inputcomp] =  PackagewithIO 
                 print(completepack)
                 print(completeioname) 


           #Checking of the package is multiple package ins the same page 
      elif Secondpackage[1].isnumeric() == False: 
                 print('Check package Multi package')
                 print('Checking the number of pins to calculate the page protocol ........') #This function will be running before calculate the page number of the list function 
                 #Checking the number of package inside 
                 for ir in Secondpackage:
                           if str(ir).isalpha() == True: 
                                 print("Nan package name")
                           elif str(ir).isalpha() == False: 
                                 Check_Packagename.append(ir)

                 print(Check_Packagename)
                 sortcheck = sorted(Check_Packagename,reverse=True)
                 Package_number = len(Check_Packagename)
                 Num_data = len(Check_Packagename) +1 #Getting the pins number 
                 io_data = len(Check_Packagename)+2 #Getting the package for the io data  
                 for il in range(2,len(df[df.columns.values[n1]])):
                              print(str(il),df[df.columns.values[n1]].values[il]) #Getting the list if the pins testing 
                              Generate_Pinspack.append(df[df.columns.values[n1]].values[il])
                 
                 for re in range(0,len(Check_Packagename)): 
                                print("Create array for pins",re)  
                                Generate_Numpack.append([])

                 for re in range(0,len(sortcheck)):
                              try: 
                                 for il in range(2,len(df[df.columns.values[re+1]])):
                                              print(str(il),df[df.columns.values[re+1]].values[il]) #Getting the list if the pins testing 
                                              Generate_Numpack[re].append(df[df.columns.values[re+1]].values[il])
                                 
                              except:
                                    print("Out of range")
                 print('Generate numpack',Generate_Numpack) 
                 #Fix this part of code 
                 for checknumgpio in range(0,len(Generate_Numpack)):
                        if Generate_Numpack[checknumgpio] !=[]:      
                              print(Generate_Numpack[checknumgpio])
                              completeNumpack[Check_Packagename[checknumgpio]] = Generate_Numpack[checknumgpio]
                                                            
                 print(completeNumpack)
                 for w in list(completeNumpack):
                        
                        print(w,completeNumpack.get(w))
                        numpack_list = completeNumpack.get(w)  # Getting the numpack list data 
                        for ty in range(0,len(numpack_list)):
                         
                              completepack[Generate_Pinspack[ty]] =  numpack_list[ty]                             
                        completePinspack[w] = completepack            
                 print(completePinspack)
                
                
                 