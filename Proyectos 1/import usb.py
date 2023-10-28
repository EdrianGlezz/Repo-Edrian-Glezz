import usb.core
import usb.util
from PySide2 import QtCore, QtWidgets
import sys
def find_device():
    device = usb.core.find(find_all=True)
    for d in device:
        if d.bDeviceClass == 0 and d.bDeviceSubClass == 0 and d.bDeviceProtocol == 0:
            return d
    return None

device = find_device()

if device is None:
    print('Dispositivo no encontrado')
    sys.exit(1)

device.set_configuration()
endpoint = device[0][(0,0)][0]

def read_data():
    try:
        data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
        label.setText(data)
    except usb.core.USBError as e:
        if e.args == ('Operation timed out',):
            pass

app = QtWidgets.QApplication(sys.argv)
label = QtWidgets.QLabel('Esperando datos...')
label.setAlignment(QtCore.Qt.AlignCenter)
label.setFixedSize(400, 100)
label.show()

timer = QtCore.QTimer()
timer.timeout.connect(read_data)
timer.start(100)

sys.exit(app.exec_())
