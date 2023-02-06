__all__ = (
    'seconds_to_str',
)

def check_and_return(number, divider):
    result = number // divider
    if result % 10 == result:
        return f'0{result}'
    return result

def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    time = []
    year_in_sec = 365 * 24 * 3600
    day_in_sec = 24 * 3600
    hour_in_sec = 3600
    minute_in_sec = 60

    if seconds >= year_in_sec:
        years = check_and_return(seconds, year_in_sec)
        time.append(f'{years}y')

    if seconds >= day_in_sec:
        days = check_and_return(seconds % year_in_sec, day_in_sec)
        time.append(f'{days}d')

    if seconds >= hour_in_sec:
        hours = check_and_return(seconds  % day_in_sec, hour_in_sec)
        time.append(f'{hours}h')

    if seconds >= minute_in_sec:
        minutes = check_and_return(seconds % hour_in_sec, minute_in_sec)
        time.append(f'{minutes}m')

    correct_seconds = seconds % 60
    if correct_seconds % 10 == correct_seconds:
        time.append(f'0{correct_seconds}s')
    else:
        time.append(f'{correct_seconds}s')

    # return sum(time)
    result = ''.join(time)
    return result




