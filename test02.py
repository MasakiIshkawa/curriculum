while True:
    my_string = 'Hello'
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        number = int(input('選択してください。: '))

        # 問①：if文を用いて、以下の画像のように処理されるように記述しましょう。
        if number == 1:
            print('↓')
            int('hoge')
            
        elif number ==2:
            print('↓')
            print(my_string[9])
            
        elif number ==3:
            print('↓')
            print('例外を発生させませんでした') 
            print('↓')
            print('もう一度選択しましょう')
        # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。
        else:
            print('↓')
            print('終了します')
            break
    except ValueError as e:
        print('ValueError')
        print(e.args)
        print('↓')
        print('もう一度選択しましょう')
    except IndexError as e:
        print('IndexError')
        print(e.args)
        print('↓')
        print('もう一度選択しましょう')

print('↓')
print('無限ループを終了します')

