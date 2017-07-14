from collections import Counter
breakfast = ["eggs", "bread", "cereal", "eggs"]
breakfast_counter = Counter(breakfast)
print(breakfast_counter)
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

#palindrome
from collections import deque
def palindrome(word):
    word_dq = deque(word)
    while(len(word_dq) > 1):
        if word_dq.popleft() != word_dq.pop():
            return False
    return True

print(palindrome("a"))
print(palindrome("radar"))
