from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
   #처음 값의 개수와 전체 elements의 개수가 같으면 True
   count = 0 
   if elements == []:
       return True
   
   for i in range(len(elements)-1):
       if elements[i] == elements[i+1]:
           count += 1
       else:
           return False
   return True

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
