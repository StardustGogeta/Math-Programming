(DEFUN LIC (coords)
	(when (= 0 coords)
		(write-line "Enter first slope and y-intercept, separated by spaces:")
		(setq s (read) y1 (read))
		(write-line "Enter second slope and y-intercept, separated by spaces:")
		(setq s2 (read) y2 (read)))
	(when (= 1 coords)
		(write-line "Enter first two coordinate pairs:")
		(setq a (read) b (read) c (read) d (read))
		(write-line "Enter second two coordinate pairs:")
		(setq e (read) f (read) g (read) h (read))
		(setq s (/ (- d b) (- c a)) s2 (/ (- h f) (- g e))
		y1 (- b (* s a)) y2 (- f (* s2 e))))
	(setq x (/ (- y2 y1) (- s s2)) y3 (+ y1 (* s x)))
	(format t "The point of intersection is (~d,~d)." x y3))