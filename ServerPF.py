
import sys, Ice
import motorStep
import time
import WeightSensor
import PetFoodSensors
import thread

class SensorControlI(PetFoodSensors.SensorControl):
	def motorTime(self,time,current):
		motorStep.move(time)
	def givefood(self,weight,current):
		print weight,"  food"
		while weight > WeightSensor.getWeightNow():
			print "giving Food"
			motorStep.move(1)
		print "done"
	def getContainerFood(self):#podria no necesitarse
		return 1
	def getFoodEated(self):#podria no necesitarse
		return 1
	def eatingNow(self,current):
		if  motorStep.isWorking():
			print "NO comiendo"
			return False
		elif (WeightSensor.variationInWeight()):
			print "Comiendo"
			return True
	def getWeight(self,current):
		print WeightSensor.getWeightNow(), "<--- wololololol"
		return WeightSensor.getWeightNow()


with Ice.initialize(sys.argv) as communicator:
	adapter = communicator.createObjectAdapterWithEndpoints("SensorControlAdapter", "default -p 10000")
	object = SensorControlI()
	adapter.add(object, communicator.stringToIdentity("SensorControl"))
	adapter.activate()
	thread.start_new_thread(WeightSensor.loopWeight,(True,))
	print("server init: " ,adapter.getEndpoints())
	communicator.waitForShutdown()
