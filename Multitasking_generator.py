from array import array
from decimal import FloatOperation
from getpass import getpass
from http.client import IncompleteRead
from multiprocessing import Process, Value, Array
from socketserver import ThreadingUnixDatagramServer
import threading # Running multithread
import multiprocessing # Getting the multi tasking function 
import re # Regular expression word 
import os #Operating system onboard 
import glob
import subprocess
import typing_extensions
import datetime #Getting the datetime for log the data of the input
import xml.etree.ElementTree as ET #Getting the xml tree reading the data from the 
from PyPDF2.generic import FloatObject
from numpy import left_shift
from numpy.lib.histograms import _histogram_bin_edges_dispatcher
from numpy.lib.utils import byte_bounds
from pyfirmata.pyfirmata import Pin #Subprocess for processing the command and extract string from the terminal
import camelot # Extract the data table from the pdf file
from PyPDF2 import PdfFileWriter, PdfFileReader
import difflib #Finding the similarlity of the matching sequence 
import wordninja
import json
import pandas as pd
import shutil 
#Getusername = getpass.getuser()
mode = 0o777
try:
   os.mkdir("ComponentDoc",mode) #Get the documentation of the components 
   os.mkdir("tempolarydocextract",mode) #Get the data extract from the table of the pdf part specification
   os.mkdir("Configuresearch",mode) #Create the configure file for the search in json 
   os.mkdir("Packagelibrary",mode)  #Create the package 
   direct_create = ['ComponentDoc','tempolarydocextract','Configuresearch','Packagelibrary'] 
   try:
     for i in direct_create:
          os.system("echo 'Rkl3548123#' | sudo -S "+"sudo chmod -R 777 "+str(i))  
   except: 
      print("Directory was created!") 
except: 
    print("Directory clreated")
username = str(subprocess.check_output("uname -a",shell=True)) # Get the the username of the computer reading from the client computer 
Getusername = username.split("-")[0].split(" ")[1]  #Get the username
PATHMAIN = "/home/"+str(Getusername)+"/Automaticsoftware/ComponentDoc"
HOME = "/home/"+str(Getusername)+"/Automaticsoftware/"
EXTRACT  = "/home/"+str(Getusername)+"/Automaticsoftware/tempolarydocextract" #Tempolary read the file extraction from the pdf specification function
CONFIG   = "/home/"+str(Getusername)+"/Automaticsoftware/Configuresearch" # Config file
PACKAGEDIR = "/home/"+str(Getusername)+"/Automaticsoftware/Packagelibrary" #Package library generated file
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# List file in the path directory on each 
listMainpath = os.listdir(PATHMAIN)  #Get the main path of the directory 
listExtract = os.listdir(EXTRACT)    #Get the extraction of the data tables in the component information pins configurection 
listConfig = os.listdir(CONFIG) #Get the list config file from the system 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#for page in input1.pages:
         
#            print(page,page.extractText())
#first_page = input1.getPage(3)
#print(first_page.extractText())
#print(wordninja.split(str(first_page.extractText())))
listConfig = os.listdir(CONFIG) #Get the config file 
Checkgeneratedfile = [] #Getting the generated file in the csv form from dictionary file
Pageclassification = [] # Save the page classification for predeict the next page output from the boundary configuretion on the json file
Packagecheck = []  # Checking the len of the list package 
Pinsquantity = []  # Get the quantity of the pins on the ic 
reforder =  []  #Save the reference breakpage order  
predictorder = [] #Save the 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
        #list devices bugget and combine for the table data type page processing
Devicesname = [] #Getting the devices name paring
Devicelist = {} #Get the list dictionary of paring group device package name 
Deviceodd = [] #Getting the device odd 
Deviceeven = [] #Getting the device even 
Devicesbucket = [] # Device bucket for the page processing 
Packagetypebucket = [] #Package type for the page processing 
Pinsbucket = [] # Getting the pins bucket data for the value of each package type data combination dictionary
reftabledetect = [] # Get the table detector referent inside the array 
refpins = [] #Get the reference pins 
refpagecal = [] # Get the referent page from the page classification algorithm
nextpage = [] #Get the prediction page 
Specpage = [] #Get the spec page data 
combinedictdata = {}  # Get the dictionarylist of the data output for page processingfunction 
Predictbreak = {} # Get the reference page and prediction page for 
Pinsextract = {} # Generate the dictionary for the page reference and the next page prediction 
csvmergepare = {} #Generate the paring csv for merging page data 
Paringlist = [] #Getting the list inside the key of the csv merge page 
Dataodd = [] #Getting the data odd 
Dataeven = [] #Getting the data even
Drifgroup = {} #Get the drif group from the table to recombine with the other directory 
Normalgroup = [] #Get the the normal group list for regrouping with the drif group
Regrouping = {} #The last grouping for the path copy renew directory for merching new order csv file
Basedir = [] #Get the base dir for modify the new directory for new group order 
Newdir = [] #Get the new directory list for putting the fileinto the group 
memdat = [] #Getting the memory of 
memtable = []
Numberfile = [] #Getting number from file csv
PinsName = [] #save append pins name of the mcu or the ic from the data table 
PinsPackage = {} #Getting the Pins list 
Typeofpins = []
PinsNumbers = [] #Getting this number for sorting
Descryptionfunction = [] #Getting the descryption function for the nlp processing data from the table
outloop = [] #Gettin the out loop data 
Datainnerloop = {} #Getting the data inner loop
rawpackdrawing = [] #Getting the raw package data with nan 
Packagedrawing = [] #Getting the package drawing list
Deviceindexheader = []
DeviceNamepack = [] #Getting the device name 
pinsclarify = []
Packagedevice = {} #Gettin the device name pack and the package type 
Packageorder = {}
DictionaryPinsdata = {} #making the type of the pins dictionary data 
NewPinsNamesorted = []
Gateconnect = []
Connectsrecord = {}
reconnect = []
reconnex = {}
SequenceMax = {}
NewKeypins = []
DictionaryPinsdata2 = {}
NewdictPinsdata = {}
refsortindex = []
Packafuldata = [] #Getting the packful data for the 
recordheader = {} #Recording the header file into the csv for writing the condition 
recordheader2 = {} #Recording the header file into the csv for writing the condition 
Numberfile2 = []
getnewjson = {} 
Packageslist  = open(CONFIG+"/"+listConfig[0],'r')# Reading the configfile 
Packagedatalist = Packageslist.readline()
PackagesLoad = json.loads(Packagedatalist)

print(PackagesLoad.get('package').get('packagesdrawing')) #Get the package of the ic for adding into the list detected 
def Pagecalculation(outputinterger): 
   if int(outputinterger) <= 144:
          print("In the range of package pins=",outputinterger)
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
               # Put the page calculation here for the 
def Configure(configfile): 
     try: 
       data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
       datas = data.readline()
       transfer = json.loads(datas)
       return transfer
     except:
        print("Not found the configure file please check again")
def Modeextractnotable(datapins,df,listdata,q): 

                  if str(listdata[q]).split(" ")[0] in datapins:
                          print("Found the header",listdata[q],"Begin extraction....") # Activate actraction begin 
                          for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])

                  if listdata[q] in datapins: 
                       print("Found the header",listdata[q],"Begin extraction....") # Activate actraction begin 
                       for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])
                              print(Pinsquantity.append(str(df[listdata[q]].values[i])))
def Modeextracttion(datapins,transfer,df,listdata,q):
               # TI pattern pinconfigureation table 
               # Pins configure 

                 
                  devicename = transfer.get("Device").get("devices") #Extracting the pins name from the TI 
                  packagedevice = transfer.get("Device").get("packagedata") # Get the Description text 
                  pinsnumber = transfer.get("Device").get("pins") #Get the pins number from the device package from the pdf file
                  Devices = ['Device']
                  Package = ['Package\nType']
                  Pinsnumber = ['Pins']
                  if datapins[0] == "Device":
                    print("Get the Device  name")  
                    if listdata[q] in datapins: 
                       print("Found the header",listdata[q],"Begin extraction string....") # Activate actraction begin 
                       for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])
                              print(Devicesbucket.append(str(df[listdata[q]].values[i])))
                  if datapins[0] == "Package\nType":
                    print("Get the Device  name")  
                    if listdata[q] in datapins: 
                       print("Found the header",listdata[q],"Begin extraction string....") # Activate actraction begin 
                       for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])
                              print(Packagetypebucket.append(str(df[listdata[q]].values[i]))) 
                  if datapins[0] == "Pins":
                    print("Get the Device  name")  
                    if listdata[q] in datapins: 
                       print("Found the header",listdata[q],"Begin extraction string....") # Activate actraction begin 
                       for i in range(1,len(df[listdata[q]])):
                              print(i,df[listdata[q]].values[i])
                              print(Pinsbucket.append(str(df[listdata[q]].values[i]))) 
#Bit bucket for the combine                                                      
def Bucketcombinefunc(devicesinput,Packagetypebucket,Pinsbucket): # Get the list from each package input  
       print("Combine each package datainto the dict") # The function to combine the dictionary file into the dictionary 
       for qw in range(0,len(devicesinput)):  # using qw to get the value in the list array 
                   print("Begin creating the dictionary data function") 
                   combinedictdata[str(devicesinput[qw])] = str(Packagetypebucket[qw])+","+str(Pinsbucket[qw])  #Get the list variable to generate the json and dictionary data structure                  
                   
def extractionalgorithm(df,listdata,configfile):
          # In the case not detected table running this function 
          try: 
              print(configfile)
              data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
              datas = data.readline()
              transfer = json.loads(datas)
              print(transfer)
          except:
              print("Not found the configure file please check again")

          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          # TI pattern for the extraction
          datapinname = transfer.get("pinsconfig").get("Pins") #Getting the pins list 
          datapins = transfer.get("Unnamed").get("Unnamed") #Extracting the pins name from the TI 
          description = transfer.get("Description").get("description") # Get the Description text 
          inputoutput = transfer.get("IO").get("io") #IO get the input output pins function matching pins
          print(inputoutput)
          print(description) 
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
               # Pins configure 
          for q in range(0,len(listdata)): 
                  Modeextractnotable(datapinname, df, listdata, q) ,Modeextractnotable(description, df, listdata, q),Modeextractnotable(datapins, df, listdata, q) 
def extractpinspackage(df,listdata,configfile): 
           print("Begin extraction the pins and package from the package information page")
           try: 
              print(configfile)
              data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
              datas = data.readline()
              transfer = json.loads(datas)
              print(transfer)
           except:
              print("Not found the configure file please check again")

          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          # TI pattern for the extraction

           devicename = transfer.get("Device").get("devices") #Extracting the pins name from the TI 
           packagedevice = transfer.get("Device").get("packagedata") # Get the Description text 
           pinsnumber = transfer.get("Device").get("pins") #Get the pins number from the device package from the pdf file
           print(devicename)  # Using the first one as the key 
           print(packagedevice) # First value 
           print(pinsnumber) # Second value 
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
               # Pins configure 
           listMode = [['Device'],['Package\nType'],['Pins']]            
           for q in range(0,len(listdata)):     
                  print(Modeextracttion(listMode[0],transfer,df,listdata,q))
           for q in range(0,len(listdata)): 
                  print(Modeextracttion(listMode[1], transfer, df, listdata, q))
           for q in range(0,len(listdata)): 
                  print(Modeextracttion(listMode[2], transfer, df, listdata, q))
