from matplotlib import pyplot as plt
# print("Plot File Excecuted ! ")
import pathlib
import numpy as np

import os
desktop = pathlib.Path.home() / 'Desktop'
desktop = str(desktop)
desktop+= "\\Generated Data\\"
GNDataFolder = desktop

def CreatePlot(Sorted_Citations,Compressed_SortedNames,Chart_Plots,doc_index,Departments):


    DepName = Departments[doc_index]


    # Nums = [x for x in range(0,len(Sorted_Citations))]
    Edited_Citations = []
    for each in Sorted_Citations : 
        if each != 0 : 
            Edited_Citations.append(each)

    Nums = [x for x in range(1,len(Sorted_Citations)+1)]
    # print("Nums = " , Nums)
    # Now I Need To Arrange The Name In Decreasing Order

# Fixing random state for reproducibility
    np.random.seed(19680801)

    plt.rcdefaults()
    fig, ax = plt.subplots(figsize=(5.5,5))

    # Example data
    y_pos = np.arange(len(Sorted_Citations))
    error = np.random.rand(len(Sorted_Citations))

    ax.barh(y_pos, Sorted_Citations, xerr=error, align='center')
    ax.set_yticks(y_pos, labels=Compressed_SortedNames,fontsize=6)
    ax.tick_params(direction='out', length=2, width=0.6, colors='r',
               grid_color='r', grid_alpha=0.5)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Citations')
    ax.set_title(DepName)

    # print("len Of Sorted Citations = " , len(Sorted_Citations))
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    # explode = [0.1 for x in range(0,len(Nums))]   # only "explode" the 2nd slice (i.e. 'Hogs')
    # Nums.reverse()
    # fig1, ax1 = plt.subplots()
    # # autopct='%1.1f%%'
    # ax1.pie(Edited_Citations, explode=explode, labels=Nums,
    #         shadow=False, startangle=90)
    # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # plt.bar(Nums, Edited_Citations, color='red', alpha=0.5, align="edge",edgecolor="green")
    
    plt.savefig(GNDataFolder+Chart_Plots[doc_index])

    # print("Citations Copy Before Finding Indexes = " , Citations_copy)
    # print("Compressed_SortedNames = ", Compressed_SortedNames)
    plt.clf()

def LastPlot(AllCitations,Departments):
    # DepName = Departments[doc_index]

    Compressed_Deps_Names = []
    for each in Departments:
        Name = each
        # print("Name = " , Name)
        Words_List = Name.split()
        # print("Words_List = " , Words_List)
        first_Name = Words_List[0]
        if first_Name == "Department":
            first_Name+=" of"
        first_Name += " "
        Second_Name = Words_List[-1]
        New_Name = first_Name + Second_Name
        # print("New_Name = " , New_Name)
        Compressed_Deps_Names.append(New_Name)

    # Departments.reverse()
#     print("AllCitations = " , AllCitations)
#     print("Departments = " , Departments)
    Compressed_Deps_Names.reverse();
    Nums = [x for x in range(1,len(AllCitations)+1)]
    Nums.reverse()

    np.random.seed(19680801)

    plt.rcdefaults()
    fig, ax = plt.subplots(figsize=(6,6))

    # Example data
    y_pos = np.arange(len(AllCitations))
    performance = 3 + 10 * np.random.rand(len(AllCitations))
    error = np.random.rand(len(AllCitations))

    ax.barh(y_pos, AllCitations, xerr=error, align='center')
    # ax.set_yticks(y_pos, labels=Compressed_Deps_Names,fontsize=4)
    ax.set_yticks(y_pos, labels=Nums,fontsize=8)

    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Citations')
    ax.set_title("All Departments Report")
    plt.savefig(GNDataFolder+"LastPlot.png")
    plt.clf()
    