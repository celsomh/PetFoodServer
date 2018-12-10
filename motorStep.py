import pyfirmata
import time
import WeightSensor

board = pyfirmata.Arduino('/dev/ttyACM0')
pin8 = board.get_pin("d:8:o")
pin9 = board.get_pin("d:9:o")
pin10 = board.get_pin("d:10:o")
pin11 = board.get_pin("d:11:o")

steps = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

working = False

def off():
	global working
	working = False
	pin8.write(0)
	pin9.write(0)
	pin10.write(0)
	pin11.write(0)

def step(i):
	pin8.write(i[0])
	pin9.write(i[1])
	pin10.write(i[2])
	pin11.write(i[3])
	time.sleep(0.003)

def move(sec):
	timeNow = int(time.time())
	timeEnd = timeNow + int(sec)
	while int(time.time()) <= timeEnd:
		for i in steps:
			step(i)
	off()
	
def isWorking():
	return working
