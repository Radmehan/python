import time
from functools import lru_cache
"""
def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n
if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("done..calling again")
    some_work(3)
    print("called again")"""

# after importing cache
@lru_cache(maxsize=32)
def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n
if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("done..calling again")
    input("Enter some words : ")
    some_work(3)
    print("called again")