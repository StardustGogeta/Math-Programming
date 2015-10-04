Module Module1

    Sub Main()
        Dim pi As Double = 3.14159265
        Console.WriteLine("Degrees (d) or radians (r)?")
        Dim angleType As String = Console.ReadLine()
        Console.WriteLine("What is the angle measure? (decimal)")
        Dim orig As Double = Console.ReadLine()
        If (angleType = "d") Then
            Console.WriteLine("sin = ")
            Console.WriteLine(Math.Sin(orig * 3.14159 / 180))
            Console.WriteLine("cos = ")
            Console.WriteLine(Math.Cos(orig * 3.14159 / 180))
            Console.WriteLine("tan = ")
            Console.WriteLine(Math.Tan(orig * 3.14159 / 180))
            Console.WriteLine("csc = ")
            Console.WriteLine(1 / Math.Sin(orig * 3.14159 / 180))
            Console.WriteLine("sec = ")
            Console.WriteLine(1 / Math.Cos(orig * 3.14159 / 180))
            Console.WriteLine("cot = ")
            Console.WriteLine(1 / Math.Tan(orig * 3.14159 / 180))
        Else
            Console.WriteLine("Is it in terms of pi? (Y=1)")
            Dim radType As Boolean = Console.ReadLine()
            If (radType = True) Then
                Console.WriteLine("sin = ")
                Console.WriteLine(Math.Sin(orig * 3.14159))
                Console.WriteLine("cos = ")
                Console.WriteLine(Math.Cos(orig * 3.14159))
                Console.WriteLine("tan = ")
                Console.WriteLine(Math.Tan(orig * 3.14159))
                Console.WriteLine("csc = ")
                Console.WriteLine(1 / Math.Sin(orig * 3.14159))
                Console.WriteLine("sec = ")
                Console.WriteLine(1 / Math.Cos(orig * 3.14159))
                Console.WriteLine("cot = ")
                Console.WriteLine(1 / Math.Tan(orig * 3.14159))
            Else
                Console.WriteLine("sin = ")
                Console.WriteLine(Math.Sin(orig))
                Console.WriteLine("cos = ")
                Console.WriteLine(Math.Cos(orig))
                Console.WriteLine("tan = ")
                Console.WriteLine(Math.Tan(orig))
                Console.WriteLine("csc = ")
                Console.WriteLine(1 / Math.Sin(orig))
                Console.WriteLine("sec = ")
                Console.WriteLine(1 / Math.Cos(orig))
                Console.WriteLine("cot = ")
                Console.WriteLine(1 / Math.Tan(orig))
            End If
        End If
    End Sub

End Module
