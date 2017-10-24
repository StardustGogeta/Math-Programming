import java.util.Scanner;
class FC4 {
    public static void main(String[] args) {
        System.out.println("What is the number?");
        Scanner in = new Scanner(System.in);
        long n = in.nextLong();
        if (n > 0)
        {
            for (long d=1; d<Math.sqrt(n); d++)
                if ((n % d) == 0)
                {
                    System.out.println(n / d + ", " + d);
                }
        }
        else
        {
        System.out.println("Please try again.");
        }
    }
}