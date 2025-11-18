def main():
     result = multiply_two(3.4, 6.3)
     result2 = multiply_two(3, 6)
     print(result)
     print(result2)
     result = subtract(5, 20)
     print(result)
     result = add(5, 6)
     print(result)
     result = divide(5, 50)
     print(result)

def multiply_two(first, second):
    return first * second


def add(bar, foo):
    return bar + foo


def subtract(bar, boo):
    return bar - boo

def divide(bar, doo):
    return bar / doo

if __name__ == '__main__':
    main()