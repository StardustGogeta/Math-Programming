(DEFUN CES (a b c d e f)
	(setq x1 (mid a c) y1 (mid b d) x2 (mid a e) y2 (mid b f) s (/ -1 (slope a b c d)) s2 (/ -1 (slope a b e f)))
	(decf y1 (* x1 s))
	(decf y2 (* x2 s2))
	(setq x (/ (- y2 y1) (- s s2)) y3 (+ y1 (* s x)))
	(format t "The center is (~d,~d).~%The equation of the circle is (x-~d)²+(y-~d)²=~d." x y3 x y3 (+ (expt (- a x) 2) (expt (- b y3) 2))))

(DEFUN slope (a b c d) (/ (- d b) (- c a)))
(DEFUN mid (a b) (/ (+ a b) 2))