def totalSubscriptions(n, english, m, french):
    return len(english.symmetric_difference(french))

if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))
    m = int(input())
    french = set(map(int, input().split()))
    print(totalSubscriptions(n, english, m, french))