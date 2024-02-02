# slice
name = "pramod" # Index : P=0, r=1, a=2, m=3, o=4, d=5
                #Length : P=1, r=2. a=3. m=4, o=5, d=6
print(name)
print("-------")

# slice
print(name[0:2]) # it means look from index 0 and select Index 2-1 letter i,e output : pr

print("-------")

print(name[0:3]) # it means look from index 0 and select Index 3-1 letter i,e output : pra

print("-------")

print(name[0:6]) # it means look from index 0 and select Index 6-1 letter(we dont have index 6) i,e output : pramod

print("-------")

print(name[0:7]) # it means look from index 0 and select Index 7-1 letter(we dont have index 6) i,e output : pramod

print("-------")

print(name[0:6]) # it means look from index 0 and select Index 6-1 letter(we dont have index 6) i,e output : pramod