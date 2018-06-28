import java.util.Scanner;
public class CES {
    private static double avg(double[] a, int b, int c) {return (a[b]+a[c])/2;}
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter your three coordinate points, separated by spaces:");
        double[] c = new double[6];
        for (int i = 0; i < 6; i++) c[i] = scan.nextDouble();
        double x0 = avg(c,0,2),y0 = avg(c,1,3),x1 = avg(c,0,4),y1 = avg(c,1,5),
        s = (c[0]-c[2])/(c[3]-c[1]), s2 = (c[0]-c[4])/(c[5]-c[1]), h, k, r2;
        h = (y1-y0+s*x0-s2*x1) / (s-s2);
	k = (h-x0)*s+y0;
	r2 = (h-c[0])*(h-c[0])+(k-c[1])*(k-c[1]);
	System.out.printf("(x - %.3f)² + (y - %.3f)² = %.3f",h,k,r2);
    }
}
