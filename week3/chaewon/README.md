# 부동소수점이란

- - -

## 정수를 표현하는 방식

- 16진수 : 7B
- 10진수 : 123
- 8진수 : 173
- 2진수 : 111 1011


## 컴퓨터가 실수를 표현하는 방식
### 2진수 표현
- 컴퓨터는 숫자를 표현할 때 2진수를 사용
    - ex) 13 = 8 + 4 + 1        (10진수)
             = 1000 + 100 + 1   (2진수)
             = 1101             (2진수)

- 하지만 소수를 나타낼 때는 특수한 경우가 생김
    - ex) 0.3 = 0.0100 1100 1100 11 ... (0011 무한반복)

    - 이처럼 2진수로 표현하지 못하는 소수는, 정확한 값이 아닌 **근사치 2진수**으로 표현되어 저장됨
    - 이 근사값을 저장하는 방법에는 두 가지가 있음


- - -

### 1. 고정소수점
- 정수를 표현하는 비트 수, 소수를 표현하는 비트 수를 미리 지정하고, 해당 비트 만큼만 사용하여 숫자 표현
    - ex) 실수 표현에 총 4byte(32bit) 사용 : 부호 1bit,  정수 16bit, 소수 15bit
          2.3 = (0) 0000 0000 0000 0010.0100 1100 1100 110
- 정수를 표현하는 bit를 늘리면 큰 수를 표현할 수는 있지만, 정밀한 수를 표현하기는 어려움
- 소수를 표현하는 bit를 늘리면 정밀한 수를 표현할 수는 있지만, 큰 수를 표현하기는 어려움

→ 그렇기에 부동소수점을 사용함


### 2. 부동소수점

- 부동소수점 또는 떠돌이소수점 방식은 실수를 컴퓨터상에서 근사하여 표현할 때 소수점의 위치를 고정하지 않고 그 위치를 나타내는 수를 따로 적는 것
- 소수점의 위치를 풀이하는 '지수', 유효 숫자를 나타내는 '가수'로 표현 

- IEEE 754 Standard for Floating-Point Arithmetic
    ![](https://steemitimages.com/DQme3vRe1nGigGs1GfZkU5ffbufAs1gSNT4MKqR7F1PcxCi/IEEE754.png)

    - ex) 고정소수점으로 표현한 2.3을 2진수 부동소수점 방식으로 표현해보기
            10.0100 1100 1100 110 ...
          → 1.0010011001100110 * 2^1 : 맨 앞의 1 바로 뒤로 소수점 배치
            - 2^1의 1 = '지수', IEEE 754에서는 지수 + 127 값을 기록
            - 소수점 이후 숫자열 = '가수'
            
            즉,
            - 부호 비트(1bit) : 0 (양수)
            - 지수 비트(8bit) : 1000 0000 (127 + 1 = 128)
            - 가수 비트(23bit) : 0010 0110 0110 0110 0000 000

    - 부동소수점을 사용하더라도 정확한 값을 나타낼 수는 없음 → **부동소수점의 오류**


- 부동소수점의 오류 예시

```python
result = 0
for _ in range(100):
    result += 0.1

print(result)
>>> 9.99999999998
```

- Python에서의 해결책

    - `decimal.Decimal`, `math.fsum()`, `round()`, `math.is_close()` 사용하기


    1) `decimal.Decimal`

    ```python
    import decimal
    decimal.Decimal('0.1') * 3 == decimal.Decimal('0.3')
    >>> True

    decimal.Decimal('0.3') + 2
    >>> Decimal('2.3')
    ```

    - 한계
    ```python
    decimal.Decimal(0.1 * 3)
    >>> Decimal('0.3000000000000000444089209850062616169452667236328125')
    ```


    2) `math.fsum()`
    ```python
    math.fsum([.1] * 10)
    >>> 1.0
    ```

    - 한계
    ```python
    math.fsum([.1, .2])
    >>> 0.30000000000000004
    ```


    3) `round()`
    ```python
    round(0.1 + 0.1 + 0.1, 10) == round(0.3, 10)
    >>> True
    ```

    - 한계
    ```python
    round(0.125, 2)
    >>> 0.12
    round(0.135, 2)
    >>> 0.14
    ```


    4) `math.is_close()`
    ```python
    import math
    math.isclose(0.1*3, 0.3)
    >>> True
    math.isclose(1.2-0.1, 1.1)
    >>> True
    math.isclose(0.1*0.1, 0.01)
    >>> True
    ```




### 참고문헌
https://wikidocs.net/106276
https://steemit.com/kr/@modolee/floating-point
https://docs.python.org/ko/dev/tutorial/floatingpoint.html