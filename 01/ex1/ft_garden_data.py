class Plant():
	def __init__(self, name, height_cm, age_days):
		self.name = name
		self.height_cm = height_cm
		self.age_days = age_days

	def display_info(self):
		print(f"{self.name.capitalize()}: {self.height_cm}cm, {self.age_days} days old")

if __name__ == "__main__":
	print("=== Garden Plant Registry ===")
	rose = Plant("Rose", 25, 30)
	sunflower = Plant("Sunflower", 80, 45)
	catcus = Plant("Cactus", 15, 120)
	rose.display_info()
	sunflower.display_info()
	catcus.display_info()
	