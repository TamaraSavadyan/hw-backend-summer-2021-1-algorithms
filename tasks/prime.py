__all__ = (
    'is_prime',
)
import math

def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number > 1:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
    else:
        return False
    
    return True
