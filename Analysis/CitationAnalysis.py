
import requests
import pandas as pd
import pathlib
from matplotlib import pyplot as plt
import csv
import sys
from docxcompose.composer import Composer
from docx import Document as Document_compose
import os
import docx
from docx import Document
from docx.shared import Cm, Pt,Inches
import shutil
import openpyxl as xl
from bs4 import BeautifulSoup
import pathlib

from os.path import isfile, join
from os import listdir

 
FolderPath = pathlib.Path().resolve()
FolderPath=str(FolderPath)
FolderPath+="\\"
# print("Thread Started And Exe Is Running ")
# Need To Change It To e Dinamic Totally
# print("Folder Path is " , FolderPath)
Data_Path = FolderPath+"Urls_Data\\"
temp = FolderPath


## Creating Generated Data Folder 
desktop = pathlib.Path.home() / 'Desktop'
desktop = str(desktop)
desktop+= "\\Generated Data"
GNDataFolder = desktop
NewName = desktop+"\\Generated Data"
if not os.path.isdir(GNDataFolder):
    os.makedirs(GNDataFolder)
## Creating Done 

dir_list = os.listdir(Data_Path)
# print("dir_list = " ,dir_list)
doc_index = 0

Deparments_Cit_Dict = {}
Chart_Plots = ["DataAnalysis1.png", "DataAnalysis2.png", "DataAnalysis3.png", "DataAnalysis4.png", "DataAnalysis5.png", "DataAnalysis6.png"
            , "DataAnalysis7.png", "DataAnalysis8.png", "DataAnalysis9.png"]

Departments = ["Information Technology Department","Electrical Engineering Department","Water and Environmental Department",
            "Mechanical Engineering Department","Chemical Engineering Department","Nutrition and Food Processing Department",
            "Vocational Education Department","Department of Basic Human Sciences","Department of Basic Scientific Sciences"]

AllCitations = []

for i in range(len(dir_list)):
    CitationsSum = 0
    CurrDataFile = dir_list[i]

    file = open(Data_Path+dir_list[i])

    csvreader = csv.reader(file)
    header = []
    rows = []
    newurls = []
    Names = []
    for row in csvreader:
            rows.append(row)
            # print("row = " , row)
            if row == [] :
                continue
            newurls.append(row[0])
            Names.append(row[10])
    c = 1
    urls = []
    NotActiveIndexes = []
    ActiveIndexes = []

    ErrorNames = []
    NumOfErrors = 0
    for i in range(0,len(newurls)) :
        try :
            request = requests.get(newurls[i])
            if request.status_code == 200:
                urls.append(newurls[i])
                ActiveIndexes.append(i)
                c += 1
            else:
                NotActiveIndexes.append(i)
                if len(Names[i]) >4 :
                    ErrorNames.append(Names[i])
                c += 1
                NumOfErrors+=1
        except :
            if len(Names[i]) >4 :
                ErrorNames.append(Names[i])

            NotActiveIndexes.append(i)
            NumOfErrors+=1


    while True:
        Citations = []
        names = []

        for i in range(0, len(urls)):

            try:
                r = requests.get(urls[i])

                soup = BeautifulSoup(r.content, "html.parser")

                rows = soup.find('td', class_="gsc_rsb_std")
                CheckName = soup.find('a',class_="gsc_rsb_f gs_ibl")

                title = soup.find('div', id="gsc_prf_in")

                name = title.text

                names.append(name)

                Citations.append(rows.text)
                CitationsSum+=int(rows.text)

            except:
                continue

        NumOfErrors = len(ErrorNames)
        for i in range(0,NumOfErrors):
            Citations.append(0)
            names.append(ErrorNames[i])

        newNames = []
        for each in names : 
            if len(each) >=4:
                newNames.append(each)

        IntCitations = []
        for each in Citations:
            each = int(each)
            IntCitations.append(each)
        Citations_copy = IntCitations.copy()
        indexesOfHighestNumbers = []
        limit = len(IntCitations)
        Sorted_Citations  = []
        Sorted_Citations = IntCitations.copy()
        Sorted_Citations.sort()
        CurrMaxNum = 0
        # I'm a Genuis !!
        for i in range(limit):
                maxnum = max(Citations_copy)
                if maxnum <= -1 :
                    break;
                indexOfMaxNum = Citations_copy.index(maxnum)
                Citations_copy[indexOfMaxNum] = -1
                # print("Citations_copy = ", Citations_copy)
                indexesOfHighestNumbers.append(indexOfMaxNum)
                if Citations_copy == [] :
                    break
                # print("indexesOfHighestNumbers = " , indexesOfHighestNumbers)
        SortedNames = []
        Compressed_Names = []
        for each in newNames:
            Name = each
            # print("Name = " , Name)
            Words_List = Name.split()
            # print("Words_List = " , Words_List)
            first_Name = Words_List[0]
            first_Name += " "
            Second_Name = Words_List[1]
            New_Name = first_Name + Second_Name
            # print("New_Name = " , New_Name)
            Compressed_Names.append(New_Name)

        for i in range(0,len(indexesOfHighestNumbers)) :
            SortedNames.append(newNames[indexesOfHighestNumbers[i]])
        # print("names = " , names)
        # print("indexesOfHighestNumbers = " , indexesOfHighestNumbers)
        # print("SortedNames = " , SortedNames)
        SortedNames.reverse()
        Compressed_SortedNames = []
        for each in SortedNames :
            Name = each
            Words_List = Name.split()
            first_Name = Words_List[0]
            first_Name+=" "
            Second_Name  = Words_List[1]

            New_Name = first_Name+Second_Name
            Compressed_SortedNames.append(New_Name)

        DepName = Departments[doc_index]

        DepName = Departments[doc_index]

        FolderPath += "Analysis\\"

        exec(open(FolderPath +"CreatePlot.py").read())

        CreatePlot(Sorted_Citations,Compressed_SortedNames,Chart_Plots,doc_index,Departments)
        # exec("GenerateTables.py")
        exec(open(FolderPath+"GenerateTables.py").read())
        # print("SortedNames = " , SortedNames)

        # print("Sorted_Citations = ", Sorted_Citations)

        # print("doc_index = ", doc_index)

        CreateTable(SortedNames, Sorted_Citations, doc_index,0)

        #  print("File Created Succefully ! ")
        AllCitations.append(CitationsSum)
        FolderPath = temp
        Deparments_Cit_Dict[CitationsSum] =  Departments[doc_index]

        break
    doc_index+=1
    
        # print("New Cycle ! ")
# print("Starting Merging Words ! ! ! ! ! ! ! ! ! ! ! !")
# execfile(AllWord)

# print("All Citations Are = " , AllCitations)
AllCitations.sort()
# exec(open("D:\LastVersionScrapper\LastEdition\Analysis\GenerateTables.py").read())

# exec("CreatePlot.py")
LastPlot(AllCitations,Departments)
# exec("GenerateTables.py")
# print("Last Table Data : " )
# print("Departments  = " , Departments)
# print("AllCitations  = " , AllCitations)
# print("doc_index  = " , doc_index)
# 1 For The Last Table 
LastSortedCitations = sorted(Deparments_Cit_Dict)
LastSortedCitations.reverse()
LastSortedDeps = []
for i in range(0,len(LastSortedCitations)):
    LastSortedDeps.append(Deparments_Cit_Dict[LastSortedCitations[i]])

CreateTable(LastSortedDeps, LastSortedCitations, doc_index, 1)


exec(open(FolderPath + "Analysis\\" +"CreateMGWord.py").read())
CreateAllReport(GNDataFolder,FolderPath)
