array_1 = [i*i for i in range(0, 20, 2)]
print(array)

array_2 = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array_2 if fruit != "초콜릿"]

print(output)