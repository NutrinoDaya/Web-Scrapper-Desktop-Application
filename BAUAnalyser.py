
import sys

#IMPORTING ALL THE NECESSERY PYSIDE2 MODULES FOR OUR APPLICATION.
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_main import Ui_MainWindow

from ui_dialog import Ui_Dialog 

from ui_error import Ui_Error 

from ui_function import * 

from about import * 

#
class dialogUi(QDialog):
    def __init__(self, parent=None):

        super(dialogUi, self).__init__(parent)
        self.d = Ui_Dialog()
        self.d.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # REMOVING WINDOWS TOP BAR AND MAKING IT FRAMELESS (AS WE HAVE AMDE A CUSTOME FRAME IN THE WINDOW ITSELF)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # MAKING THE WINDOW TRANSPARENT SO THAT TO GET A TRUE FLAT UI

        self.d.bn_min.clicked.connect(lambda: self.showMinimized())

        self.d.bn_close.clicked.connect(lambda: self.close())

        self.d.bn_east.clicked.connect(lambda: self.close())
        self.d.bn_west.clicked.connect(lambda: self.close())
        ##############################################################################################

        self.dragPos = self.pos()   
        def movedialogWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.d.frame_top.mouseMoveEvent = movedialogWindow  #CALLING THE FUNCTION TO CJANGE THE POSITION OF THE DIALOGBOX DURING MOUSE DRAG
        ################
    #----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    #################################################################################################

    def dialogConstrict(self, heading, message, icon, btn1, btn2):
        self.d.lab_heading.setText(heading)
        self.d.lab_message.setText(message)
        self.d.bn_east.setText(btn2)
        self.d.bn_west.setText(btn1)
        pixmap = QtGui.QPixmap(icon)
        self.d.lab_icon.setPixmap(pixmap)
    ##################################################################################################

class errorUi(QDialog):
    def __init__(self, parent=None):

        super(errorUi, self).__init__(parent)
        self.e = Ui_Error()
        self.e.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #-----> CLOSE APPLICATION FUNCTION BUTTON: CORRESPONDING TO THE bn_ok OF THE ERRORBOX
        self.e.bn_ok.clicked.connect(lambda: self.close())

#---> MOVING THE WINDOW WHEN LEFT MOUSE PRESSED AND DRAGGED OVER ERRORBOX TOPBAR
        self.dragPos = self.pos()   #INITIAL POSOTION OF THE ERRORBOX
        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
#############################################

    def PopUpWindow(self, heading, icon, btnOk):
            self.e.lab_heading.setText(heading)
            self.e.bn_ok.setText(btnOk)
            pixmap2 = QtGui.QPixmap(icon)
            self.e.lab_icon.setPixmap(pixmap2)

# OUR APPLICATION MAIN WINDOW :
#-----> MAIN APPLICATION CLASS
class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #----> SET WINDOW TITLE AND ICON
        applicationName = "Livix"
        self.setWindowTitle(applicationName)           
       
        UIFunction.initStackTab(self)
        ############################################################

        
        UIFunction.constantFunction(self)
        #############################################################

        self.ui.toodle.clicked.connect(lambda: UIFunction.toodleMenu(self, 160, True))
        #############################################################


        #----> MENU BUTTON PRESSED EVENTS
        self.ui.bn_home.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_home'))
   
        self.ui.AddUser.clicked.connect(lambda: UIFunction.buttonPressed(self, 'AddUser'))
        #############################################################


        UIFunction.stackPage(self)
        #############################################################


        #WHENEVER NECESSERY.
        self.diag = dialogUi()
        self.error = errorUi()



        #---> MOVING THE WINDOW WHEN LEFT MOUSE PRESSED AND DRAGGED OVER APPNAME LABEL
        #SAME TO SAY AS IN COMMENT (C2)
        self.dragPos = self.pos()
        def moveWindow(event):

            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunction.returStatus() == 1: 
                UIFunction.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
            # Maximize at start 

        # WIDGET TO MOVE: WE CHOOSE THE TOPMOST FRAME WHERE THE APPLICATION NAME IS PRESENT AS THE AREA TO MOVE THE WINDOW.
        self.ui.frame_appname.mouseMoveEvent = moveWindow  #CALLING THE FUNCTION TO CJANGE THE POSITION OF THE WINDOW DURING MOUSE DRAG
        
    #----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE: NECESSERY FOR THE moveWindow FUNCTION
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    #############################################################

    def OnClickingSaveData(self, heading, icon, btnOk):
        errorUi.PopUpWindow(self.error, heading, icon, btnOk)
        self.error.exec_()

    
    def dialogexec(self, heading, message, icon, btn1, btn2):
        dialogUi.dialogConstrict(self.diag, heading, message, icon, btn1, btn2)
        self.diag.exec_()
    #############################################################


   

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.showMaximized()
    # GLOBAL_STATE = 1
    window.ui.bn_max.setToolTip("Restore") 
    window.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/restore.png")) #CHANGE THE MAXIMISE ICON TO RESTOR ICON
    window.ui.frame_drag.hide() #HIDE DRAG AS NOT NECESSERY

    sys.exit(app.exec_())


############################################################################################################################################################