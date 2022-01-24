import matplotlib.pyplot as plt
import random


def roll_dice(number_of_dice: int, sides: int = 6) -> int:
    """Simulates dice throws."""
    result = 0
    for _ in range(number_of_dice):
        result += random.randint(1, sides)
    return result

def simulate_die_throws(number_of_rolls: int, amount_of_dice: int, sides:int = 6) -> dict:
    """Simulates dice throws for a certain number of times. Returns a dictionary of the distribution."""
    results = {num: 0 for num in range(amount_of_dice, amount_of_dice * sides + 1)}
    for _ in range(number_of_rolls):
        results[roll_dice(amount_of_dice, sides)] += 1
    return results

def get_probability(distribution: dict, total_throws: int) -> dict:
    """Returns a dictionary with probabilities of dice throw outcomes."""
    output = distribution
    for res, outcome in distribution.items():
        output[res] = round((outcome / total_throws) * 100, 2)
    return output

def main() -> None:
    # Configuring throws
    amount_of_dice = 2
    sides_per_dice = 6
    amount_of_throws = 100000

    # Getting distribution
    distribution = simulate_die_throws(amount_of_throws, amount_of_dice, sides_per_dice)

    # Getting and printing probabilities
    probability = get_probability(distribution, 100000)
    print(probability)

    # Plotting distribution
    plt.bar(distribution.keys(), distribution.values())
    plt.xticks([num for num in range(amount_of_dice, amount_of_dice * sides_per_dice + 1)])
    plt.title(f'Distribution of dice throws (N={amount_of_throws})')
    plt.xlabel('Result')
    plt.ylabel('Times result occured')
    plt.show()

if __name__ == '__main__':
    main()
