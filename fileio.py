#write test

f=open('test.txt', 'w', encoding='utf-8')
writesize = f.write('안녕하세요 \n김계현입니다.')
print(writesize)
f.close()


# read test
f = open('test.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()

# copy binary file
f_src = open('python.png', 'rb')
data = f_src.read()
f_src.close()


f_dest  = open('python2.png', 'wb')
f_dest.write(data)
f_dest.close()

