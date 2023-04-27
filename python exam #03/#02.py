x = input("Sizda kompyuter bormi (Ha / Yo`q)")
if x.lower() == "ha":
    ram = int(input("Kompyuteringizni tezkor xotirasini o`lchamini kiriting: "))
    disk = int(input("Xotirasini kiriting (Gb): "))
    display = int(input("Ekram o`lchami Nechchi duyum: "))
    razyad = int(input("Kompyuteringiz razyadini kiriting: "))

    if ram >= 8 and disk >= 50 and display > 20 and razyad == 64:
        print("Kompyuteringiz Python dasturlash tilini ko`tara olishi aniq. va sizga maslaxat Visual Studio Code dasturini o`rnating")
    elif ram < 8 and ram >= 4 and disk < 50 and disk > 30:
        print("Kompyuteringiz Python dasturlash tilini ko`taradi lekin ozgina qiynalishi mumkin va siz python dasturini o`zidan foydalaning")   
    elif ram < 4 and disk < 30 and disk > 10:
        print("Kompyuteringiz Python dasturlash tilini ko`tara oladi.")
else:
    print("Kompyuter dasturlash tilini o`rganish uchun zarur.")