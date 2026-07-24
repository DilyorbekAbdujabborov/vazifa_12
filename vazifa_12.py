talaba = "Dilyorbek"
print(talaba[0]) # D 
print(talaba[-1]) # k 
print(len(talaba)) 

# teskari aylantirish
print(talaba[::-1])
print(talaba[0:3])
print(talaba[4:])

# F-string
yosh = 17 
gpa = 4.5
data = f"Talaba: {talaba}, {yosh} yosh, GPA {gpa:.2f}"
print(data)

# format() va %
print("Talaba: {}, {}-yil".format(talaba, 2026-17))
print("Talaba: %s, %d-yil" % (talaba, 2026-17))

# Escape
yol = r"C:\Users\Dilyorbek\documents\vazifa.txt"
print(yol)

# Str methods

# full_name = "        Abdujabborov    Dilyorbek      "
full_name = input("To'liq ismingnizni kiriting: ")
print(full_name.title()) 

authors = "Ali Bekzod Bekmirza Mirzabek"
print(authors.split())
print(", ".join(authors.split()))

kitob = "O'tgan kunlar"
print(kitob.replace("kunlar", "oylar"))




