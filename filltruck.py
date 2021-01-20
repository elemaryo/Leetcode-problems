import collections


class Solution:
    def __init__(self, truckSpace, packagesSpace):
        self.main(truckSpace, packagesSpace)

    def main(self, truckSpace, packagesSpace):
        paths = collections.defaultdict(int)
        final = []
        for index, item in enumerate(packagesSpace):
            print(item, paths)
            print(truckSpace-item-30)
            if truckSpace-item-30 in paths:
                print("yes")
                final.append([paths[truckSpace-item-30], index])
            paths[item] = index

        print(final)


test = Solution(90, [1, 10, 25, 35, 60])


def fill_truck(boxes, units, truckSize):

    # [3, 4, 6]
    # [5, 3 ,2]
    # truck size = 4 boxes

    products = [(units[i], boxes[i]) for i in range(len(boxes))]
    products.sort(reverse=True)
    print(products)
    units_loaded = 0
    boxes_loaded = 0
    i = 0
    while (boxes_loaded < truckSize and i < len(boxes)):
        p_units, p_boxes = products[i]
        boxes_to_load = min(p_boxes, truckSize - boxes_loaded)
        boxes_loaded += boxes_to_load
        units_loaded += boxes_to_load * p_units
        i += 1
    return units_loaded

    #  3
    # return max number of units you can fit in truck
test_boxes = [5, 23, 63]
test_units = [53, 23, 34]
truck_size = 3
print(fill_truck(test_boxes, test_units, truck_size))
