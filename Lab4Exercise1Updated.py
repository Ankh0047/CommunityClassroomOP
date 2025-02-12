spring = "Хавар болж цэцэгс дэлгэрлээ."
summer = "Зун болж халуун боллоо."
autumn = "Намар болж навчис уналаа."
winter = "Өвөл болж цас орлоо."

print("Улирлаа оруулна уу. 1=Хавар, 2=Зун, 3=Намар, 4=Өвөл")

def my_function(season):
    if season == 1:
        print(spring)
    elif season == 2:
        print(summer)
    elif season == 3:
        print(autumn)
    elif season == 4:
        print(winter)
    else:
        print("Таны оруулсан улирал буруу байна.")

user_input = int(input())
my_function(user_input)