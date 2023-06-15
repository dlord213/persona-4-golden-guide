import sys
import json
from enum import Enum
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from persona_4_ui import Ui_persona4Window

class ElementAffinity(Enum):
    Weak = 0,
    NaN = 1,
    Resistant = 2,
    Null = 3,
    Reflect = 4,
    Drain = 5

class User(Enum):
    Protagonist = 0,
    Yosuke = 1,
    Chie = 2,
    Yukiko = 3,
    Kanji = 4,
    Teddie = 5,
    Naoto = 6

class ShadowStats:
    def __init__(self, strength: int, magic: int, endurance: int, agility: int, luck: int):
        self.strength = strength
        self.magic = magic
        self.endurance = endurance
        self.agility = agility
        self.luck = luck

    def getStats(self):
        return {
            'str': self.strength,
            'magic': self.magic,
            'endurance': self.endurance,
            'agility': self.agility,
            'luck': self.luck
        }

class personaApp(QMainWindow, Ui_persona4Window):
    with open('./data/persona_4_golden_shadows.json', 'r') as shadowsData:
        goldenShadows = json.load(shadowsData)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.initializeApp()
        self.initializeButtons()
        self.initializeWeaponsData()
        self.getQuestsTableData()
        self.getAnswersTableData()
        self.getShadowNames()

    def initializeApp(self):
        self.mainStackedWidget.setCurrentIndex(0)
        
        pixMapWidgets = [
            self.iconPixmap, self.iconPixmap_2, self.iconPixmap_3, self.iconPixmap_4,
            self.iconPixmap_5, self.iconPixmap_6, self.iconPixmap_7,
        ]

        self.iconPixmap_7.setPixmap(QPixmap('./images/wind.png'))
        self.iconPixmap_6.setPixmap(QPixmap('./images/physical.png'))
        self.iconPixmap_5.setPixmap(QPixmap('./images/light.png'))
        self.iconPixmap_4.setPixmap(QPixmap('./images/ice.png'))
        self.iconPixmap_3.setPixmap(QPixmap('./images/fire.png'))
        self.iconPixmap_2.setPixmap(QPixmap('./images/electricity.png'))
        self.iconPixmap.setPixmap(QPixmap('./images/darkness.png'))

        for widget in pixMapWidgets:
            widget.setStyleSheet(
                "border: 2px solid grey"
            )

    def initializeButtons(self):
        self.questsHomeBtn.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(0))
        self.answersHomeBtn.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(0))
        self.shadowsHomeBtn.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(0))
        self.weaponsHomeBtn.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(0))

        self.questsBtn_2.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(1))
        self.answersBtn_2.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(2))
        self.shadowsBtn_2.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(3))
        self.weaponsBtn_2.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(4))

    def resizeWindow(self):
        self.resize(800, 600)

    def getQuestsTableData(self):
        table = self.questsTable
        table.setRowCount(69)

        with open('./data/persona_4_golden_quest.json', 'r') as questData:
            goldenQuests = json.load(questData)
            
            for index, dictionary in enumerate(goldenQuests):
                for key, val in dictionary.items():
                    if key == 'Quest':
                        table.setItem(index, 0, QTableWidgetItem(str(val)))
                    elif key == 'Quest Giver':
                        table.setItem(index, 1, QTableWidgetItem(str(val)))
                    elif key == 'Available':
                        table.setItem(index, 2, QTableWidgetItem(str(val)))
                    elif key == 'Reward':
                        table.setItem(index, 3, QTableWidgetItem(str(val)))
                    elif key == 'Remarks':
                        table.setItem(index, 4, QTableWidgetItem(str(val)))

            for row in range(0, 69):
                for column in range(0, 5):
                    table.item(row, column).setFont(QFont('Inter', 12))

        table.verticalHeader().setVisible(True)
        table.horizontalHeader().setVisible(True)
        table.resizeRowsToContents()

    def getAnswersTableData(self):
        table = self.answersTable
        table.setRowCount(94)

        with open('./data/persona_4_golden_answers.json', 'r') as answerData:
            goldenAnswers = json.load(answerData)

            for index, dictionary in enumerate(goldenAnswers):
                for key, val in dictionary.items():
                    if key == 'dateAsked':
                        table.setItem(index, 0, QTableWidgetItem(str(val)))
                    elif key == 'questionAsked':
                        table.setItem(index, 1, QTableWidgetItem(str(val)))
                    elif key == 'questionAnswer':
                        table.setItem(index, 2, QTableWidgetItem(str(val)))

            for row in range(0, 94):
                for column in range(0, 3):
                    table.item(row, column).setFont(QFont('Inter', 12))

        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setVisible(True)
        table.resizeRowsToContents()

    def getAffinity(self, affinity: int):
        if affinity == 0:
            return str('Wk')
        elif affinity == 1:
            return '-'
        elif affinity == 2:
            return 'Str'
        elif affinity == 3:
            return 'Nul'
        elif affinity == 4:
            return 'Rpl'
        elif affinity == 5:
            return 'Dr'

    def getShadowData(self):
        listWidget = self.shadowsList

        shadowInfos = self.goldenShadows[listWidget.currentRow()]
        skillCount = len(shadowInfos['skills'])

        nameLvlStr = '{name} - Level {level}'.format(**shadowInfos)
        hpSpStr = 'HP {hp} | SP {sp}\nEXP {experience} | {yen}'.format(**shadowInfos)
        statsStr = 'STRENGTH {strength} | MAGIC {magic} | ENDURANCE {endurance} | AGILITY {agility} | LUCK {luck}'.format(**shadowInfos['stats'])

        skillWidgets = [
            self.skill1, self.skill2, self.skill3, self.skill4,
            self.skill5, self.skill6, self.skill7, self.skill8, 
        ]

        for elem, affinity in shadowInfos['elementAffinities'].items():
            if elem == 'physical':
                self.physAffinityLbl.setText(self.getAffinity(affinity))
            elif elem == 'fire':
                self.fireAffinityLbl.setText(self.getAffinity(affinity))
            elif elem == 'ice':
                self.iceAffinityLbl.setText(self.getAffinity(affinity))
            elif elem == 'electricity':
                self.elecAffinityLbl.setText(self.getAffinity(affinity))
            elif elem == 'wind':
                self.windAffinityLbl.setText(self.getAffinity(affinity))
            elif elem == 'light':
                self.lightAffinityLbl.setText(self.getAffinity(affinity))
            elif elem == 'darkness':
                self.darkAffinityLbl.setText(self.getAffinity(affinity))

        for widget in skillWidgets:
            widget.setText('')

        for index in range(0, skillCount):
            skillWidgets[index].setText(shadowInfos['skills'][index])

        self.lvlLbl.setText(nameLvlStr)
        self.hpSpLbl.setText(hpSpStr)
        self.statsLbl.setText(statsStr)

    def getShadowNames(self):
        listWidget = self.shadowsList

        for shadow in self.goldenShadows:
            for key, val in shadow.items():
                if key == 'name':
                    listWidget.addItem(
                        QListWidgetItem(str(val))
                    )

        listWidget.itemClicked.connect(lambda: self.getShadowData())

    def getWeaponsData(self, table: QTableWidget, rowCount: int, file: str):
        table.setRowCount(rowCount)

        with open(f'./data/{file}', 'r') as data:
            fileData = json.load(data)

            for index, dictionary in enumerate(fileData):
                for key, val in dictionary.items():
                    if key == 'Weapon':
                        table.setItem(index, 0, QTableWidgetItem(str(val)))
                    elif key == 'Attack':
                        table.setItem(index, 1, QTableWidgetItem(str(val)))
                    elif key == 'Accuracy':
                        table.setItem(index, 2, QTableWidgetItem(str(val)))
                    elif key == 'Effect':
                        table.setItem(index, 3, QTableWidgetItem(str(val)))
            
            for row in range(0, rowCount):
                for column in range(0, 4):
                    table.item(row, column).setFont(QFont('Inter', 12))
            
        table.verticalHeader().setVisible(True)
        table.horizontalHeader().setVisible(True)
        table.resizeRowsToContents()

    def initializeWeaponsData(self):
        self.getWeaponsData(self.mcWeaponsTable, 34, "weapons/golden_mc.json")
        self.getWeaponsData(self.yosukeWeaponsTable, 31, "weapons/golden_yosuke.json")
        self.getWeaponsData(self.chieWeaponsTable, 30, "weapons/golden_chie.json")
        self.getWeaponsData(self.yosukeWeaponsTable, 31, "weapons/golden_yosuke.json")
        self.getWeaponsData(self.yukikoWeaponsTable, 27, "weapons/golden_yukiko.json")
        self.getWeaponsData(self.kanjiWeaponsTable, 25, "weapons/golden_kanji.json")
        self.getWeaponsData(self.teddieWeaponsTable, 21, "weapons/golden_teddie.json")
        self.getWeaponsData(self.naotoWeaponsTable, 14, "weapons/golden_naoto.json")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = personaApp()
    
    window.show()
    app.exec()