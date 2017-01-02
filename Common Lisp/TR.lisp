(DEFUN TR (deg a)
	(if (= 1 deg) (setq a (* a (/ pi 180)))
		(progn
			(write-line "In terms of pi? (Y=1)")
			(if (= 1 (read)) (setq a (* a pi)))))
	(format t "sin=~,3f, cos=~,3f, tan=~,3f,~%csc=~,3f, sec=~,3f, cot=~,3f"
			(sin a) (cos a) (tan a) (/ 1 (sin a)) (/ 1 (cos a)) (/ 1 (tan a))))		