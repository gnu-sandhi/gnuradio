import serial
import os
from time import localtime, strftime, sleep

MAP_FILE = './map_machine_ids.txt'
LOG_FILE = '/var/sbhspylog/sbhserr.log'

OUTGOING_MACHINE_ID  = 252
INCOMING_FAN  = 253
INCOMING_HEAT = 254
OUTGOING_TEMP = 255

MAX_HEAT = 100
MAX_FAN = 100

class Sbhs:
    """ This is the Single Board Heater System class """

    def __init__(self):
        # status of the board
        # 0 = not connected
        # 1 = connected
        self.machine_id = -1
        self.device_num = -1
        self.boardcon = False
        self.status = 0

    def connect(self, machine_id):
        """ Open a serial connection via USB to the SBHS using the machine id """
        # check for valid machine id number
        try:
            self.machine_id = int(machine_id)
        except:
            print 'Invalid machine id specified'
            return False

        # get the usb device file from the machine map file
        try:
            map_file = open(MAP_FILE, 'r')
            usb_device_file = False
            for mapping_str in map_file.readlines():
                mapping = mapping_str.split('=')
                # if mapping for the machine id found set the usb device file and break out of loop
                if mapping[0] == str(self.machine_id):
                    usb_device_file = mapping[1].strip()
                    break
            # reached end of file and check if machine id entry is present in the machine map file
            map_file.close()
            if not usb_device_file:
                print 'Error: cannot locate the USB device in the map table for machine id %d' % self.machine_id
                self.log('cannot locate the USB device in the map table for machine id %d' % self.machine_id, 'ERROR')
                return False
        except:
            map_file.close()
            print 'Error: cannot get the USB device path for the machine id %d' % self.machine_id
            self.log('cannot get the USB device path for the machine id %d' % self.machine_id, 'ERROR')
            return False

        # check if SBHS device is connected
        if not os.path.exists(usb_device_file):
            print 'SBHS device file ' + usb_device_file + ' does not exists'
            self.log('SBHS device file ' + usb_device_file + ' does not exists', 'ERROR')
            return False
        try:
            self.boardcon = serial.Serial(port=usb_device_file, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=2)
            self.status = 1
            return True
        except:
            print 'Error: cannot connect to machine id %d' % self.machine_id
            self.log('cannot connect to machine id %d' % self.machine_id, 'ERROR')
            self.machine_id = -1
            self.device_num = -1
            self.boardcon = False
            self.status = 0
        return False

    def connect_device(self, device_num):
        """ Open a serial connection via USB to the SBHS using USB Device Number"""
        # check for valid device number
        try:
            self.device_num = int(device_num)
        except:
            print 'Invalid device number specified'
            return False

        usb_device_file = '/dev/ttyUSB%d' % self.device_num
        # check if SBHS device is connected
        if not os.path.exists(usb_device_file):
            print 'SBHS device file ' + usb_device_file + ' does not exists'
            self.log('SBHS device file ' + usb_device_file + ' does not exists', 'ERROR')
            return False
        try:
            self.boardcon = serial.Serial(port=usb_device_file, baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=2)
            self.machine_id = self.getMachineId()
            return True
        except:
            print 'Error: cannot connect to device %s' % usb_device_file
            self.log('cannot connect to device %s' % usb_device_file, 'ERROR')
        return False

    def setHeat(self, val):
        """ Set the heat """
        if val > MAX_HEAT or val < 0:
            print 'Error: heat value cannot be more than %d' % MAX_HEAT
            return False

        try:
            self._write(chr(INCOMING_HEAT))
            self._write(chr(val))
            return True
        except:
            print 'Error: cannot set heat for machine id %d' % self.machine_id
            self.log('cannot set heat for machine id %d' % self.machine_id, 'ERROR')
            return False

    def setFan(self, val):
        """ Set the fan """
        if val > MAX_FAN or val < 0:
            print 'Error: fan value cannot be more than %d' % MAX_FAN
            return False
        try:
            self._write(chr(INCOMING_FAN))
            self._write(chr(val))
            return True
        except:
            print 'Error: cannot set fan for machine id %d' % self.machine_id
            self.log('cannot set fan for machine id %d' % self.machine_id, 'ERROR')
            return False

    def getTemp(self):
        """ Get the temperature """
        try:
            self.boardcon.flushInput()
            self._write(chr(OUTGOING_TEMP))
            temp = ord(self._read(1)) + (0.1 * ord(self._read(1)))
            return temp
        except:
            print 'Error: cannot read temperature from machine id %d' % self.machine_id
            self.log('cannot read temperature from machine id %d' % self.machine_id, 'ERROR')
        return  0.0

    def getMachineId(self):
        """ Get machine id from the device """
        try:
            self.boardcon.flushInput()
            self._write(chr(OUTGOING_MACHINE_ID))
            sleep(0.5) # sleep before reading machine id
            machine_id = ord(self._read(1))
            return machine_id
        except:
            print 'Error: cannot read machine id from %s' % self.boardcon.port
            self.log('cannot read machine id from %s' % self.boardcon.port, 'ERROR')
        return -1

    def disconnect(self):
        """ Reset the board fan and heat values and close the USB connection """
        try:
            self.boardcon.close()
            self.boardcon = False
            self.status = 0
            return True
        except:
            print 'Error: cannot close connection to the machine'
            self.log('cannot close connection to the machine', 'ERROR')
            return False

    def reset_board(self):
        self.setFan(100)
        self.setHeat(0)

    def _read(self, size):
        try:
            data = self.boardcon.read(size)
            return data
        except:
            print 'Error: cannot read from machine id %d' % self.machine_id
            self.log('cannot read from machine id %d' % self.machine_id, 'ERROR')
            raise Exception

    def _write(self, data):
        try:
            self.boardcon.write(data)
            return True
        except:
            print 'Error: cannot write to machine id %d' % self.machine_id
            self.log('cannot write to machine id %d' % self.machine_id, 'ERROR')
            raise Exception

    def log(self, msg, level):
        try:
            errfile = open(LOG_FILE, 'a') # open error log file in append mode
            if not errfile:
                return
            log_msg = '%s %s %s\n' %(level, strftime('%d:%m:%Y %H:%M:%S', localtime()), msg)
            errfile.write(log_msg)
            errfile.close()
            return
        except:
            return

