from typing import Optional
import re

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    new = re.split('\W+', text.strip())
    new.sort(key=len)
    if new[0]:
        return (new[0], new[-1])
    
    return (None, None)

