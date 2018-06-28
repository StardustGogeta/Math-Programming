fc4 = function(x) {
	r = 1:floor(sqrt(x))
	factors = r[!x%%r]
	return(sort(c(factors,x/factors)))
}
