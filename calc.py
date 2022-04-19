from PyQt5 import QtCore, QtGui, QtWidgets
import re


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(357, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(20, 10, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setAutoFillBackground(False)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 120, 320, 391))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.XButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("*"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.XButton.sizePolicy().hasHeightForWidth())
        self.XButton.setSizePolicy(sizePolicy)
        self.XButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.XButton.setFont(font)
        self.XButton.setIconSize(QtCore.QSize(25, 16))
        self.XButton.setObjectName("XButton")
        self.gridLayout.addWidget(self.XButton, 4, 3, 1, 1)
        self.fiveButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("5"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fiveButton.sizePolicy().hasHeightForWidth())
        self.fiveButton.setSizePolicy(sizePolicy)
        self.fiveButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fiveButton.setFont(font)
        self.fiveButton.setIconSize(QtCore.QSize(25, 16))
        self.fiveButton.setObjectName("fiveButton")
        self.gridLayout.addWidget(self.fiveButton, 5, 1, 1, 1)
        self.equalButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.math_it())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equalButton.sizePolicy().hasHeightForWidth())
        self.equalButton.setSizePolicy(sizePolicy)
        self.equalButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.equalButton.setFont(font)
        self.equalButton.setIconSize(QtCore.QSize(25, 16))
        self.equalButton.setObjectName("equalButton")
        self.gridLayout.addWidget(self.equalButton, 7, 3, 1, 1)
        self.nineButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("9"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nineButton.sizePolicy().hasHeightForWidth())
        self.nineButton.setSizePolicy(sizePolicy)
        self.nineButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nineButton.setFont(font)
        self.nineButton.setIconSize(QtCore.QSize(25, 16))
        self.nineButton.setObjectName("nineButton")
        self.gridLayout.addWidget(self.nineButton, 4, 2, 1, 1)
        self.twoButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("2"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twoButton.sizePolicy().hasHeightForWidth())
        self.twoButton.setSizePolicy(sizePolicy)
        self.twoButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.twoButton.setFont(font)
        self.twoButton.setIconSize(QtCore.QSize(25, 16))
        self.twoButton.setObjectName("twoButton")
        self.gridLayout.addWidget(self.twoButton, 6, 1, 1, 1)
        self.fourButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("4"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fourButton.sizePolicy().hasHeightForWidth())
        self.fourButton.setSizePolicy(sizePolicy)
        self.fourButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fourButton.setFont(font)
        self.fourButton.setIconSize(QtCore.QSize(25, 16))
        self.fourButton.setObjectName("fourButton")
        self.gridLayout.addWidget(self.fourButton, 5, 0, 1, 1)
        self.plusButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("+"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusButton.sizePolicy().hasHeightForWidth())
        self.plusButton.setSizePolicy(sizePolicy)
        self.plusButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plusButton.setFont(font)
        self.plusButton.setIconSize(QtCore.QSize(25, 16))
        self.plusButton.setObjectName("plusButton")
        self.gridLayout.addWidget(self.plusButton, 6, 3, 1, 1)
        self.plusminusButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.inverse_it())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusminusButton.sizePolicy().hasHeightForWidth())
        self.plusminusButton.setSizePolicy(sizePolicy)
        self.plusminusButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setIconSize(QtCore.QSize(25, 16))
        self.plusminusButton.setObjectName("plusminusButton")
        self.gridLayout.addWidget(self.plusminusButton, 7, 0, 1, 1)
        self.divideButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("/"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divideButton.sizePolicy().hasHeightForWidth())
        self.divideButton.setSizePolicy(sizePolicy)
        self.divideButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.divideButton.setFont(font)
        self.divideButton.setIconSize(QtCore.QSize(25, 16))
        self.divideButton.setObjectName("divideButton")
        self.gridLayout.addWidget(self.divideButton, 3, 3, 1, 1)
        self.threeButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("3"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threeButton.sizePolicy().hasHeightForWidth())
        self.threeButton.setSizePolicy(sizePolicy)
        self.threeButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.threeButton.setFont(font)
        self.threeButton.setIconSize(QtCore.QSize(25, 16))
        self.threeButton.setObjectName("threeButton")
        self.gridLayout.addWidget(self.threeButton, 6, 2, 1, 1)
        self.minusButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("-"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minusButton.sizePolicy().hasHeightForWidth())
        self.minusButton.setSizePolicy(sizePolicy)
        self.minusButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.minusButton.setFont(font)
        self.minusButton.setIconSize(QtCore.QSize(25, 16))
        self.minusButton.setObjectName("minusButton")
        self.gridLayout.addWidget(self.minusButton, 5, 3, 1, 1)
        self.oneButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("1"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneButton.sizePolicy().hasHeightForWidth())
        self.oneButton.setSizePolicy(sizePolicy)
        self.oneButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.oneButton.setFont(font)
        self.oneButton.setIconSize(QtCore.QSize(25, 16))
        self.oneButton.setObjectName("oneButton")
        self.gridLayout.addWidget(self.oneButton, 6, 0, 1, 1)
        self.eightButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("8"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eightButton.sizePolicy().hasHeightForWidth())
        self.eightButton.setSizePolicy(sizePolicy)
        self.eightButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.eightButton.setFont(font)
        self.eightButton.setIconSize(QtCore.QSize(25, 16))
        self.eightButton.setObjectName("eightButton")
        self.gridLayout.addWidget(self.eightButton, 4, 1, 1, 1)
        self.dotButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.dot_it())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dotButton.sizePolicy().hasHeightForWidth())
        self.dotButton.setSizePolicy(sizePolicy)
        self.dotButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dotButton.setFont(font)
        self.dotButton.setIconSize(QtCore.QSize(25, 16))
        self.dotButton.setObjectName("dotButton")
        self.gridLayout.addWidget(self.dotButton, 7, 2, 1, 1)
        self.zeroButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("0"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zeroButton.sizePolicy().hasHeightForWidth())
        self.zeroButton.setSizePolicy(sizePolicy)
        self.zeroButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.zeroButton.setFont(font)
        self.zeroButton.setIconSize(QtCore.QSize(25, 16))
        self.zeroButton.setObjectName("zeroButton")
        self.gridLayout.addWidget(self.zeroButton, 7, 1, 1, 1)
        self.sevenButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("7"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sevenButton.sizePolicy().hasHeightForWidth())
        self.sevenButton.setSizePolicy(sizePolicy)
        self.sevenButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sevenButton.setFont(font)
        self.sevenButton.setIconSize(QtCore.QSize(25, 16))
        self.sevenButton.setObjectName("sevenButton")
        self.gridLayout.addWidget(self.sevenButton, 4, 0, 1, 1)
        self.sixButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("6"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sixButton.sizePolicy().hasHeightForWidth())
        self.sixButton.setSizePolicy(sizePolicy)
        self.sixButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sixButton.setFont(font)
        self.sixButton.setIconSize(QtCore.QSize(25, 16))
        self.sixButton.setObjectName("sixButton")
        self.gridLayout.addWidget(self.sixButton, 5, 2, 1, 1)
        self.arrowButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.remove_it())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arrowButton.sizePolicy().hasHeightForWidth())
        self.arrowButton.setSizePolicy(sizePolicy)
        self.arrowButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.arrowButton.setFont(font)
        self.arrowButton.setIconSize(QtCore.QSize(25, 16))
        self.arrowButton.setObjectName("arrowButton")
        self.gridLayout.addWidget(self.arrowButton, 3, 2, 1, 1)
        self.CButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("C"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CButton.sizePolicy().hasHeightForWidth())
        self.CButton.setSizePolicy(sizePolicy)
        self.CButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CButton.setFont(font)
        self.CButton.setIconSize(QtCore.QSize(25, 16))
        self.CButton.setObjectName("CButton")
        self.gridLayout.addWidget(self.CButton, 3, 1, 1, 1)
        self.percentButton = QtWidgets.QPushButton(self.widget, clicked = lambda: self.press_it("%"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentButton.sizePolicy().hasHeightForWidth())
        self.percentButton.setSizePolicy(sizePolicy)
        self.percentButton.setBaseSize(QtCore.QSize(31, 12))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.percentButton.setFont(font)
        self.percentButton.setIconSize(QtCore.QSize(25, 16))
        self.percentButton.setObjectName("percentButton")
        self.gridLayout.addWidget(self.percentButton, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 357, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #removing a charactere
    def remove_it(self):

        self.outputLabel.setText(self.outputLabel.text()[:-1])

    # calculating the output
    def math_it(self):

        #taking the input string and python make the math for you
        result = eval(self.outputLabel.text())

        #updating the label accordingly to the result
        self.outputLabel.setText(str(result))

    #getting the numbers witouht math operations
    def get_numbers(self):

        math_char = "\*|\\||\+|-|=|/|%"
        screen = self.outputLabel.text()

        chunks = re.split(math_char, screen)

        return chunks

    def inverse_it(self):
        screen = self.outputLabel.text()

        #getting the last number
        try:
            current_number = self.get_numbers()[-1]
        except IndexError:
            current_number = self.get_numbers()
        
        # finally:
        #     print(f"{current_number=}")


        # getting the text without the last number and adding the new inversed one
        new_output = screen[:-len(str(current_number))] + str(-int(current_number))

        if "--" in new_output:
            new_output = new_output.replace("--", "+")
            if "++" in new_output:
                new_output = new_output.replace("++", "+")

        #updating the text
        self.outputLabel.setText(new_output)

    # add a decimal
    def dot_it(self):
        screen =  self.outputLabel.text()

        #checking the current working number and seeing if he is already a decimal
        if "." in self.get_numbers()[-1]:
            pass
        else:
            self.outputLabel.setText(self.outputLabel.text() + ".")

    def press_it(self, pressed):
        """the function wich handle the action of pressed buttons"""
        if pressed == "C":
            #erase fonctionnality
            self.outputLabel.setText("0")

        else:
            # erasing the starting zero
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            #concatenning the input of the user to the label
            self.outputLabel.setText(self.outputLabel.text() + pressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.XButton.setText(_translate("MainWindow", "*"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.dotButton.setText(_translate("MainWindow", "."))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.CButton.setText(_translate("MainWindow", "C"))
        self.percentButton.setText(_translate("MainWindow", "%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
