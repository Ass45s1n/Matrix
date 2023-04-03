class Matrix:
    def __init__(self,m):
        self.m = m

    @staticmethod
    def define():
        nor = int(input('Enter No of Rows: '))
        noc = int(input('Enter No of Columns: '))
        m = []
        for i in range(nor):
            r = []
            for j in range(noc):
                value = float(input(f'Enter Value of Element {i+1},{j+1}: '))
                r.append(value)
            m.append(r)
        return m

    def display(self,m):
        print()
        for i in m:
            for j in i:
                print('%10.3f'%j,end=' ')
            print()
        print()

    def __add__(self,other):
        if len(self.m) == len(other.m) and len(self.m[0]) == len(other.m[0]):
            addmat = []
            for i in range(len(self.m)):
                r = []
                for j in range(len(self.m[0])):
                    s = self.m[i][j] + other.m[i][j]
                    r.append(s)
                addmat.append(r)
            return self.display(addmat)
        else:
            return print('Addition is Not Possible')

    def __sub__(self,other):
        if len(self.m) == len(other.m) and len(self.m[0]) == len(other.m[0]):
            submat = []
            for i in range(len(self.m)):
                r = []
                for j in range(len(self.m[0])):
                    s = self.m[i][j] - other.m[i][j]
                    r.append(s)
                submat.append(r)
            return self.display(submat)
        else:
            return print('Subtraction is Not Possible')
    
    def __mul__(self,other):
        if len(self.m[0]) == len(other.m):
            mulmat = []
            for x in range(len(self.m)):
                r = []
                for y in range(len(other.m[0])):
                    s = 0
                    for z in range(len(other.m)):
                        s += self.m[x][z]*other.m[z][y]
                    r.append(s)
                mulmat.append(r)
            return self.display(mulmat)
        else:
            return 'Multiplication is Not Possible'

    def __truediv__(self,other):
        if len(self.m) == len(other.m) and len(self.m[0]) == len(other.m[0]):
            divmat = []
            for i in range(len(self.m)):
                r = []
                for j in range(len(self.m[0])):
                    try:
                        s = self.m[i][j] / other.m[i][j]
                    except Exception as a:
                        return print('Error:',a)
                    r.append(s)
                divmat.append(r)
            return self.display(divmat)
        else:
            return print('Division is Not Possible')

    def determinant(self):
        a1 = 1
        a2 = 1
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                if i == j:
                    for x in range(len(self.m)):
                        for y in range(len(self.m[x])):
                            if x == y:
                                a1 = a1 * self.m[x][y]
                    if a1 == 0:
                        return a1
                    ele = self.m[i][j]
                    for r in range(len(self.m[0])):
                            self.m[i][r] = self.m[i][r] / ele
                    for r in range(len(self.m)):
                        if r != i:
                            multiply = -self.m[r][j]
                            for c in range(len(self.m[i])):
                                self.m[r][c] = self.m[r][c] + (multiply * self.m[i][c])
                    a2 = a2 * ele
        return a2

    def transpose(self):
        trans = []
        for i in range(len(self.m[0])):
            r = []
            for j in range(len(self.m)):
                b = self.m[j][i]
                r.append(b)
            trans.append(r)
        return self.display(trans)

    def __power(self,b,p):
        if p==0:
            return 1
        else:
            return b*self.__power(b,p-1)

    def __red_mat(self,a,b):
        d = []
        for i in range(len(self.m)):
            r = []
            for j in range(len(self.m[0])):
                if i == a or j == b:
                    continue
                r.append(self.m[i][j])
            if r != []:
                d.append(r)
        return Submatrix(d)

    def adjoint(self):
        res = []
        for i in range(len(self.m)):
            r = []
            for j in range(len(self.m[0])):
                val = self.__power(-1,(i+1)+(j+1)) * self.__red_mat(i,j).determinant()
                r.append(val)
            res.append(r)
        res = Matrix(res)
        return res.transpose()

class Submatrix(Matrix):
    def __init__(self,m):
        self.m = m


# m1 = Matrix.define()
# m1 = Matrix(m1)
# print(m1.adjoint())
a = [[4,5,3],[2,4,1]]
b = [[3,1,5],[1,2,3]]
c = Matrix(a)
d = Matrix(b)
e = c - d