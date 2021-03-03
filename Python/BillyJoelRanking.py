import math

songs = [
    "Piano Man",
    "The Longest Time",
    "Elvis Presley Boulevard",
    "Uptown Girl",
    "Tell Her About It",
    "The Downeaster Alexa",
    "My Life",
    "Shameless",
    "State of Grace",
    "This Is the Time",
    "This Night",
    "Until the Night",
    "Get It Right the First Time"
]

def compare(x, y):
    if not x:
        return 1
    if not y:
        return 0
    # Type [q] to select left or [e] to select right
    print(f"{x}\t\t or \t\t{y}?")
    if input("") == "q":
        return 0
    else:
        return 1

def merge(a, b):
    """ Returns list with a and b merged together. """
    i = 0
    j = 0
    ret = []
    while i < len(a) and j < len(b):
        L = a[i]
        R = b[j]
        cmp = compare(L, R)
        if cmp:
            ret.append(R)
            j += 1
        else:
            ret.append(L)
            i += 1
    while i < len(a):
        ret.append(a[i])
        i += 1
    while j < len(b):
        ret.append(b[j])
        j += 1
    return ret

def isPow2(n):
    log = math.log2(n)
    return n == 2 ** round(log)

def mergeSort(ls):
    #print(ls)
    if len(ls) < 2:
        return ls
    while not isPow2(len(ls)):
        ls.append(0)
        #print("ADDING")
    ln = len(ls)
    left = ls[:ln//2]
    right = ls[ln//2:]
    return list(filter(lambda x: x, merge(mergeSort(left), mergeSort(right))))

print(mergeSort(songs))
# ['Until the Night', 'My Life', 'The Longest Time', 'Elvis Presley Boulevard', 'Piano Man', 'Uptown Girl', 'The Downeaster Alexa', 'Tell Her About It', 'This Is the Time', 'This Night', 'State of Grace', 'Shameless', 'Get It Right the First Time']
