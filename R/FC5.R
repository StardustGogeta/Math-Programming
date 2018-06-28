library(bit64)
# bit64 is a required package, to allow support for large numbers
# Large numbers must be placed in quotes to maintain precision!

options('scipen'=30)
findFactor = function(x) {
	r = 2:floor(sqrt(x))
	f = r[!x%%r][1]
	if (is.na(f)) return (x)
	else return (f)
}

fc5 = function(x) {
	n = as.integer64(x)
	factors = 1
	while (n>1) {
		f = findFactor(n)
		n = n/f
		factors = unique(c(factors,f*factors))
	}
	return(sort(factors))
}

#fc5("100000000000")

