from typing import Any

groceries = ['rice', 'wheat', 'almond', 'dates', 'walnut', 'daal']
quantity = [1, 1, 1, 1, 1, 1]
price = [60, 56, 89, 35, 37, 28]


def bill_calculation(items, kilograms):
    total_price = 0
    for i in items:
        for j in groceries:
            if i == j:
                index1 = groceries.index(j)
                index2 = items.index(i)
                total_price = total_price + (price[index1] * kilograms[index2])
    return total_price
