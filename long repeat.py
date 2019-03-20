def long_repeat(line):
    line = list(line)
    most = 0
    result = []
    
    if not line:
        return 0
    else:
        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                most += 1
                result.append(most)
            else:
                most = 0
    
    if result == []:
        return 1
                
    return max(result)+1
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
  #  assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
  #  assert long_repeat('abababaab') == 2, "Third"
  #  assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
