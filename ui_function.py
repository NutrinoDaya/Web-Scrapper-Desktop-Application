
from BAUAnalyser import * #IMPORTING THE BAUAnalyser.PY FILE
import time
import sys
from about import *
from subprocess import run
from distutils.core import setup
import urllib.request
import requests
import threading
import os
import pathlib
import os
import csv
# from polyglot.detect import Detector
# from textblob import TextBlob

GLOBAL_STATE = 0 #NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
GLOBAL_TITLE_BAR = True #NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
init = False # NECRESSERY FOR INITITTION OF THE WINDOW.

Departments = ["Information Technology Department","Electrical Engineering Department","Water and Environmental Department",
            "Mechanical Engineering Department","Chemical Engineering Department","Nutrition and Food Processing Department",
            "Vocational Education Department","Department of Basic Human Sciences","Department of Basic Scientific Sciences"]

DataFiles = ["Data1.csv","Data2.csv","Data3.csv","Data4.csv","Data5.csv",
"Data6.csv","Data7.csv","Data8.csv","Data9.csv"]

# tab_Buttons = ['bn_home', 'bn_bug', 'bn_android', 'bn_cloud'] #BUTTONS IN MAIN TAB  
# android_buttons = ['bn_android_contact', 'bn_android_game', 'bn_android_clean', 'bn_android_world'] #BUTTONS IN ANDROID STACKPAGE

