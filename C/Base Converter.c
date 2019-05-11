#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main() {
    char num[500];
    int fromBase, toBase;
    printf("What is the number?\n");
    scanf("%s", &num);
    printf("What is the current base? (<=36)\n");
    scanf("%d", &fromBase);
    printf("What is the desired base? (<=10)\n");
    scanf("%d", &toBase);
    if (1 < fromBase < 37 && 1 < toBase < 11) {
        char ret[500] = "", temp[2] = "";
        unsigned long long n = strtoull(num, NULL, fromBase);
        while (n) {
            sprintf(temp, "%d", n % toBase);
            strcat(ret, temp);
            n /= toBase;
        }
        printf("\nYour number is %s.\n", strrev(ret));
    }
    else
        printf("\nInvalid base!\n");
}
