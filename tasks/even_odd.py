__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    odd_sum = 0
    even_sum = 0
    
    for number in arr:
        if number % 2:
            odd_sum += number
        else:
            even_sum += number

    result = even_sum / odd_sum
    return result            

