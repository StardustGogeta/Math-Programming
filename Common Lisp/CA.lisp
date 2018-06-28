(DEFUN CA (a)
	(format t "The coterminal angles closest to 0° are ~d° and ~d°." (mod a 360) (- (mod a 360) 360)))