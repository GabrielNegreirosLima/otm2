# LAW OF LARGE NUMBERS TEST

import random
import statistics

def get_average_from_dice(dice, times):
    sum = 0

    for _ in range(times):
        sum += random.choice(dice)
    
    return sum / times


normal_dice = [1, 2, 3, 4, 5, 6]
print(f"Normal dice mean: {statistics.mean(normal_dice)}")

# Try 10 times and prints the average that will not be near to the mean
average = get_average_from_dice(normal_dice, 10)
print(f"[NORMAL] Average problably no near to the mean: {average}")


# Try 1000 times and prints the average that will be near to the mean
average = get_average_from_dice(normal_dice, 1000)
print(f"[NORMAL] Average problably near to the mean: {average}")


addicted_dice = [1, 2, 3, 4, 5] + [6] * 4
print(f"\nNormal dice mean: {statistics.mean(addicted_dice)}")
average = get_average_from_dice(addicted_dice, 10)
print(f"[ADDICTED] Average problably no near to the mean: {average}")

average = get_average_from_dice(addicted_dice, 1000)
print(f"[ADDICTED] Average problably near to the mean: {average}")

