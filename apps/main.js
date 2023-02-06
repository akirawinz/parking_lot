class Car {
  constructor(registrationNumber, color) {
    this.slot = null
  }
}

class ParkingLot {
  constructor(slots) {
    this.slots = Array(slots).fill(null)
  }
}

const parkingLot = new ParkingLot(6)
console.log('parkingLot: ', parkingLot)
