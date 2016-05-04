Imports MathNet.Numerics.LinearAlgebra.Double

Module Module1
    Sub Main()
        ' -2 7 -9 0 -10 -5
        Console.WriteLine("Enter your three coordinate points, separated by spaces.")
        Dim i As String() = Console.ReadLine().Split(" ")
        For Each w As String In i
            w = Convert.ToInt64(w)
        Next
        Dim a, b, c, d, e, f, x, y, z As Double
        a = i(0)
        b = i(1)
        c = i(2)
        d = i(3)
        e = i(4)
        f = i(5)
        Dim DEF As Matrix = DenseMatrix.OfArray(New Double(2, 2) {{a, b, 1}, {c, d, 1}, {e, f, 1}}).Solve(DenseMatrix.OfArray(New Double(2, 0) {{-a * a - b * b}, {-c * c - d * d}, {-e * e - f * f}}))
        x = DEF(0, 0) / -2
        y = DEF(1, 0) / -2
        z = DEF(2, 0)
        Console.WriteLine("(x - {0}){3} + (y - {1}){3} = {2}", x, y, -z + x * x + y * y, ChrW(&H00B2))
    End Sub
End Module