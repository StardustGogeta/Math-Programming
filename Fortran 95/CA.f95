program ca
	implicit Integer(kind=8)(I)
	print *, "Please state an angle in degrees."
	read *, I
	I = mod(I,360)
	print '("The coterminal angles include ",(i0)," and ",(i0)".")', I, I-sign(int8(360),I)
end program ca
