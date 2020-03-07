from collections import deque
from typing import List


def two_sum(numbers: List[float], target: int) -> List[int]:
    subtract_map = {}

    for i, n in enumerate(numbers):
        if n in subtract_map:
            return [subtract_map[n], i]
        subtract_map[target - n] = i

    raise ValueError('No two sum solution')


def balanced_brackets(s: str) -> str:
    brackets_map = {'}': '{', ']': '[', ')': '('}
    opened = ('(', '[', '{')
    stack = deque()

    if len(s) % 2 or s[-1] in opened:
        return 'Não'

    for char in s:
        if char in opened:
            stack.append(char)
            continue

        if not stack or brackets_map[char] != stack.pop():
            return 'Não'

    return 'Sim' if not stack else 'Não'


def best_transaction_profit(stock_prices: List[int]) -> int:
    min_price = None
    max_profit = 0

    for price in stock_prices:
        if min_price is None or price < min_price:
            min_price = price
            continue

        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit


def retained_water(elevation_map: List[int]) -> int:
    retained = 0
    max_left = 0
    max_right = 0
    left_index = 0
    right_index = len(elevation_map)-1

    while left_index < right_index:
        height_left = elevation_map[left_index]
        height_right = elevation_map[right_index]

        if height_left < height_right:
            if height_left >= max_left:
                max_left = height_left
            else:
                retained += max_left - height_left
            left_index += 1
        else:
            if height_right >= max_right:
                max_right = height_right
            else:
                retained += max_right - height_right
            right_index -= 1

    return retained
