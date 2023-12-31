# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.setEnabled(True)
        Form.resize(800, 500)
        Form.setMinimumSize(QtCore.QSize(800, 500))
        Form.setMaximumSize(QtCore.QSize(19200, 10800))
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setAcceptDrops(True)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.MainFrame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy)
        self.MainFrame.setAutoFillBackground(False)
        self.MainFrame.setStyleSheet("QFrame#MainFrame {\n"
"\n"
"    \n"
"    background-color:rgb(0,0,0); \n"
"\n"
"} \n"
"\n"
"QLabel{\n"
"    \n"
"    \n"
"    \n"
"    color: rgb(51, 108, 200);\n"
"}\n"
"\n"
"QFrame#frameJabil {\n"
"    border-image:url(logo1)\n"
"\n"
"} \n"
"\n"
"QLabel#LBFailmode{\n"
"     \n"
"    \n"
"    \n"
"    \n"
"    color: rgb(255, 255, 0);\n"
"}\n"
"\n"
"QLabel#LBRework{\n"
" \n"
"    color: rgb(255, 255, 0);\n"
"}\n"
"\n"
"QLabel#LBMachine {\n"
" \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel#LBSerialNumber {\n"
" \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"Qlabel#TESerialNumber {\n"
"color: rgb(255, 255, 0);\n"
"}\n"
"")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainFrame.setLineWidth(0)
        self.MainFrame.setObjectName("MainFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MainFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DataFrame = QtWidgets.QFrame(self.MainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataFrame.sizePolicy().hasHeightForWidth())
        self.DataFrame.setSizePolicy(sizePolicy)
        self.DataFrame.setAutoFillBackground(False)
        self.DataFrame.setStyleSheet("")
        self.DataFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DataFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DataFrame.setLineWidth(0)
        self.DataFrame.setObjectName("DataFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.DataFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LBTitle1 = QtWidgets.QLabel(self.DataFrame)
        self.LBTitle1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBTitle1.sizePolicy().hasHeightForWidth())
        self.LBTitle1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LBTitle1.setFont(font)
        self.LBTitle1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LBTitle1.setAlignment(QtCore.Qt.AlignCenter)
        self.LBTitle1.setObjectName("LBTitle1")
        self.verticalLayout_2.addWidget(self.LBTitle1)
        self.LBSerialNumber = QtWidgets.QLabel(self.DataFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBSerialNumber.sizePolicy().hasHeightForWidth())
        self.LBSerialNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LBSerialNumber.setFont(font)
        self.LBSerialNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LBSerialNumber.setAutoFillBackground(False)
        self.LBSerialNumber.setText("")
        self.LBSerialNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.LBSerialNumber.setObjectName("LBSerialNumber")
        self.verticalLayout_2.addWidget(self.LBSerialNumber)
        self.LBTitle2 = QtWidgets.QLabel(self.DataFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBTitle2.sizePolicy().hasHeightForWidth())
        self.LBTitle2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LBTitle2.setFont(font)
        self.LBTitle2.setAlignment(QtCore.Qt.AlignCenter)
        self.LBTitle2.setObjectName("LBTitle2")
        self.verticalLayout_2.addWidget(self.LBTitle2)
        self.LBFailmode = QtWidgets.QLabel(self.DataFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBFailmode.sizePolicy().hasHeightForWidth())
        self.LBFailmode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LBFailmode.setFont(font)
        self.LBFailmode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LBFailmode.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LBFailmode.setAlignment(QtCore.Qt.AlignCenter)
        self.LBFailmode.setObjectName("LBFailmode")
        self.verticalLayout_2.addWidget(self.LBFailmode)
        self.LBTitle3 = QtWidgets.QLabel(self.DataFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBTitle3.sizePolicy().hasHeightForWidth())
        self.LBTitle3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LBTitle3.setFont(font)
        self.LBTitle3.setAlignment(QtCore.Qt.AlignCenter)
        self.LBTitle3.setObjectName("LBTitle3")
        self.verticalLayout_2.addWidget(self.LBTitle3)
        self.LBRework = QtWidgets.QLabel(self.DataFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBRework.sizePolicy().hasHeightForWidth())
        self.LBRework.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LBRework.setFont(font)
        self.LBRework.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LBRework.setAutoFillBackground(False)
        self.LBRework.setAlignment(QtCore.Qt.AlignCenter)
        self.LBRework.setObjectName("LBRework")
        self.verticalLayout_2.addWidget(self.LBRework)
        self.LBTitle4 = QtWidgets.QLabel(self.DataFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBTitle4.sizePolicy().hasHeightForWidth())
        self.LBTitle4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LBTitle4.setFont(font)
        self.LBTitle4.setAlignment(QtCore.Qt.AlignCenter)
        self.LBTitle4.setObjectName("LBTitle4")
        self.verticalLayout_2.addWidget(self.LBTitle4)
        self.LBMachine = QtWidgets.QLabel(self.DataFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBMachine.sizePolicy().hasHeightForWidth())
        self.LBMachine.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LBMachine.setFont(font)
        self.LBMachine.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LBMachine.setAlignment(QtCore.Qt.AlignCenter)
        self.LBMachine.setObjectName("LBMachine")
        self.verticalLayout_2.addWidget(self.LBMachine)
        self.horizontalLayout.addWidget(self.DataFrame)
        self.StatusFrame = QtWidgets.QFrame(self.MainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StatusFrame.sizePolicy().hasHeightForWidth())
        self.StatusFrame.setSizePolicy(sizePolicy)
        self.StatusFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.StatusFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.StatusFrame.setLineWidth(0)
        self.StatusFrame.setObjectName("StatusFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.StatusFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PB01 = QtWidgets.QPushButton(self.StatusFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PB01.sizePolicy().hasHeightForWidth())
        self.PB01.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.PB01.setFont(font)
        self.PB01.setAutoFillBackground(False)
        self.PB01.setIconSize(QtCore.QSize(12, 12))
        self.PB01.setCheckable(False)
        self.PB01.setObjectName("PB01")
        self.verticalLayout.addWidget(self.PB01)
        self.label = QtWidgets.QLabel(self.StatusFrame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox1 = QtWidgets.QComboBox(self.StatusFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox1.sizePolicy().hasHeightForWidth())
        self.comboBox1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox1.setFont(font)
        self.comboBox1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox1.setObjectName("comboBox1")
        self.verticalLayout.addWidget(self.comboBox1)
        self.LBTitle1_3 = QtWidgets.QLabel(self.StatusFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBTitle1_3.sizePolicy().hasHeightForWidth())
        self.LBTitle1_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.LBTitle1_3.setFont(font)
        self.LBTitle1_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LBTitle1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.LBTitle1_3.setObjectName("LBTitle1_3")
        self.verticalLayout.addWidget(self.LBTitle1_3)
        self.TESerialNumber = QtWidgets.QPlainTextEdit(self.StatusFrame)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TESerialNumber.setFont(font)
        self.TESerialNumber.setMouseTracking(True)
        self.TESerialNumber.setTabletTracking(False)
        self.TESerialNumber.setAcceptDrops(False)
        self.TESerialNumber.setAutoFillBackground(False)
        self.TESerialNumber.setStyleSheet("\n"
"selection-background-color: rgb(0, 0, 0);")
        self.TESerialNumber.setFrameShape(QtWidgets.QFrame.HLine)
        self.TESerialNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TESerialNumber.setLineWidth(1)
        self.TESerialNumber.setTabChangesFocus(False)
        self.TESerialNumber.setUndoRedoEnabled(False)
        self.TESerialNumber.setReadOnly(False)
        self.TESerialNumber.setOverwriteMode(False)
        self.TESerialNumber.setTabStopWidth(1)
        self.TESerialNumber.setMaximumBlockCount(26)
        self.TESerialNumber.setCenterOnScroll(True)
        self.TESerialNumber.setObjectName("TESerialNumber")
        self.verticalLayout.addWidget(self.TESerialNumber)
        self.frame_Counter = QtWidgets.QFrame(self.StatusFrame)
        self.frame_Counter.setStyleSheet("QLabel#LBCounter1 {\n"
"color:rgb(198, 65, 255)\n"
"}\n"
"QLabel#LBCounter2 {\n"
"color:rgb(198, 65, 255)\n"
"}\n"
"QLabel#LBCounter1 {\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLabel#LBCounter2 {\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_Counter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Counter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Counter.setObjectName("frame_Counter")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_Counter)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LBCounter1 = QtWidgets.QLabel(self.frame_Counter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.LBCounter1.setFont(font)
        self.LBCounter1.setFrameShape(QtWidgets.QFrame.Panel)
        self.LBCounter1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LBCounter1.setLineWidth(3)
        self.LBCounter1.setMidLineWidth(0)
        self.LBCounter1.setObjectName("LBCounter1")
        self.gridLayout_2.addWidget(self.LBCounter1, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_Counter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.LBCounter2 = QtWidgets.QLabel(self.frame_Counter)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.LBCounter2.setFont(font)
        self.LBCounter2.setFrameShape(QtWidgets.QFrame.Panel)
        self.LBCounter2.setLineWidth(3)
        self.LBCounter2.setObjectName("LBCounter2")
        self.gridLayout_2.addWidget(self.LBCounter2, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_Counter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_Counter)
        self.frame_2 = QtWidgets.QFrame(self.StatusFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.QReset = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.QReset.setFont(font)
        self.QReset.setObjectName("QReset")
        self.horizontalLayout_2.addWidget(self.QReset)
        spacerItem3 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.frameJabil = QtWidgets.QFrame(self.StatusFrame)
        self.frameJabil.setAutoFillBackground(False)
        self.frameJabil.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameJabil.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameJabil.setObjectName("frameJabil")
        self.gridLayout = QtWidgets.QGridLayout(self.frameJabil)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addWidget(self.frameJabil)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(7, 5)
        self.verticalLayout.setStretch(8, 2)
        self.verticalLayout.setStretch(9, 4)
        self.PB01.raise_()
        self.label.raise_()
        self.comboBox1.raise_()
        self.LBTitle1_3.raise_()
        self.frame_Counter.raise_()
        self.frame_2.raise_()
        self.frameJabil.raise_()
        self.TESerialNumber.raise_()
        self.horizontalLayout.addWidget(self.StatusFrame)
        self.horizontalLayout.setStretch(0, 3)
        self.verticalLayout_3.addWidget(self.MainFrame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.LBTitle1.setText(_translate("Form", "<html><head/><body><p>Serial Number</p></body></html>"))
        self.LBTitle2.setText(_translate("Form", "<html><head/><body><p>Fail mode/Modo de Falla</p></body></html>"))
        self.LBFailmode.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.LBTitle3.setText(_translate("Form", "<html><head/><body><p>Disposicion</p></body></html>"))
        self.LBRework.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.LBTitle4.setText(_translate("Form", "<html><head/><body><p>De que Maquina viene?</p></body></html>"))
        self.LBMachine.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.PB01.setText(_translate("Form", "Refresh"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; font-style:italic;\">Customer</span></p></body></html>"))
        self.comboBox1.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.LBTitle1_3.setText(_translate("Form", "INPUT SN"))
        self.LBCounter1.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">-</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Fallas BGPT2</span></p></body></html>"))
        self.LBCounter2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">-</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Fallas BGPT1</span></p></body></html>"))
        self.QReset.setText(_translate("Form", "RESET COUNTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
