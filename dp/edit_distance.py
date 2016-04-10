class EditDistance:

    def __init__(self):
        self.f = None

    def min_distance(self, s1, s2):
        self.f = [[float('inf')]*(len(s2)+1) for i in range(len(s1)+1)]
        f = self.f
        for i in range(len(s1)+1):
            f[i][0] = i
        for i in range(len(s2)+1):
            f[0][i] = i
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                f[i][j] = min(f[i][j-1]+1,f[i-1][j]+1,f[i-1][j-1]) if s1[i-1]==s2[j-1] else min(f[i][j-1]+1,f[i-1][j]+1,f[i-1][j-1]+1)
        return f[len(s1)][len(s2)]

    def retrieve_edits(self):
        f = self.f
        path = []
        i = len(f)-1
        j = len(f[0])-1
        while i and j:
            if j-1>=0 and f[i][j-1]+1==f[i][j]:
                j -= 1
                path.append('a{}'.format(i))
            elif i-1>=0 and f[i-1][j]+1==f[i][j]:
                i -= 1
                path.append('d{}'.format(i))
            else:
                i -= 1
                j -= 1
                if f[i][j] < f[i+1][j+1]:
                    path.append('r{}'.format(i))
        return reversed(path)


s = EditDistance()
s.min_distance('mart', 'karma')
print('mart => karma')
for row in s.f:
    print(row)
print(list(s.retrieve_edits()))
