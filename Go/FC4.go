package main
import "fmt"
import "math"
func main() {
	fmt.Println("Enter a number.")
	a := float64(0)
	fmt.Scanf("%f",&a)
	for n:=float64(0); n<=math.Floor(math.Sqrt(a)); n++ {
		if math.Mod(a,n)==0 {
			fmt.Printf("%d, %d\n",int64(a/n),int64(n))
		}
	}
	fmt.Println("List complete.")
}