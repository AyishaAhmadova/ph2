def kv_var_mi(liste):
    for eded in liste:
        if (eded ** 2) in liste:
            print(f"{eded} nin kvadratı da siyahıda mövcuddur.")

mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
kv_var_mi(mylist)
#////////////////////////////
def tekrarlanmayan_elementler(liste):
    tekrarlanmayanlar = []
    for element in liste:
        if liste.count(element) == 1:
            tekrarlanmayanlar.append(element)
    return tekrarlanmayanlar

input_list = [-1, 1, 2, 2, 6, 7, 7, 'say']
print(tekrarlanmayan_elementler(input_list))
#////////////
def vurma(input_list):
    hasil = 1
    for element in input_list:
        if isinstance(element, (int, float)):
            hasil *= element
    return hasil

input_list = [-1, 1, 2, 2, 6, 7, 7]
print(vurma(input_list))
#//////////////////
def bolenler(sayi):
    return [x for x in range(1, sayi + 1) if sayi % x == 0]

verilmis_sayi = 12
print(f"{verilmis_sayi} reqemin bölenleri: {bolenler(verilmis_sayi)}")
#//////////////////////////
mylist = ['may', 'iyun', 'iyul']
ay_uzunluq = {ay: len(ay) for ay in mylist}
print(ay_uzunluq)
#////////////////////////////
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

def adlari_al(name_list):
    return [name.split()[0].lower() for name in name_list]

adlar = adlari_al(names)
print(adlar)
#////////////////////////
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
results = [(nums1[i] + nums2[i]) / 2 for i in range(len(nums1))]
print(results)