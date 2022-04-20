def is_valid(string):
    # 여기에 코드를 작성해주세요.

    memo = [0] * 6

    if len(string) == 1:
        return False

    for sdx, s in enumerate(string):

        if s == '(' and string[sdx + 1] not in ']}':
            memo[0] += 1
        if s == ')':
            memo[1] += 1
        if s == '[' and string[sdx + 1] not in ')}':
            memo[2] += 1
        if s == ']':
            memo[3] += 1
        if s == '{' and string[sdx + 1] not in ')]':
            memo[4] += 1
        if s == '}':
            memo[5] += 1

    if (memo[0] == memo[1]) and (memo[2] == memo[3]) and (memo[4] == memo[5]):
        return True
    else:
        return False


is_valid("()[]{}")
