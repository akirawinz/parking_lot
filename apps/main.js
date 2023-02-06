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

  leave(slot) {
    if (this.slots[slot - 1] === null) {
      console.log('This slot is already empty')
      return
    }
    const car = this.slots[slot - 1]
    this.slots[slot - 1] = null
    this.cars.splice(this.cars.indexOf(car), 1)
    console.log(`Slot number ${slot} is free`)
  }

  status() {
    console.log('Slot No.\tRegistration \t\tNo Colour')
    this.cars.forEach((car) => {
      console.log(`${car.slot}\t\t${car.registrationNumber}\t\t${car.color}`)
    })
  }

  getSlotNumbersForCarsWithColor(color) {
    const cars = this.cars.filter((car) => car.color === color)
    const slotNumbers = cars.map((car) => car.slot)
    console.log(slotNumbers.join(', '))
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
parkingLot.leave(4)
parkingLot.status()
parkingLot.park(new Car('KA-01-P-333', 'White'))
parkingLot.park(new Car('DL-12-AA-9999', 'White'))
parkingLot.getSlotNumbersForCarsWithColor('White')
