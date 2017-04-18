class Car(object):

	def __init__(self, name = None, model = None, carType = None):

		two_door_coupes = ['Koenigsegg','Porshe']
		more_than_four_wheelers = ['trailer']

		self.speed = 0

		if carType == 'trailer':
			self.carType = carType
			self.speed = 0
		else:
			self.carType = 'saloon'

		if name is None:
			self.name = 'General'
		else:
			self.name = name

		if model is None:
			self.model = 'GM'
		else:
			self.model = model

		if name in two_door_coupes:
			self.num_of_doors = 2
		else:		
			self.num_of_doors = 4

		if self.carType  in more_than_four_wheelers:
			self.num_of_wheels = 8
		else:		
			self.num_of_wheels = 4


	def drive(self,speed):
		if speed == 3:
			self.speed = 1000
		elif speed == 7:	
			self.speed = 77

		return self
	
	def is_saloon(self):
		if self.carType == "saloon":
			return True