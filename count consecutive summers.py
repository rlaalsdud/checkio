def count_consecutive_summers(num):
    count = 0 
    result = 0
    a = int(num/2) + 1
    for i in range (1, a):
       j = i
       for j in range(j, num):
           print(j)
           count += j
           if count == num:
               count = 0
               result += 1
               break
           if count > num:
               count = 0
               break
    return result + 1

if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))
 
    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
