(DEFUN BC (orig base1 base2)
	(write-to-string (parse-integer (write-to-string orig) :radix base1) :base base2))