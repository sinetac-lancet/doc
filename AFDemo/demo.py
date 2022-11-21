'''
-*- coding: utf-8 -*-
@Time  : 2022/11/20 21:24
@author: dutengfei
'''
from AFDemo.windows import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
import sys


# 这边的第一个参数，新建的时候是什么，就选什么
# 新建一个class是为了后面方便写按钮方法和绑定
# 如果你的功能不是很复杂，完全可以不写，照着方法一的代码调用也行
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # 初始化父类，把 MyMainWindow 的对象 self 转成父类 QMainWindow 对象，并调用 init 函数。
        super(MyWindow, self).__init__(parent)
        # 继承 windows.py 中的 Ui_MainWindow 界面类，调用 Ui_MainWindow 类的setupUi() 方法。
        self.setupUi(self)
        self.inputDir = self.lineEdit_input_dir
        self.outDir = self.lineEdit_out_dir
        self.btFvPd = self.pb_fv_pd_calculate
        print('inputDir:{}'.format(self.inputDir))
        print('outDir:{}'.format(self.outDir))
        print('btFvPd:{}'.format(self.btFvPd))

        # 给FV/PD计算按钮绑定槽函数
        self.btFvPd.clicked.connect(self.fv_and_pd_calculate)

    #
    def fv_and_pd_calculate(self):
        # 获取文本框输入参数
        windows_config = self.lineEdit_windows_config.text()
        box_number = self.lineEdit_box_number.text()
        raw_size = self.lineEdit_raw_size.text()
        # 获取下拉框选择参数
        # 0: ; 1: ;2: ;
        pd_type = self.comboBox_pd_type.currentIndex()

        print('输入参数：',windows_config, box_number, raw_size, pd_type)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    myWin = MyWindow()
    # myWin.setGeometry(400, 400, 400, 300)
    myWin.setWindowTitle("PyQt5 Tutorial")
    myWin.show()

    # 设置窗口一直运行指导使用关闭按钮进行关闭
    sys.exit(app.exec_())