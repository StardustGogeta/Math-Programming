Module Module1

    Sub Main()
        Dim pi As Double = 3.14159265
        Console.WriteLine("Degrees (0) or radians (1)?")
        Dim ang As Double = Console.ReadLine()
        Console.WriteLine("What is the angle measure?")
        Dim o As Double = Console.ReadLine()
        If ang = 0 Then
            o = o * pi / 180
        Else
            Console.WriteLine("In terms of pi (1) or not (0)?")
            Dim rad As Double = Console.ReadLine()
            If rad = 1 Then
                o = pi * o
            End If
        End If
        Console.WriteLine("sin = {0}{6}cos = {1}{6}tan = {2}{6}csc = {3}{6}sec = {4}{6}cot = {5}", Math.Sin(o), Math.Cos(o), Math.Tan(o), 1 / Math.Sin(o), 1 / Math.Cos(o), 1 / Math.Tan(o), Environment.NewLine)
    End Sub

End Module