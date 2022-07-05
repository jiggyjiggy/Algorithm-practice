def complex_number_multiply(a, b):
    # 여기에 코드를 작성해주세요.
    a_real_num = int(a.split('+')[0])
    a_imagenary_num = int(a.split('+')[1].rstrip("i"))

    b_real_num = int(b.split('+')[0])
    b_imagenary_num = int(b.split('+')[1].rstrip("i"))

    # real_num * real_num = real_num
    target1 = (a_real_num * b_real_num)
    # imagenary * imagenary = real_num
    target2 = -(a_imagenary_num * b_imagenary_num)

    result_real_num = str(target1 + target2)

    # real_num * imagenary = imagenary
    target3 = (a_real_num * b_imagenary_num) + (a_imagenary_num * b_real_num)

    result_imagenary_num = str(target3) + "i"

    result = result_real_num + "+" + result_imagenary_num

    return result