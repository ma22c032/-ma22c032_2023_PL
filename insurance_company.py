# -*- coding: utf-8 -*-
"""Insurance company

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_-8NHZHyOvyeXP21WfKoRcsbPR1PuNk1
"""

def probability_of_ruin(q, R):
    # Calculate the probability of ruin starting from $1000
    P_0 = (1 - (1 - q) ** (1000 / R)) / (1 - (1 - q) ** (1000 / R) * (1 - q ** (R / 100)))
    return P_0

def find_reserve_to_limit_ruin_probability(q, target_probability):
    # Binary search to find the reserve ($R) that limits ruin probability to the target value
    lower_bound = 0
    upper_bound = 1000  # A reasonable upper bound for the reserve
    tolerance = 0.0001  # Tolerance for the binary search

    while upper_bound - lower_bound > tolerance:
        mid = (lower_bound + upper_bound) / 2
        P_0 = probability_of_ruin(q, mid)

        if P_0 > target_probability:
            upper_bound = mid
        else:
            lower_bound = mid

    return upper_bound

if __name__ == '__main__':
    q = 0.46  # Probability of receiving a claim
    target_probability = 0.001  # Target probability of ruin (0.1%)

    reserve = find_reserve_to_limit_ruin_probability(q, target_probability)
    print(f"The company's reserve to limit ruin probability to {target_probability * 100}% or less is ${reserve:.2f}")