import numpy as np

# 1. Massiv yaratish (Array Creation)
# 1 dan 10 gacha bo'lgan sonlardan iborat massiv
massiv = np.array([10, 20, 30, 40, 50])
print("Asl massiv:", massiv)

# 2. Matematik amallar
# Har bir elementga 5 ni qo'shish
print("Har bir elementga +5:", massiv + 5)

# Har bir elementni kvadratga oshirish
print("Elementlar kvadrati:", massiv ** 2)

# 3. Statistik hisob-kitoblar
print("-" * 30)
print("Elementlar yig'indisi:", np.sum(massiv))
print("O'rta arifmetik qiymat (Mean):", np.mean(massiv))
print("Eng katta element (Max):", np.max(massiv))
print("Standart og'ish (Standard Deviation):", np.std(massiv))

# 4. Ko'p o'lchamli massivlar (Matrix) bilan ishlash
# 2x3 o'lchamli matritsa yaratish
matritsa = np.array([[1, 2, 3], [4, 5, 6]])
print("-" * 30)
print("2x3 Matritsa:\n", matritsa)
print("Matritsa shakli (shape):", matritsa.shape)

# 5. Tasodifiy sonlar yaratish
# 0 va 1 oralig'ida 3 ta tasodifiy son
random_sonlar = np.random.rand(3)
print("-" * 30)
print("Tasodifiy sonlar:", random_sonlar)
