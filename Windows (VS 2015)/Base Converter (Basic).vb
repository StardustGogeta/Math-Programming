Module Module1

    Sub Main()
        Console.WriteLine("What is the number? (Positive)")
        Dim firstNumber As Long = Console.ReadLine()
        Console.WriteLine("What is the current base? (Between 2 and 10)")
        Dim firstBase As Int16 = Console.ReadLine()
        Console.WriteLine("What is the desired base? (Between 2 and 10)")
        Dim secondBase As Int16 = Console.ReadLine()
        If firstBase < 2 Or firstBase > 10 Or secondBase < 2 Or secondBase > 10 Then
            Console.Write(Environment.NewLine)
            Console.WriteLine("Please stop wasting my time.")
        Else
            Dim Counter As Long
            Dim Digit As Long = 0
            Dim trueValue As Long
            Dim trueValueTotal As Long = 0
            Dim digitValue As Long = 1
            Dim digitPower As Long
            While firstNumber > 0
                Digit = 0
                Counter = firstNumber
                trueValue = 1
                'Figuring out the first digit and its position.
                While Counter >= 10
                    Counter /= 10
                    Digit += 1
                End While
                digitPower = (10 ^ Digit)
                'Figuring out how much that digit position is "worth."
                digitValue = (firstBase ^ Digit)
                'Obtaining the true value of the digit and subtracting it from the original, in order to repeat again.
                trueValue *= Counter * digitValue
                firstNumber -= Counter * digitPower
                trueValueTotal += trueValue
            End While
            Dim trueValueTotalNew As Long = 1
            Dim secondNumber As Long
            Dim finalSolution As Long = 0
            While trueValueTotalNew > 0
                Dim secondBasePower As Long = 1
                Digit = 0
                'Finding the correct digit with a high enough value to encapsulate the number.
                While secondBasePower <= trueValueTotal
                    secondBasePower *= secondBase
                    Digit += 1
                End While
                secondBasePower /= secondBase
                'Finding the remainder.
                trueValueTotalNew = trueValueTotal Mod secondBasePower
                digitPower = (10 ^ (Digit - 1))
                secondNumber = (trueValueTotal - trueValueTotalNew) * digitPower / secondBasePower
                trueValueTotal = trueValueTotalNew
                finalSolution += secondNumber
            End While
            Console.Write(Environment.NewLine)
            Console.Write("Your desired number is ")
            Console.Write(finalSolution)
            Console.Write(".")
            Console.Write(Environment.NewLine)
        End If
    End Sub

End Module
