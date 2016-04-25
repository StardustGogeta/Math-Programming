L:
    .ascii "Hello, world!\12\0"
.globl _main
_main:
    pushl    %ebp
    movl    %esp, %ebp
    subl    $8, %esp
    movl    %eax, -4(%ebp)
    movl    -4(%ebp), %eax
    movl    $L, (%esp)
    call    _printf
    leave
    ret
