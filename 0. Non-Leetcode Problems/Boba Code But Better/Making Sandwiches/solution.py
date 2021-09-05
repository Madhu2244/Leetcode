def main():
    q = int(input())
    for i in range (q):
        data = input().split()
        data = list(map(int,data))
        data[0] = data[0] // 2
        print(sum(data)//3)
    
if __name__ == '__main__':
    main()
