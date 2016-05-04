program tr
	implicit Real(kind=16)(I)
	print *, "Degrees (0) or radians (1)?"
	read *, Ia
	print *, "What is the angle measure?"
	read *, Ib
	IP=4*atan(1.0)
	if (Ia==1) then
		print *, "In terms of pi? (Y=1)"
		read *, Ic
		if (Ic==1) then
			Ib=Ib*IP
        end if
    else
		Ib=Ib*IP/180
    end if
    print *, "sin = ",round(sin(Ib),8)
    print *, "cos = ",round(cos(Ib),8)
    print *, "tan = ",round(tan(Ib),8)
    print *, "csc = ",round(1/sin(Ib),8)
    print *, "sec = ",round(1/cos(Ib),8)
    print *, "cot = ",round(1/tan(Ib),8)
end program tr

real function round(x,y)
	real(kind=16) x
	integer y
	round = nint(10**y*x)/10.0**y
end
