from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys
import logging

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                            filename='new.log',
                            filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                            # a是追加模式，默认如果不写的话，就是追加模式
                            format=
                            '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                            # 日志格式
                            )
        super().__init__(*args, **kwargs)
        # 窗口
        self.setWindowTitle("Epoint")
        self.setWindowIcon(QIcon('../icons/penguin.png'))
        self.showMaximized()
        # 添加浏览器到窗口中
        self.browser = QWebEngineView()
        url = "http://www.baidu.com"
        self.browser.setUrl(QUrl(url))
        self.setCentralWidget(self.browser)
        # 添加导航栏
        navigation_bar = QToolBar('Navigation')
        navigation_bar.setIconSize(QSize(16, 16))
        self.addToolBar(navigation_bar)

        # 添加主页、前进、后退、停止加载和刷新的按钮
        homepage_button = QAction(QIcon('../icons/penguin.png'), 'Home', self)
        back_button = QAction(QIcon('../icons/back.png'), 'Back', self)
        next_button = QAction(QIcon('../icons/next.png'), 'Forward', self)
        reload_button = QAction(QIcon('../icons/renew.png'), 'Reload', self)

        homepage_button.triggered.connect(self.back_to_homepage)  # 信号与相应的处理函数进行连接绑定
        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        reload_button.triggered.connect(self.browser.reload)
        # 将按钮添加到导航栏上
        navigation_bar.addAction(homepage_button)
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(reload_button)
        # 添加地址栏
        self.urlbar = QLineEdit()
        # 响应回车
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)
        self.browser.urlChanged.connect(self.renew_urlbar)

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        logging.debug('urlbar')
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)

    def renew_urlbar(self, q):
        logging.debug('write url')
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def back_to_homepage(self):
        q = QUrl('http://www.baidu.com')
        self.browser.setUrl(q)


# 创建应用
app = QApplication(sys.argv)
# 主窗口
window = MainWindow()
# 最大化显示
window.showMaximized()
# 运行应用并监听事件
app.exec_()
