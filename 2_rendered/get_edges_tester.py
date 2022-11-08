surfaces = [
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    ]

test = set()

for surface in surfaces:
    for i in range(len(surface)):
        test.add(tuple(sorted((surface[i], surface[(i+1)%(len(surface))]))))

print(len(list(test)))