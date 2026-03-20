#!/usr/bin/env python3
"""
改进版代码 - 添加缓存、类型提示和测试
功能：计算斐波那契数列（带缓存优化）
"""

from typing import Dict

# 缓存字典，避免重复计算
_fib_cache: Dict[int, int] = {0: 0, 1: 1}

def fibonacci(n: int) -> int:
    """
    计算斐波那契数列的第n项（带缓存优化）
    
    Args:
        n: 要计算的项索引（从0开始）
    
    Returns:
        斐波那契数列的第n项
    
    Raises:
        ValueError: 如果n为负数
    """
    if n < 0:
        raise ValueError("n必须为非负整数")
    
    # 检查缓存
    if n in _fib_cache:
        return _fib_cache[n]
    
    # 计算并缓存结果
    result = fibonacci(n - 1) + fibonacci(n - 2)
    _fib_cache[n] = result
    return result

def fibonacci_iterative(n: int) -> int:
    """
    迭代方式计算斐波那契数列（避免递归深度限制）
    
    Args:
        n: 要计算的项索引
    
    Returns:
        斐波那契数列的第n项
    """
    if n < 0:
        raise ValueError("n必须为非负整数")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def get_fibonacci_sequence(n: int) -> list[int]:
    """
    获取斐波那契数列的前n项
    
    Args:
        n: 要获取的项数
    
    Returns:
        斐波那契数列前n项的列表
    """
    return [fibonacci(i) for i in range(n)]

def main() -> None:
    """主函数"""
    print("斐波那契数列计算器（改进版）")
    print("=" * 40)
    
    try:
        # 获取用户输入
        n = int(input("请输入要计算的项数: "))
        
        if n < 0:
            print("错误：请输入非负整数")
            return
        
        # 使用迭代方法计算（避免递归问题）
        result = fibonacci_iterative(n)
        print(f"\n斐波那契数列第{n}项是: {result:,}")
        
        # 显示前n项（限制显示数量）
        max_display = min(n, 20)  # 最多显示20项
        sequence = get_fibonacci_sequence(max_display)
        print(f"\n前{max_display}项: {' '.join(map(str, sequence))}")
        
        if n > 20:
            print(f"（共{n}项，仅显示前20项）")
        
        # 性能对比
        print(f"\n性能信息：")
        print(f"- 缓存中已存储 {len(_fib_cache)} 个结果")
        
    except ValueError as e:
        print(f"输入错误: {e}")
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"发生未知错误: {e}")

def run_tests() -> None:
    """运行简单测试"""
    test_cases = [
        (0, 0),
        (1, 1),
        (5, 5),
        (10, 55),
        (20, 6765)
    ]
    
    print("运行测试...")
    for n, expected in test_cases:
        result = fibonacci(n)
        status = "✅" if result == expected else "❌"
        print(f"{status} fibonacci({n}) = {result} (期望: {expected})")

if __name__ == "__main__":
    # 运行测试
    run_tests()
    print()
    
    # 运行主程序
    main()