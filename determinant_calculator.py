def det_calc(matrix, mul=1):

    width = len(matrix)
    if width == 1:
        return mul * (matrix[0][0])
    else:
        sign = -1
        answer = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            answer = answer + mul * det_calc(m, sign * (matrix[0][i]))
    return answer