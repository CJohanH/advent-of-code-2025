class Dial:

    def __init__(self):
        self.point = 50
        self.counter = 0

    def rotate(self):
        with open("input.txt") as file:
            for line in file:
                if line.startswith("L"):
                    self.point = (self.point - int(line[1:])) % 100
                else:
                    self.point = (self.point + int(line[1:])) % 100
                if self.point == 0:
                    self.counter += 1


if __name__ == "__main__":
    dial = Dial()
    dial.rotate()
    print(dial.counter)
