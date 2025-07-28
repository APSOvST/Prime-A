import numpy as np
import matplotlib.pyplot as plt

# 2. 建立一个一维数组 a 初始化为[4,5,6]
a = np.array([4, 5, 6])
print("2.1 a的类型:", type(a))
print("2.2 a的形状:", a.shape)
print("2.3 a的第一个元素:", a[0])
print("-" * 50)

# 3. 建立一个二维数组 b
b = np.array([[4, 5, 6], [1, 2, 3]])
print("3.1 b的形状:", b.shape)
print("3.2 b(0,0), b(0,1), b(1,1):", b[0, 0], b[0, 1], b[1, 1])
print("-" * 50)

# 4. 建立各种矩阵
a = np.zeros((3, 3), dtype=int)
b = np.ones((4, 5))
c = np.eye(4)
d = np.random.random((3, 2))
print("4.1 全0矩阵:\n", a)
print("4.2 全1矩阵:\n", b)
print("4.3 单位矩阵:\n", c)
print("4.4 随机数矩阵:\n", d)
print("-" * 50)

# 5. 建立数组 a
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("5.1 数组a:\n", a)
print("5.2 下标为(2,3)和(0,0)的元素:", a[2, 3], a[0, 0])
print("-" * 50)

# 6. 切片操作
b = a[0:2, 2:4]
print("6.1 数组b:\n", b)
print("6.2 b的(0,0)元素:", b[0, 0])
print("-" * 50)

# 7. 切片操作
c = a[1:3, :]  # 或 a[-2:, :]
print("7.1 数组c:\n", c)
print("7.2 c中第一行的最后一个元素:", c[0, -1])
print("-" * 50)

# 8. 建立数组a并输出特定元素
a = np.array([[1, 2], [3, 4], [5, 6]])
print("8. (0,0),(1,1),(2,0)元素:", a[[0, 1, 2], [0, 1, 0]])
print("-" * 50)

# 9. 建立矩阵a并输出特定元素
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
b = np.array([0, 2, 0, 1])
print("9. (0,0),(1,2),(2,0),(3,1)元素:", a[np.arange(4), b])
print("-" * 50)

# 10. 对特定元素加10
a[np.arange(4), b] += 10
print("10. 修改后的数组a:\n", a)
print("-" * 50)

# 11. 输出数据类型
x = np.array([1, 2])
print("11. x的数据类型:", x.dtype)
print("-" * 50)

# 12. 输出数据类型
x = np.array([1.0, 2.0])
print("12. x的数据类型:", x.dtype)
print("-" * 50)

# 13. 矩阵加法
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
print("13.1 x + y:\n", x + y)
print("13.2 np.add(x, y):\n", np.add(x, y))
print("-" * 50)

# 14. 矩阵减法
print("14.1 x - y:\n", x - y)
print("14.2 np.subtract(x, y):\n", np.subtract(x, y))
print("-" * 50)

# 15. 矩阵乘法
print("15.1 x * y (元素乘法):\n", x * y)
print("15.2 np.multiply(x, y):\n", np.multiply(x, y))
print("15.3 np.dot(x, y) (矩阵乘法):\n", np.dot(x, y))

# 非方阵示例
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2], [3, 4], [5, 6]])
print("15.4 非方阵矩阵乘法:\n", np.dot(a, b))
print("-" * 50)

# 16. 矩阵除法
print("16. x / y:\n", np.divide(x, y))
print("-" * 50)

# 17. 开方
print("17. x的开方:\n", np.sqrt(x))
print("-" * 50)

# 18. 点积
print("18.1 x.dot(y):\n", x.dot(y))
print("18.2 np.dot(x, y):\n", np.dot(x, y))
print("-" * 50)

# 19. 求和
print("19.1 总和:", np.sum(x))
print("19.2 列和:", np.sum(x, axis=0))
print("19.3 行和:", np.sum(x, axis=1))
print("-" * 50)

# 20. 求平均数
print("20.1 总平均:", np.mean(x))
print("20.2 列平均:", np.mean(x, axis=0))
print("20.3 行平均:", np.mean(x, axis=1))
print("-" * 50)

# 21. 矩阵转置
print("21. x的转置:\n", x.T)
print("-" * 50)

# 22. e的指数
print("22. e的指数:\n", np.exp(x))
print("-" * 50)

# 23. 最大值下标
print("23.1 全局最大下标:", np.argmax(x))
print("23.2 每列最大下标:", np.argmax(x, axis=0))
print("23.3 每行最大下标:", np.argmax(x, axis=1))
print("-" * 50)

# 24. 画图 y = x*x
x = np.arange(0, 100, 0.1)
y = x * x
plt.plot(x, y)
plt.title("y = x*x")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print("-" * 50)

# 25. 画正弦和余弦函数
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x, y_sin, label="sin(x)")
plt.plot(x, y_cos, label="cos(x)")
plt.title("Sine and Cosine functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()