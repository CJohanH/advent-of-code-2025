# I don't like this solution, it was done a bit hasty and is hard to follow

class Dial:

    def __init__(self):
        self.point = 50
        self.counter = 0

    def rotate(self):
        with open("input.txt") as file:
            for line in file:
                rotation = int(line[1:])
                self.counter += (rotation // 100)
                if line.startswith("L"):
                    if self.point != 0 and ((self.point - rotation) % 100) > self.point:
                        self.counter += 1
                    self.point = (self.point - rotation) % 100
                else:
                    if self.point != 0 and 0 < ((self.point + rotation) % 100) < self.point:
                        self.counter += 1
                    self.point = (self.point + rotation) % 100
                if self.point == 0:
                    self.counter += 1

if __name__ == "__main__":
    dial = Dial()
    dial.rotate()
    print(dial.counter)
