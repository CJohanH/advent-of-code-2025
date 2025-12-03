# Started off using the s+s[1:-1] solution, but it doesn't apply when pattern is repeated
# odd amount of times. e.g. 565656 would match, but we don't want that, went with regex instead.

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
                        # Disallow id of odd length
                        if len(str_product_id) % 2:
                            continue
                        # Regex to the rescue
                        match = re.match(r"^(.*)\1+$", str_product_id)
                        # Disallow matching groups with single digit matches
                        if match and len(match.group(1)) == len(str_product_id) / 2:
                            self.sum += product_id


if __name__ == "__main__":
    checker = Checker()
    checker.check()
    print(checker.sum)
