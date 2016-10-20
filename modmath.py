def gcd(a,b):
    if a>b:
        (m,x,y)=gcd(b,a)
        return (m,y,x)
    if a ==0:
        return (b,0,1)
    else:
        (x,y,z) = gcd(b%a,a)
        return (x, z-(b/a)*y,y)
        
def mult_mod_inverse(a,m):
    (x,y,z) = gcd(a,m)
    if (x==1):
        return y
    else:
        raise Exception("no inverse")

def prime_sieve(m):
    l = range(2,m)
    primes = list()
    while len(l)>0:
        p = l[0]
        
        primes.append(p)
        l = [z for z in l if z%p !=0]
    return primes
    
def factor(m):
    primes=prime_sieve(int(m**.5))
    factors=list()
    for p in primes:
        while m%p ==0:
            factors.append(p)
            m = m/p
    return factors
    
def totient(m):
    p = [1-1.0/z for z in set(factor(m())]
    	return m*prod(p)
    	
    
