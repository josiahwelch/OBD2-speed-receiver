#!/bin/python3
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication
from threading import Thread

from PyQt6 import QtCore

from serial_receiver import SerialReceiver


# Josiah Welch
# 8/19/2025
# Shows the speed received from LoRa, designed for NU-ROVE

class SpeedLabel(QLabel):
    def __init__(self, com_port, parent=None):
        super(SpeedLabel, self).__init__(parent)
        self.setStyleSheet(f"qproperty-alignment: {int(QtCore.Qt.AlignmentFlag.AlignCenter)};background-color: rgb(0, 64, 255);")
        self.setText("INIT")
        self.listening_thread = Thread(target=self._run)
        self._serial_receiver = SerialReceiver(com_port=com_port, timeout=1)

    def start_listening(self):
        self.listening_thread.start()

    def stop_listening(self):
        self.listening_thread.join()

    def _run(self):
        self.setText(self._serial_receiver.get_data())

class SpeedShowGUI(QMainWindow):
    def __init__(self, com_port, parent=None):
        super().__init__()
        self.setWindowTitle("Speed Receiver")
        self.setGeometry(300, 300, 600, 600)
        self.speed_label = SpeedLabel(com_port=com_port, parent=self)
        self.speed_label.start_listening()
        self.setCentralWidget(self.speed_label)

def __main__():
    app = QApplication(sys.argv)
    #window = SpeedShowGUI(sys.argv[1], parent=app)
    window = SpeedShowGUI("COM4")
    window.show()

    app.exec()

if __name__ == "__main__":
    __main__()