def Tabledetector(input1,inputcomp,Pinsquantity,searchpinsconfiguretion): 
        #Pinsearchfunction(input1,searchpinsconfiguretion)
        for i in reversed(range(0,input1.getNumPages())):  # Running the page for the back checking 
         first_page = input1.getPage(i)
         print(first_page.extractText())
         print(wordninja.split(str(first_page.extractText())))
         outputdat = str(first_page.extractText())
         Extracteddata = wordninja.split(str(first_page.extractText())) # Get the list to searching the pattern of the product type
         if 'PACKAGING'in Extracteddata: 
                   print("Found package")
                   if 'INFORMATION' in Extracteddata: 
                                  print("Found information break....")
                                  print("".join(Extracteddata))
                                  packlist = PackagesLoad.get('package').get('rootpackages')
                                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                                  print("Case 1")  
                                  tables = camelot.read_pdf(PATHMAIN +"/"+str(inputcomp)+".pdf",pages=str(i))
                                  if len(tables) == 0: 
                                         print("Not Found the data table",len(tables))
                                         for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")
                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              print(Pinsquantity.append(str(outputinterger)))

                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)   
                                                              print(Pinsquantity.append(str(outputinterger)))
                                                              if int(outputinterger) <= 144:
                                                                      print("In the range of package pins=",outputinterger)

                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                                      #one page output calculation   
                                          except:
                                             print("This part is not found in the list package")
                                  if len(tables) > 1:
                                         #Data table found then classify and extract the pins and packages 
                                         print("Found the data table",len(tables)) 
                                         print(tables[0].df)
                                         print(tables[0].parsing_report)
                                         tables[0].to_csv(EXTRACT +"/"+str(inputcomp)+'.csv') 
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         print("Reading pandas....")
                                         df = pd.read_csv (r''+EXTRACT+"/"+str(inputcomp)+'.csv')
                                         print(df)
                                         print(Configure(listConfig[0])) # Get the data from the json file
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         # Algorithm for classify the extraction of the text 
                                         index = df.index
                                         number_of_rows = len(index)
                                         print(number_of_rows)
                                         listdata = list(df.columns.values)
                                         print(listdata)
                                         extractpinspackage(df,listdata,listConfig[0])
                                  
                                  break
         if 'PACKAGE'in Extracteddata: 
                   print("Found package")
                   if 'MATERIALS' in Extracteddata: 
                           print("Found Material")
                           if 'INFORMATION' in Extracteddata: 
                                  print("Found information break....")
                                  print("".join(Extracteddata))
                                  packlist = PackagesLoad.get('package').get('rootpackages')
                                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                                  print("Case 2")
                                  tables = camelot.read_pdf(PATHMAIN +"/"+str(inputcomp)+".pdf",pages=str(i))
                                  if len(tables) == 0: 
                                         print("Not Found the data table",len(tables))
                                         for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   print(outputinterger)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(wordninja.split(str(outputinterger)))
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")

                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         print(wordninja.split(str(outputinterger)))
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              print(Pinsquantity.append(str(outputinterger)))

                                                              if outputinterger <=144: 
                                                                     print("In the ranage of the package pins",outputinterger) 
                                                                     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                                                    #Get the page calculation here  
                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              print(Pinsquantity.append(str(outputinterger)))

                                                              if outputinterger <= 144:
                                                                      print("In the range of package pins",outputinterger)
                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                   break                                       
                                          except:
                                             print("This part is not found in the list package")  
                                  if len(tables) >= 1:
                                         print("Found the data table",len(tables))
                                         reftabledetect.append(str(len(tables))) # checking the len after fererence if found then equal 1 
                                         print(tables[0].df)
                                         print(tables[0].parsing_report)
                                         tables[0].to_csv(EXTRACT +"/"+str(inputcomp)+'.csv') 
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         print("Reading pandas....")
                                         df = pd.read_csv (r''+EXTRACT+"/"+str(inputcomp)+'.csv')
                                         print(df)
                                         print(Configure(listConfig[0])) # Get the data from the json file
                                         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                         # Algorithm for classify the extraction of the text 
                                         index = df.index
                                         number_of_rows = len(index)
                                         print(number_of_rows)
                                         listdata = list(df.columns.values)
                                         print(listdata)
                                         extractpinspackage(df,listdata,listConfig[0])
                                  break
def CheckingPins(input1):
       for i in reversed(range(0,input1.getNumPages())):  # Running the page for the back checking 
         first_page = input1.getPage(i)
         print(first_page.extractText())
         print(wordninja.split(str(first_page.extractText())))
         outputdat = str(first_page.extractText())
         Extracteddata = wordninja.split(str(first_page.extractText())) # Get the list to searching the pattern of the product type
         if 'PACKAGING'in Extracteddata: 
                   print("Found package")
                   if 'INFORMATION' in Extracteddata: 
                                  print("Found information break....")
                                  print("".join(Extracteddata))
                                  packlist = PackagesLoad.get('package').get('rootpackages')
                                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                                  print("Case 1")
                                  for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")
                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)   
                                                              if int(outputinterger) <= 144:
                                                                      print("In the range of package pins=",outputinterger)
                                                                      Packagecheck.append(outputinterger)
                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                                      #one page output calculation   
                                                          
                                          except:
                                             print("This part is not found in the list package")
                                  break
         if 'PACKAGE'in Extracteddata: 
                   print("Found package")
                   if 'MATERIALS' in Extracteddata: 
                           print("Found Material")
                           if 'INFORMATION' in Extracteddata: 
                                  print("Found information break....")
                                  print("".join(Extracteddata))
                                  packlist = PackagesLoad.get('package').get('rootpackages')
                                  packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                                  print("Case 2")
                                  for i in range(0,len(packlist)):
                                          check = any(item in wordninja.split(str(packlist[i])) for item in Extracteddata)
                                          print(check)
                                          try:
                                             if check == True: 
                                                   print(Extracteddata[Extracteddata.index(packlist[i])])
                                                   print(wordninja.split(str(packlist[i])),len(wordninja.split(str(packlist[i]))))
                                                   outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(packlist[i])))]
                                                   check2 = any(item in wordninja.split(str(outputinterger)) for item in Extracteddata)
                                                   print(outputinterger)
                                                   if outputinterger.strip().isdigit():
                                                         print("Output is Number")
                                                         print(wordninja.split(str(outputinterger)))
                                                         print(outputinterger) #Get tge output here to calculate the page output data 
                                                   else:
                                                      print("Output is string")

                                                      if check2 == True:
                                                         print("Check loop 2")
                                                         print(wordninja.split(str(outputinterger)))
                                                         if len(outputinterger) >1:
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              if outputinterger <=144: 
                                                                     print("In the ranage of the package pins",outputinterger) 
                                                                     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                                                    #Get the page calculation here  
                                                         if len(outputinterger) == 1: 
                                                              print("detected len integer")
                                                              outputinterger = Extracteddata[Extracteddata.index(packlist[i])+len(outputinterger)+len(wordninja.split(str(outputinterger)))+len(wordninja.split(str(packlist[i])))]
                                                              print(outputinterger)
                                                              if outputinterger <= 144:
                                                                      print("In the range of package pins",outputinterger)
                                                                      Packagecheck.append(outputinterger) #Get the output integer of the pins and save into the package check list to classify the pins 
                                                                      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
                                                                                    #Get the page calculation here 
                                                   break                                       
                                          except:
                                             print("This part is not found in the list package")         
                                  break
def Pinsearchfunction(input1,inputcomp,searchpinsconfiguretion):   
               input1 = PdfFileReader(open(PATHMAIN+"/"+inputcomp+".pdf", "rb"))
               pagenumber = input1.getNumPages()
               print(pagenumber)
               for i in range(0,int(pagenumber)):
                   print("Page",i)
                   first_page = input1.getPage(i)
                   first_page.extractText()
                   dataextract =  wordninja.split(str(first_page.extractText()))
                   print(dataextract)
                   datasearch = str(searchpinsconfiguretion).split(" ") 
                   print(datasearch)
                   #check2 = any(item in dataextract for item in datasearch)
                   check2 = bool(set(datasearch)&set(dataextract))
                   packdrawing = PackagesLoad.get('package').get('packagesdrawing')
                   boundary = ['0','1','2']
                   check0 = any(item in list(str(i)) for item in boundary) # Setting default check bundary 
                   if check0 == False:
                      print("Check false page")
                      print("Check list 2:",check2)
                      if check2 == True:
                                  print("Found the Pins configuretion","page",str(i))
                                  break

                
# Search specification function 
def SpecificationExtract(input1,searchSpecification): 
       print("Start the specification extraction....") #Specification page extraction 
       for i in range(3,input1.getNumPages()):  # Running the page for the back checking 
                  first_page = input1.getPage(i)
                  print(wordninja.split(str(first_page.extractText())))
                  outputdat = str(first_page.extractText())
                  Extracteddata = wordninja.split(str(first_page.extractText())) # Get the list to searching the pattern of the product type
                  print(Extracteddata)
                  datasearch = str(searchSpecification).split(" ")
                  boundary = ['0','1','2']
                  check0 = any(item in list(str(i)) for item in boundary) # Setting default check bundary
                  print(check0)
                  if datasearch[0] in Extracteddata: 
                            print(str(i),Extracteddata)
                            Specpage.append(str(i)) #Toget the number of real page you need to +1 beacause it's started from 0
                            first_page = input1.getPage(i)
                            print(first_page.extractText()) 
                            break         
def SpecificationExtract2(input1,searchSpecification): 
       print("Start the specification extraction....") #Specification page extraction 
       for i in range(3,input1.getNumPages()):  # Running the page for the back checking 
                  first_page = input1.getPage(i)
                  print(wordninja.split(str(first_page.extractText())))
                  outputdat = str(first_page.extractText())
                  Extracteddata = wordninja.split(str(first_page.extractText())) # Get the list to searching the pattern of the product type
                  print(Extracteddata)
                  datasearch = str(searchSpecification).split(" ")
                  boundary = ['0','1','2']
                  check0 = any(item in list(str(i)) for item in boundary) # Setting default check bundary
                  print(check0)
                  if datasearch[0] in Extracteddata: 
                            print(str(i),Extracteddata)
                            Specpage.append(str(int(i)+1)) #Toget the number of real page you need to +1 beacause it's started from 0
                            first_page = input1.getPage(i)
                            print(first_page.extractText()) 
                            break                                                       

