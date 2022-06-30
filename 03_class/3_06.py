import car
import racing as rc

myCarGame = rc.CarRacing()
Car01 = car.Car('Car01', 'White', 250)
Car02 = car.Car('Car02', 'Black', 200)
Car03 = car.Car('Car03', 'Yellow', 220)
Car04 = car.Car('Car04', 'Red', 280)
Car05 = car.Car('Car05', 'Blue', 150)

myCarGame.addCar(Car01)
myCarGame.addCar(Car02)
myCarGame.addCar(Car03)
myCarGame.addCar(Car04)
myCarGame.addCar(Car05)

myCarGame.startRacing()