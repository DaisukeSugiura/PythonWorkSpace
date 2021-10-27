fruits = ['バナナ','リンゴ','オレンジ']
while True:
    a = input("果実をカタカナで入力してください：")
    if a == '':
        break


    if a in fruits:
        print(a + "は、知っています！")
    else:
        print(a + "は、知りませんでした。覚えておきます。")
        fruits.append(a)

print('知っている果物')
print(fruits)