def Classifypagematch(input1,inputcomp,Pinsquantity,Packagecheck):
             print("Begin predict the next page")
             pageclassifylist = PackagesLoad.get("Pageclassify")
             #print(pageclassifylist)
             print(Packagecheck,Pinsquantity) # Show the input page variable and the pins quantity 
             val_list = list(pageclassifylist.values())  # Get the page classify list 
             print(val_list)
             for i in range(0,len(val_list)):
                    try: 
                        if int(val_list[i][0]) <= int(Pinsquantity[0]) <= int(val_list[i][1]): 
                           try:
                                 position = val_list.index(val_list[i])
                                 print("Array position",position)
                                 print(list(pageclassifylist)[position])
                                 if int(list(pageclassifylist)[position]) == 1:
                                         savenextpage = int(Packagecheck[0])+int(list(pageclassifylist)[position])-1
                                         Packagecheck.append(str(savenextpage))
                                         print(Packagecheck[0])      
                                         refpagecal.append(Packagecheck[0]) #Get the reference of the page  
                                 if int(list(pageclassifylist)[position]) >= 2:
                                         
                                         refpage =  int(Packagecheck[0])+int(list(pageclassifylist)[position])-1 # ref starter page 
                                         savenextpage = int(Packagecheck[0])+int(list(pageclassifylist)[position]) #Real page in the document 
                                         Packagecheck.clear() # Clear the recent page before append the new page 
                                         Packagecheck.append(str(savenextpage)) # Real page classification 
                                         print(refpage) # Get the reference starter page 
                                         print(Packagecheck[0])      
                                         refpagecal.append(refpage) #Get the reference of the page in array mode 
                                         #Pageclassification.append(refpagecal[0]) # replace the refernce page into the starter page
                                         nextpage.append(Packagecheck[0]) # Next page append  in array mode    
                                                                 
                                 break
                           except:
                               print("Not in the list",str(i))
                    except: 
                        print("Not in the list",str(i))       
