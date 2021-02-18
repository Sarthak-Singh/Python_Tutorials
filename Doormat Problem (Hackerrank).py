a = list(input().split())
for x in range(int(a[0])//2):
    print('-'*((int(a[1])-3*(2*x+1))//2) + '.|.'*(2*x+1) + '-'*((int(a[1])-3*(2*x+1))//2))
print('-'*((int(a[1])-7)//2) + 'WELCOME' + '-'*((int(a[1])-7)//2))
x = int(a[0])//2 - 1
while x >= 0:
    print('-'*((int(a[1])-3*(2*x+1))//2) + '.|.'*(2*x+1) + '-'*((int(a[1])-3*(2*x+1))//2))
    x -= 1