# THIS CLASS HOUSES ALL FUNCTION NECESSERY FOR OUR PROGRAMME TO RUN.
class UIFunction(MainWindow):

    #----> INITIAL FUNCTION TO LOAD THE FRONT STACK WIDGET AND TAB BUTTON I.E. HOME PAGE 
    #INITIALISING THE WELCOME PAGE TO: HOME PAGE IN THE STACKEDWIDGET, SETTING THE BOTTOM LABEL AS THE PAGE NAME, SETTING THE BUTTON STYLE.
    def initStackTab(self):
        global init
        if init==False:
            self.ui.line_android_name.setEnabled(True)
            # self.ui.line_android_adress.setEnabled(True)
            self.ui.line_android_org.setEnabled(True)

            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.lab_tab.setText("Home")
            self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            init = True
            self.ui.lab_tab.setText("Home \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Created By Mohammad Dayarneh")

    ################################################################################################


    #------> SETING THE APPLICATION NAME IN OUR CUSTOME MADE TAB, WHERE LABEL NAMED: lab_appname()
    # def labelTitle(self, appName):
    #     self.ui.lab_appname.setText(appName)
    # ################################################################################################


    #----> MAXIMISE/RESTORE FUNCTION
    #THIS FUNCTION MAXIMISES OUR MAINWINDOW WHEN THE MAXIMISE BUTTON IS PRESSED OR IF DOUBLE MOUSE LEFT PRESS IS DOEN OVER THE TOPFRMAE.
    #THIS MAKE THE APPLICATION TO OCCUPY THE WHOLE MONITOR.
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.bn_max.setToolTip("Restore") 
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/restore.png")) #CHANGE THE MAXIMISE ICON TO RESTOR ICON
            self.ui.frame_drag.hide() #HIDE DRAG AS NOT NECESSERY
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.bn_max.setToolTip("Maximize")
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/max.png")) #CHANGE BACK TO MAXIMISE ICON
            self.ui.frame_drag.show()
    ################################################################################################


    #----> RETURN STATUS MAX OR RESTROE
    #NECESSERY OFR THE MAXIMISE FUNCTION TRO WORK.
    def returStatus():
        return GLOBAL_STATE


    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status


    #------> TOODLE MENU FUNCTION
    #THIS FUNCTION TOODLES THE MENU BAR TO DOUBLE THE LENGTH OPENING A NEW ARE OF ABOUT TAB IN FRONT.
    #ASLO IT SETS THE ABOUT>HOME AS THE FIRST PAGE.
    #IF THE PAGE IS IN THE ABOUT PAGE THEN PRESSING AGAIN WILL RESULT IN UNDOING THE PROCESS AND COMMING BACK TO THE 
    #HOME PAGE.
    def toodleMenu(self, maxWidth, clicked):

        #------> THIS LINE CLEARS THE BG OF PREVIOUS TABS : I.E. MAKING THEN NORMAL COLOR THAN LIGHTER COLOR.
        for each in self.ui.frame_bottom_west.findChildren(QFrame): 
            each.setStyleSheet("background:rgb(51,51,51)")

        if clicked:
            currentWidth = self.ui.frame_bottom_west.width() #Reads the current width of the frame
            minWidth = 80 #MINIMUN WITDTH OF THE BOTTOM_WEST FRAME
            if currentWidth==80:
                extend = maxWidth
                #----> MAKE THE STACKED WIDGET PAGE TO ABOUT HOME PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_home)
                self.ui.lab_tab.setText("About > Home \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Created By Mohammad Dayarneh")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            else:
                extend = minWidth
                #-----> REVERT THE ABOUT HOME PAGE TO NORMAL HOME PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                self.ui.lab_tab.setText("Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            #THIS ANIMATION IS RESPONSIBLE FOR THE TOODLE TO MOVE IN A SOME FIXED STATE.
            self.animation = QPropertyAnimation(self.ui.frame_bottom_west, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(minWidth)
            self.animation.setEndValue(extend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
    ################################################################################################


    #-----> DEFAULT ACTION FUNCTION
    def constantFunction(self):
        #-----> DOUBLE CLICK RESULT IN MAXIMISE OF WINDOW
        def maxDoubleClick(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunction.maximize_restore(self))

        #----> REMOVE NORMAL TITLE BAR 
        if True:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_appname.mouseDoubleClickEvent = maxDoubleClick
        else:
            self.ui.frame_close.hide()
            self.ui.frame_max.hide()
            self.ui.frame_min.hide()
            self.ui.frame_drag.hide()

        #-----> RESIZE USING DRAG                                       THIS CODE TO DRAG AND RESIZE IS IN PROTOPYPE.
        #self.sizegrip = QSizeGrip(self.ui.frame_drag)
        #self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        #SINCE THERE IS NO WINDOWS TOPBAR, THE CLOSE MIN, MAX BUTTON ARE ABSENT AND SO THERE IS A NEED FOR THE ALTERNATIVE BUTTONS IN OUR
        #DIALOG BOX, WHICH IS CARRIED OUT BY THE BELOW CODE
        #-----> MINIMIZE BUTTON FUNCTION 
        self.ui.bn_min.clicked.connect(lambda: self.showMinimized())
        

        #-----> MAXIMIZE/RESTORE BUTTON FUNCTION
        self.ui.bn_max.clicked.connect(lambda: UIFunction.maximize_restore(self))
        # self.ui.AddUser_contact_save.clicked.connect(lambda: MainWindow.OnClickingSaveData(self,"Happy to Know you liked the UI", "icons/1x/smile2Asset 1.png", "Ok"))

        #-----> CLOSE APPLICATION FUNCTION BUTTON
        self.ui.bn_close.clicked.connect(lambda: self.close())
    ################################################################################################################


    #----> BUTTON IN TAB PRESSED EXECUTES THE CORRESPONDING PAGE IN STACKEDWIDGET PAGES
    def buttonPressed(self, buttonName):

        index = self.ui.stackedWidget.currentIndex()

        #------> THIS LINE CLEARS THE BG OF PREVIOUS TABS I.E. FROM THE LITER COLOR TO THE SAME BG COLOR I.E. TO CHANGE THE HIGHLIGHT.
        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if buttonName=='bn_home':
            if self.ui.frame_bottom_west.width()==80  and index!=0:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                self.ui.lab_tab.setText("Home \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Created By Mohammad Dayarneh")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST 

            elif self.ui.frame_bottom_west.width()==160  and index!=1:  # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_home)
                self.ui.lab_tab.setText("About > Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='bn_bug':
            if self.ui.frame_bottom_west.width()==80 and index!=5:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_bug)
                self.ui.lab_tab.setText("Bug")
                self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width()==160 and index!=4:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_bug)
                self.ui.lab_tab.setText("About > Bug")
                self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='AddUser':
            if self.ui.frame_bottom_west.width()==80  and index!=7:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_android)
                self.ui.lab_tab.setText("Android")
                self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                UIFunction.androidStackPages(self, "page_contact")

            elif self.ui.frame_bottom_west.width()==160  and index!=3:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_android)
                self.ui.lab_tab.setText("About > Android")
                self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST


            # elif self.ui.frame_bottom_west.width()==160 and index!=2:   # ABOUT PAGE STACKED WIDGET
            #     self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_cloud)
            #     self.ui.lab_tab.setText("About > Cloud")
            #     self.ui.frame_cloud.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        #ADD ANOTHER ELIF STATEMENT HERE FOR EXECTUITING A NEW MENU BUTTON STACK PAGE.
    ########################################################################################################################

   
    def stackPage(self):

        ######### PAGE_HOME ############# BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_HOME
        self.ui.lab_home_main_hed.setText("Main Window")
        self.ui.lab_home_stat_hed.setText("Status")

        ######### PAGE_BUG ############## BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_bug

        # THIS CALLS A SIMPLE FUNCTION LOOPS THROW THE NUMBER FORWARDED BY THE COMBOBOX 'comboBox_bug' AND DISPLAY IN PROGRESS BAR
        #ALONGWITH MOVING THE PROGRESS CHUNK FROM 0 TO 100%

        #########PAGE ANDROID WIDGET AND ITS STACKANDROID WIDGET PAGES
        self.ui.AddUser_contact.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_contact"))

        ######ANDROID > PAGE CONTACT >>>>>>>>>>>>>>>>>>>>
        # self.ui.AddUser_contact_delete.clicked.connect(lambda: self.dialogexec("Warning", "The Contact Infromtion will be Deleted, Do you want to continue.", "icons/1x/errorAsset 55.png", "Cancel", "Yes"))

        # self.ui.AddUser_contact_edit.clicked.connect(lambda: APFunction.editable(self))
        self.ui.AddUser_contact_Analise.clicked.connect(lambda: APFunction.AnalyseData(self))
        # self.ui.AddUser_contact_Analise.clicked.connect(lambda: )  

        self.ui.AddUser_contact_save.clicked.connect(lambda: APFunction.SaveUserData(self))

        #######ANDROID > PAGE GAMEPAD >>>>>>>>>>>>>>>>>>>
        self.ui.textEdit_gamepad.setVerticalScrollBar(self.ui.vsb_gamepad)   # SETTING THE TEXT FILED AREA A SCROLL BAR
        self.ui.textEdit_gamepad.setText("Type Here Something, or paste something here")

        ######ANDROID > PAGE CLEAN >>>>>>>>>>>>>>>>>>>>>>
        #NOTHING HERE
 
        ##########PAGE: ABOUT HOME #############
        self.ui.text_about_home.setVerticalScrollBar(self.ui.vsb_about_home)
        self.ui.text_about_home.setText(aboutHome)
    ################################################################################################################################


    #-----> FUNCTION TO SHOW CORRESPONDING STACK PAGE WHEN THE ANDROID BUTTONS ARE PRESSED: CONTACT, GAME, CLOUD, WORLD
    # SINCE THE ANDROID PAGE AHS A SUB STACKED WIDGET WIT FOUR MORE BUTTONS, ALL THIS 4 PAGES CONTENT: BUTTONS, TEXT, LABEL E.T.C ARE INITIALIED OVER HERE. 
    def androidStackPages(self, page):
        print("The Current Page is  = " ,page) 
        #------> THIS LINE CLEARS THE BG COLOR OF PREVIOUS TABS
        for each in self.ui.frame_android_menu.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_contact":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_contact)
            self.ui.lab_tab.setText("Main > Adding User \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Created By Mohammad Dayarneh")
            self.ui.frame_android_contact.setStyleSheet("background:rgb(91,90,90)")

        # elif page == "page_game":
        #     self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_game)
        #     self.ui.lab_tab.setText("Android > GamePad")
        #     self.ui.frame_android_game.setStyleSheet("background:rgb(91,90,90)")

        # elif page == "page_clean":
        #     self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_clean)
        #     self.ui.lab_tab.setText("Android > Clean")
        #     self.ui.frame_android_clean.setStyleSheet("background:rgb(91,90,90)")

        # elif page == "page_world":
        #     self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_world)
        #     self.ui.lab_tab.setText("Android > World")
        #     self.ui.frame_android_world.setStyleSheet("background:rgb(91,90,90)")

        #ADD A ADDITIONAL ELIF STATEMNT WITH THE SIMILAR CODE UP ABOVE FOR YOUR NEW SUBMENU BUTTON IN THE ANDROID STACK PAGE.
    ##############################################################################################################
  
