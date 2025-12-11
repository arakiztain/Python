class Plant:
	def __init__(self, name, height_cm, age_days):
		self.name = name
		self.height_cm = height_cm
		self.age_days = age_days

	def display_info(self):
		print(f"{self.name.capitalize()}: {self.height_cm}cm, {self.age_days} days old")

class FloweringPlant(Plant):