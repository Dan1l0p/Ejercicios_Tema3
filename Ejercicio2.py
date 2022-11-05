def mdet(matriz):
    return (matriz[0][0]*matriz[1][1]*matriz[2][2])+(matriz[1][0]*matriz[2][1]*matriz[0][2])-(matriz[0][2]*matriz[1][1]*matriz[2][0])-(matriz[0][1]*matriz[1][2]*matriz[2][0])

print(mdet([[3,2,3],[5,3,4],[9,1,7]]))