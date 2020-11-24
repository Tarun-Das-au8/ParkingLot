class Vehicle:
    def __init__(self, regno, color):
        self.color = color
        self.regno = regno


class Parking(Vehicle):
    def __init__(self):
        self.capacity = 0
        self.slotId = 0
        self.occupiedSlots = 0

    def createParkingSlot(self, capacity):
        self.capacity = capacity
        self.slots = [-1] * capacity
        return self.capacity

    def empty(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park(self, regno, color):
        if self.occupiedSlots < self.capacity:
            slotId = self.empty()
            self.slots[slotId] = Vehicle(regno, color)
            self.slotId += 1
            self.occupiedSlots += 1
            return slotId + 1
        else:
            return -1

    def status(self):
        print("Slot No \t Regd No \t\t Colour")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i+1)+"\t\t" +
                      str(self.slots[i].regno)+"\t\t"+str(self.slots[i].color))
            else:
                print(str(i+1) + "\t\t" + "slot is free now ")

    def leave(self, slotId):
        if self.occupiedSlots > 0 and self.slots[slotId-1] != -1:
            self.slots[slotId-1] = -1
            self.occupiedSlots = self.occupiedSlots - 1
            return True
        else:
            return False

    def getRegdnoByColor(self, color):
        regnos = []
        for i in self.slots:
            if i == -1:
                continue
            if i.color == color:
                regnos.append(i.regno)
        return regnos

    def findSlotByRegdno(self, regno):
        for i in range(len(self.slots)):
            if self.slots[i].regno == regno:
                return i+1
            else:
                continue
        return -1

    def findSlotByColor(self, color):
        slotnos = []
        for i in range(len(self.slots)):

            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                slotnos.append(str(i+1))
        return slotnos

    def show(self, value):
        if value.startswith('create_parking_lot'):
            n = int(value.split(' ')[1])
            res = self.createParkingSlot(n)
            print(str(res)+' Parking slots created.')

        elif value.startswith('park'):
            regno = value.split(' ')[1]
            color = value.split(' ')[2]
            res = self.park(regno, color)
            if res == -1:
                print("Parking lot is full")
            else:
                print("Slot allocated number : "+str(res))

        elif value.startswith('status'):
            self.status()

        elif value.startswith('leave'):
            slotId = int(value.split(' ')[1])
            status = self.leave(slotId)
            if status:
                print('Slot number '+str(slotId)+' is free')

        elif value.startswith('registration_numbers_for_cars_with_colour'):
            color = value.split(' ')[1]
            regnos = self.getRegdnoByColor(color)
            print(', '.join(regnos))

        elif value.startswith('slot_number_for_registration_number'):
            regno = value.split(' ')[1]
            slotno = self.findSlotByRegdno(regno)
            if slotno == -1:
                print("Not found")
            else:
                print(slotno)

        elif value.startswith('slot_numbers_for_cars_with_colour'):
            color = value.split(' ')[1]
            slotnos = self.findSlotByColor(color)
            print(', '.join(slotnos))

        elif value.startswith('exit'):
            exit(0)


parking = Parking()
while True:
    value = input('$ ')
    parking.show(value)
