# importing required libraries
from PyQt5 import *
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWebEngineWidgets import * 
from PyQt5.QtPrintSupport import * 
import os
import sys
import pyfiglet 


os.system(' clear ')  

# creating main window class
class MainWindow(QMainWindow):
  
    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
  
        self.setStyleSheet("background-color: red;") # color for window 
        # creating a QWebEngineView
        self.browser = QWebEngineView()
  
        # setting default browser url as google
        #https://duckduckgo.com/
        self.browser.setUrl(QUrl("https://duckduckgo.com"))
  
        # adding action when url get changed
        self.browser.urlChanged.connect(self.update_urlbar)

        self.browser.loadFinished.connect(self.update_title)
  
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
  
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
  
        self.addToolBar(navtb)

        back_btn = QAction("Back", self)
  
        back_btn.setStatusTip("Back to previous page")

        back_btn.triggered.connect(self.browser.back)

        navtb.addAction(back_btn)

        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")
  
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)
  

        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")

        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)
  
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
  
        navtb.addSeparator()
  
        # creating a line edit for the url
        self.urlbar = QLineEdit()
  
        # adding action when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)
  
        # adding this to the tool bar
        navtb.addWidget(self.urlbar)
  
        # adding stop action to the tool bar
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)
        # show commands
        self.show()
    # method for updating the title of the window
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - A Hackers Browser" % title)
    
    def navigate_home(self):
  
        # search query for links adding more links and applets 
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.browser.setUrl(QUrl("https://youtube.com"))
        self.browser.setUrl(QUrl("https://www.shodan.io/"))
        self.browser.setUrl(QUrl("https://null-byte.wonderhowto.com/"))


    # method called by the line edit when return key is pressed
    def navigate_to_url(self):
  
        # getting url and converting it to QUrl objetc
        q = QUrl(self.urlbar.text())
        # if it = nothing yet just move onto http link for google 
        if q.scheme() == "":
            # set url scheme to html
            q.setScheme("index.html")
            #q.setScheme("http")
            #q.setScheme("https")
            #q.setScheme("file")
            
  
        self.browser.setUrl(q)

    def update_urlbar(self, q):
  
        # url bar
        self.urlbar.setText(q.toString())
  
        # cursor psoition foer url bar 
        self.urlbar.setCursorPosition(0)
  
  
# creating a pyQt5 application
app = QApplication(sys.argv)
  
# setting name to the application
app.setApplicationName("Hackers Browser")
# main window/GUI
window = MainWindow()
  
# window loop cause if not broqwser go deadddd
app.exec_()