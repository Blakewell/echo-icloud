import json
from pyicloud import PyiCloudService

class ICloudHelper:

	config = None

	def getDevice(self, name): 
		
		deviceConfig = self.config["devices"][0];	

		for device in self.config["devices"]: 
			if device["name"].lower() == name.lower():
				deviceConfig = device
				break

		iCloudApi = PyiCloudService(deviceConfig["userName"],deviceConfig["password"])
		return iCloudApi.devices[int(deviceConfig["deviceIdx"])]

	def findMyPhone(self, name):
		device = self.getDevice(name)
		device.play_sound()

	def __init__(self):
		with open('config.json') as config_file:
			self.config = json.load(config_file)

