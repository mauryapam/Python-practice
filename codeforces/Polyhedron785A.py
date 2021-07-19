n=int(input())
lst = []
for p in range(n):
    ply=input()
    lst.append(ply)
poly={"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
faces=0
for i in lst:
    if i in poly.keys():
        faces+=poly[i]
print(faces)
      
