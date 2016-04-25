
> 'Please input something.'
< a
< b, 'Now input something else.\n'
> 'You just said '+a+" and " + b
--if 1:
	--print('Hi!')
	>'Bypassing works!'

? True : > 'This is true.' : > 'This is false.'
? True : > 'Single-line if-statements without "else" work too!'

? 1==1
	> 'This is the beauty of KerbalSpace!'
> 'The conditional stops because there is no indent here.'

<python>
	print("Hello world!\nThis is embedded Python.")
	a = input("Please input something.\n")
	print('Your input is '+a)
	if    ("h"):
		print('If-statements also work!')
</python>
