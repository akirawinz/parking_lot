class Car {
  constructor(registrationNumber, color) {
    this.registrationNumber = registrationNumber
    this.color = color
    this.slot = null
  }
}

class ParkingLot {
  constructor(slots) {
    this.slots = Array(slots).fill(null)
    this.cars = []
  }

  park(car) {
    for (let i = 0; i < this.slots.length; i++) {
      if (this.slots[i] === null) {
        this.slots[i] = car
        car.slot = i + 1
        this.cars.push(car)
        console.log(`Allocated slot number: ${car.slot}`)
        return
      }
    }
    console.log('Sorry, parking lot is full')
  }
}

const parkingLot = new ParkingLot(6)
console.log('parkingLot: ', parkingLot)
parkingLot.park(new Car('KA-01-HH-1234', 'White'))
parkingLot.park(new Car('KA-01-HH-9999', 'White'))
parkingLot.park(new Car('KA-01-BB-0001', 'Black'))
parkingLot.park(new Car('KA-01-HH-7777', 'Red'))
parkingLot.park(new Car('KA-01-HH-2701', 'Blue'))
parkingLot.park(new Car('KA-01-HH-3141', 'Black'))
console.log('parkingLot: ', parkingLot)