def Classifyselectionfunction(input1,inputcomp,Pinsquantity,Packagecheck,reftabledetect,combinedictdata): #Get the reftable for setting the condition function and the combination dictionary data for get the key and value of the ic  
                    print("Classify the reference detection",str(reftabledetect))
                    if str(reftabledetect) == '1':
                           print("Detected table in the page")
                           for w in range(0,len(list(combinedictdata))):
                                     print("#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                     print(str(w),list(combinedictdata)[w])
                                     Devicesname.append(list(combinedictdata)[w]) #Getting the combine dictionary 
                                     pinsoutput = combinedictdata.get(str(list(combinedictdata)[w])).split(",")[1] # Get the pins out from the string to add the array value into the classification base 
                                     #Reference 
                                     refpins.append(pinsoutput)# add the reference pins and clear after running the new process 
                                     print("Pins number",refpins[0])
                                     Classifypagematch(input1,inputcomp,refpins,Packagecheck) #Get the refpins into the loop and calculate the page from the input estimation 
                                     #after add the estimation page delete the refpins to be ready for adding the new one
                                     refpins.clear() # Clear the refferent pins 
                                     print(refpagecal) # Adding the reference page int the array 
                                     #Getting the refpage and the predictpage 
                                     print("#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                     
                    if str(reftabledetect) == '0': 
                           print("Not detected table in the page") 
                           Classifypagematch(input1,inputcomp,Pinsquantity,Packagecheck) #Get the refpins into the loop and calculate the page from the input estimation 
def Devicenameparing(combinedictdata): #Device name paring function 
      print("Start paring devices name")
      Devicelist = list(combinedictdata)
      for i in range(0,len(Devicelist)):
                     if i%2 == 0: 
                          Deviceeven.append(Devicelist[i])
                          print("Device even:",Deviceeven)
                     if i%2 == 1: 
                          Deviceodd.append(Devicelist[i])
                          print("Device odd",Deviceodd)
def Groupingdevicelist(Deviceeven,Deviceodd):
      try:                
          for kr in range(0,len(Deviceeven)):
                  Devicelist[str(kr)] = str(Deviceeven[kr]) +","+str(Deviceodd[kr])
      except:
            print("Out of range")
            if len(Deviceeven) > len(Deviceodd): 
                   print("Paring add new order in group....")
                   print(str(Deviceeven[len(Deviceeven)-1]))
                   Devicelist[str(len(Deviceodd))] = str(Deviceeven[len(Deviceeven)-1])
                   print(Devicelist)
                   
            if len(Deviceeven) < len(Deviceodd): 
                   print("Paring add new order in group....")     
                   Devicelist[str(len(Deviceeven))] = str(Deviceodd[len(Deviceodd)-1])
                   print(Deviceodd)

def SavebreakPinsconfigtable(referencepage,predictnextpage,Specpage): # Getting the page reference and predict page specpage input 
       print("Start save breaking pinsconfig......")  # Breaking end configuretion page 
       for s in range(0,len(referencepage)):
                  print("Starting.....") #Getting the page comparation into the loop 
                  try:
                     reforder.append(str(referencepage[s]))     
                     predictorder.append(str(predictnextpage[s]))     #Running until found the break order 
                  
                     if int(referencepage[s]) == int(Specpage[0]): 
                              print(referencepage[s]) #reference page compare specpage number 
                              reforder.remove(reforder[s])
                              break 
                     if int(predictnextpage[s]) == int(Specpage[0]): 
                              print(predictnextpage[s])
                              predictorder.remove(predictnextpage[s])
                              break
                  except: 
                       print("No need table paring !")          

def Retrivepage(reforder,predictorder):
           print("Retrieving page order")
           for r in range(0,len(reforder)): 
                     print("Create the dictionary....")
                     try: 
                         Predictbreak[str(r)] = str(reforder[r])+","+ str(predictorder[r])  #Make the dictionary porder prediction list for textracting the certain devices 
                         print(Predictbreak) # Show the predict page dictionary
                     except: 
                           print("Out of range list...") # Find the outrange dictionary and add the value into the dictionary list
                           if len(reforder) < len(predictorder):
                              Predictbreak[str(len(predictorder)-1)] = str(predictorder[len(predictorder)-1])
                              print(Predictbreak)
                           if len(reforder) > len(predictorder): 
                              Predictbreak[str(len(reforder)-1)] = str(reforder[len(reforder)-1])
                              print(Predictbreak)    

def Groupingpinextractor(Pathway,pagevalue,tables,varm,megaposition): 
         tables[int(len(tables))-int(varm)].df
         print("Found the data table",len(tables))
         print(tables[int(len(tables))-int(varm)].df)
         print(tables[int(len(tables))-int(varm)].parsing_report)
         tables[int(len(tables))-int(varm)].to_csv(Pathway +"/"+str(inputcomp)+"_"+str(pagevalue)+"_"+str(megaposition)+'.csv') 
         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
         print("Reading pandas....")
         df = pd.read_csv (r''+Pathway+"/"+str(inputcomp)+"_"+str(pagevalue)+"_"+str(megaposition)+'.csv')
         print(df)
         print(Configure(listConfig[0])) # Get the data from the json file
         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
         # Algorithm for classify the extraction of the text 
         index = df.index
         number_of_rows = len(index)
         print(number_of_rows)
         listdata = list(df.columns.values)
         print(listdata)
def Grouploopanalysis(Pathway,pagevalue,tables):
   for i in range(0,len(tables)): 
         tables[i].df
         print("Found the data table",len(tables))
         print(tables[i].df)
         print(tables[i].parsing_report)
         tables[i].to_csv(Pathway +"/"+str(inputcomp)+"_"+str(pagevalue)+"_"+str(i)+'.csv') 
         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
         print("Reading pandas....")
         df = pd.read_csv (r''+Pathway+"/"+str(inputcomp)+"_"+str(pagevalue)+"_"+str(i)+'.csv')
         print(df)
         print(Configure(listConfig[0])) # Get the data from the json file
         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
         # Algorithm for classify the extraction of the text 
         index = df.index
         number_of_rows = len(index)
         print(number_of_rows)
         listdata = list(df.columns.values)
         print(listdata)
def Cutheader(Pathdata): 
       print("Removing header data") #Removing the header data
       listcut = os.listdir(Pathdata)
       for rt in range(0,len(listcut)): 
               print("list directory from path",listcut[rt]) 
               listfile = os.listdir(Pathdata+"/"+listcut[rt]) 
               if len(listfile) >= 2: 
                        for ik in range(0,len(listfile)):
                                 
                                 if ik%2 == 1:
                                         
                                        print("Getting the file name to cut header",listfile[ik]) # Getting the list of the file name from the odd numner after grouping the file
                                        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                              #Getting the file name for extracting 
                                        df = pd.read_csv(Pathdata+"/"+listcut[rt]+"/"+listfile[ik]) #Getting the filename and running the head custter and replace the old file before merging data
                                        print(df) #Getting the data frame of the original csv header mark 
                                        print(df.values.tolist()) #Getting the data in list 
                                        #Getting the function of the header cutter
                                        memdat.clear() #Clear the memdat before adding the new list of the dataset 
                                        for ir in range(0,len(df.values.tolist())):
                                                extractdat = df.values.tolist()[ir]
                                                print(extractdat)
                                                memdat.append(extractdat)  #Getting the extract data from the dataset 
                                        memdataextract(Pathdata)
                                       #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
def memdataextract(Pathdata): 
       print("Removing header beginn") #Removing the header data
       listcut = os.listdir(Pathdata)
       for rt in range(0,len(listcut)): 
               print("list directory from path",listcut[rt]) 
               listfile = os.listdir(Pathdata+"/"+listcut[rt]) 
               if len(listfile) == 2: 
                        for ik in range(0,len(listfile)):  
                                 if ik%2 == 1:
                                    for rl in range(0,1):
                                       memdat.remove(memdat[rl]) 
                                        
                        da = pd.DataFrame(memdat)
                        da.to_csv(r""+Pathdata+"/"+listcut[rt]+"/"+listfile[ik]) #Getting the file header cut off to convert into the csv file
def precisecuthead(Pathdata): 
       print("Removing header data") #Removing the header data
       listcut = os.listdir(Pathdata)
       for rt in range(0,len(listcut)): 
               print("list directory from path",listcut[rt]) 
               listfile = os.listdir(Pathdata+"/"+listcut[rt])
               sorting  = sorted(listfile,reverse=False) 
               if len(sorting) >= 2: 
                        for ik in range(0,len(sorting)):
                                 if ik%2 == 1:               
                                        print("Getting the file name to cut header",sorting[ik]) # Getting the list of the file name from the odd numner after grouping the file
                                        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                              #Getting the file name for extracting 
                                        df = pd.read_csv(Pathdata+"/"+listcut[rt]+"/"+sorting[ik]) #Getting the filename and running the head custter and replace the old file before merging data
                                        datatrans = df.values.tolist() #Getting the data transformation 
                                        for r in range(0,2):
                                              datatrans.remove(datatrans[0]) #remove the header out from the list 
                                        da = pd.DataFrame(datatrans)
                                        print(da)
                                        da.to_csv(Pathdata+"/"+listcut[rt]+"/"+sorting[ik],index=False)
                                         

def Mergecsvalgorithm(Pathdata):
       print("Starting merging the csv file....") # Merging the csv file for the devices pins function
       listreadymerge = os.listdir(Pathdata) #Getting the directory in the path 
       print("Running the directory for merging data:",listreadymerge) #Getting the ready merge list for running the merging data
       for ir in range(0,len(listreadymerge)): 
                   os.chdir(Pathdata+"/"+listreadymerge[ir]) #Getting the list directory to merge the data on each directory
                   extension = 'csv'
                   all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
                   print(all_filenames)
                   all_filesort = sorted(all_filenames, reverse=False)
                   print(all_filesort)
                
                   # Looping multiple file in the group concaticatination
                   memtable.clear() #Clear the data before get into new file merge
                   for f in range(0,len(all_filesort)):
                         
                         df = pd.read_csv(all_filesort[f],header=None) 
                         df.reset_index(inplace=True, drop=True) #reset index 
                         memtable.append(df)
                         combined_csv = pd.concat(memtable,axis=0) # Concatinate the file
                         getfilename = listreadymerge[ir].split("_")[0]
                         print("Filename in directory",getfilename)
                         combined_csv.to_csv(str(getfilename)+".csv",header=0,index=False, encoding='utf-8-sig')
                         print(combined_csv) # Getting the csv merged display on the terminal 
                         
                   #getfilename = listreadymerge[ir].split("_")[0]
                   #print("Filename in directory",getfilename)
                   #combined_csv.to_csv(str(getfilename)+".csv",index=False, encoding='utf-8-sig')
                   #print(combined_csv) # Getting the csv merged display on the terminal       

def Cutoutgroup(devicenamedata,Pathway,megapositon):
       print("Starting grouping cut ....")
       seekingovergroup  = os.listdir(Pathway)   #Get the list of the file and seek the over groupping 
       print(sorted(seekingovergroup, reverse=False))
       splitfile =  sorted(seekingovergroup, reverse=False)
       for i in range(0,len(splitfile)): 
               print(splitfile[i])
               getfilename = splitfile[i].split(".csv")[0]
               Getclassfile = getfilename.split("_")
               print(Getclassfile)
               if len(Getclassfile) == 3: 
                       print("Detected file name pattern")
                       if int(Getclassfile[2]) >=1:
                               print("Diff group of data tables:",splitfile[i]) #Get the file name for regrouping the table with the new upcoming file in directory
                               # append process here  
                               Drifgroup[str(devicenamedata) + "_"+str(megapositon)] = str(splitfile[i]) #Get the file append in the list  
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3                            
def Processingregroup(Pathdata,Normalgroup,Drifgroup): 
          print("Processing the group of the ") #Getting the data from the directory management processing
          datapath = os.listdir(Pathdata) #Get the directory from the list to extract the file name from the next directory to copy int the new group 
          sortedpath = sorted(datapath,reverse=False) #Get the path of the directory 
          print(sortedpath,len(sortedpath)) #Get sorted path
          for i in range(0,len(list(Drifgroup))):
                PositionPath = sortedpath.index(str(list(Drifgroup)[i])) 
                print("Getting the position of sorted path:",PositionPath) #Getting the position of the path 
                for ri in range(int(PositionPath)+1,int(len(sortedpath))): #Getting the prediction of the next directory
                          print("Copy loop to the new path",sortedpath[ri]) #Getting the the function from the sorted list
                          Basedir.append(sortedpath[ri]) #getting the reorder directory name
                          copyPath = os.listdir(Pathdata +"/"+sortedpath[ri])
                          print('Copy file path',copyPath) #Getting the list of the file inner directory 
                          for rk in range(0,len(copyPath)): 
                                    Normalgroup.append(copyPath[rk]) #Getting the append of the file from the next path into the list to combine with the function 
def Reoderprocessinggroup(Pathdata): #Getting the path data for processing the size of the path file re-ordering
          print("Reorder group of the file in the path directory...")
          Drifdata = list(Drifgroup.values())
         
          if len(Drifdata) < len(Normalgroup):
                     print("Drif group is bigger than Normal group")
                     try: 
                        for ij in range(0,len(Normalgroup)):

                              Regrouping[str(ij)] =str(Normalgroup[ij]) +","+ str(Drifdata[ij]) #
                     except:
                           Regrouping[str(ij)] = str(Normalgroup[ij])#                       
                        

          if len(Drifdata) > len(Normalgroup):
                        print("Normal group is bigger than Drif group")
                        try: 
                            for ij in range(0,len(Drifdata)):
                                 Regrouping[str(ij)] =str(Normalgroup[ij]) +","+ str(Drifdata[ij]) #
                        except:
                             Regrouping[str(ij)] = str(Drifdata[ij])# 
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
               # Make new directory in the pathdata
          print("Showing the current list of directory for new group:",Basedir)
          for r in range(0,len(Basedir)): 
                     print("Current base dir:",Basedir[r])
                     newdir = str(Basedir[r]) +"_"+"new"  #new file name reorder
                     Newdir.append(newdir) #Getting the new directory list    
                     try:      
                        os.mkdir(EXTRACT+"/"+str(inputcomp)+"/"+str(newdir),mode)
                     except: 
                        print("Directory was created")
          print("Created the directory",os.listdir(Pathdata)) #Show the list directory to see new directory created
          Newdirectorycreator(Pathdata)
          
def Newdirectorycreator(Pathdata): 
        print("Create new directory.....") #Getting the list of the reorder to create the new directory 
        #Fiding the directory for copying into the new file 
        findnewdir = os.listdir(Pathdata) #Finding the new data of the list file 
        for il in range(0,len(findnewdir)): 
                  splitfile = str(findnewdir[il]).split("_")
                  if "new" in splitfile: 
                          print("Found new",str(splitfile))
                          print("Here is the target directory",findnewdir[il]) #get the new dir
                          #Getting the base dir for copy the file to new directory
                          Newpathdir = Pathdata+"/"+findnewdir[il] #Getting the new file directory
                          Getoverlistdata = list(Drifgroup)
                          Regroupdata = list(Regrouping)   #Getting the data from the regrouping by seaching the value of the data 
                          print(Regrouping)
                          for ij in range(0,len(Getoverlistdata)):
                                  print("Getting the file to copy",Getoverlistdata) #  
                                  Readingdir = Pathdata+"/"+Getoverlistdata[ij]
                                  readingdir = os.listdir(Pathdata+"/"+Getoverlistdata[ij])
                                  print("Check seeking file",str(readingdir))
                                  for ikl in range(0,len(Regroupdata)): 
                                             listcheck = Regrouping.get(Regroupdata[ikl]).split(",") #Getting the list
                                             print("Data from list check",listcheck) 
                                             if len(listcheck) != 1:
                                                  intersecfile = intersection(readingdir,listcheck) #Getting the file same file from the list  
                                                  if intersecfile != []:
                                                     for ih in range(0,len(intersecfile)):
                                                         try:
                                                            os.mkdir(Readingdir+"/"+intersecfile[ih]+"\t"+"-t"+"\t"+Pathdata+"/"+findnewdir[il],mode) # Get the documentation of the components 
                                                         except: 
                                                             print("Directory was created")
                                  #Checking the loop of the base dir and the regrouping list compattibility

                                  for ikh in range(0,len(Regroupdata)): 
                                             listcheck = Regrouping.get(Regroupdata[ikh]).split(",") #Getting the list
                                             print("Data from list check",listcheck)
                                             if len(listcheck) != 1:        
                                                for ihl in range(0,len(Basedir)): 
                                                      checkbasedir = os.listdir(Pathdata+"/"+Basedir[ihl]) 
                                                      print("Base directory file checklist:",checkbasedir) #Getting the list from the base directory to find the fintersection and remove the file
                                                      Readingdir2 = Pathdata+"/"+Basedir[ihl] #Checking base dir for path file copy instruction 
                                                      intersecfile = intersection(checkbasedir,listcheck) #Getting the file same file from the list                                                        
                                                      print("Second intersection:",intersecfile) 
                                                      if intersecfile != []:
                                                            for ih in range(0,len(intersecfile)):
                                                                 print("Position",ih)
                                                                 try:
                                                                    os.mkdir(Readingdir2+"/"+intersecfile[ih]+"\t"+"-t"+"\t"+Pathdata+"/"+findnewdir[il],mode) # Get the documentation of the components 
                                                                 except: 
                                                                    print("Directory was created") 
                                  #check if the file inside is equal regrouping dictionary  data if yes then copy into the new directory 
                                  
#Finding the merging position                                                           
def Paringtables(inputcomp,Predictbreak):  #Bredict the breaking data 
        Pathdata = EXTRACT+"/"+str(inputcomp) #Create the path from the input 
        print("Begin paring tables data......")
        #Extracting the tables page from the  
        Getpagevalue = list(Predictbreak) #Get the list of the predictbreak key
        print("Predictbrake list",Getpagevalue) 
        for i in range(0,len(Getpagevalue)): 
                print(Getpagevalue[i]) #Get the page value from the list 
                pagevalue = Predictbreak.get(Getpagevalue[i]).split(",") #Get the list of the page for checking table len extraction and paring the page data 
                print(pagevalue) #Get the page paring value for the table data extraction
                Paringlist.append(pagevalue) #Getting the page value to make the list 
                #print("Paringlist",Paringlist)
        #Created the main directory system 
        try: 
           os.mkdir(EXTRACT+"/"+str(inputcomp),mode)
        except: 
           print("Directory was created")
        if len(Getpagevalue) <=1: 
                print("Processing one page mode")
                for rl in range(0,len(Getpagevalue)):
                          try:
                            os.mkdir(EXTRACT+"/"+str(inputcomp)+"/"+str(inputcomp),mode)
                            shutil.copy2(EXTRACT+"/"+str(inputcomp)+".csv",EXTRACT+"/"+str(inputcomp)+"/"+str(inputcomp)) #Getting the number of the pins on the package data
                          except: 
                             print("Directory was created")
        if len(Getpagevalue) >1:
            for qw in range(0,len(Getpagevalue)):        
                       pagevalue = Predictbreak.get(Getpagevalue[qw]).split(",")  
                       for a in range(0,len(pagevalue)): 
                               print("Page array data:",pagevalue[a])#get the prediction of each value in the page
                               for kc in range(0,len(Paringlist)):
                                        if str(pagevalue[a]) in Paringlist[kc]:
                                              megapositon = Paringlist.index(Paringlist[kc]) #Getting the mega position of the array for the page meging group 
                                              print("Array position:",pagevalue,megapositon)
                                              if int(megapositon) == int(Getpagevalue[qw]): #Always check the type of the variable in this case using integer to define the array position
                                                                   devicenamedata = list(Devicelist.values())[megapositon].split(",")[0] 
                                                                   try:
                                                                      os.mkdir(EXTRACT+"/"+str(inputcomp)+"/"+str(devicenamedata)+"_"+str(megapositon),mode) #Getting the number of the pins on the package data    
                                                                   except:
                                                                      print("Directory was created")
                                                                   Pathway = EXTRACT+"/"+str(inputcomp)+"/"+str(devicenamedata)+"_"+str(megapositon) #Getting the path for the directory and file grouping input
                                                                   print("Getting the mega positon page",megapositon) # Find the way to put the megaposition back into the 
                                                                   tables = camelot.read_pdf(PATHMAIN + "/"+str(inputcomp)+".pdf",pages=str(pagevalue[a]))
                                                                   Cutoutgroup(devicenamedata,Pathway,megapositon)                      
                                                                   if megapositon == 0:
                                                                           Groupingpinextractor(Pathway,pagevalue[a],tables,1,megapositon) # Starter directory 
                                                                   if megapositon >= 1:
                                                                           Grouploopanalysis(Pathway,pagevalue[a],tables) #Looping analysis 
                                                                                   
                   
        # Merge the CSV file frim the table and access key of the devices 
        Processingregroup(Pathdata,Normalgroup,Drifgroup) 
        Reoderprocessinggroup(Pathdata) #Getting the reorder processing 
        
def Editingxmlpreprocess(inputcomp,listConfig): 
   listpath = EXTRACT+"/"+str(inputcomp)
   listdirectory = os.listdir(listpath)
   for il in range(0,len(listdirectory)):
         listdirect = str(listdirectory[il])
         listfiletitle = str(listdirectory[il]).split("_")[0] 
         Checkgeneratedfile.append(str(listdirect)) #Append and check generated file
         listfiledata = os.listdir(listpath+"/"+listdirectory[il]) #Getting the list file
         sorting = sorted(listfiledata,reverse=False)
         print("Getting the title header file",listfiletitle)
         print("Directory packackages name",Checkgeneratedfile) #Getting the list of the packages generated file
         for ir in range(0,len(sorting)):
                if str(listfiletitle)+".csv" in sorting[ir]:
                          print("Found the file target",str(listfiletitle)+".csv")
                          #Reading the file progress and running the pandas data extraction 
                          print("Begin pins function and name")
                          df = pd.read_csv(r''+listpath+"/"+listdirectory[il]+"/"+str(listfiletitle)+'.csv')
                          print(df) #Getting the data frame for the pins extraction algorithm 
                          #print(Configure(listConfig[0]))
                          index = df.index
                          number_of_rows = len(index)
                          print("Number of row include header",number_of_rows)
                          print("Number of pin",int(number_of_rows))
                          listdata = list(df.columns.values)
                          print(listdata)
                          extractionalgorithm(df,listdata,listConfig[0])
  
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def Checkinginsidedirectory(inputcomp): 
            print("Checking the directory blank")
            listcheckdir = os.listdir(EXTRACT+"/"+inputcomp+"/")
            print("Seeking directory",listcheckdir) 
            if listcheckdir == []:
                   print("There is blank directory define more accurate methode")
                   SpecificationExtract2(input1,searchSpecification)
                   print("spec page number:",Specpage) # Reference for the specpage  
                   Classifyselectionfunction(input1,inputcomp,Pinsquantity,Packagecheck,len(reftabledetect),combinedictdata)
                  
def Select_package_library(Packageinput,packagename,vav2_sorting,listConfig):  
  #Adding path
  print("Activate select package function")
  print("Confirm package data",Packageinput,packagename)
  tree = ET.parse(str(Packageinput)+".lbr")  #Loading the lbr file from the package recheck from the OS python library  
  root = tree.getroot()   
  print(ET.tostring(root, encoding='utf8', method='xml')) #Getting the xml utf code included    
  print(root.attrib) 
  for drawing in root.findall('drawing'):
        print("Found drawing")
        print(drawing.attrib)
        if drawing.find('library'):
            print("Found library")
            if drawing.find('library').find('packages3d'):
                print("Found packages3d")
                package3ddata = drawing.find('library').find('packages3d')
                if package3ddata.find('package3d'):
                            print("Found Package3d data") 
                            if package3ddata.find('package3d').findall('description'):
                                   print("Found description")
                                   for package in root.iter('package'):
                                           print(package.attrib)
                                           desc = package.find('description').text
                                           print(desc,type(desc))
                                           Packagecheckdata = desc.split(",")[0].split(" ")[0] #Getting the package recheck from the json file 
                                           print("Package data:",desc.split(",")[0].split(" ")[0]) #Getting the package data
                                           try: 
                                               print("Start extracting the config file")
                                               print(listConfig) #Getting file listconfig
                                               data = open(CONFIG+"/"+str(listConfig),'r') #Open the file from the listconfig file 
                                               datas = data.readline()
                                               transfer = json.loads(datas)
                                               print(transfer)
                                               packageout = transfer.get("package").get("rootpackages")
                                               print(packageout)
                                               for rik in range(0,len(packageout)):
                                                       print("Package checking......")
                                                       decryptionext = desc.split(",")[0].split(" ")[0].split("-")[1] #Extracting the description extraction 
                                                       checkingintersec = intersection(packageout[rik],desc.split(",")[0].split(" ")[0].split("-")[1])
                                                       print(checkingintersec,packageout[rik],decryptionext) #Checking the library packageout on the intersection process 
                                                       percent=difflib.SequenceMatcher(None,packageout[rik],decryptionext)
                                                       print(percent.ratio()*100)
                                                       if percent.ratio()*100 == 100:
                                                               print("Found packagedata in the list now breaking...")
                                                               for package in root.iter('package3d'):
                                                                    print(package.attrib)  
                                                               if drawing.find('library').find('symbols'):
                                                                   print("Found symbols")
                                                                   print(drawing.find('library').find('symbols'))
                                                                   for pin in drawing.find('library').find('symbols').iter('pin'):
                                                                            print(pin.attrib)
                                                                            print(pin)
                                                                            pinsclarify.append(pin) #getting the code of the pins positon from the array created here
                                                                            #one time record process for the pins address 
                                                                            #pin.set('name','testing')  #Getting the data index input from the pdf extraction 
                                                                   print(pinsclarify) #Getting the pins clarify 

                                                                   for pin in drawing.find('library').find('symbols').iter('pin'):
                                                                                print(pin.attrib)
                                                                                positionrecall = pinsclarify.index(pin) #Getting the position feedback from the loop 
                                                                                print("Position of the array:",positionrecall)  #Getting the positon to call the list name index of the pins to edit in the loop    
                                                                                print(NewPinsNamesorted)
                                                                                if NewPinsNamesorted != []:
                                                                                   pin.set('name',NewPinsNamesorted[positionrecall])
                                                                                else:
                                                                                   print("New pins sorted blank find the cause of the error")    
                                                                   for deviceset in drawing.find('library').find('devicesets').iter('deviceset'):
                                                                                #print("Found devicesets found")
                                                                                print(deviceset.attrib)
                                                                   for gates in drawing.find('library').find('devicesets').iter('connect'):
                                                                                 print(gates.attrib)
                                                                                 Gateconnect.append(gates.attrib.get('pad'))
                                                                   print(Gateconnect)
                                                                        #print(key_gate[vav_gate.index(Gateconnect[irl])]) #Getting the value of the index input
                                                                   print(DictionaryPinsdata)
                                                                   key3_gate = list(DictionaryPinsdata.keys())
                                                                   vav3_gate = list(DictionaryPinsdata.values())
                                                                   for ikl in range(0,len(list(DictionaryPinsdata))):
                                                                             print(vav3_gate[ikl],key3_gate[vav3_gate.index(vav3_gate[ikl])]) #Getting the gate key data output 
                                                                             if vav3_gate[ikl] == '—':
                                                                                    vav3_gate[ikl] = str(ikl+1)
                                                                             if vav3_gate[ikl] == '-':
                                                                                    vav3_gate[ikl] = str(ikl+1)       
                                                                   print(vav3_gate)
                                                                   for irl in range(0,len(key3_gate)):
                                                                            Connectsrecord[key3_gate[irl]] = vav3_gate[irl]    #Record the connection pins 
                                                                      
                                                                   print(Connectsrecord)
                                                                   key_connect = list(Connectsrecord.keys())
                                                                   vav_connect = list(Connectsrecord.values())      
                                                                   for irk in range(0,len(Gateconnect)): 
                                                                             #print(key_connect[irk],Gateconnect[irk],vav_connect[irk])
                                                                             print(key_connect[vav_connect.index(Gateconnect[irk])])         
                                                                   for gates in drawing.find('library').find('devicesets').iter('connect'):
                                                                                  print(gates.attrib)          
                                                                                  print(key_connect[vav_connect.index(gates.attrib.get('pad'))])
                                                                                  gateconfig = key_connect[vav_connect.index(gates.attrib.get('pad'))]
                                                                                  gates.set('pin',str(gateconfig)) #Getting the gate config to configure name on the certain pins function
                                                                                  
                                                                  
                                                                   #tree.write('/home/kornbotdev/Automaticsoftware/output3.lbr',encoding="UTF-8",xml_declaration=True)
                                                               with open(PACKAGEDIR+"/"+packagename+'.lbr', 'wb') as f:
                                                                              f.write('<?xml version="1.0" encoding="UTF-8" ?>\n''<!DOCTYPE eagle SYSTEM "eagle.dtd">\n'.encode('utf8'))
                                                                              tree.write(f, 'utf-8')
                                                               #tree.write('/home/kornbotdev/Automaticsoftware/output2.lbr',encoding="UTF-8",xml_declaration=True) 
                                                               
                                                               break
                                                                  
                                           except:
                                               print("Not found configfile in the config search directory")
                                           print(desc.split(","))
                                           
                            for package in root.iter('package3d'):
                                      print(package.attrib)

def Packagefor_3dlibclass(input1,inputcomp,listConfig):
       print("Package for 3d libraly class for editing selection")
       for i in reversed(range(0,input1.getNumPages())):  # Running the page for the back checking 
              #Getting the datatables
              #Making the directory for the datatable analysis 
              try:
                  os.mkdir(EXTRACT+"/"+inputcomp,mode)
              except: 
                  print("Directory was created")
              tables = camelot.read_pdf(PATHMAIN+"/"+inputcomp+".pdf",pages=str(i+1)) #Getting the datatable from all the page that detected table and save into the directory      
              if len(tables) >=1:
                     for rl in range(0,len(tables)): 
                              print(tables[rl].df)  #Getting the dataframe 
                              tables[rl].to_csv(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(i+1)+".csv")
                  
       datalist = os.listdir(EXTRACT+"/"+inputcomp) #Getting the list from the directory name 
       #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            #Generating the function of the page clasified in seperate directory
       try:
          os.mkdir(EXTRACT+"/"+inputcomp+"/"+inputcomp+"R"+"Pinsfunc",mode)
       except:
          print("Directory was created !")
       PINSFUNC = EXTRACT+"/"+inputcomp+"/"+inputcomp+"R"+"Pinsfunc"  #Getting the new path for the classified page pdf data from the extracted file csv 

       if datalist != []: #Checking if the directory is not blank  
           for ri in range(0,len(datalist)): 
                  removextention = str(datalist[ri]).split(".")[0]
                  try:
                    dataout = removextention.split("_")[1]
                  except: 
                     print("Out of range data splitter") #Getting the data splitter outout range  
                  Numberfile.append(int(dataout)) #Getting the dataout from the file append       
           sorting = sorted(Numberfile,reverse=False) 
           print(sorting) #Getting the data of the sorted list in datalist
           for ir in range(0,len(sorting)):
                     print("Data frame from page:",sorting[ir]) #Getting page number of the sorting list 
                     df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(sorting[ir])+".csv") #Getting the data frame from the list csv file
                     print(df) #Getting the dataframe of the csv file 
                     listdataindex = list(df.columns.values) 
                     print("Reading header columns for matching check:",listdataindex) #getting the data index 
                     print("Begin recording data of header")
                     recordheader[str(sorting[ir])] = listdataindex #Record data frame
           print("Recorded data from the header columns")
           print(recordheader) 
           #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                               # Classified the page from the extracted csv 
           #Calling the list of the extracted csv from the new directory data 

           listrecorder = list(recordheader) 
           data = open(CONFIG+"/"+str(listConfig),'r') #Open the configuretion file for the path 
           datas = data.readline()
           transfer = json.loads(datas)
           #Beginning to move the file into the new directory 
           print("Moving file to pins function process")
           for il in range(0,len(listrecorder)):
                       listheader =  recordheader.get(listrecorder[il]) 
                       print(listheader) #Getting the list header recorded
                       gettopic = transfer.get("Pin connection function").get("Pin functions")
                       #print("Getting the topic header",gettopic)
                       checkmatch = intersection(gettopic,listheader) #Getting the topic check list 
                       if checkmatch !=[]:
                              print("Found intersection topic:",checkmatch)
                              percent=difflib.SequenceMatcher(None,checkmatch,gettopic)
                              print("Match found:"+str(percent.ratio()*100)+"%") #Getting the percent matching 
                              if percent.ratio()*100 >= 85.71428571428571 and percent.ratio()*100 <= 100.0: 
                                       print("Begin process pins editor processing here..........")
                                       #Getting the record header function for extracting keys list for page number 
                                       key_list = list(recordheader.keys()) 
                                       val_list = list(recordheader.values())
                                       getpage = key_list[val_list.index(listheader)] #Getting the list header value for getting the page number for classification 
                                       print("Page number:",getpage) #Get the page number 
                                       #Getting the csv file and dataframe 
                                       df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(getpage)+".csv")
                                       print(df) #Getting the data frame before extracting the name from the columns into the list and starte to running the editor in xml file
                                       #Getting the pins name data 
                                       print(df.columns.values[0]) #Getting the the columns 0 of the data frame testing getting name from the detected dataframe 
                                       #Initial data get pins from the list of the tables 
                                       print("Begin copy file process")
                                       #shutil.copy2(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(getpage)+".csv",PINSFUNC) #Moving the file extracted into the pins function 
                                       os.system("echo 'Rkl3548123' | sudo -S cp"+"\t"+EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(getpage)+".csv"+"\t"+"-t"+"\t"+PINSFUNC) #Moving the file extracted into the pins function 

           #New sorting here for the data classification  
           datalist2 = os.listdir(PINSFUNC)
           print("Datalist2",datalist2)  #Getting the datalist from the PINFUNC path directory 
           if datalist2 != []: #Checking if the directory is not blank  
              #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                   #Rename the file in the list before resorting the function 
             
              for ri in range(0,len(datalist2)): 
                  removextention = str(datalist2[ri]).split(".")[0]
                  try:
                    dataout = removextention.split("_")[1]
                  except: 
                     print("Out of range data splitter") #Getting the data splitter outout range  
                  Numberfile2.append(int(dataout)) #Getting the dataout from the file append       
              sorting2 = sorted(Numberfile2,reverse=False) 
              print("Sorting page 2 in pins func directory",sorting2) #Getting the data of the sorted list in datalist    
             
              #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                  #Start the record header 2 here 
              #Change the name before sorting the list name     
              
           #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
           #Matching sequence 
           listrecorder = list(recordheader) 
           data = open(CONFIG+"/"+str(listConfig),'r') #Open the configuretion file for the path 
           datas = data.readline()
           transfer = json.loads(datas)
           for il in range(0,len(listrecorder)):
                       listheader =  recordheader.get(listrecorder[il]) 
                       print(listheader) #Getting the list header recorded
                       gettopic = transfer.get("Pin connection function").get("Pin functions")
                       #print("Getting the topic header",gettopic)
                       checkmatch = intersection(gettopic,listheader) #Getting the topic check list 
                       if checkmatch !=[]:
                              print("Found intersection topic:",checkmatch)
                              percent=difflib.SequenceMatcher(None,checkmatch,gettopic)
                              print("Match found:"+str(percent.ratio()*100)+"%") #Getting the percent matching 
                              if percent.ratio()*100 >= 85.71428571428571 and percent.ratio()*100 <= 100.0: 
                                       print("Begin process pins editor processing here..........")
                                       #Getting the record header function for extracting keys list for page number 
                                       key_list = list(recordheader.keys()) 
                                       val_list = list(recordheader.values())
                                       getpage = key_list[val_list.index(listheader)] #Getting the list header value for getting the page number for classification 
                                       print("Page number:",getpage) #Get the page number 
                                       #Getting the csv file and dataframe 
                                       df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(getpage)+".csv")
                                       print(df) #Getting the data frame before extracting the name from the columns into the list and starte to running the editor in xml file
                                       #Getting the pins name data 
                                       print(df.columns.values[0]) #Getting the the columns 0 of the data frame testing getting name from the detected dataframe 
                                       #Initial data get pins from the list of the tables 
                                       #for il in range(0,len(df[df.columns.values[0]])):
                                       #       print(str(il),df[df.columns.values[0]].values[il]) #Getting the list if the pins testing 
                                       #       PinsName.append(df[df.columns.values[0]].values[il]) #Append the pins name for processing in the pins data 
                                       #Getting the pins type data and append into the list
                                       
                                       
                                       for rl in range(0,len(df[df.columns.values[0]])): 
                                                
                                                print(str(rl),df[df.columns.values[0]].values[rl])
                                                PinsName.append(str(df[df.columns.values[0]].values[rl]))
                                                
                                                #PinsPackage[str(listheader[len(listheader)-5])] = PinsNumbers
                                       print(PinsName)
                                       for rk in range(1,len(listheader)-2):          
                                                print(df.columns.values[rk])
                                                #print(df[df.columns.values[rk]],len(df[df.columns.values[rk]]))
                                                PinsNumbers.clear()                                              
                                                for ir in range(0,len(df[df.columns.values[rk]])):
                                                        
                                                         print(str(ir),df[df.columns.values[rk]].values[ir])
                                                         PinsNumbers.append(df[df.columns.values[rk]].values[ir])
                                                         
                                                print(PinsNumbers) 
                                                rawpackdrawing.append(PinsNumbers[0]) #Getting the wat package drawing function for the paring package name data 
                                                
                                                if str(PinsNumbers[0]) != "nan":
                                                        print("Package drawing detected")
                                                        Packagedrawing.append(PinsNumbers[0])
                                                if str(PinsNumbers[0]) == "nan":
                                                        PinsNumbers.remove(PinsNumbers[0]) #Remove the nan from the list
                                                #print(Datainnerloop.append(PinsNumbers))
                                                PinsPackage[str(df.columns.values[rk])] = PinsNumbers
                                      
                                       for il in range(0,len(df[df.columns.values[len(listheader)-2]])):
                                               print(str(il),df[df.columns.values[len(listheader)-2]].values[il]) 
                                               Typeofpins.append(df[df.columns.values[len(listheader)-2]].values[il]) 
                                       print(PinsName)    #Getting the pins name 
                                       print(Typeofpins)  #Getting the type of the pins             
                                       print(Packagedrawing) #Getting the package drawing data 
                                       print(PinsPackage) #Getting the pins package data 
                                       for ik in range(0,len(list(PinsPackage.values()))):
                                                 print(list(PinsPackage.values())[ik][0]) #Getting the header data of the device package name 
                                                 Deviceindexheader.append(list(PinsPackage.values())[ik][0]) #Getting the header package name 
                                       print(Deviceindexheader) #Getting the list of the index header  
                       #Checking the chip package type match for choosing the chip data from the directory
                       Packageget = transfer.get("Device package").get("Package") #Getting the package data from the search intersection                  
                       checkpackage = intersection(Packageget,listheader)
                       if checkpackage !=[]: 
                              print("Found package:",checkpackage) #Checking the package of the 
                              percent=difflib.SequenceMatcher(None,checkpackage,listheader)
                              print("Match found:"+str(percent.ratio()*100)+"%") #Getting the percent matching 
                              DeviceNamepack.clear()
                              if percent.ratio()*100 >= 85.71428571428571 and percent.ratio()*100 <= 100.0: 
                                       print("Begin process Package json data ..........")
                                       #Beginning the xml editor for the library generator
                                       #Package type classification 
                                       key_list = list(recordheader.keys()) 
                                       val_list = list(recordheader.values())
                                       getpage = key_list[val_list.index(listheader)] #Getting the list header value for getting the page number for classification 
                                       print("Page number:",getpage) #Get the page number 
                                       #Getting the csv file and dataframe 
                                       df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(getpage)+".csv")
                                       print(df) #Getting the data frame before extracting the name from the columns into the list and starte to running the editor in xml file
                                       #Getting the pins name data 
                                       print(df.columns.values[0]) #Getting the the columns 0 of the data frame testing getting name from the detected dataframe 
                                       for il in range(0,len(df[df.columns.values[0]])):
                                              print(str(il),df[df.columns.values[0]].values[il]) #Getting the list if the pins testing 
                                              DeviceNamepack.append(df[df.columns.values[0]].values[il]) #Append the device name 
                                              
                                       print("New package data",DeviceNamepack) #
                                       #split package 
                                       print("Split package",DeviceNamepack[0].split("\n"))
                                       for ril in range(0,len(DeviceNamepack)):  #Getting all range of the package to rechecking with the package drawing 
                                                  print(DeviceNamepack,Packagedrawing) #Getting the package drawing data
                                                  
                                       try:
                                          for il in range(0,len(df[df.columns.values[1]])):
                                                print(str(il),df[df.columns.values[1]].values[il]) #Getting the list if the pins testing 
                                                
                                                Packageorder[str(DeviceNamepack[il])] = df[df.columns.values[1]].values[il]+","+df[df.columns.values[2]].values[il] #Append the device name                           
                                       except: 
                                           print("Found only 1 columns in data") 
                                       
                                       print("Package order",Packageorder) #Getting the list of the package order for the device have morethan 1 package data
                                       
                                       if Deviceindexheader[0] != "NO.":
                                           for ij in range(0,len(Deviceindexheader)): #Getting the device name pack combine with drawing package for search package  
                                                 if Deviceindexheader[ij] != "NO.":
                                                           DevicenamePackful  =  Deviceindexheader[ij] +list(Packageorder.values())[ij].split(",")[1] 
                                                           #rearrangedata =  list(DevicenamePackful),list(list(Packageorder.keys())[ij])
                                                           #print(DevicenamePackful,rearrangedata)
                                                           print("Device name and package combine",DevicenamePackful)
                                                           Packafuldata.append(DevicenamePackful) #Getting the device name and package combine
                                                 if Deviceindexheader[ij] == "NO.":
                                                           DevicenamePackful  = list(Packageorder.values())[ij].split(",")[1] 
                                                           #rearrangedata =  list(DevicenamePackful),list(list(Packageorder.keys())[ij])
                                                           #print(DevicenamePackful,rearrangedata)
                                                           print("Device name and package combine",DevicenamePackful)
                                                           Packafuldata.append(DevicenamePackful) #Getting the device name and package combine
                                       if Deviceindexheader[0] == "NO.":
                                                   print("Found NO. next processing packfuldata for append the package device into it") 
                                                   
                                       print("Getting list name and package combination:",Packafuldata)
                                       print("Pinsname:",PinsName) 
                                       print("Pins package",PinsPackage)
                                       #This section of code will extract the package from the dicitonary file by classifying the name and package drawing from the device from the intersection 
                                       print("Checking packfull",list(Packafuldata))
                                       print("Checking packorder",list(Packageorder))
                                       if list(Packafuldata) and list(Packageorder) != []:    
                                           for ikl in range(0,len(list(Packageorder))):
                                                
                                                checkingintersect =  intersection(list(Packafuldata[ikl]),list(list(Packageorder)[ikl])) #Getting the package order intersection
                                                print(checkingintersect,list(Packageorder)[ikl]) #Checking the list intersection function   
                                                percent = difflib.SequenceMatcher(None,list(Packafuldata[ikl]),list(list(Packageorder)[ikl]))
                                                print("Checking matching sequence possibility",list(Packageorder)[ikl],percent.ratio()*100,"%") #Checking the package match sequence from the maximum possibility matching 
                                                SequenceMax[percent.ratio()*100] = list(Packageorder)[ikl] 
                                           print(SequenceMax)
                                           print("Maximum from the list",max(list(SequenceMax)))
                                      
                                           for ikl in range(0,len(list(Packageorder))):
                                                
                                             checkingintersect =  intersection(list(Packafuldata[ikl]),list(list(Packageorder)[ikl])) #Getting the package order intersection
                                             print(checkingintersect,list(Packageorder)[ikl]) #Checking the list intersection function   
                                             percent = difflib.SequenceMatcher(None,list(Packafuldata[ikl]),list(list(Packageorder)[ikl]))
                                             print("Checking matching sequence possibility",list(Packageorder)[ikl],percent.ratio()*100,"%") #Checking the package match sequence from the maximum possibility matching 
                                             # Using for loop on the top and using this maximum value for classification data  
                                             key_sequence = list(Packageorder.keys())
                                             vav_sequence = list(Packageorder.values()) 
                                             if percent.ratio()*100 >= max(list(SequenceMax)):
                                                      print("Starting select package:",list(Packageorder)[ikl],ikl+1)
                                                      print("Extracting package:",Packageorder.get(list(Packageorder)[ikl])) #Getting the value index from the input key data
                                                      Packagedata = Packageorder.get(list(Packageorder)[ikl]).split(",")[0]
                                                      print("Package data:",Packagedata) #Getting the package data 
                                                      #Starting simplify the pins classification
                                                      if list(Packageorder)[len(list(Packageorder))-1] == list(Packageorder)[ikl]:
                                                             if PinsName[0] == "NAME":
                                                                   PinsName.remove("NAME") 
                                                             print("Found the package",list(PinsPackage.values())[0]) #Getting the list to edit the xml from the concerning package data 
                                                             print("Pins name",PinsName)
                                                             for il in range(0,len(PinsName)):
                                                                      DictionaryPinsdata[str(PinsName[il])] = list(PinsPackage.values())[0][il] 
                                                             print("Marking dictionary data",DictionaryPinsdata)
                                                             #Sorting process begin here 
                                                             key_dictpins = list(DictionaryPinsdata.keys())
                                                             print(key_dictpins)
                                                             for ril in range(0,len(list(DictionaryPinsdata))):
                                                                   #print(key_dictpins[ril])
                                                                   if key_dictpins[ril] != "PAD":
                                                                             vavcheck = DictionaryPinsdata.get(key_dictpins[ril])
                                                                             if vavcheck == "—": 
                                                                                    print(key_dictpins[ril])
                                                                                    del DictionaryPinsdata[key_dictpins[ril]] #Delete unwanted key and value from the dictionary list 
                                                                   if key_dictpins[ril] == 'nan':
                                                                       print(key_dictpins[ril])
                                                                       del DictionaryPinsdata["nan"] 
                                                             print("ready data for sorting",DictionaryPinsdata)
                                                             key3_sorting = list(DictionaryPinsdata.keys())
                                                             vav3_sorting = list(DictionaryPinsdata.values())
                                                             sortingpins = sorted(vav3_sorting,reverse=False)
                                                             print("Sorted pins",sortingpins)
                                                             #checking the - values detected 
                                                             for redd in range(0,len(sortingpins)):
                                                                     if sortingpins[redd] == "-":
                                                                          sortingpins += [sortingpins.pop(sortingpins.index(sortingpins[redd]))]  #Getting the index input from detected position index list
                                                             print("moved permute data",sortingpins) #Getting the moved data 
                                                             #Sorting list converting into the dictionary 
                                                             for ikr in range(0,len(sortingpins)):
                                                                        print(key3_sorting[vav3_sorting.index(sortingpins[ikr])])
                                                                        NewKeypins.append(key3_sorting[vav3_sorting.index(sortingpins[ikr])])   #Getting the new keypins for sorting the key data 
                                                                        
                                                             print(NewKeypins)
                                                             for rkl in range(0,len(NewKeypins)):
                                                                       DictionaryPinsdata2[NewKeypins[rkl]] = sortingpins[rkl]
                                                             print("New pins dictionary data",DictionaryPinsdata2)      
                                                             #Sorting data of the 
                                                             key_sortset = list(DictionaryPinsdata2.keys())
                                                             vav_sortset = list(DictionaryPinsdata2.values())
                                                             print("Get ",vav_sortset)
                                                             for ikr in range(0,len(vav_sortset)):
                                                                    if key_sortset[ikr] != "PAD":
                                                                       refsortindex.append(int(vav_sortset[ikr])) 
                                                                    if key_sortset[ikr] == "PAD":
                                                                       refsortindex.append(int(ikr)+1) #Getting the PAD   
                                                             print("Ref sorting value:",refsortindex) #Getting the reference sorting index value          
                                                             #Sorting index data of the pins before adding into the select package and pins configuretion part 
                                                             sorting = sorted(refsortindex,reverse=False)
                                                             print(sorting) #Getting the sorting index of the new list path 
                                                             for ikl in range(0,len(key_sortset)):
                                                                  if key_sortset[ikl] != "PAD":   
                                                                      print(key_sortset[vav_sortset.index(str(sorting[ikl]))])  #Getting new key sorting 
                                                                      NewdictPinsdata[key_sortset[vav_sortset.index(str(sorting[ikl]))]] = str(sorting[ikl])
                                                               
                                                             NewdictPinsdata["PAD"] =  "-"              
                                                             print("New dictpins sorted list:",NewdictPinsdata) #Getting the sorted list dictionarys 
                                                             vav2_sortset = list(NewdictPinsdata.values()) #Getting new value input for the select package 
                                                             key2_sortset = list(NewdictPinsdata.keys())
                                                             print("Sort set data:",vav2_sortset)
                                                             for irl in range(0,len(key2_sortset)):
                                                                    NewPinsNamesorted.append(key2_sortset[irl]) #Adding the sortset of Newpins sorted
                                                             print(list(Packageorder)[len(list(Packageorder))-1],Packagedata)
                                                             try:
                                                                  Select_package_library(Packagedata,list(Packageorder)[len(list(Packageorder))-1],vav2_sortset,listConfig) #Select package data
                                                             except:
                                                                 print("Not found the config file")
                       #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
                          #Activate this function when working on the single type of the chip with no difference type of chip package or pins 
                     
                       if listrecorder[il] == listrecorder[len(listrecorder)-1]:
                          vav_Detectnum = list(PinsPackage.values())
                          print(PinsName,vav_Detectnum[0][0]) #Top header of the data table extraction from the list    
                          
                          if checkpackage  == []:
                              if vav_Detectnum[0][0] == "NO.":
                                  print("Found NO. select new classification operation") 
                                  #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
                                  #Input the new task here for the package classification                                         
                                  #First getting the package order value and getting the package name no need to select the flassification with NO. mode 
                                  print(Packageorder) #Getting the package order value 
                                  vav_packorder = list(Packageorder.values()) #Getting the values package order 
                                  
                                  for iwl in range(0,len(list(Packageorder))): 
                                      print(list(Packageorder)[iwl], vav_packorder[iwl].split(",")[0], vav_packorder[iwl].split(",")[1]) #Getting the package keyname of the devices 
                                      print("Starting select package:",list(Packageorder)[iwl],iwl+1)
                                      print("Extracting package:",Packageorder.get(list(Packageorder)[iwl])) #Getting the value index from the input key data
                                      Packagedata = Packageorder.get(list(Packageorder)[iwl]).split(",")[0]
                                  print("Package data:",Packagedata) #Getting the package data 
                                  if PinsName[0] == "NAME":
                                             PinsName.remove("NAME")
                                  if vav_Detectnum[0][0] == "NO.":
                                            vav_Detectnum[0].remove("NO.")           
                                  print("Remove name:", PinsName) 
                                  print("Remove NO.:",vav_Detectnum[0])
                                  print(DictionaryPinsdata)
                                  for irl in range(0,len(PinsName)):
                                           DictionaryPinsdata[PinsName[irl]] = vav_Detectnum[0][irl]
                                  print("Dictionary pins:",DictionaryPinsdata) 
                                  vav_newdict = list(DictionaryPinsdata.values()) #Getting the values of new generated dictionary
                                  
                                  try:
                                       Select_package_library(Packagedata,list(Packageorder)[len(list(Packageorder))-1],vav_newdict,listConfig) #Select package data
                                  except:
                                       print("Not found the config file")
                                      
                       Orderableoackage = transfer.get("Orderablepackage").get("Orderable") #Getting the package data from the search intersection                  
                       checkpackage = intersection(Orderableoackage,listheader)
                       if checkpackage !=[]: 
                              print("Found package:",checkpackage) #Checking the package of the 
                              percent=difflib.SequenceMatcher(None,checkpackage,listheader)
                              print("Match found:"+str(percent.ratio()*100)+"%") #Getting the percent matching 
                              print(listheader[0].split("\n"))
                              if percent.ratio()*100 >= 85.71428571428571 and percent.ratio()*100 <= 100.0: 
                                       print("Begin process Package json data ..........")
                                       #Beginning the xml editor for the library generator
                                       #Package type classification 
                                       key_list = list(recordheader.keys()) 
                                       val_list = list(recordheader.values())
                                       getpage = key_list[val_list.index(listheader)] #Getting the list header value for getting the page number for classification 
                                       print("Page number:",getpage) #Get the page number 
                                       #Getting the csv file and dataframe 
                                       df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(getpage)+".csv")
                                       print(df) #Getting the data frame before extracting the name from the columns into the list and starte to running the editor in xml file
                                       #Getting the pins name data 
                                       print(df.columns.values[0]) #Getting the the columns 0 of the data frame testing getting name from the detected dataframe 
                                       for il in range(0,len(df[df.columns.values[0]])):
                                              print(str(il),df[df.columns.values[0]].values[il]) #Getting the list if the pins testing 
                                              DeviceNamepack.append(df[df.columns.values[0]].values[il]) #Append the device name 
                                              
                                       print(DeviceNamepack[0].split("\n"))
                                       listnamepackage = DeviceNamepack[0].split("\n")
                                       print("Beginning adding the package name and package device into the dictionary list")
                                       Packagedevice[str(listnamepackage[0])] = listnamepackage[2] #Getting the package and the value of the devices 
                                       print("Map package list info",Packagedevice,"Total package",len(Packagedevice)) #Getting the data of the package device 
                                       key_val = list(Packagedevice.keys())
                                       print("Package name",key_val)
                                       values_pack = list(Packagedevice.values())
                                       print("Values package:",values_pack)
                                       for ik in range(0,len(key_val)):
                                               if len(key_val) <= 1:
                                                    print("Getting name:",key_val[ik])
                                                    print("Getting package type:",values_pack[ik]) 
                                                    print(Packagedrawing[len(Packagedrawing)-1])
                                                    checkintersec = intersection(list(key_val[ik]),list(Packagedrawing[len(Packagedrawing)-1]))
                                                    if checkintersec != []:
                                                       print(checkintersec)
                                                       duplicate = set([x for x in checkintersec if checkintersec.count(x) > 1])
                                                       print(list(duplicate))
                                                       checkintersec.remove(list(duplicate)[0])
                                                       print("Start checking intersect",checkintersec)
                                                    #"""
                                                    print("Check intersect 1",Packagedrawing[len(Packagedrawing)-1]) #Checking the package drawing list
                                                    print("Joining list check","".join(checkintersec)) #Checking the joining list 
                                                    print(list(PinsPackage.values())[0])
                                                    print(PinsName)
                                                    #"""
                                                    #Rechecking this part of code some of them may not working
                                                    if Packagedrawing[len(Packagedrawing)-1] == "".join(checkintersec): # Fix this code 
                                                            print("Getting drawing package process....")
                                                            list(PinsPackage.values())[0].remove("".join(checkintersec))
                                                            if PinsName[0] == "NAME":
                                                                   PinsName.remove("NAME")
                                                            
                                                            #if "-" in list(PinsPackage.values())[0]:
                                                            #       list(PinsPackage.values())[0].remove("-") #remove - from the list because not found the pins data from the list
                                                            print("Found the package",list(PinsPackage.values())[0]) #Getting the list to edit the xml from the concerning package data 
                                                            print("Pins name",PinsName)
                                                            for il in range(0,len(PinsName)):
                                                                      DictionaryPinsdata[str(PinsName[il])] = list(PinsPackage.values())[0][il] 
                                                            print("Marking dictionary data",DictionaryPinsdata)
                                                            #Sorting process begin here 
                                                            key_dictpins = list(DictionaryPinsdata.keys())
                                                            values_dictpins = list(DictionaryPinsdata.values())
                                                            for ril in range(0,len(list(DictionaryPinsdata))):
                                                                   #print(key_dictpins[ril])
                                                                   if key_dictpins[ril] != "PAD":
                                                                             vavcheck = DictionaryPinsdata.get(key_dictpins[ril])
                                                                             if vavcheck == "—": 
                                                                                    print(key_dictpins[ril])
                                                                                    del DictionaryPinsdata[key_dictpins[ril]] #Delete unwanted key and value from the dictionary list 
                                                                   if key_dictpins[ril] == 'nan':
                                                                       print(key_dictpins[ril])
                                                                       del key_dictpins['nan'] 
                                                            print("ready data for sorting",DictionaryPinsdata)
                                                            vav2_sorting = list(DictionaryPinsdata.values())
                                                            key2_sorting = list(DictionaryPinsdata.keys())
                                                            sortingpins = sorted(vav2_sorting,reverse=False)
                                                            print(sortingpins)
                                                            for rik in range(0,len(sortingpins)):
                                                               
                                                                      print(key2_sorting[vav2_sorting.index(sortingpins[rik])],sortingpins[rik])
                                                                      NewPinsNamesorted.append(key2_sorting[vav2_sorting.index(sortingpins[rik])]) #Getting the list of the name for input into the select pins package function 
                                                            print(NewPinsNamesorted) #Getting the pins mame to input into the select package function
                                                            #Package selection for editing data 
                                                            #function here 
                                                            try:
                                                                                                      #Name package input at the key_val[ik]
                                                               Select_package_library(values_pack[ik],key_val[ik],vav2_sorting,listConfig) #Select the package for editing the pins data
                                                                
                                                            except: 
                                                                print("Not found any package in the list")
                                                            #"""
                                                            #Edit the xml file for the xml generator 
                                                            #Checking the pins package of the data 
                                                    #"""        
                       Characteristic = transfer.get("Electrical characteristic").get("Characteristic") #Getting the package data from the search intersection                  
                       Electricalpackage = intersection(Characteristic,listheader)
                       if Electricalpackage !=[]: 
                              print("Found package:",Electricalpackage,listheader) #Checking the package of the 
                              percent=difflib.SequenceMatcher(None,Electricalpackage,listheader)
                              print("Match found:"+str(percent.ratio()*100)+"%") #Getting the percent matching 
                              if percent.ratio()*100 >= 85.71428571428571 and percent.ratio()*100 <= 100.0: 
                                       print("Begin process json update data ..........")
                                       key_list = list(recordheader.keys()) 
                                       val_list = list(recordheader.values())
                                       getpage = key_list[val_list.index(listheader)] #Getting the list header value for getting the page number for classification 
                                       print("Page number:",getpage) #Get the page number 
                                       #Getting the csv file and dataframe 
                                       df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(getpage)+".csv")
                                       print(df) #Getting the data frame before extracting the name from the columns into the list and starte to running the editor in xml file
                                       #Getting the pins name data 
                                       print(df.columns.values[0]) #Getting the the columns 0 of the data frame testing getting name from the detected dataframe 
                                       #Beginning the xml editor for the library generator
                                       #Package type classification                 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                      #Get the data sopecification function for the 
