import json
from pyicloud import PyiCloudService

class ICloudHelper:

	iPhone = None
	iCloudApi = None

	def findMyPhone(self):
		self.iPhone.play_sound()

	def __init__(self):
		with open('config.json') as config_file:
			config = json.load(config_file)

		defaultDevice = config["devices"][0] 

		self.iCloudApi = PyiCloudService(defaultDevice["userName"],defaultDevice["password"])
		self.iPhone = self.iCloudApi.devices[int(defaultDevice["deviceIdx"])]
