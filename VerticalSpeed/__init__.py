import string

angle = 1


def simbologia(label):
    res = 0
    value = [0, 0, 0, 0]
    list(reversed(label))
    """att = label[14:28]"""
    if label[14] == '1':
        value[3] = value[3] + 1
    if label[15] == '1':
        value[3] = value[3] + 2
    if label[16] == '1':
        value[3] = value[3] + 4
    if label[17] == '1':
        value[3] = value[3] + 8
    res += value[3]

    if label[18] == '1':
        value[2] = value[2] + 1
    if label[19] == '1':
        value[2] = value[2] + 2
    if label[20] == '1':
        value[2] = value[2] + 4
    if label[21] == '1':
        value[2] = value[2] + 8
    res += value[2] * 10

    if label[22] == '1':
        value[1] = value[1] + 1
    if label[23] == '1':
        value[1] = value[1] + 2
    if label[24] == '1':
        value[1] = value[1] + 4
    if label[25] == '1':
        value[1] = value[1] + 8
    res += value[1] * 100

    if label[26] == '1':
        value[0] = value[0] + 1
    if label[27] == '1':
        value[0] = value[0] + 2
    if label[28] == '1':
        value[0] = value[0] + 4
    res += value[0] * 1000

    res = res / 2
    return res


def negativ(label, res):
    if label[29:30] == ['1', '1']:
        res = res * (-1)
    return res


inf = "011010001000000000PPPP0000001000"
inf = list(reversed(inf))

if inf[0:7] == ['0', '0', '0', '1', '0', '0', '0']:
    angle = simbologia(inf)
    angle = negativ(inf, angle)

print(inf)
print(inf[29:30])
print(inf[29])
print(inf[30])
print(angle)