class APFunction():
    #-----> ADDING NUMBER TO ILLUSTRATE THE CAPABILITY OF THE PROGRESS BAR WHEN THE 'START' BUTTON IS PRESSED
    def addNumbers(self, number, enable):
        # print("Progress bar Started ! !  !")
        if enable:
            lastProgress = 0
            for x in range(0, int(number), 1):
                progress = int((x/int(number))*100)
                if progress!=lastProgress:
                    self.ui.progressBar_bug.setValue(progress)
                    lastProgress = progress
            self.ui.progressBar_bug.setValue(100)
    ###########################



    #-----> FUNCTION IN ACCOUNT OF CONTACT PAGE IN ANDROID MENU
    def editable(self):
        self.ui.line_android_name.setEnabled(True)
        # self.ui.line_android_adress.setEnabled(True)
        self.ui.line_android_org.setEnabled(True)
        self.ui.bn_android_contact_save.setEnabled(True)
        self.ui.bn_android_contact_edit.setEnabled(False)
        self.ui.bn_android_contact_share.setEnabled(False)
        self.ui.bn_android_contact_delete.setEnabled(False)
    def AnalyseData(self):
        try : 
            newurls = ["http://google.com","https://www.artstation.com/","https://web.facebook.com/"
            ,"https://www.youtube.com/","https://animelek.me/#","https://twitter.com/"]
            InternetCheck = False
            # print("Initial Internet Check = " , InternetCheck)
            for i in range(0,6):
                    request = requests.get(newurls[i])
                    if request.status_code == 200:
                        print("Website Does Exist")
                        InternetCheck  = True 
                        print("New Internet Check = " , InternetCheck)
                        break;
            # print("InternetCheck = " , InternetCheck)
        except : 
            InternetCheck = False
        
        if InternetCheck == False : 
            MainWindow.OnClickingSaveData(self,"لا يوجد اتصال بالانترت", "icons/1x/smile2Asset 1.png", "Ok")
        
        else :

            # print("Starting Progress ! ")
            FolderPath = pathlib.Path().resolve()
            # print("Main Folder Path = " , FolderPath)
            self.showMinimized()
            self.ui.AddUser_contact_Analise.clicked.connect(lambda: APFunction.addNumbers(self, 10000000, True))  
            FolderPath = str(FolderPath)
            exes = [
                    FolderPath+"\\Analysis\dist\CitationAnalysis\CitationAnalysis.exe",
                ]
            threads = [
                    threading.Thread(target=os.system, args=(exe,)) for exe in exes
                ]
            for thread in threads:
                    thread.start()
            for thread in threads:
                    thread.join()
            APFunction.addNumbers(self, 10000000, True)


        



