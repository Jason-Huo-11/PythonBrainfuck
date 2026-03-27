crr = 0
save = []
def chk():
    x = unit[crr]
    if x == -1:
        unit[crr] = 255
    elif x == 256:
        unit[crr] = 0
def grm(i):
    global crr
    s = ins[i]
    if s == '-':
        unit[crr] -= 1
        chk()
    elif s == '+':
        unit[crr] += 1
        chk()
    elif s == '<':
        crr -= 1
    elif s == '>':
        crr += 1
    elif s == ',':
        ipt = input()
        try:
            unit[crr] = int(ipt)
            chk()
        except ValueError:
            unit[crr] = int(ord(ipt))
            chk()
    elif s == '.':
        print(chr(unit[crr]), end='')
    elif s == '[':
        save.append(i)
    elif s == ']':
        if unit[crr] != 0:
            for x in range(save[len(save) - 1], i + 1):
                grm(x)
flag = False
while True:
    unit = [0 for i in range(30000)]
    ins = input()
    for i in range(len(ins)):
        if flag and ins[i] != ']':
            continue
        if ins[i] == '[':
            flag = True
        if ins[i] == ']':
            flag = False
        grm(i)
    print()