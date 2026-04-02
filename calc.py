def main():
    print("Let's implement division. Type two numbers for x and y")
    
    x = int(input("x > "))
    y = int(input("y > "))
    
    # 0으로 나눌 경우 여기서 TypeError가 발생할 수 있습니다.
    print("%d / %d = %0.3f" % (x, y, divide(x, y)))
    
    
def add(a, b):
    return a + b
    
    
# TODO: divide() 함수 정의
def divide(a, b):
    if b == 0:
        print("Error: cannot divide by zero.")
        # 아무것도 return 하지 않음 (기본적으로 None이 반환됨)
    else:
        return a / b
        

if __name__ == "__main__":
    main()