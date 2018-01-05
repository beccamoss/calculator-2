"""Math functions for calculator."""


def add(list_nums):
    """Return the sum of the two inputs."""

    total = 0
    for num in list_nums:
        total += num
    return total


def subtract(list_nums):
    """Return the second number subtracted from the first."""

    total = list_nums[0]
    for i in range(1, len(list_nums)):
        total -= list_nums[i]
    return total


def multiply(list_nums):
    """Multiply the two inputs together."""

    total = 1
    for num in list_nums:
        total *= num
    return total


def divide(list_nums):
    """Divide the first input by the second and return the result."""

    total = list_nums[0]
    for i in range(1, len(list_nums)):
        total /= list_nums[i]
    return total


def square(list_nums):
    """Return the square of the input."""
    total = 1
    for num in list_nums:
        total *= (num * num)

    return total


def cube(list_nums):
    """Return the cube of the input."""
    total = 1
    for num in list_nums:
        total *= (num ** 3)

    return total



def power(list_nums):
    """Raise num1 to the power of num and return the value."""

    total = list_nums[0]**list_nums[1]
    for i in range(2, len(list_nums)):
        total **= list_nums[i]
        #print total

    return total


def mod(list_nums):
    """Return the remainder of num / num2."""

    total = list_nums[0]
    for i in range(1, len(list_nums)):
        total = total % list_nums[i]
        #print total
    return total
