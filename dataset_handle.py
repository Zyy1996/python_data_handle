import os
import sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore


color_plate = [
    (255,0,0),
    (0,0,0),
    (0,255,0),
    (0,0,255),
    (220,220,0)
]

class Table_drawing:
    def __init__(self, data_type, title_lab) -> None:
        self.data = []
        self.data_type = data_type
        self.app = pg.mkQApp("Plotting")
        self.win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        self.win.resize(1000, 600)
        self.win.setWindowTitle('消耗统计')

        pg.setConfigOptions(antialias=True)
        self.p6 = self.win.addPlot(title=title_lab)
        self.p6.addLegend()
        self.p6.showGrid(y=1)
        self.p6.setLabel("bottom", "运行时间", "s")
        self.p6.setLabel("left", "cpu消耗", "%")
        self.curve = self.p6.plot(pen='y')

    def table_drawing_get_data(self, data):
        if self.data_type == 1:
            self.data.append(int(data))
        else:
            print(self.data_type, "err")

    def table_drawing_finish(self):
        # print(self.data)
        self.curve.setData(self.data)
        pg.exec()

class Polt_draw:
    def __init__(self,data_type:int,title_lab:str,data:dict) -> None:
        self.data_type = data_type
        self.app = pg.mkQApp("Plotting")
        self.win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
        self.win.resize(1000, 600)
        self.win.setWindowTitle('消耗统计')
        pg.setConfigOptions(antialias=True)
        self.win.setBackground((255,255,255))
        self.p1 = self.win.addPlot(title=title_lab)
        self.p1.showGrid(y=1)
        self.p1.setMouseEnabled(True,True)
        self.p1.addLegend(offset=(10,10))
        self.data = 0
        for key,value in data.items():
            if isinstance(value,list) and len(value) > 0:
                self.p1.plot(value, pen=color_plate[self.data], name=str(key))
                self.data = self.data + 1
                self.win.nextRow()
                
                self.win.addLabel("%s平均值:%6.2f" %(key,sum(value)/len(value)))
            else:
                print("value err")
        # self.p2 = self.win.addLabel("qqwqw {}" %sum)

    def set_bottom_Label(self,text=None,units=None):
        self.p1.setLabel("bottom", text, units,"--")

    def set_left_Label(self,text=None,units=None):
        self.p1.setLabel("left", text, units,"--")

    def show(self):
        pg.exec()

if __name__ == '__main__':

    a = Polt_draw(0,"cpu消耗",{"data":123})
    a.show()