# Solding the data table detection algorithm first
#Tabledetector(input1,inputcomp,Pinsquantity,searchpinsconfiguretion) #Get the pins and quantity of the package specificatoin 
#print("Pins quantity:",Pinsquantity) 
#Pinsearchfunction(input1,inputcomp,searchpinsconfiguretion) #Get the pins function of the input pdf file 
components = ['tps62750','drv8428e','drv8320','drv8846']
#components = os.listdir('ComponentDoc')

def Processing_component_packages(components):
  listcreate = os.listdir(EXTRACT) # Getting the list of the directory created 
  if len(listcreate) == 0: 
   for r in range(0,len(listcreate)-1):

      if listcreate[r] in components: 
            print("Preparing new process........")
            file_ext = open('listtocleara.py','r')
            datafile = file_ext.readlines()
            for re in datafile:
                    print("Clearing list ====> ",re.split("=")[0]) 
                    exec(re.split("=")[0]+".clear()")  
      if listcreate[r] not in components:      
            output = PdfFileWriter() #drv8428e #tps62750
            inputcomp = components # Get the component input data 
            input1 = PdfFileReader(open(PATHMAIN+"/"+inputcomp+".pdf", "rb"))  #using oslist dir readding the file and extract all the value in the loop 
            Pathdata = EXTRACT+"/"+str(inputcomp)
            # Pins search continued function for long range pins configurection 
            searchpinsconfiguretion = "Pin Configuration and Functions"
            searchConfigcontinued = "Pin Functions"
            searchSpecification = "Absolute Maximum Ratings"  # Get the specifications page and break from the pins configuretion and functions
            specificationExtract = ""
            # print how many pages input1 has:
            print("document1.pdf has %d pages." % input1.getNumPages())
            Packagefor_3dlibclass(input1,inputcomp,listConfig[0]) #Getting the dataframe using this function to processing in multitasking
            print("listconfig",listConfig[0]) #Getting the list configuretion
            print("Pins package list",PinsPackage)
            print("pinsdata",DictionaryPinsdata)
            getnewjson[inputcomp] = DictionaryPinsdata
            print("Components:",getnewjson)
 
  if len(listcreate) != 0: 
   for r in range(0,len(listcreate)):

      if listcreate[r] in components: 
            print("Preparing new process........")
            file_ext = open('listtocleara.py','r')
            datafile = file_ext.readlines()
            for re in datafile:
                    print("Clearing list ====> ",re.split("=")[0]) 
                    exec(re.split("=")[0]+".clear()")  
      if listcreate[r] not in components:      
            output = PdfFileWriter() #drv8428e #tps62750
            inputcomp = components # Get the component input data 
            input1 = PdfFileReader(open(PATHMAIN+"/"+inputcomp+".pdf", "rb"))  #using oslist dir readding the file and extract all the value in the loop 
            Pathdata = EXTRACT+"/"+str(inputcomp)
            # Pins search continued function for long range pins configurection 
            searchpinsconfiguretion = "Pin Configuration and Functions"
            searchConfigcontinued = "Pin Functions"
            searchSpecification = "Absolute Maximum Ratings"  # Get the specifications page and break from the pins configuretion and functions
            specificationExtract = ""
            # print how many pages input1 has:
            print("document1.pdf has %d pages." % input1.getNumPages())
            Packagefor_3dlibclass(input1,inputcomp,listConfig[0]) #Getting the dataframe using this function to processing in multitasking
            print("listconfig",listConfig[0]) #Getting the list configuretion
            print("Pins package list",PinsPackage)
            print("pinsdata",DictionaryPinsdata)
            getnewjson[inputcomp] = DictionaryPinsdata
            print("Components:",getnewjson) 

#Processing_component_packages(components[0]) 
if  __name__ =='__main__': 
      for i in components:     
         try:
            t1 = threading.Thread(target=Processing_component_packages(i))
            t1.start()
            t1.join()
         except: 
            print("Package fail to rethreive")
'''
#multitasking processing
if __name__ =="__main__": 
       listcomcreated = os.listdir(EXTRACT)
       print(listcomcreated) 
       p1 = multiprocessing.Process(target=Processing_component_packages(components[0]))
       p2 = multiprocessing.Process(target=Processing_component_packages(components[1]))
       p1.start() 
       p2.start()
       p1.join() 
       p2.join() 
'''      
       
