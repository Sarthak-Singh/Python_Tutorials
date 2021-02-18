def num_checker(num_list):
    if num_list[0] == num_list[len(num_list)-1]:
        return True
    else:
        return False


print(num_checker([10, 20, 30, 40, 10]))
