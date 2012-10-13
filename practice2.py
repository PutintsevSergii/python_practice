#!/usr/bin/env python
"practice # 2"


def simple(num): 
    """Return the arr. In arr we have simple digits"""
    assert num > 0
    assert type(num) is not float 
    assert type(num) is int 
    assert num != 0   
    arr = []
    devider = 1
    while num ** 0.5 > 1:
        devider += 1
        if num % devider == 0:
            num /= devider
            arr.append(devider)
            devider -= 1             
    return arr

def str_wrk(string):
    """Return the result. in result we add substrings which not repeat
    , or substring once if it repeats several times
    if we have # - simbol we repeat last added simbol in result""" 
    assert type(string) is  str
    result = ''
    rez = False    
    for i in range(len(string)-1):
        if string[i] == string[i+1] and string[i] != '#':
            if rez == False:
                result += string[i]
                rez = True 
        elif string[i] == '#' and len(result) > 0 :
            result += result[len(result) - 1]         
        else:
            rez = False
    if string[len(string)-1] == '#' and len(result) > 0:
        result += result[len(result) - 1]
    return result

def gnom_sort(arr):
    """Returns the sorted array, GNOM SORT"""
    assert type(arr) is  not str 
    i = 0
    while i < len(arr)-1:
        if arr[i] <= arr[i + 1]:
            i += 1
        else:
            buf = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = buf
            if i != 0:
                i -= 1
    return arr

def check_simple():
    "unit tests for simple"
    assert simple(123456789) == [3, 3, 3607, 3803]
    assert simple(3)==[3]
    #assert simple(-1)==[]
    #assert simple(3.14)==[]
    #assert simple(0)==[]    
    #assert simple("678uytt")==[]
    #assert simple ("lsdfjasd")==[]

def check_str_work():
    "unit twst for str_work"
    assert str_wrk("22#2233#") == "22233"
    #assert str_wrk(15) == ''
    assert str_wrk("##########") == ""
    assert str_wrk("###444ddd55533#") == "4d533"
    
def check_gnom_sort():
    "unit test for gnom_str"
    assert gnom_sort ([4, 8, 7, 6, 4, 3, 2, 1]) == [1, 2, 3, 4, 4, 6, 7, 8]
    #assert gnom_sort ("acbdesf") == []

def main():    
    "main"
    print check_simple()    
    print check_str_work()
    print check_gnom_sort()
    return 0
    

if __name__ == '__main__':
    main()