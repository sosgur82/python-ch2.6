# print() 연습
import sys

print(1)
print('hello', 'world', sep=' ', end='\n')
print('hello python')
x = 0.2
a = 'hello'

print(x, a)
print(str(x) + ":" + a)
print(x, a, sep=":")
print('{0}:{1}'.format(x, a))

# 기본적으로 print() 호출은 아래와 같다
print(sep=' ', end='\n')

# file 파라미터
print('Hello Wolrd', file=sys.stdout)
print('Error: Hello Wolrd', file=sys.stderr)

#file로 출력
f = open('hello.txt', 'w')
print('Hello World',file=f)

# 참고
sys.stdout.write('hello world')
