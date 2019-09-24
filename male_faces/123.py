import sys
from os import rename, listdir
# 현재 위치의 파일 목록
files = listdir('.') # 파일명에 번호 추가하기
count = 0
for name in files:
# 파이썬 실행파일명은 변경하지 않음
    if sys.argv[0].split("\\")[-1] == name:
        continue

    new_name = name.replace(".", "{0:03d}.".format(count))
    rename(name,new_name)
    count += 1

