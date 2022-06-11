# 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
    n = len(a)
    for i in range(n //2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요 : '))
    x = [None] * nx
    
    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요 : '))

    reverse_array(x)    # x를 역순으로 정렬
    
    print('배열 원소를 역순으로 정렬했습니다.')
    
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
        
        
        
# 리스트를 역순으로 정렬
# reverse()함수를 사용하면 된다
# = list(reversed(x)) 와 같다
# x의 원소를 역순으로 꺼내는 iterator(반복자)를 반환하는 것