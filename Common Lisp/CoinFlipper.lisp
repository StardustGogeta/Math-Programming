(DEFUN CoinFlipper (heads flips trials)
	(setq c 0)
	(loop for _ from 1 to trials
		do (setq r 0)
		(loop for _ from 1 to flips
			do (incf r (random 2))
		)
		(when (= r heads) (incf c))
	)
	(format t "This combination will happen ~,2f% of the time." (* 100 (/ c trials)))
)
