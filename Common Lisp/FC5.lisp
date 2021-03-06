(DEFUN fc5 (n)
	(setq Fs (list 1))
	(loop while (> n 1)
		do (setq f (block findFactor (loop for d from 2 to (sqrt n)
						do (when (= 0 (rem n d)) (return-from findFactor d)))
						(return-from findFactor n))
			Fs (remove-duplicates (append (mapcar #'(lambda (x) (* f x)) Fs) Fs))
			n (/ n f)))
	(return-from fc5 (sort Fs #'>)))
