class Plant():
	def __init__(self, name, height_cm, age_days):
		self.name = name
		self.height_cm = height_cm
		self.age_days = age_days

	def get_info(self):
		print(f"{self.name.capitalize()}: {self.height_cm}cm, {self.age_days} days old")

	def grow(self):
		self.height_cm += 1

	def age(self, days):
		self.age_days += days

if __name__ == "__main__":
	rose = Plant("Rose", 25, 30)
	
	print("=== Day 1 ===")
	rose.get_info()
	
	days_to_simulate = 7
	for day in range(days_to_simulate - 1):
		rose.grow()
		rose.age(1)
	
	print(f"=== Day {days_to_simulate} ===")
	rose.get_info()