import  re

python='it was developed by guido van rossum, since 1989'
d=re.match('it ',python)

if d:
    print('It is matched')

else:
    print('not matched')

