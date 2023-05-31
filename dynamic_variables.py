# 변수 동적 할당
for i in range(1, 3):
globals()['variable_name{}'.format(i)] = 0

