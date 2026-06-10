class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * capacity

    def get(self, i: int) -> int:

        return self.array[i]

    def set(self, i: int, n: int) -> None:
        
        if i < self.capacity:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        
        if self.length == self.capacity:
            self.resize()

        self.set(self.length, n)
        self.length += 1
        print(self.length)

    def popback(self) -> int:

        end = self.array[self.length - 1]
        self.array[self.length - 1] = 0
        self.length -= 1
 
        return end

    def resize(self) -> None:
        temp = self.array
        self.capacity = 2 * self.capacity
        self.array = [0] * self.capacity
        self.array[:(self.capacity//2)] = temp

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
