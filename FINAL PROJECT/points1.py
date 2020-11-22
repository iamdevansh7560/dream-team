# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'points.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
team1=sqlite3.connect("dreamteam.db")


class Bk_otherwindow(object):
    def setupUi(self, otherwindow):
        otherwindow.setObjectName("otherwindow")
        otherwindow.resize(898, 695)
        self.centralwidget = QtWidgets.QWidget(otherwindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMaximumSize(QtCore.QSize(700, 150))
        self.label_7.setText("")
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setObjectName("label_38")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_38, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 2, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 2, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMaximumSize(QtCore.QSize(90, 90))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 2, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMaximumSize(QtCore.QSize(90, 90))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 5, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 2, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(90, 90))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMaximumSize(QtCore.QSize(90, 90))
        self.label_9.setText("")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setMaximumSize(QtCore.QSize(90, 90))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 2, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 6, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_2.addWidget(self.label_39, 3, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_2.addWidget(self.label_40, 3, 2, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_2.addWidget(self.label_41, 3, 3, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout_2.addWidget(self.label_42, 3, 4, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout_2.addWidget(self.label_43, 3, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 2, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 6, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setText("")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 2, 4, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 2, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 2, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setMaximumSize(QtCore.QSize(90, 90))
        self.label_15.setText("")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setMaximumSize(QtCore.QSize(1500, 90))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setMaximumSize(QtCore.QSize(90, 90))
        self.label_16.setText("")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 5, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setText("")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 2, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setMaximumSize(QtCore.QSize(90, 90))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setMaximumSize(QtCore.QSize(90, 90))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 3, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout_3.addWidget(self.label_44, 3, 1, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.gridLayout_3.addWidget(self.label_45, 3, 2, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.gridLayout_3.addWidget(self.label_46, 3, 3, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.gridLayout_3.addWidget(self.label_47, 3, 4, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.gridLayout_3.addWidget(self.label_48, 3, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 2, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_4.addWidget(self.label_35, 3, 3, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.centralwidget)
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.gridLayout_4.addWidget(self.label_52, 4, 4, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 3, 2, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setText("")
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_4.addWidget(self.label_36, 3, 4, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setMaximumSize(QtCore.QSize(90, 90))
        self.label_20.setText("")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 2, 4, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_4.addWidget(self.label_33, 3, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setMaximumSize(QtCore.QSize(90, 90))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 2, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setMaximumSize(QtCore.QSize(90, 90))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 2, 1, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.gridLayout_4.addWidget(self.label_49, 4, 1, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.gridLayout_4.addWidget(self.label_50, 4, 2, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setText("")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_4.addWidget(self.label_37, 3, 5, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setMaximumSize(QtCore.QSize(90, 90))
        self.label_21.setText("")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 2, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 2, 6, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setMaximumSize(QtCore.QSize(90, 90))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 2, 3, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.centralwidget)
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.gridLayout_4.addWidget(self.label_53, 4, 5, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.centralwidget)
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.gridLayout_4.addWidget(self.label_51, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.label_54 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setText("")
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.verticalLayout.addWidget(self.label_54)
        otherwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(otherwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 26))
        self.menubar.setObjectName("menubar")
        otherwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(otherwindow)
        self.statusbar.setObjectName("statusbar")
        otherwindow.setStatusBar(self.statusbar)

        self.bat=[self.label_23,self.label_24,self.label_25,self.label_26,self.label_27]
        self.ar=[self.label_28,self.label_29,self.label_30,self.label_31,self.label_32]
        self.bwl=[self.label_33,self.label_34,self.label_35,self.label_36,self.label_37]
        self.batsimg=[self.label_8,self.label_6,self.label_10,self.label_9,self.label_11]
        self.arimg=[self.label_12,self.label_13,self.label_14,self.label_15,self.label_16]
        self.bwlimg=[self.label_17,self.label_18,self.label_19,self.label_20,self.label_21]
        self.arpoint=[self.label_44,self.label_45,self.label_46,self.label_47,self.label_48]
        self.batpoint=[self.label_39,self.label_40,self.label_41,self.label_42,self.label_43]
        self.bwlpoint=[self.label_49,self.label_50,self.label_51,self.label_52,self.label_53]
        self.showteam(otherwindow)

        

        self.retranslateUi(otherwindow)
        QtCore.QMetaObject.connectSlotsByName(otherwindow)

    def showteam(self,otherwindow):
        total=0
        batsman=[]
        wk=[]
        ar=[]
        bwl=[]
        point={}
        cur=team1.cursor()
        sql="select name from teams;"
        cur=cur.execute(sql)
        teams=[]
        for row in cur:
            teams.append(row[0])
        team, ok = QtWidgets.QInputDialog.getItem(otherwindow, "Dream Team Selector",
                "Choose a team", teams, 0, False)
        if ok and team:
            match=["MATCH1","MATCH2","MATCH3"]
            match, ok = QtWidgets.QInputDialog.getItem(otherwindow, "Dream Team Selector",
                "Choose a match", match, 0, False)
            if ok and match:
                sql1="select players from teams where name='"+team+"';"
                self.label_2.setText(team)
                cur=cur.execute(sql1)
                row=cur.fetchone()
                selected=row[0].split(',')
                for i in selected:
                    sql2="SELECT ctg,player FROM stats WHERE player='"+i+"';"
                    cur=cur.execute(sql2)
                    row=cur.fetchone()
                    if row[0]=="WK":
                        wk.append(row[1])
                    if row[0]=="BAT":
                        batsman.append(row[1])
                    if row[0]=="AR":
                        ar.append(row[1])
                    if row[0]=="BWL":
                        bwl.append(row[1])
                
                    
                for i in selected:
                    ttl, batscore, bowlscore, fieldscore=0,0,0,0
                    sql3="SELECT * FROM '"+match+"' WHERE player='"+i+"';"
                    cur=cur.execute(sql3)
                    result=cur.fetchone()
                    batscore=int(result[1]/2)
                    if batscore>=50: batscore+=5
                    if batscore>=100: batscore+=10
                    if result[1]>0:
                        sr=result[1]/result[2]
                        if sr>=80 and sr<100: batscore+=2
                        if sr>=100:batscore+=4
                    batscore=batscore+result[3]
                    batscore=batscore+2*result[4]
                    bowlscore=result[8]*10
                    if result[8]>=3: bowlscore=bowlscore+5
                    if result[8]>=5: bowlscore=bowlscore=bowlscore+10
                    if result[7]>0:
                        er=6*result[7]/result[5]
                        if er<=2: bowlscore=bowlscore+10
                        if er>2 and er<=3.5: bowlscore=bowlscore+7
                        if er>3.5 and er<=4.5: bowlscore=bowlscore+4
                    fieldscore=(result[9]+result[10]+result[11])*10            
                    ttl=batscore+bowlscore+fieldscore
                    total=total+ttl
                    point[i]=ttl

                self.label_22.setText(wk[0])
                if wk[0]=="Dhoni":
                    self.label_7.setPixmap(QtGui.QPixmap("WK\msd.png"))
                    self.label_38.setText(str(point["Dhoni"]))
                else:
                    self.label_7.setPixmap(QtGui.QPixmap("WK\dk.png"))
                    self.label_38.setText(str(point["Kartik"]))
                
                for i in range(len(ar)):
                    self.ar[i].setText(ar[i])
                    if ar[i]=="Kedar":
                        self.arimg[i].setPixmap(QtGui.QPixmap("AR\kedar.jpg"))
                        self.arpoint[i].setText(str(point[ar[i]]))
                    elif ar[i]=="Jadeja":
                        self.arpoint[i].setText(str(point[ar[i]]))
                        self.arimg[i].setPixmap(QtGui.QPixmap("AR\jadeja.jpg"))
                    elif ar[i]=="Axar":
                        self.arpoint[i].setText(str(point[ar[i]]))
                        self.arimg[i].setPixmap(QtGui.QPixmap("AR\\axar.jpg"))
                    elif ar[i]=="Pandya":
                        self.arpoint[i].setText(str(point[ar[i]]))
                        self.arimg[i].setPixmap(QtGui.QPixmap("AR\hardik.jpg"))
                   
                
                for i in range(len(batsman)):
                    self.bat[i].setText(batsman[i])
                    if batsman[i]=="Kohli":
                        self.batpoint[i].setText(str(point[batsman[i]]))
                        self.batsimg[i].setPixmap(QtGui.QPixmap("batsman\kohli.png"))
                    elif batsman[i]=="Dhawan":
                        self.batpoint[i].setText(str(point[batsman[i]]))
                        self.batsimg[i].setPixmap(QtGui.QPixmap("batsman\dhawan.png"))
                    elif batsman[i]=="Rohit":
                        self.batpoint[i].setText(str(point[batsman[i]])) 
                        self.batsimg[i].setPixmap(QtGui.QPixmap("batsman\\rohit.png"))
                    elif batsman[i]=="Rahane":
                        self.batpoint[i].setText(str(point[batsman[i]])) 
                        self.batsimg[i].setPixmap(QtGui.QPixmap("batsman\\rahane.jpg"))
                    elif batsman[i]=="Yuvraj":
                        self.batpoint[i].setText(str(point[batsman[i]])) 
                        self.batsimg[i].setPixmap(QtGui.QPixmap("batsman\yuvraj.jpg"))

                for i in range(len(bwl)):
                    self.bwl[i].setText(bwl[i])
                    if bwl[i]=="Bhuwaneshwar":
                        self.bwlpoint[i].setText(str(point[bwl[i]]))
                        self.bwlimg[i].setPixmap(QtGui.QPixmap("BWL\\bhuvi.jpg"))
                    elif bwl[i]=="Umesh":
                        self.bwlpoint[i].setText(str(point[bwl[i]]))
                        self.bwlimg[i].setPixmap(QtGui.QPixmap("BWL\\umesh.jpg"))
                    elif bwl[i]=="Bumrah":
                        self.bwlpoint[i].setText(str(point[bwl[i]]))
                        self.bwlimg[i].setPixmap(QtGui.QPixmap("BWL\\bumrah.jpg"))
                    elif bwl[i]=="Ashwin":
                        self.bwlpoint[i].setText(str(point[bwl[i]]))
                        self.bwlimg[i].setPixmap(QtGui.QPixmap("BWL\\ashwin.jpg"))
                    
                self.label_54.setText("TOTAL POINTS = "+str(total) )
            else:
                otherwindow.close()
        else:
            otherwindow.close() 


            
        

    def retranslateUi(self, otherwindow):
        _translate = QtCore.QCoreApplication.translate
        otherwindow.setWindowTitle(_translate("otherwindow", "MainWindow"))

        self.label.setText(_translate("otherwindow", "WICKET KEEPER"))
        self.label_3.setText(_translate("otherwindow", "BATSMAN"))

        self.label_4.setText(_translate("otherwindow", "ALL-ROUNDER"))
        self.label_5.setText(_translate("otherwindow", "BOWLER"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    otherwindow = QtWidgets.QMainWindow()
    ui = Bk_otherwindow()
    ui.setupUi(otherwindow)
    otherwindow.show()
    sys.exit(app.exec_())
