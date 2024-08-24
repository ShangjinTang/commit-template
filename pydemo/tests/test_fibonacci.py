from pydemo.fibonacci import fibonacci


def test_fibonacci():
    # 测试生成空序列
    assert list(fibonacci(0)) == []

    # 测试生成长度为 1 的序列
    assert list(fibonacci(1)) == [0]

    # 测试生成长度为 2 的序列
    assert list(fibonacci(2)) == [0, 1]

    # 测试生成长度为 5 的序列
    assert list(fibonacci(5)) == [0, 1, 1, 2, 3]

    # 测试生成长度为 10 的序列
    assert list(fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
