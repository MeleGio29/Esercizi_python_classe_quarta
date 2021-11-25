import math
quadrati_perfetti = [k for k in range(1001) if math.sqrt(k) % 1 == 0]

print(quadrati_perfetti)