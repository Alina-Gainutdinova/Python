def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    else:
        if a + b > c and c + a > b and b + c > a:
            return True
        
def main():
    x = int(input('Введите 1 сторону треугольника: '))
    y = int(input('Введите 2 сторону треугольника: '))
    z = int(input('Введите 3 сторону треугольника: '))      
    if triangle(x, y, z) == True:
        print('Треугольник возможен')
    else:
        print('Треугольник не возможен')
main()