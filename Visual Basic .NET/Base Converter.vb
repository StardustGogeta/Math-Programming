Module Module1

    Sub Main()
        Console.WriteLine("What is the number?")
        Dim fN As Long = Console.ReadLine()
        Console.WriteLine("What is the current base? (1<x<11)")
        Dim fB As Int16 = Console.ReadLine()
        Console.WriteLine("What is the desired base? (1<x<11)")
        Dim sB As Int16 = Console.ReadLine()
        If 2 < fB < 10 And 2 < sB < 10 Then
            Dim tVT As Long = Convert.ToInt64(fN, fB)
            Dim sN As String = ""
            While tVT
                sN += Str(tVT Mod sB)
                tVT = Math.Floor(tVT / sB)
            End While
            Console.Write(Environment.NewLine)
            Console.WriteLine("Your desired number is {0}.", Replace(StrReverse(sN), " ", ""))
            Console.Write(Environment.NewLine)
        Else
            Console.WriteLine("Please stop wasting my time.")
        End If
    End Sub

End Module