from docx import Document
from docxcompose.composer import Composer
# from PyPDF2 import PdfMerger
import sys
from docx import Document as Document_compose
import os
import shutil




    
Departments = ["Information Technology Department","Electrical Engineering Department","Water and Environmental Department",
            "Mechanical Engineering Department","Chemical Engineering Department","Nutrition and Food Processing Department",
            "Vocational Education Department","Department of Basic Human Sciences","Department of Basic Scientific Sciences"]

Chart_Plots = ["DataAnalysis1.png", "DataAnalysis2.png", "DataAnalysis3.png", "DataAnalysis4.png", "DataAnalysis5.png", "DataAnalysis6.png"
            , "DataAnalysis7.png", "DataAnalysis8.png", "DataAnalysis9.png"]


def CreateAllReport(GNDataFolder,FolderPath):
        # word_document = Document()
        # word_document.save(GNDataFolder + "All Departments Report.docx")

    for i in range(0,len(Chart_Plots)):
        
        PathToData = "%s" % GNDataFolder
        PathToData +="\\"
        PathToData+=Chart_Plots[i]
        os.remove(PathToData)

        LastPlotPic = "%s" % GNDataFolder
        LastPlotPic+="\\"
        LastPlotPic+="LastPlot.png"
    MainPagePath = FolderPath+"Analysis\\"+"MainPage\\"+"AllDtMain.docx"
    shutil.copy2(MainPagePath, GNDataFolder)
    FolderPath
        #filename_master is name of the file you want to merge the docx file into

    master = Document_compose(GNDataFolder+"AllDtMain.docx")

    composer = Composer(master)
    # index was 1 so the program skipped the first file (Information Tech Department )
    for i in range(0,len(Departments)):
        doc2 = Document_compose(GNDataFolder+Departments[i]+".docx")
        composer.append(doc2)
    lastdoc = Document_compose(GNDataFolder+"All Departments Report.docx")
    composer.append(lastdoc)
    os.remove(GNDataFolder+"All Departments Report.docx")

    composer.save(GNDataFolder+"Citations Report BAU.docx")

    for i in range(0,len(Departments)):
        os.remove(GNDataFolder+Departments[i]+".docx")
    os.remove(GNDataFolder+"LastPlot.png")
    os.remove(GNDataFolder+"AllDtMain.docx")
    
