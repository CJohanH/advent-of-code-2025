class BatteryBanks:

    def __init__(self):
        self.sum = 0
        self._capacity = 12

    def turn_on_battery_banks(self):
        with open("input.txt") as file:
            for line in file:
                bank = line.strip()  # Remove newlines
                max_joltage = ""
                current_joltage = ""

                for i in range(len(bank)):
                    battery = bank[i]

                    # If there is a joltage to compare to and there is enough space in the battery bank,
                    # iterate over batteries until one with more voltage is found.
                    while (
                            len(current_joltage)
                            and current_joltage[-1] < battery
                            and len(current_joltage) + (len(bank) - i) > self._capacity
                    ):
                        current_joltage = current_joltage[:-1]

                    # Always add a new battery if we have not reached capacity...
                    if len(current_joltage) < self._capacity:
                        current_joltage += battery

                    # Capacity reached!
                    if len(current_joltage) == self._capacity:
                        if current_joltage > max_joltage:
                            max_joltage = current_joltage

                self.sum += int(max_joltage)


if __name__ == "__main__":
    batteryBanks = BatteryBanks()
    batteryBanks.turn_on_battery_banks()
    print(batteryBanks.sum)
