import sys

input, vertices_in, surfaces_in = sys.argv, [], []

if len(input)<2: print('provide an object file'); quit()
elif len(input)>2: print('provide ONE file only'); quit()

lines = open(sys.argv[1], 'r').readlines()
counts = lines[0].split(","); vertices_count = int(counts[0])

for vertex_raw in lines[1:vertices_count+1]:
    vertex = [float(v) for v in vertex_raw.strip().split(",")[1:]]
    vertex.append(1)
    vertices_in.append(tuple(vertex))

for surface_raw in lines[vertices_count+1:]:
    surface = [int(s)-1 for s in surface_raw.strip().split(",")]
    surfaces_in.append(tuple(surface))

print('%s\n%s' %(vertices_in, surfaces_in))

def test(k):
    a, b = 1+1, 3+5
    return a, b

print(test(2)[0])
