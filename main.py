def main():
    print('欢迎使用我的软件！')
    print('版本: 1.0')

def calculate_sum(a, b):
    '''计算两个数的和'''
    return a + b

if __name__ == '__main__':
    main()
    result = calculate_sum(10, 20)
    print(f'10 + 20 = {result}')
