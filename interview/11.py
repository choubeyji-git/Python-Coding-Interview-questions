

s1 = '{}[]()'
s2 = '{}('
s3 = '{[()]}'


def balPar(s):
    for i in s:
        if ('{' and '}') or ('[' and ']') or ('(' and ')') in s:
            return True


print(balPar(s3))