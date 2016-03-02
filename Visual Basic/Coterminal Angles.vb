Module Module1

    Sub Main()
        Console.Write("Please state your angle.")
        Console.Write(Environment.NewLine)
        Dim orig As Int32 = Console.ReadLine()
        Dim ang1 As Int32 = orig
        Dim ang2 As Int32 = orig
        If (orig > 0) Then
            If (orig > 360) Then
                While (ang1 > 360)
                    ang1 -= 360
                End While
                ang2 = ang1 - 360
            Else
                ang1 += 360
                ang2 -= 360
            End If
        Else
            If (orig < -360) Then
                While (ang1 < -360)
                    ang1 += 360
                End While
                ang2 = ang1 + 360
            Else
                ang1 -= 360
                ang2 += 360
            End If
        End If
        Console.Write(Environment.NewLine)
        Console.Write("The coterminal angles are ")
        Console.Write(ang1)
        Console.Write(" and ")
        Console.Write(ang2)
        Console.Write(".")
        Console.Write(Environment.NewLine)
    End Sub

End Module
