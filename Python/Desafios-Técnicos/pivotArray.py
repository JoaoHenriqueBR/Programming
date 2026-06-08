""" LeetCode (2161): Partition Array According to Given Pivot

You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

    - Every element less than pivot appears before every element greater than pivot.
    - Every element equal to pivot appears in between the elements less than and greater than pivot.
    - The relative order of the elements less than pivot and the elements greater than pivot is maintained.
        - More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.

Return nums after the rearrangement.
"""

def pivotArray(nums: list[int], pivot: int) -> list[int]:
    left = []
    right = []
    mid = []
    c = 0
    for i in nums:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            mid.append(i)
        else:
            right.append(i)

    result = left + mid + right

    return result


if __name__ == '__main__':

    numbers_count = int(input('Numbers quantity: ').strip())
    pivot = int(input('Pivot: ').strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input(f'Number {_}: ').strip())
        numbers.append(numbers_item)

    result = pivotArray(numbers, pivot)

    print(result)