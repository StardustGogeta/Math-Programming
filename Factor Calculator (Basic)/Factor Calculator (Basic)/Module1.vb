Module Module1

    Sub Main()
        Console.Write("Please input your number.")
        Console.Write(Environment.NewLine)
        Dim Input As Long = Console.ReadLine()
        Console.Write(Environment.NewLine)

        If (Input > 0) Then
            Dim Divisor As Long = 1
            For Divisor = 1 To Math.Sqrt(Input)
                If (Input Mod Divisor = 0) Then
                    Console.Write(Input / Divisor)
                    Console.Write(Environment.NewLine)
                    Console.Write(Divisor)
                    Console.Write(Environment.NewLine)
                    '<< Input / Divisor << "\n" << Divisor << "\n";
                End If
            Next
            Console.Write(Environment.NewLine)
            Console.Write("The list of factors has been successfully generated.")
            Console.Write(Environment.NewLine)
        Else
            Console.Write("Are you trying to kill me?")
            Console.Write(Environment.NewLine)
            Console.Write("You will pay for that.")
        End If
    End Sub

End Module
