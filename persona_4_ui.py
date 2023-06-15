# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'persona_4.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_persona4Window(object):
    def setupUi(self, persona4Window):
        if not persona4Window.objectName():
            persona4Window.setObjectName(u"persona4Window")
        persona4Window.resize(800, 600)
        persona4Window.setMaximumSize(QSize(800, 600))
        self.mainWidget = QWidget(persona4Window)
        self.mainWidget.setObjectName(u"mainWidget")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(12)
        self.mainWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainStackedWidget = QStackedWidget(self.mainWidget)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")
        self.mainStackedWidget.setStyleSheet(u"QWidget {\n"
"	background-color: #FFEE32;\n"
"}\n"
"QLabel {\n"
"	color: #333533;\n"
"}")
        self.landingPage = QWidget()
        self.landingPage.setObjectName(u"landingPage")
        self.verticalLayout_2 = QVBoxLayout(self.landingPage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.landingPage)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setStyleSheet(u"QFrame#headerFrame {\n"
"	background-color: #FFEE32;\n"
"}\n"
"QLabel {\n"
"	border-radius: 12px;\n"
"}")
        self.headerFrame.setFrameShape(QFrame.NoFrame)
        self.headerFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.headerFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.headingLbl = QLabel(self.headerFrame)
        self.headingLbl.setObjectName(u"headingLbl")
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(48)
        font1.setBold(True)
        self.headingLbl.setFont(font1)

        self.verticalLayout_3.addWidget(self.headingLbl)

        self.bodyLbl = QLabel(self.headerFrame)
        self.bodyLbl.setObjectName(u"bodyLbl")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bodyLbl.sizePolicy().hasHeightForWidth())
        self.bodyLbl.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.bodyLbl.setFont(font2)
        self.bodyLbl.setStyleSheet(u"background-color: grey;\n"
"color: white;\n"
"padding: 4px 4px 4px 4px;")

        self.verticalLayout_3.addWidget(self.bodyLbl)


        self.verticalLayout_2.addWidget(self.headerFrame)

        self.selectionFrame = QFrame(self.landingPage)
        self.selectionFrame.setObjectName(u"selectionFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selectionFrame.sizePolicy().hasHeightForWidth())
        self.selectionFrame.setSizePolicy(sizePolicy1)
        self.selectionFrame.setStyleSheet(u"QFrame#selectionFrame{\n"
"	background-color: #FFD100;\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"}\n"
"QWidget#ps2Frame, QWidget#goldenFrame {\n"
"	background-color: #333533;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton {\n"
"	background-color: #fff6cc;\n"
"	color: #333533;\n"
"	padding: 12px 12px 12px 12px;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #333533;\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"}")
        self.selectionFrame.setFrameShape(QFrame.NoFrame)
        self.selectionFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.selectionFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.goldenFrame = QWidget(self.selectionFrame)
        self.goldenFrame.setObjectName(u"goldenFrame")
        self.goldenFrame.setStyleSheet(u"QLabel {\n"
"	background-color: #333533;\n"
"	color: white;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.goldenFrame)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(14, 14, 14, 14)
        self.headingLbl_3 = QLabel(self.goldenFrame)
        self.headingLbl_3.setObjectName(u"headingLbl_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.headingLbl_3.sizePolicy().hasHeightForWidth())
        self.headingLbl_3.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.headingLbl_3.setFont(font3)
        self.headingLbl_3.setWordWrap(False)

        self.verticalLayout_5.addWidget(self.headingLbl_3)

        self.questsBtn_2 = QPushButton(self.goldenFrame)
        self.questsBtn_2.setObjectName(u"questsBtn_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.questsBtn_2.sizePolicy().hasHeightForWidth())
        self.questsBtn_2.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.questsBtn_2.setFont(font4)
        self.questsBtn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.questsBtn_2)

        self.weaponsBtn_2 = QPushButton(self.goldenFrame)
        self.weaponsBtn_2.setObjectName(u"weaponsBtn_2")
        sizePolicy3.setHeightForWidth(self.weaponsBtn_2.sizePolicy().hasHeightForWidth())
        self.weaponsBtn_2.setSizePolicy(sizePolicy3)
        self.weaponsBtn_2.setFont(font4)
        self.weaponsBtn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.weaponsBtn_2)

        self.answersBtn_2 = QPushButton(self.goldenFrame)
        self.answersBtn_2.setObjectName(u"answersBtn_2")
        sizePolicy3.setHeightForWidth(self.answersBtn_2.sizePolicy().hasHeightForWidth())
        self.answersBtn_2.setSizePolicy(sizePolicy3)
        self.answersBtn_2.setFont(font4)
        self.answersBtn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.answersBtn_2.setFlat(False)

        self.verticalLayout_5.addWidget(self.answersBtn_2)

        self.shadowsBtn_2 = QPushButton(self.goldenFrame)
        self.shadowsBtn_2.setObjectName(u"shadowsBtn_2")
        sizePolicy3.setHeightForWidth(self.shadowsBtn_2.sizePolicy().hasHeightForWidth())
        self.shadowsBtn_2.setSizePolicy(sizePolicy3)
        self.shadowsBtn_2.setFont(font4)
        self.shadowsBtn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.shadowsBtn_2)


        self.horizontalLayout.addWidget(self.goldenFrame)


        self.verticalLayout_2.addWidget(self.selectionFrame)

        self.mainStackedWidget.addWidget(self.landingPage)
        self.questsPage = QWidget()
        self.questsPage.setObjectName(u"questsPage")
        self.questsPage.setStyleSheet(u"QFrame#infoFrame {\n"
"	background-color: #FFD100;\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"}\n"
"QPushButton {\n"
"	background-color: #fff6cc;\n"
"	color: #333533;\n"
"	padding: 12px 12px 12px 12px;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #333533;\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.questsPage)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.headerFrame_2 = QFrame(self.questsPage)
        self.headerFrame_2.setObjectName(u"headerFrame_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.headerFrame_2.sizePolicy().hasHeightForWidth())
        self.headerFrame_2.setSizePolicy(sizePolicy4)
        self.headerFrame_2.setStyleSheet(u"QFrame#headerFrame {\n"
"	background-color: #FFEE32;\n"
"}\n"
"QLabel {\n"
"	border-radius: 12px;\n"
"}")
        self.headerFrame_2.setFrameShape(QFrame.NoFrame)
        self.headerFrame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.headerFrame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.headingLbl_4 = QLabel(self.headerFrame_2)
        self.headingLbl_4.setObjectName(u"headingLbl_4")
        self.headingLbl_4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.headingLbl_4)

        self.headerInfoFrame = QFrame(self.headerFrame_2)
        self.headerInfoFrame.setObjectName(u"headerInfoFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.headerInfoFrame.sizePolicy().hasHeightForWidth())
        self.headerInfoFrame.setSizePolicy(sizePolicy5)
        self.headerInfoFrame.setFrameShape(QFrame.NoFrame)
        self.headerInfoFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.headerInfoFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.questsHomeBtn = QPushButton(self.headerInfoFrame)
        self.questsHomeBtn.setObjectName(u"questsHomeBtn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.questsHomeBtn.sizePolicy().hasHeightForWidth())
        self.questsHomeBtn.setSizePolicy(sizePolicy6)
        self.questsHomeBtn.setFont(font2)
        self.questsHomeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.questsHomeBtn)

        self.bodyLbl_2 = QLabel(self.headerInfoFrame)
        self.bodyLbl_2.setObjectName(u"bodyLbl_2")
        sizePolicy.setHeightForWidth(self.bodyLbl_2.sizePolicy().hasHeightForWidth())
        self.bodyLbl_2.setSizePolicy(sizePolicy)
        self.bodyLbl_2.setFont(font2)
        self.bodyLbl_2.setStyleSheet(u"background-color: grey;\n"
"color: white;\n"
"padding: 4px 4px 4px 4px;")

        self.verticalLayout_10.addWidget(self.bodyLbl_2)


        self.horizontalLayout_3.addWidget(self.headerInfoFrame)


        self.verticalLayout_11.addWidget(self.headerFrame_2)

        self.infoFrame = QFrame(self.questsPage)
        self.infoFrame.setObjectName(u"infoFrame")
        sizePolicy2.setHeightForWidth(self.infoFrame.sizePolicy().hasHeightForWidth())
        self.infoFrame.setSizePolicy(sizePolicy2)
        self.infoFrame.setStyleSheet(u"QTableWidget::item {\n"
"	background-color: #4D4D4D;\n"
"	color: white;\n"
"	text-align: center;\n"
"}\n"
"QTableView {\n"
"	background-color: #333533;\n"
"	border-radius: 12px;\n"
"	gridline-color: white;\n"
"}\n"
"QAbstractItemView {\n"
"	background-color: #333533;\n"
"}\n"
"QHeaderView::section {\n"
"	background-color: #202020;\n"
"	color: white;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"	border-top: 6px solid white;\n"
"}")
        self.infoFrame.setFrameShape(QFrame.NoFrame)
        self.infoFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_9 = QVBoxLayout(self.infoFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.questsTable = QTableWidget(self.infoFrame)
        if (self.questsTable.columnCount() < 5):
            self.questsTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.questsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.questsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.questsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.questsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.questsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.questsTable.rowCount() < 50):
            self.questsTable.setRowCount(50)
        font5 = QFont()
        font5.setFamilies([u"Inter"])
        font5.setPointSize(8)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font5);
        self.questsTable.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self.questsTable.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font5);
        self.questsTable.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font5);
        self.questsTable.setItem(0, 3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font5);
        self.questsTable.setItem(0, 4, __qtablewidgetitem9)
        self.questsTable.setObjectName(u"questsTable")
        sizePolicy2.setHeightForWidth(self.questsTable.sizePolicy().hasHeightForWidth())
        self.questsTable.setSizePolicy(sizePolicy2)
        self.questsTable.setStyleSheet(u"")
        self.questsTable.setFrameShape(QFrame.NoFrame)
        self.questsTable.setFrameShadow(QFrame.Plain)
        self.questsTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.questsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.questsTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.questsTable.setTabKeyNavigation(True)
        self.questsTable.setDragEnabled(False)
        self.questsTable.setDragDropOverwriteMode(False)
        self.questsTable.setAlternatingRowColors(False)
        self.questsTable.setSelectionMode(QAbstractItemView.NoSelection)
        self.questsTable.setTextElideMode(Qt.ElideRight)
        self.questsTable.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.questsTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.questsTable.setShowGrid(True)
        self.questsTable.setGridStyle(Qt.SolidLine)
        self.questsTable.setSortingEnabled(False)
        self.questsTable.setWordWrap(True)
        self.questsTable.setCornerButtonEnabled(True)
        self.questsTable.setRowCount(50)
        self.questsTable.setColumnCount(5)
        self.questsTable.horizontalHeader().setVisible(False)
        self.questsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.questsTable.horizontalHeader().setMinimumSectionSize(32)
        self.questsTable.horizontalHeader().setDefaultSectionSize(100)
        self.questsTable.horizontalHeader().setHighlightSections(True)
        self.questsTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.questsTable.horizontalHeader().setStretchLastSection(True)
        self.questsTable.verticalHeader().setVisible(False)
        self.questsTable.verticalHeader().setCascadingSectionResizes(False)
        self.questsTable.verticalHeader().setProperty("showSortIndicator", False)
        self.questsTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_9.addWidget(self.questsTable)


        self.verticalLayout_11.addWidget(self.infoFrame)

        self.mainStackedWidget.addWidget(self.questsPage)
        self.answersPage = QWidget()
        self.answersPage.setObjectName(u"answersPage")
        self.answersPage.setStyleSheet(u"QFrame#infoFrame_2 {\n"
"	background-color: #FFD100;\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"}\n"
"QPushButton {\n"
"	background-color: #fff6cc;\n"
"	color: #333533;\n"
"	padding: 12px 12px 12px 12px;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #333533;\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.answersPage)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.headerFrame_3 = QFrame(self.answersPage)
        self.headerFrame_3.setObjectName(u"headerFrame_3")
        sizePolicy4.setHeightForWidth(self.headerFrame_3.sizePolicy().hasHeightForWidth())
        self.headerFrame_3.setSizePolicy(sizePolicy4)
        self.headerFrame_3.setStyleSheet(u"QFrame#headerFrame {\n"
"	background-color: #FFEE32;\n"
"}\n"
"QLabel {\n"
"	border-radius: 12px;\n"
"}")
        self.headerFrame_3.setFrameShape(QFrame.NoFrame)
        self.headerFrame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.headerFrame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.headingLbl_5 = QLabel(self.headerFrame_3)
        self.headingLbl_5.setObjectName(u"headingLbl_5")
        self.headingLbl_5.setFont(font1)

        self.horizontalLayout_4.addWidget(self.headingLbl_5)

        self.headerInfoFrame_2 = QFrame(self.headerFrame_3)
        self.headerInfoFrame_2.setObjectName(u"headerInfoFrame_2")
        sizePolicy5.setHeightForWidth(self.headerInfoFrame_2.sizePolicy().hasHeightForWidth())
        self.headerInfoFrame_2.setSizePolicy(sizePolicy5)
        self.headerInfoFrame_2.setFrameShape(QFrame.NoFrame)
        self.headerInfoFrame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_12 = QVBoxLayout(self.headerInfoFrame_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.answersHomeBtn = QPushButton(self.headerInfoFrame_2)
        self.answersHomeBtn.setObjectName(u"answersHomeBtn")
        sizePolicy6.setHeightForWidth(self.answersHomeBtn.sizePolicy().hasHeightForWidth())
        self.answersHomeBtn.setSizePolicy(sizePolicy6)
        self.answersHomeBtn.setFont(font2)
        self.answersHomeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.answersHomeBtn)

        self.bodyLbl_3 = QLabel(self.headerInfoFrame_2)
        self.bodyLbl_3.setObjectName(u"bodyLbl_3")
        sizePolicy.setHeightForWidth(self.bodyLbl_3.sizePolicy().hasHeightForWidth())
        self.bodyLbl_3.setSizePolicy(sizePolicy)
        self.bodyLbl_3.setFont(font2)
        self.bodyLbl_3.setStyleSheet(u"background-color: grey;\n"
"color: white;\n"
"padding: 4px 4px 4px 4px;")

        self.verticalLayout_12.addWidget(self.bodyLbl_3)


        self.horizontalLayout_4.addWidget(self.headerInfoFrame_2)


        self.verticalLayout_4.addWidget(self.headerFrame_3)

        self.infoFrame_2 = QFrame(self.answersPage)
        self.infoFrame_2.setObjectName(u"infoFrame_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.infoFrame_2.sizePolicy().hasHeightForWidth())
        self.infoFrame_2.setSizePolicy(sizePolicy7)
        self.infoFrame_2.setStyleSheet(u"QTableWidget::item {\n"
"	background-color: #4D4D4D;\n"
"	color: white;\n"
"	text-align: center;\n"
"}\n"
"QTableView {\n"
"	background-color: #333533;\n"
"	border-radius: 12px;\n"
"	gridline-color: white;\n"
"}\n"
"QAbstractItemView {\n"
"	background-color: #333533;\n"
"}\n"
"QHeaderView::section {\n"
"	background-color: #202020;\n"
"	color: white;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"	border-top: 6px solid white;\n"
"}")
        self.infoFrame_2.setFrameShape(QFrame.NoFrame)
        self.infoFrame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.infoFrame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.answersTable = QTableWidget(self.infoFrame_2)
        if (self.answersTable.columnCount() < 3):
            self.answersTable.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font2);
        self.answersTable.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font2);
        self.answersTable.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font2);
        self.answersTable.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        self.answersTable.setObjectName(u"answersTable")
        sizePolicy2.setHeightForWidth(self.answersTable.sizePolicy().hasHeightForWidth())
        self.answersTable.setSizePolicy(sizePolicy2)
        self.answersTable.setStyleSheet(u"")
        self.answersTable.setFrameShape(QFrame.NoFrame)
        self.answersTable.setFrameShadow(QFrame.Plain)
        self.answersTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.answersTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.answersTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.answersTable.setTabKeyNavigation(False)
        self.answersTable.setDragEnabled(False)
        self.answersTable.setDragDropOverwriteMode(False)
        self.answersTable.setAlternatingRowColors(False)
        self.answersTable.setSelectionMode(QAbstractItemView.NoSelection)
        self.answersTable.setTextElideMode(Qt.ElideRight)
        self.answersTable.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.answersTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.answersTable.setShowGrid(True)
        self.answersTable.setGridStyle(Qt.SolidLine)
        self.answersTable.setSortingEnabled(False)
        self.answersTable.setWordWrap(True)
        self.answersTable.setCornerButtonEnabled(True)
        self.answersTable.setRowCount(0)
        self.answersTable.setColumnCount(3)
        self.answersTable.horizontalHeader().setVisible(False)
        self.answersTable.horizontalHeader().setCascadingSectionResizes(False)
        self.answersTable.horizontalHeader().setMinimumSectionSize(32)
        self.answersTable.horizontalHeader().setDefaultSectionSize(100)
        self.answersTable.horizontalHeader().setHighlightSections(True)
        self.answersTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.answersTable.horizontalHeader().setStretchLastSection(True)
        self.answersTable.verticalHeader().setVisible(False)
        self.answersTable.verticalHeader().setCascadingSectionResizes(False)
        self.answersTable.verticalHeader().setProperty("showSortIndicator", False)
        self.answersTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_6.addWidget(self.answersTable)


        self.verticalLayout_4.addWidget(self.infoFrame_2)

        self.mainStackedWidget.addWidget(self.answersPage)
        self.shadowsPage = QWidget()
        self.shadowsPage.setObjectName(u"shadowsPage")
        self.shadowsPage.setStyleSheet(u"QFrame#infoFrame_3 {\n"
"	background-color: #FFD100;\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"}\n"
"QFrame#shadowInfoFrame {\n"
"	background-color: #fff6cc;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton {\n"
"	background-color: #fff6cc;\n"
"	color: #333533;\n"
"	padding: 12px 12px 12px 12px;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #333533;\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.shadowsPage)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.headerFrame_4 = QFrame(self.shadowsPage)
        self.headerFrame_4.setObjectName(u"headerFrame_4")
        sizePolicy4.setHeightForWidth(self.headerFrame_4.sizePolicy().hasHeightForWidth())
        self.headerFrame_4.setSizePolicy(sizePolicy4)
        self.headerFrame_4.setStyleSheet(u"QFrame#headerFrame {\n"
"	background-color: #FFEE32;\n"
"}\n"
"QLabel {\n"
"	border-radius: 12px;\n"
"}")
        self.headerFrame_4.setFrameShape(QFrame.NoFrame)
        self.headerFrame_4.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.headerFrame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.headingLbl_6 = QLabel(self.headerFrame_4)
        self.headingLbl_6.setObjectName(u"headingLbl_6")
        self.headingLbl_6.setFont(font1)

        self.horizontalLayout_5.addWidget(self.headingLbl_6)

        self.headerInfoFrame_3 = QFrame(self.headerFrame_4)
        self.headerInfoFrame_3.setObjectName(u"headerInfoFrame_3")
        sizePolicy5.setHeightForWidth(self.headerInfoFrame_3.sizePolicy().hasHeightForWidth())
        self.headerInfoFrame_3.setSizePolicy(sizePolicy5)
        self.headerInfoFrame_3.setFrameShape(QFrame.NoFrame)
        self.headerInfoFrame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout_13 = QVBoxLayout(self.headerInfoFrame_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.shadowsHomeBtn = QPushButton(self.headerInfoFrame_3)
        self.shadowsHomeBtn.setObjectName(u"shadowsHomeBtn")
        sizePolicy6.setHeightForWidth(self.shadowsHomeBtn.sizePolicy().hasHeightForWidth())
        self.shadowsHomeBtn.setSizePolicy(sizePolicy6)
        self.shadowsHomeBtn.setFont(font2)
        self.shadowsHomeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.shadowsHomeBtn)

        self.bodyLbl_4 = QLabel(self.headerInfoFrame_3)
        self.bodyLbl_4.setObjectName(u"bodyLbl_4")
        sizePolicy.setHeightForWidth(self.bodyLbl_4.sizePolicy().hasHeightForWidth())
        self.bodyLbl_4.setSizePolicy(sizePolicy)
        self.bodyLbl_4.setFont(font2)
        self.bodyLbl_4.setStyleSheet(u"background-color: grey;\n"
"color: white;\n"
"padding: 4px 4px 4px 4px;")

        self.verticalLayout_13.addWidget(self.bodyLbl_4)


        self.horizontalLayout_5.addWidget(self.headerInfoFrame_3)


        self.verticalLayout_8.addWidget(self.headerFrame_4)

        self.infoFrame_3 = QFrame(self.shadowsPage)
        self.infoFrame_3.setObjectName(u"infoFrame_3")
        sizePolicy7.setHeightForWidth(self.infoFrame_3.sizePolicy().hasHeightForWidth())
        self.infoFrame_3.setSizePolicy(sizePolicy7)
        self.infoFrame_3.setStyleSheet(u"QListView {\n"
"	border-top: 6px solid white;\n"
"}\n"
"QListView::item {\n"
"	background-color: #4D4D4D;\n"
"	color: white;\n"
"}\n"
"QAbstractItemView {\n"
"	background-color: #333533;\n"
"}\n"
"QScrollBar:vertical {\n"
"	width: 12px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: grey;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 4px solid grey;\n"
"    background: white;\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.infoFrame_3.setFrameShape(QFrame.NoFrame)
        self.infoFrame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.infoFrame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.shadowsList = QListWidget(self.infoFrame_3)
        self.shadowsList.setObjectName(u"shadowsList")
        sizePolicy2.setHeightForWidth(self.shadowsList.sizePolicy().hasHeightForWidth())
        self.shadowsList.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setFamilies([u"Inter"])
        font6.setPointSize(12)
        font6.setBold(False)
        self.shadowsList.setFont(font6)
        self.shadowsList.setFrameShape(QFrame.NoFrame)
        self.shadowsList.setFrameShadow(QFrame.Plain)
        self.shadowsList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.shadowsList.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.shadowsList.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.shadowsList)

        self.shadowInfoFrame = QFrame(self.infoFrame_3)
        self.shadowInfoFrame.setObjectName(u"shadowInfoFrame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.shadowInfoFrame.sizePolicy().hasHeightForWidth())
        self.shadowInfoFrame.setSizePolicy(sizePolicy8)
        self.shadowInfoFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #333533;\n"
"	border-radius: 6px;\n"
"}\n"
"QFrame#propertiesFrame {\n"
"	background-color: #202020;\n"
"}\n"
"QFrame#skillsFrame {\n"
"	background-color: #D6D6D6;\n"
"}")
        self.shadowInfoFrame.setFrameShape(QFrame.NoFrame)
        self.shadowInfoFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.shadowInfoFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.propertiesFrame = QFrame(self.shadowInfoFrame)
        self.propertiesFrame.setObjectName(u"propertiesFrame")
        self.propertiesFrame.setStyleSheet(u"QFrame#nameLvlFrame {\n"
"	background-color: #80b918;\n"
"	color: white;\n"
"}\n"
"QLabel#nameLbl {\n"
"	background-color: #ffb700;\n"
"}\n"
"QLabel#lvlLbl, QLabel#hpSpLbl, QLabel#statsLbl {\n"
"	background-color: none;\n"
"	color: white;\n"
"}")
        self.propertiesFrame.setFrameShape(QFrame.NoFrame)
        self.propertiesFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_21 = QVBoxLayout(self.propertiesFrame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 9, 9, 9)
        self.nameLvlFrame = QFrame(self.propertiesFrame)
        self.nameLvlFrame.setObjectName(u"nameLvlFrame")
        self.nameLvlFrame.setFrameShape(QFrame.NoFrame)
        self.nameLvlFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.nameLvlFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lvlLbl = QLabel(self.nameLvlFrame)
        self.lvlLbl.setObjectName(u"lvlLbl")
        sizePolicy2.setHeightForWidth(self.lvlLbl.sizePolicy().hasHeightForWidth())
        self.lvlLbl.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setFamilies([u"Inter"])
        font7.setPointSize(18)
        font7.setBold(True)
        self.lvlLbl.setFont(font7)
        self.lvlLbl.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.lvlLbl)

        self.hpSpLbl = QLabel(self.nameLvlFrame)
        self.hpSpLbl.setObjectName(u"hpSpLbl")
        self.hpSpLbl.setFont(font)
        self.hpSpLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.hpSpLbl)


        self.verticalLayout_21.addWidget(self.nameLvlFrame)

        self.statsFrame = QFrame(self.propertiesFrame)
        self.statsFrame.setObjectName(u"statsFrame")
        self.statsFrame.setFrameShape(QFrame.NoFrame)
        self.statsFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.statsFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.statsLbl = QLabel(self.statsFrame)
        self.statsLbl.setObjectName(u"statsLbl")
        font8 = QFont()
        font8.setFamilies([u"Inter"])
        font8.setPointSize(10)
        self.statsLbl.setFont(font8)
        self.statsLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.statsLbl)


        self.verticalLayout_21.addWidget(self.statsFrame)


        self.verticalLayout_7.addWidget(self.propertiesFrame)

        self.affinitiesFrame = QFrame(self.shadowInfoFrame)
        self.affinitiesFrame.setObjectName(u"affinitiesFrame")
        self.affinitiesFrame.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.affinitiesFrame.setFrameShape(QFrame.StyledPanel)
        self.affinitiesFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.affinitiesFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.physFrame = QFrame(self.affinitiesFrame)
        self.physFrame.setObjectName(u"physFrame")
        self.physFrame.setFrameShape(QFrame.NoFrame)
        self.physFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_14 = QVBoxLayout(self.physFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.iconPixmap_6 = QLabel(self.physFrame)
        self.iconPixmap_6.setObjectName(u"iconPixmap_6")
        sizePolicy.setHeightForWidth(self.iconPixmap_6.sizePolicy().hasHeightForWidth())
        self.iconPixmap_6.setSizePolicy(sizePolicy)
        self.iconPixmap_6.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.iconPixmap_6)

        self.physAffinityLbl = QLabel(self.physFrame)
        self.physAffinityLbl.setObjectName(u"physAffinityLbl")
        sizePolicy2.setHeightForWidth(self.physAffinityLbl.sizePolicy().hasHeightForWidth())
        self.physAffinityLbl.setSizePolicy(sizePolicy2)
        font9 = QFont()
        font9.setFamilies([u"Inter"])
        font9.setPointSize(12)
        font9.setBold(True)
        self.physAffinityLbl.setFont(font9)
        self.physAffinityLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.physAffinityLbl)


        self.horizontalLayout_6.addWidget(self.physFrame)

        self.fireFrame = QFrame(self.affinitiesFrame)
        self.fireFrame.setObjectName(u"fireFrame")
        self.fireFrame.setFrameShape(QFrame.NoFrame)
        self.fireFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_15 = QVBoxLayout(self.fireFrame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.iconPixmap_3 = QLabel(self.fireFrame)
        self.iconPixmap_3.setObjectName(u"iconPixmap_3")
        sizePolicy.setHeightForWidth(self.iconPixmap_3.sizePolicy().hasHeightForWidth())
        self.iconPixmap_3.setSizePolicy(sizePolicy)
        self.iconPixmap_3.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.iconPixmap_3)

        self.fireAffinityLbl = QLabel(self.fireFrame)
        self.fireAffinityLbl.setObjectName(u"fireAffinityLbl")
        self.fireAffinityLbl.setFont(font9)
        self.fireAffinityLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.fireAffinityLbl)


        self.horizontalLayout_6.addWidget(self.fireFrame)

        self.iceFrame = QFrame(self.affinitiesFrame)
        self.iceFrame.setObjectName(u"iceFrame")
        self.iceFrame.setFrameShape(QFrame.NoFrame)
        self.iceFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_16 = QVBoxLayout(self.iceFrame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.iconPixmap_4 = QLabel(self.iceFrame)
        self.iconPixmap_4.setObjectName(u"iconPixmap_4")
        sizePolicy.setHeightForWidth(self.iconPixmap_4.sizePolicy().hasHeightForWidth())
        self.iconPixmap_4.setSizePolicy(sizePolicy)
        self.iconPixmap_4.setScaledContents(True)

        self.verticalLayout_16.addWidget(self.iconPixmap_4)

        self.iceAffinityLbl = QLabel(self.iceFrame)
        self.iceAffinityLbl.setObjectName(u"iceAffinityLbl")
        self.iceAffinityLbl.setFont(font9)
        self.iceAffinityLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.iceAffinityLbl)


        self.horizontalLayout_6.addWidget(self.iceFrame)

        self.elecFrame = QFrame(self.affinitiesFrame)
        self.elecFrame.setObjectName(u"elecFrame")
        self.elecFrame.setFrameShape(QFrame.NoFrame)
        self.elecFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_17 = QVBoxLayout(self.elecFrame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.iconPixmap_2 = QLabel(self.elecFrame)
        self.iconPixmap_2.setObjectName(u"iconPixmap_2")
        sizePolicy.setHeightForWidth(self.iconPixmap_2.sizePolicy().hasHeightForWidth())
        self.iconPixmap_2.setSizePolicy(sizePolicy)
        self.iconPixmap_2.setScaledContents(True)

        self.verticalLayout_17.addWidget(self.iconPixmap_2)

        self.elecAffinityLbl = QLabel(self.elecFrame)
        self.elecAffinityLbl.setObjectName(u"elecAffinityLbl")
        self.elecAffinityLbl.setFont(font9)
        self.elecAffinityLbl.setScaledContents(False)
        self.elecAffinityLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.elecAffinityLbl)


        self.horizontalLayout_6.addWidget(self.elecFrame)

        self.windFrame = QFrame(self.affinitiesFrame)
        self.windFrame.setObjectName(u"windFrame")
        self.windFrame.setFrameShape(QFrame.NoFrame)
        self.windFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_18 = QVBoxLayout(self.windFrame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.iconPixmap_7 = QLabel(self.windFrame)
        self.iconPixmap_7.setObjectName(u"iconPixmap_7")
        sizePolicy.setHeightForWidth(self.iconPixmap_7.sizePolicy().hasHeightForWidth())
        self.iconPixmap_7.setSizePolicy(sizePolicy)
        self.iconPixmap_7.setScaledContents(True)

        self.verticalLayout_18.addWidget(self.iconPixmap_7)

        self.windAffinityLbl = QLabel(self.windFrame)
        self.windAffinityLbl.setObjectName(u"windAffinityLbl")
        self.windAffinityLbl.setFont(font9)
        self.windAffinityLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.windAffinityLbl)


        self.horizontalLayout_6.addWidget(self.windFrame)

        self.lightFrame = QFrame(self.affinitiesFrame)
        self.lightFrame.setObjectName(u"lightFrame")
        self.lightFrame.setFrameShape(QFrame.NoFrame)
        self.lightFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_19 = QVBoxLayout(self.lightFrame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.iconPixmap_5 = QLabel(self.lightFrame)
        self.iconPixmap_5.setObjectName(u"iconPixmap_5")
        sizePolicy.setHeightForWidth(self.iconPixmap_5.sizePolicy().hasHeightForWidth())
        self.iconPixmap_5.setSizePolicy(sizePolicy)
        self.iconPixmap_5.setScaledContents(True)

        self.verticalLayout_19.addWidget(self.iconPixmap_5)

        self.lightAffinityLbl = QLabel(self.lightFrame)
        self.lightAffinityLbl.setObjectName(u"lightAffinityLbl")
        self.lightAffinityLbl.setFont(font9)
        self.lightAffinityLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.lightAffinityLbl)


        self.horizontalLayout_6.addWidget(self.lightFrame)

        self.darkFrame = QFrame(self.affinitiesFrame)
        self.darkFrame.setObjectName(u"darkFrame")
        self.darkFrame.setFrameShape(QFrame.NoFrame)
        self.darkFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_20 = QVBoxLayout(self.darkFrame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.iconPixmap = QLabel(self.darkFrame)
        self.iconPixmap.setObjectName(u"iconPixmap")
        sizePolicy.setHeightForWidth(self.iconPixmap.sizePolicy().hasHeightForWidth())
        self.iconPixmap.setSizePolicy(sizePolicy)
        self.iconPixmap.setScaledContents(True)

        self.verticalLayout_20.addWidget(self.iconPixmap)

        self.darkAffinityLbl = QLabel(self.darkFrame)
        self.darkAffinityLbl.setObjectName(u"darkAffinityLbl")
        self.darkAffinityLbl.setFont(font9)
        self.darkAffinityLbl.setScaledContents(False)
        self.darkAffinityLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.darkAffinityLbl)


        self.horizontalLayout_6.addWidget(self.darkFrame)


        self.verticalLayout_7.addWidget(self.affinitiesFrame)

        self.skillsFrame = QFrame(self.shadowInfoFrame)
        self.skillsFrame.setObjectName(u"skillsFrame")
        self.skillsFrame.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.skillsFrame.setFrameShape(QFrame.NoFrame)
        self.skillsFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.skillsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.skill5 = QLabel(self.skillsFrame)
        self.skill5.setObjectName(u"skill5")
        self.skill5.setFont(font)
        self.skill5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.skill5, 0, 1, 1, 1)

        self.skill6 = QLabel(self.skillsFrame)
        self.skill6.setObjectName(u"skill6")
        self.skill6.setFont(font)
        self.skill6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.skill6, 1, 1, 1, 1)

        self.skill8 = QLabel(self.skillsFrame)
        self.skill8.setObjectName(u"skill8")
        self.skill8.setFont(font)
        self.skill8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.skill8, 3, 1, 1, 1)

        self.skill7 = QLabel(self.skillsFrame)
        self.skill7.setObjectName(u"skill7")
        self.skill7.setFont(font)
        self.skill7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.skill7, 2, 1, 1, 1)

        self.skill2 = QLabel(self.skillsFrame)
        self.skill2.setObjectName(u"skill2")
        self.skill2.setFont(font)
        self.skill2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.skill2, 1, 0, 1, 1)

        self.skill1 = QLabel(self.skillsFrame)
        self.skill1.setObjectName(u"skill1")
        self.skill1.setFont(font)
        self.skill1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.skill1, 0, 0, 1, 1)

        self.skill3 = QLabel(self.skillsFrame)
        self.skill3.setObjectName(u"skill3")
        self.skill3.setFont(font)
        self.skill3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.skill3, 2, 0, 1, 1)

        self.skill4 = QLabel(self.skillsFrame)
        self.skill4.setObjectName(u"skill4")
        self.skill4.setFont(font)
        self.skill4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.skill4, 3, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.skillsFrame)


        self.horizontalLayout_2.addWidget(self.shadowInfoFrame)


        self.verticalLayout_8.addWidget(self.infoFrame_3)

        self.mainStackedWidget.addWidget(self.shadowsPage)
        self.weaponsPage = QWidget()
        self.weaponsPage.setObjectName(u"weaponsPage")
        self.weaponsPage.setStyleSheet(u"QFrame#infoFrame_4 {\n"
"	background-color: #FFD100;\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"}\n"
"QPushButton {\n"
"	background-color: #fff6cc;\n"
"	color: #333533;\n"
"	padding: 12px 12px 12px 12px;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #333533;\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"}")
        self.verticalLayout_41 = QVBoxLayout(self.weaponsPage)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.headerFrame_5 = QFrame(self.weaponsPage)
        self.headerFrame_5.setObjectName(u"headerFrame_5")
        sizePolicy4.setHeightForWidth(self.headerFrame_5.sizePolicy().hasHeightForWidth())
        self.headerFrame_5.setSizePolicy(sizePolicy4)
        self.headerFrame_5.setStyleSheet(u"QFrame#headerFrame_5 {\n"
"	background-color: #FFEE32;\n"
"}\n"
"QLabel {\n"
"	border-radius: 12px;\n"
"}")
        self.headerFrame_5.setFrameShape(QFrame.NoFrame)
        self.headerFrame_5.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.headerFrame_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.headingLbl_7 = QLabel(self.headerFrame_5)
        self.headingLbl_7.setObjectName(u"headingLbl_7")
        self.headingLbl_7.setFont(font1)

        self.horizontalLayout_9.addWidget(self.headingLbl_7)

        self.headerInfoFrame_4 = QFrame(self.headerFrame_5)
        self.headerInfoFrame_4.setObjectName(u"headerInfoFrame_4")
        sizePolicy5.setHeightForWidth(self.headerInfoFrame_4.sizePolicy().hasHeightForWidth())
        self.headerInfoFrame_4.setSizePolicy(sizePolicy5)
        self.headerInfoFrame_4.setFrameShape(QFrame.NoFrame)
        self.headerInfoFrame_4.setFrameShadow(QFrame.Plain)
        self.verticalLayout_22 = QVBoxLayout(self.headerInfoFrame_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.weaponsHomeBtn = QPushButton(self.headerInfoFrame_4)
        self.weaponsHomeBtn.setObjectName(u"weaponsHomeBtn")
        sizePolicy6.setHeightForWidth(self.weaponsHomeBtn.sizePolicy().hasHeightForWidth())
        self.weaponsHomeBtn.setSizePolicy(sizePolicy6)
        self.weaponsHomeBtn.setFont(font2)
        self.weaponsHomeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_22.addWidget(self.weaponsHomeBtn)

        self.bodyLbl_5 = QLabel(self.headerInfoFrame_4)
        self.bodyLbl_5.setObjectName(u"bodyLbl_5")
        sizePolicy.setHeightForWidth(self.bodyLbl_5.sizePolicy().hasHeightForWidth())
        self.bodyLbl_5.setSizePolicy(sizePolicy)
        self.bodyLbl_5.setFont(font2)
        self.bodyLbl_5.setStyleSheet(u"background-color: grey;\n"
"color: white;\n"
"padding: 4px 4px 4px 4px;")

        self.verticalLayout_22.addWidget(self.bodyLbl_5)


        self.horizontalLayout_9.addWidget(self.headerInfoFrame_4)


        self.verticalLayout_41.addWidget(self.headerFrame_5)

        self.infoFrame_4 = QFrame(self.weaponsPage)
        self.infoFrame_4.setObjectName(u"infoFrame_4")
        sizePolicy7.setHeightForWidth(self.infoFrame_4.sizePolicy().hasHeightForWidth())
        self.infoFrame_4.setSizePolicy(sizePolicy7)
        self.infoFrame_4.setStyleSheet(u"QListView {\n"
"	border-top: 6px solid white;\n"
"}\n"
"QListView::item {\n"
"	background-color: #4D4D4D;\n"
"	color: white;\n"
"}\n"
"QAbstractItemView {\n"
"	background-color: #333533;\n"
"}\n"
"QScrollBar:vertical {\n"
"	width: 12px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: grey;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 4px solid grey;\n"
"    background: white;\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.infoFrame_4.setFrameShape(QFrame.NoFrame)
        self.infoFrame_4.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.infoFrame_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.weaponsTabWidget = QTabWidget(self.infoFrame_4)
        self.weaponsTabWidget.setObjectName(u"weaponsTabWidget")
        self.weaponsTabWidget.setFont(font9)
        self.weaponsTabWidget.setStyleSheet(u"QFrame {\n"
"	background-color: #333533;\n"
"}\n"
"QLabel {\n"
"	color: white;\n"
"}\n"
"QTableWidget::item {\n"
"	background-color: #4D4D4D;\n"
"	color: white;\n"
"	text-align: center;\n"
"}\n"
"QTabWidget::pane {\n"
"	border: none;\n"
"}\n"
"QTabBar::tab {\n"
"	background-color: #333533;\n"
"	color: white;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color: #4D4D4D\n"
"}\n"
"QTableView {\n"
"	background-color: #333533;\n"
"	border-radius: 12px;\n"
"	gridline-color: white;\n"
"}\n"
"QAbstractItemView {\n"
"	background-color: #333533;\n"
"}\n"
"QHeaderView::section {\n"
"	background-color: #202020;\n"
"	color: white;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"	border-top: 6px solid white;\n"
"}")
        self.mcTab = QWidget()
        self.mcTab.setObjectName(u"mcTab")
        self.horizontalLayout_14 = QHBoxLayout(self.mcTab)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.mcWeaponsTable = QTableWidget(self.mcTab)
        if (self.mcWeaponsTable.columnCount() < 4):
            self.mcWeaponsTable.setColumnCount(4)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font2);
        self.mcWeaponsTable.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font2);
        self.mcWeaponsTable.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font2);
        self.mcWeaponsTable.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font2);
        self.mcWeaponsTable.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        self.mcWeaponsTable.setObjectName(u"mcWeaponsTable")
        self.mcWeaponsTable.setFrameShape(QFrame.NoFrame)
        self.mcWeaponsTable.setFrameShadow(QFrame.Plain)
        self.mcWeaponsTable.setProperty("showDropIndicator", False)
        self.mcWeaponsTable.setDragDropOverwriteMode(False)
        self.mcWeaponsTable.setShowGrid(True)
        self.mcWeaponsTable.setGridStyle(Qt.SolidLine)
        self.mcWeaponsTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.mcWeaponsTable.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_14.addWidget(self.mcWeaponsTable)

        self.weaponsTabWidget.addTab(self.mcTab, "")
        self.yosukeTab = QWidget()
        self.yosukeTab.setObjectName(u"yosukeTab")
        self.verticalLayout_23 = QVBoxLayout(self.yosukeTab)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.yosukeWeaponsTable = QTableWidget(self.yosukeTab)
        if (self.yosukeWeaponsTable.columnCount() < 4):
            self.yosukeWeaponsTable.setColumnCount(4)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font2);
        self.yosukeWeaponsTable.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font2);
        self.yosukeWeaponsTable.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font2);
        self.yosukeWeaponsTable.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font2);
        self.yosukeWeaponsTable.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        self.yosukeWeaponsTable.setObjectName(u"yosukeWeaponsTable")
        self.yosukeWeaponsTable.setFrameShape(QFrame.NoFrame)
        self.yosukeWeaponsTable.setFrameShadow(QFrame.Plain)
        self.yosukeWeaponsTable.setProperty("showDropIndicator", False)
        self.yosukeWeaponsTable.setDragDropOverwriteMode(False)
        self.yosukeWeaponsTable.setShowGrid(True)
        self.yosukeWeaponsTable.setGridStyle(Qt.SolidLine)
        self.yosukeWeaponsTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.yosukeWeaponsTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_23.addWidget(self.yosukeWeaponsTable)

        self.weaponsTabWidget.addTab(self.yosukeTab, "")
        self.chieTab = QWidget()
        self.chieTab.setObjectName(u"chieTab")
        self.verticalLayout_24 = QVBoxLayout(self.chieTab)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.chieWeaponsTable = QTableWidget(self.chieTab)
        if (self.chieWeaponsTable.columnCount() < 4):
            self.chieWeaponsTable.setColumnCount(4)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font2);
        self.chieWeaponsTable.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font2);
        self.chieWeaponsTable.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font2);
        self.chieWeaponsTable.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font2);
        self.chieWeaponsTable.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        self.chieWeaponsTable.setObjectName(u"chieWeaponsTable")
        self.chieWeaponsTable.setFrameShape(QFrame.NoFrame)
        self.chieWeaponsTable.setFrameShadow(QFrame.Plain)
        self.chieWeaponsTable.setProperty("showDropIndicator", False)
        self.chieWeaponsTable.setDragDropOverwriteMode(False)
        self.chieWeaponsTable.setShowGrid(True)
        self.chieWeaponsTable.setGridStyle(Qt.SolidLine)
        self.chieWeaponsTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.chieWeaponsTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_24.addWidget(self.chieWeaponsTable)

        self.weaponsTabWidget.addTab(self.chieTab, "")
        self.yukikoTab = QWidget()
        self.yukikoTab.setObjectName(u"yukikoTab")
        self.verticalLayout_25 = QVBoxLayout(self.yukikoTab)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.yukikoWeaponsTable = QTableWidget(self.yukikoTab)
        if (self.yukikoWeaponsTable.columnCount() < 4):
            self.yukikoWeaponsTable.setColumnCount(4)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font2);
        self.yukikoWeaponsTable.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font2);
        self.yukikoWeaponsTable.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font2);
        self.yukikoWeaponsTable.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font2);
        self.yukikoWeaponsTable.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        self.yukikoWeaponsTable.setObjectName(u"yukikoWeaponsTable")
        self.yukikoWeaponsTable.setFrameShape(QFrame.NoFrame)
        self.yukikoWeaponsTable.setFrameShadow(QFrame.Plain)
        self.yukikoWeaponsTable.setProperty("showDropIndicator", False)
        self.yukikoWeaponsTable.setDragDropOverwriteMode(False)
        self.yukikoWeaponsTable.setShowGrid(True)
        self.yukikoWeaponsTable.setGridStyle(Qt.SolidLine)
        self.yukikoWeaponsTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.yukikoWeaponsTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_25.addWidget(self.yukikoWeaponsTable)

        self.weaponsTabWidget.addTab(self.yukikoTab, "")
        self.kanjiTab = QWidget()
        self.kanjiTab.setObjectName(u"kanjiTab")
        self.verticalLayout_26 = QVBoxLayout(self.kanjiTab)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.kanjiWeaponsTable = QTableWidget(self.kanjiTab)
        if (self.kanjiWeaponsTable.columnCount() < 4):
            self.kanjiWeaponsTable.setColumnCount(4)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font2);
        self.kanjiWeaponsTable.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font2);
        self.kanjiWeaponsTable.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font2);
        self.kanjiWeaponsTable.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font2);
        self.kanjiWeaponsTable.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        self.kanjiWeaponsTable.setObjectName(u"kanjiWeaponsTable")
        self.kanjiWeaponsTable.setFrameShape(QFrame.NoFrame)
        self.kanjiWeaponsTable.setFrameShadow(QFrame.Plain)
        self.kanjiWeaponsTable.setProperty("showDropIndicator", False)
        self.kanjiWeaponsTable.setDragDropOverwriteMode(False)
        self.kanjiWeaponsTable.setShowGrid(True)
        self.kanjiWeaponsTable.setGridStyle(Qt.SolidLine)
        self.kanjiWeaponsTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.kanjiWeaponsTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_26.addWidget(self.kanjiWeaponsTable)

        self.weaponsTabWidget.addTab(self.kanjiTab, "")
        self.teddieTab = QWidget()
        self.teddieTab.setObjectName(u"teddieTab")
        self.verticalLayout_27 = QVBoxLayout(self.teddieTab)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.teddieWeaponsTable = QTableWidget(self.teddieTab)
        if (self.teddieWeaponsTable.columnCount() < 4):
            self.teddieWeaponsTable.setColumnCount(4)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font2);
        self.teddieWeaponsTable.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font2);
        self.teddieWeaponsTable.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font2);
        self.teddieWeaponsTable.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font2);
        self.teddieWeaponsTable.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        self.teddieWeaponsTable.setObjectName(u"teddieWeaponsTable")
        self.teddieWeaponsTable.setFrameShape(QFrame.NoFrame)
        self.teddieWeaponsTable.setFrameShadow(QFrame.Plain)
        self.teddieWeaponsTable.setProperty("showDropIndicator", False)
        self.teddieWeaponsTable.setDragDropOverwriteMode(False)
        self.teddieWeaponsTable.setShowGrid(True)
        self.teddieWeaponsTable.setGridStyle(Qt.SolidLine)
        self.teddieWeaponsTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.teddieWeaponsTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_27.addWidget(self.teddieWeaponsTable)

        self.weaponsTabWidget.addTab(self.teddieTab, "")
        self.naotoTab = QWidget()
        self.naotoTab.setObjectName(u"naotoTab")
        self.verticalLayout_28 = QVBoxLayout(self.naotoTab)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.naotoWeaponsTable = QTableWidget(self.naotoTab)
        if (self.naotoWeaponsTable.columnCount() < 4):
            self.naotoWeaponsTable.setColumnCount(4)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font2);
        self.naotoWeaponsTable.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font2);
        self.naotoWeaponsTable.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font2);
        self.naotoWeaponsTable.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font2);
        self.naotoWeaponsTable.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        self.naotoWeaponsTable.setObjectName(u"naotoWeaponsTable")
        self.naotoWeaponsTable.setFrameShape(QFrame.NoFrame)
        self.naotoWeaponsTable.setFrameShadow(QFrame.Plain)
        self.naotoWeaponsTable.setProperty("showDropIndicator", False)
        self.naotoWeaponsTable.setDragDropOverwriteMode(False)
        self.naotoWeaponsTable.setShowGrid(True)
        self.naotoWeaponsTable.setGridStyle(Qt.SolidLine)
        self.naotoWeaponsTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.naotoWeaponsTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_28.addWidget(self.naotoWeaponsTable)

        self.weaponsTabWidget.addTab(self.naotoTab, "")

        self.horizontalLayout_13.addWidget(self.weaponsTabWidget)


        self.verticalLayout_41.addWidget(self.infoFrame_4)

        self.mainStackedWidget.addWidget(self.weaponsPage)

        self.verticalLayout.addWidget(self.mainStackedWidget)

        persona4Window.setCentralWidget(self.mainWidget)

        self.retranslateUi(persona4Window)

        self.mainStackedWidget.setCurrentIndex(4)
        self.weaponsTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(persona4Window)
    # setupUi

    def retranslateUi(self, persona4Window):
        persona4Window.setWindowTitle(QCoreApplication.translate("persona4Window", u"Persona 4 Golden Guide App", None))
        self.headingLbl.setText(QCoreApplication.translate("persona4Window", u"Home", None))
        self.bodyLbl.setText(QCoreApplication.translate("persona4Window", u"Welcome to Persona 4 Guide App", None))
        self.headingLbl_3.setText(QCoreApplication.translate("persona4Window", u"Persona 4 Golden", None))
        self.questsBtn_2.setText(QCoreApplication.translate("persona4Window", u"Quests", None))
        self.weaponsBtn_2.setText(QCoreApplication.translate("persona4Window", u"Weapons", None))
        self.answersBtn_2.setText(QCoreApplication.translate("persona4Window", u"Answers", None))
        self.shadowsBtn_2.setText(QCoreApplication.translate("persona4Window", u"Shadows", None))
        self.headingLbl_4.setText(QCoreApplication.translate("persona4Window", u"Quests", None))
        self.questsHomeBtn.setText(QCoreApplication.translate("persona4Window", u"Home", None))
        self.bodyLbl_2.setText(QCoreApplication.translate("persona4Window", u"Persona 4 Golden", None))
        ___qtablewidgetitem = self.questsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("persona4Window", u"Quest", None));
        ___qtablewidgetitem1 = self.questsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("persona4Window", u"Person", None));
        ___qtablewidgetitem2 = self.questsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("persona4Window", u"Date", None));
        ___qtablewidgetitem3 = self.questsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("persona4Window", u"Remarks", None));
        ___qtablewidgetitem4 = self.questsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("persona4Window", u"Reward", None));

        __sortingEnabled = self.questsTable.isSortingEnabled()
        self.questsTable.setSortingEnabled(False)
        self.questsTable.setSortingEnabled(__sortingEnabled)

        self.headingLbl_5.setText(QCoreApplication.translate("persona4Window", u"Answers", None))
        self.answersHomeBtn.setText(QCoreApplication.translate("persona4Window", u"Home", None))
        self.bodyLbl_3.setText(QCoreApplication.translate("persona4Window", u"Persona 4 Golden", None))
        ___qtablewidgetitem5 = self.answersTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("persona4Window", u"Date Asked", None));
        ___qtablewidgetitem6 = self.answersTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("persona4Window", u"Question", None));
        ___qtablewidgetitem7 = self.answersTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("persona4Window", u"Answer", None));
        self.headingLbl_6.setText(QCoreApplication.translate("persona4Window", u"Shadows", None))
        self.shadowsHomeBtn.setText(QCoreApplication.translate("persona4Window", u"Home", None))
        self.bodyLbl_4.setText(QCoreApplication.translate("persona4Window", u"Persona 4 Golden", None))
        self.lvlLbl.setText(QCoreApplication.translate("persona4Window", u"Name - Level 79", None))
        self.hpSpLbl.setText(QCoreApplication.translate("persona4Window", u"HP 403 | SP 203\n"
"Experience 3760 | 3570 Y", None))
        self.statsLbl.setText("")
        self.iconPixmap_6.setText("")
        self.physAffinityLbl.setText("")
        self.iconPixmap_3.setText("")
        self.fireAffinityLbl.setText("")
        self.iconPixmap_4.setText("")
        self.iceAffinityLbl.setText("")
        self.iconPixmap_2.setText("")
        self.elecAffinityLbl.setText("")
        self.iconPixmap_7.setText("")
        self.windAffinityLbl.setText("")
        self.iconPixmap_5.setText("")
        self.lightAffinityLbl.setText("")
        self.iconPixmap.setText("")
        self.darkAffinityLbl.setText("")
        self.skill5.setText("")
        self.skill6.setText("")
        self.skill8.setText("")
        self.skill7.setText("")
        self.skill2.setText("")
        self.skill1.setText("")
        self.skill3.setText("")
        self.skill4.setText("")
        self.headingLbl_7.setText(QCoreApplication.translate("persona4Window", u"Weapons", None))
        self.weaponsHomeBtn.setText(QCoreApplication.translate("persona4Window", u"Home", None))
        self.bodyLbl_5.setText(QCoreApplication.translate("persona4Window", u"Weapons", None))
        ___qtablewidgetitem8 = self.mcWeaponsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("persona4Window", u"Name", None));
        ___qtablewidgetitem9 = self.mcWeaponsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("persona4Window", u"Attack", None));
        ___qtablewidgetitem10 = self.mcWeaponsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("persona4Window", u"Accuracy", None));
        ___qtablewidgetitem11 = self.mcWeaponsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("persona4Window", u"Effect", None));
        self.weaponsTabWidget.setTabText(self.weaponsTabWidget.indexOf(self.mcTab), QCoreApplication.translate("persona4Window", u"Protagonist", None))
        ___qtablewidgetitem12 = self.yosukeWeaponsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("persona4Window", u"Name", None));
        ___qtablewidgetitem13 = self.yosukeWeaponsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("persona4Window", u"Attack", None));
        ___qtablewidgetitem14 = self.yosukeWeaponsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("persona4Window", u"Accuracy", None));
        ___qtablewidgetitem15 = self.yosukeWeaponsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("persona4Window", u"Effect", None));
        self.weaponsTabWidget.setTabText(self.weaponsTabWidget.indexOf(self.yosukeTab), QCoreApplication.translate("persona4Window", u"Yosuke", None))
        ___qtablewidgetitem16 = self.chieWeaponsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("persona4Window", u"Name", None));
        ___qtablewidgetitem17 = self.chieWeaponsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("persona4Window", u"Attack", None));
        ___qtablewidgetitem18 = self.chieWeaponsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("persona4Window", u"Accuracy", None));
        ___qtablewidgetitem19 = self.chieWeaponsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("persona4Window", u"Effect", None));
        self.weaponsTabWidget.setTabText(self.weaponsTabWidget.indexOf(self.chieTab), QCoreApplication.translate("persona4Window", u"Chie", None))
        ___qtablewidgetitem20 = self.yukikoWeaponsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("persona4Window", u"Name", None));
        ___qtablewidgetitem21 = self.yukikoWeaponsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("persona4Window", u"Attack", None));
        ___qtablewidgetitem22 = self.yukikoWeaponsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("persona4Window", u"Accuracy", None));
        ___qtablewidgetitem23 = self.yukikoWeaponsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("persona4Window", u"Effect", None));
        self.weaponsTabWidget.setTabText(self.weaponsTabWidget.indexOf(self.yukikoTab), QCoreApplication.translate("persona4Window", u"Yukiko", None))
        ___qtablewidgetitem24 = self.kanjiWeaponsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("persona4Window", u"Name", None));
        ___qtablewidgetitem25 = self.kanjiWeaponsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("persona4Window", u"Attack", None));
        ___qtablewidgetitem26 = self.kanjiWeaponsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("persona4Window", u"Accuracy", None));
        ___qtablewidgetitem27 = self.kanjiWeaponsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("persona4Window", u"Effect", None));
        self.weaponsTabWidget.setTabText(self.weaponsTabWidget.indexOf(self.kanjiTab), QCoreApplication.translate("persona4Window", u"Kanji", None))
        ___qtablewidgetitem28 = self.teddieWeaponsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("persona4Window", u"Name", None));
        ___qtablewidgetitem29 = self.teddieWeaponsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("persona4Window", u"Attack", None));
        ___qtablewidgetitem30 = self.teddieWeaponsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("persona4Window", u"Accuracy", None));
        ___qtablewidgetitem31 = self.teddieWeaponsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("persona4Window", u"Effect", None));
        self.weaponsTabWidget.setTabText(self.weaponsTabWidget.indexOf(self.teddieTab), QCoreApplication.translate("persona4Window", u"Teddie", None))
        ___qtablewidgetitem32 = self.naotoWeaponsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("persona4Window", u"Name", None));
        ___qtablewidgetitem33 = self.naotoWeaponsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("persona4Window", u"Attack", None));
        ___qtablewidgetitem34 = self.naotoWeaponsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("persona4Window", u"Accuracy", None));
        ___qtablewidgetitem35 = self.naotoWeaponsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("persona4Window", u"Effect", None));
        self.weaponsTabWidget.setTabText(self.weaponsTabWidget.indexOf(self.naotoTab), QCoreApplication.translate("persona4Window", u"Naoto", None))
    # retranslateUi

