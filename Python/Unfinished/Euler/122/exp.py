cache = dict()
def m(k, opts = [1]):
    if k in opts: return 1
    potOpts = list(opt for opt in opts if opt <= k)
    s = str(k)+str(potOpts)
    if s in cache: return cache[s]
    ret = min(m(k-opt, opts + [opts[-1] + opt]) for opt in potOpts)
    cache[s] = ret
    #print(k, opts, potOpts, ret)
    return ret + 1

#for n in range(1, 21):
#    print(n, m(n))
