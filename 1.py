best_result = 0
result = int(input())

while result != -1:
    if result > best_result:
        best_result = result
    result = int(input())

print(best_result)