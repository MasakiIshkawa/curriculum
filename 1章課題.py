# int型のリストdataを作成し、値を1,3,5,7で初期化
data = [1,3,5,7]

for i in data[:4]:
    print(i**2)


for j in range(1,8,2):
    print(j**2)



all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
    if place in get_place :
        print(place + "のチケットが当選しました！")
    elif place in wait_place:
        print(place + "のチケットは結果待ち")
    else:
        print(place + "のチケットは落選しました")

list = get_place + wait_place

list_0 = list[0]
list_1 = list[1]
list_2 = list[2]

print('{}と{}と{}のチケットが当選しました！'.format(list_0,list_1,list_2))






















