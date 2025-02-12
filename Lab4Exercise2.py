first_store = "Бамбарууш" 
second_store = "Жимсхэн" 
third_store = "Fruits"

print(first_store + " дэлгүүрийн хувьд: ")
a = int(input("Жилд зарагдсан алимны тоо: "))
b = int(input("Алим бүрийн жижэглэнгийн үнэ: "))
c = int(input("Жилд зарагдсан жүржийн тоо: "))
d = int(input("Жүрж бүрийн жижэглэнгийн үнэ: "))

x = a * b + c * d

print(second_store + " дэлгүүрийн хувьд: ")
e = int(input("Жилд зарагдсан алимны тоо: "))
f = int(input("Алим бүрийн жижэглэнгийн үнэ: "))
g = int(input("Жилд зарагдсан жүржийн тоо: "))
h = int(input("Жүрж бүрийн жижэглэнгийн үнэ: "))

y = e * f + g * h

print(third_store + " дэлгүүрийн хувьд: ")
i = int(input("Жилд зарагдсан алимны тоо: "))
j = int(input("Алим бүрийн жижэглэнгийн үнэ: "))
k = int(input("Жилд зарагдсан жүржийн тоо: "))
l = int(input("Жүрж бүрийн жижэглэнгийн үнэ: "))

z = i * j + k * l

print(first_store + " дэлгүүрийн орлого: " + str(x))
print(second_store + " дэлгүүрийн орлого: " + str(y))
print(third_store + " дэлгүүрийн орлого: " + str(z))