Module Module1
    Sub Main()
        Console.WriteLine("Please state your angle.")
        Dim o As Int64 = Console.ReadLine() Mod 360
        Console.WriteLine("The coterminal angles include {0} and {1}.", o, o - Math.Sign(o) * 360)
    End Sub
End Module