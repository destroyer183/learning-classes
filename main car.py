from car import Car

car1 = Car('Chevy', 'Corvette', 2021, 'Blue')

car2 = Car('Ford', 'Mustang', 2022, 'Red')

print('')

print(f"car 1 make: {car1.make}")

print(f"car 1 model: {car1.model}")

print(f"car 1 year: {car1.year}")

print(f"car 1 color: {car1.color}")

print('')

car1.drive()

car1.stop()

print('\n\n\n')

print(f"car 2 make: {car2.make}")

print(f"car 2 model: {car2.model}")

print(f"car 2 year: {car2.year}")

print(f"car 2 color: {car2.color}")

print('')

car2.drive()

car2.stop()