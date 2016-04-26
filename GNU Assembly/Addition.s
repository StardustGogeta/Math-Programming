L:
    .ascii "5 + 21 = \0"
.data
	num1:	.byte 5
	num2:	.byte 21
.globl _main
_main:
    pushl    %ebp
    movl    %esp, %ebp
    subl    $8, %esp
    movl    %eax, -4(%ebp)
    movl    -4(%ebp), %eax
    movl    $num1, (%esp)
    call    _printf
	movl	$num1, (%ebp)
	addl	$num2, (%ebp)
	movl	%ebp, %esp
    call    _printf
    leave
    ret