#-----> FUNCTION TO SAVE THE MODOFOED TEXT FIELD
    def SaveUserData(self):
        Name = self.ui.line_android_name.text()
        url = self.ui.line_android_org.text()
        # detector = Detector(Name)
        # b = TextBlob(Name)
        # Lang = b.detect_language()
        # if(Lang =="Arabic" ):
        #     MainWindow.OnClickingSaveData(self,"يجب ان يكون الاسم باللغة الانجليزية", "icons/1x/smile2Asset 1.png", "Ok")
        
        if len(url) >20:
            DeparmentName = self.ui.DepartmentsBox.currentText()
            # print("DeparmentName = " , DeparmentName)

            Vals = {"Information Technology Department":0,"Electrical Engineering Department":1,"Water and Environmental Department":2,
            "Mechanical Engineering Department":3,"Chemical Engineering Department":4,"Nutrition and Food Processing Department":5,
            "Vocational Education Department":6,"Department of Basic Scientific Sciences":7,"Department of Basic Scientific Sciences":8}
            FolderPath = pathlib.Path().resolve()
            FolderPath=str(FolderPath)
            FolderPath+="\\"
            Data_Path = FolderPath+"Urls_Data\\"
            indexOfFile  = Vals[DeparmentName]
            DTFileName = DataFiles[indexOfFile]
            Data_Path+=DTFileName
            # print("Data_Path = " , Data_Path)
            file = open(Data_Path)

            csvreader = csv.reader(file)
            header = []
            rows = []
            urls = []
            Names = []
            for row in csvreader:
                    rows.append(row)
                    # print("row = " , row)
                    if row == [] :
                        continue
                    else  : 
                        urls.append(row[0])
                        Names.append(row[10])
            tempUrls = urls.copy()
            tempNames = Names.copy()
        
            if url in urls : 
                # print("Opeining Pop Up")
                MainWindow.OnClickingSaveData(self,"الرابط موجود في قاعدة البيانات", "icons/1x/smile2Asset 1.png", "Ok")
            else :
                tempUrls.append(url)
                tempNames.append(Name)
                # print("TempUrls = " , tempUrls)
                # print("tempNames = " , tempNames)
                # Setting The Number Of Spaces Manually 
                n = 9
                # print("The Number Of Spaces Should be = " , n)
                AllData = []
                TempList= []
                for i in range(0,len(tempUrls)):
                    TempList.append(tempUrls[i])
                    for k in range(0,n):
                        TempList.append(" ")
                    TempList.append(tempNames[i])
                    # print("Curr Temp List IS = " ,TempList)
                    AnotherTemp  = TempList.copy()
                    AllData.append(AnotherTemp)
                    TempList.clear()
                # for each in AllData : 
                    # print("Data = " , each)
                # print("Data File Path = " ,Data_Path )
                with open(Data_Path, 'w') as f:
                    writer = csv.writer(f)
                    for Data in AllData : 
                        writer.writerow(Data)

                tempUrls.clear()
                tempNames.clear()
                
                MainWindow.OnClickingSaveData(self,"تمت الاضافة بنجاح", "icons/1x/smile2Asset 1.png", "Ok")
        else : 
            MainWindow.OnClickingSaveData(self,"الرجاء ادخال رابط صحيح", "icons/1x/smile2Asset 1.png", "Ok")



###############################################################################################################################################################