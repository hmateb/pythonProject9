a = -5
b = -5
c = -5
d = -5
while a < 0 or a > 255:
    a = int(input("Írja be az 1. oktet értékét az IP címből (0-255):"))
while b < 0 or b > 255:
    b = int(input("Írja be az 2. oktet értékét az IP címből (0-255):"))
while c < 0 or c > 255:
    c = int(input("Írja be az 3. oktet értékét az IP címből (0-255):"))
while d < 0 or d > 255:
    d = int(input("Írja be az 4. oktet értékét az IP címből (0-255):"))
print("A",a,".", b,".", c,".", d, "IPV4 cím kettes számrendszerben kifejezve=")
While: True
szam2=szam2-a
for i in range(7,-1,-1):
 if 2**i<=szam2:
     print("1")
else:
    print("0")