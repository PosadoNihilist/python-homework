import numpy as np

#1. Создать массив из 25 нулей +  
arr1_1 = [0 for i in range(25)]
arr1_2 = np.zeros(25)

#2. Создать массив из 10 единиц +
arr2_1 = [1 for i in range(10)]
arr2_2 = np.ones(10)

#3. Создать массив из 12 пятерок +
arr3_1 = [5 for i in range(12)]
arr3_2 = np.full(12, 5)

#4. Создать массив из целых чисел от 12 до 51 +
arr4_1 = [i+12 for i in range(40)]
arr4_2 = np.arange(12, 52)

#5. Создать массив из целых четных чисел от 12 до 51 +
arr5_1 = [(i+6)*2 for i in range(20)]
arr5_2 = np.arange(12, 52, 2)

#6. Создать матрицу 3х3 с числами от 1 до 9 +
arr6_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr6_2 = np.arange(1, 10).reshape(3, 3)

#7. Создать единичную матрицу 5х5 +
arr7_1 =  [[1 for i in range(5)] for i in range(5)]
arr7_2 = np.ones(25).reshape(5, 5)

#8. Создайте матрицу
arr8 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)

#9. Создайте матрицу 
arr9 = np.arange(1, 26).reshape(5, 5)

#10. Извлечь подматрицу из 9 задания
arr10 = arr9[2:, 1:]

#11. Написать код, который извлечет число 15 из 9 задания +
arr11_1 = arr9[2][4]
arr11_2 = arr9[2,4]

#12. Извлечь из 9 задания матрицу +
arr12_1 = arr9[[1, 2, 3], [1]]
arr12_2 = arr9[1:4, 1:2]

#13. Извлечь из 9 задания строку +
arr13_1 = arr9[4:]
arr13_2 = arr9[4:5, :]

#14. Извлечь две строки из 9 задания +
arr14_1 = arr9[3:]
arr14_2 = arr9[3:5, :]

# 15. Получить сумму всех значений из матрицы в задании 9 +

sum15_1 = arr9.sum()
sum15_2 = sum([element for row in arr9 for element in row])

#16. Получить сумму значений в колонках из матрицы в задании 9 +
sum16_1 = np.sum(arr9, 0)
sum16_2 = [sum(col) for col in zip(*arr9)]
print(sum16_2)