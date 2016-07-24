import sys
from PyQt5.QtWidgets \
    import * #QWidget,QApplication,QVBoxLayout,QPushButton,QGridLayout,QLabel
import Cly



class AddressBook(QWidget):
    def __init__(self,praent=None):
        super(AddressBook,self).__init__(praent)
        self.text_area = QTextBrowser()
        self.send_area = QLineEdit()
        self.send_btn = QPushButton("send")
        mainLay = QVBoxLayout()
        subLay = QHBoxLayout()
        #self.infoBar = QLabel("")
        self.send_btn.clicked.connect(self.push_send)
        #subLay.addWidget(self.btn[i],i/5,i%5)
        mainLay.addWidget(self.text_area)
        subLay.addWidget(self.send_area)
        subLay.addWidget(self.send_btn)
        mainLay.addLayout(subLay)
        #mainLay.addLayout()
        self.setLayout(mainLay)


    def push_send(self):
        print('pushed')
        send_mes = self.send_area.text()
        self.text_area.append('You:' + send_mes)
        self.cly.sent(send_mes)

    def rcv(self,rcv_str):
        self.text_area.append('othre:' + rcv_str)


    def set_cly(self,cly):
        self.cly = cly


if __name__ == '__main__':
    app = QApplication(sys.argv)

    print('adores:')
    ip = str(input())
    main_window = AddressBook()
    cly = Cly.Cly(main_window,6000,ip)
    main_window.set_cly(cly)
    main_window.show()
    sys.exit(app.exec_())
