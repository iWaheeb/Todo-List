from PyQt5 import QtCore, QtGui, QtWidgets
from functionality import Operations


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 497)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.add_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: Operations.add_task(self))
        self.add_button.setGeometry(QtCore.QRect(10, 50, 131, 41))
        self.add_button.setObjectName("add_button")

        self.delete_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: Operations.delete_task(self))
        self.delete_button.setGeometry(QtCore.QRect(150, 50, 131, 41))
        self.delete_button.setObjectName("delete_button")

        self.clear_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: Operations.clear_list(self))
        self.clear_button.setGeometry(QtCore.QRect(290, 50, 141, 41))
        self.clear_button.setObjectName("clear_button")

        self.tasks_list = QtWidgets.QListWidget(self.centralwidget)
        self.tasks_list.setGeometry(QtCore.QRect(10, 110, 421, 341))
        self.tasks_list.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tasks_list.setObjectName("tasks_lists")

        self.input_line = QtWidgets.QLineEdit(self.centralwidget)
        self.input_line.setGeometry(QtCore.QRect(10, 10, 421, 31))
        self.input_line.setObjectName("input_line")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Retrieve all the tasks stored in the database
        Operations.retrieve_tasks(self)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "قائمة المهام"))
        self.delete_button.setText(_translate("MainWindow", "حذف المهمة"))
        self.clear_button.setText(_translate("MainWindow", "حذف الكل"))
        self.add_button.setText(_translate("MainWindow", "إضافة مهمة"))



