package bc;
import java.util.Scanner;
class BC {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("What is the number?");
        String fN = in.nextLine();
        System.out.println("What is the current base? (<=36)");
        int fB = in.nextInt();
        System.out.println("What is the desired base? (<=36)");
        int sB = in.nextInt();
        System.out.print("Your number is "+Integer.toString(Integer.parseInt(fN,fB),sB)+".\n");
        //11110100001000111111 is 999999 in base 10
    }
}
