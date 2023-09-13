def display(theme):
    """输出本章主题"""
    print(f"Theme is{theme} ")
display("函数")
def favorite(book):
    print(f"One of my favorie books is {book.title()} ")
favorite("Alice in Wonderland")#此处赋值
favorite("heart flow")
def people_name(first_name,last_name):
    full_name=f"{first_name}\t{last_name}"
    return full_name#使这两行调回函数格式使用
musician=people_name("lin","cheng")
print(musician)
def city_copenration(city_name,belonng_contry):
    full_information=f"{city_name} {belonng_contry}"
    return full_information.title()
music=city_copenration("washington","America")
music2=city_copenration("Beijing","China")
music3=city_copenration("xini","Austrian")
print(f"{music}\n,{music3}\n,{music2}\n")
def make_abulm(singer,abulm,number="none"):
    content={"S":singer,"A":abulm}
    if number:
       content['number']=number#?此处number是make abulm中的
    return content#返回cntent中，输出的是contet这个字典
music4=make_abulm("Jay","fantacy",11)
print(music4)
def make_abulm2(singer,abulm,number2="none"):
   content2 = {"S": singer, "A": abulm}
   if number2:
      content2['number'] = number2  # ?此处number是make abulm中的
   return content2  # 返回cntent中，输出的是contet这个字典
while True:
    print("please input singer's name.")
    hee=input("singer's name:")
    if hee=="q":
        break
    print(("please input abulm's name."))
    hll=input("song's name:")
    if hll=="q":
        break
music5=make_abulm2("hee","hll",2)