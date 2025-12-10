class Plant():
	def __init__(self, name, height_cm, age_days):
		self.name = name
		self.height_cm = height_cm
		self.age_days = age_days

	def display_info(self):
		print(f"{self.name.capitalize()}: {self.height_cm}cm, {self.age_days} days old")

	def grow(self, growth_per_day_cm):
		self.height_cm += growth_per_day_cm

	def age(self, days):
		self.age_days += days

if __name__ == "__main__":
	print("=== Plant Growth Simulation ===")
	# Create a plant instance
	rose = Plant("Rose", 25, 30)
	
	# Display initial info
	print("=== Day 1 ===")
	rose.display_info()
	
	# Simulate growth over 10 days
	days_to_simulate = 7
	growth_per_day_cm = 1  # Rose grows 2 cm per day
	for day in range(days_to_simulate):
		rose.grow(growth_per_day_cm)
		rose.age(1)
	
	# Display final info after simulation
	print(f"\nAfter {days_to_simulate} days of growth:")
	rose.display_info()