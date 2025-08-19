# Josiah Welch
# 8/19/2025
# Serial communicator to LoRa module, designed for NU-ROVE

from serial import Serial

class SerialReceiver:
    def __init__(self, com_port, timeout=1):
        self.ser = Serial(com_port, 9600, timeout=timeout)

    def get_data(self):
        return self.ser.readline().decode('utf-8').strip()

