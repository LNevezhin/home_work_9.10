def sum_of_pairs(L1, L2):
    sum_of_pairs = []
    try:
        for i in range(len(L1)):
            sum_of_pairs.append(L1[i] + L2[i])
        print("sumOfPairs = ", sum_of_pairs)
    except IndexError as index_err:
        print("Проверьте длину списков\n", index_err)
    except TypeError as type_err:
        print("Проверьте правильность данных\n", type_err)


try:
    L1 = [1, 2, 3, 4]
    L2 = [3, 2, 1]

    sum_of_pairs(L1, L2)

    L1 = [1, 2, "3"]
    L2 = [3, 2, 1]

    sum_of_pairs(L1, L2)

    L1 = [1, 2, 3]
    L2 = [3, 2, i]

    sum_of_pairs(L1, L2)

except NameError as name_err:
    print("Проверьте корректность данных\n", name_err)
