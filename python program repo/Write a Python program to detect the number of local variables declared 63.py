def count_local_variables():
    variable1 = 10
    variable2 = 'Hello'
    variable3 = [1, 2, 3]
    variable4 = True

    count = 0
    local_variables = list(locals().keys())
    for variable in local_variables:
        if variable != 'count':
            count += 1

    return count

result = count_local_variables()
print("Number of local variables:", result)
