#!/usr/bin/env python3
"""
示例代码 - 用于代码审查测试
功能：计算斐波那契数列
"""

def fibonacci(n):
    """计算斐波那契数列的第n项"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

def main():
    """主函数"""
    print("斐波那契数列计算器")
    
    # 获取用户输入
    try:
        n = int(input("请输入要计算的项数: "))
        if n < 0:
            print("请输入非负整数")
            return
        
        # 计算并显示结果
        result = fibonacci(n)
        print(f"斐波那契数列第{n}项是: {result}")
        
        # 显示前n项
        print(f"前{n}项: ", end="")
        for i in range(n):
            print(fibonacci(i), end=" ")
        print()
        
    except ValueError:
        print("请输入有效的整数")

if __name__ == "__main__":
    main()