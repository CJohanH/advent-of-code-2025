# To make this solution work all that needed to be done was to remove the check
# for odd length product id and matching groups with single digit matches

import re


class Checker:

    def __init__(self):
        self.sum = 0

    def check(self):
        with open("input.txt") as file:
            for line in file:
                for id_range in line.split(","):
                    min_range, max_range = id_range.split("-", 1)
                    for product_id in range(int(min_range), int(max_range)+1):
                        str_product_id = str(product_id)
                        # Regex to the rescue
                        match = re.match(r"^(.*)\1+$", str_product_id)
                        if match:
                            self.sum += product_id



if __name__ == "__main__":
    checker = Checker()
    checker.check()
    print(checker.sum)
