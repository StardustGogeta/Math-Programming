Module Module1

    Sub Main()
        Console.WriteLine("Please input your number.")
        Dim i As Long = Console.ReadLine()
        Console.Write(Environment.NewLine)
        If (i > 0) Then
            For d = 1 To Math.Sqrt(i)
                If (i Mod d = 0) Then
                    Console.WriteLine("{0}, {1}", i / d, d)
                End If
            Next
            Console.Write(Environment.NewLine)
            Console.WriteLine("The list of factors has been successfully generated.")
        Else
            Console.WriteLine("What are you doing?")
        End If
    End Sub

End Module
