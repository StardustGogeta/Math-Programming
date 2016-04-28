program fc4
	implicit Integer(kind=8)(I)
	print *, "Enter a number."
	read *, Ia
	do i=1, sqrt(real(Ia))
		if (mod(Ia,i)==0) then
			print *, Ia/i, i
        end if
    end do
    print *, "List complete."
end program fc4
