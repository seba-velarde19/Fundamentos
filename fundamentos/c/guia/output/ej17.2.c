#include <stdio.h>

int calcularFactorial(int n) {
    int i = 1;
    int factorial = 1;
    for (i;i<=n;i++) {
        factorial = factorial *i ;
    }
    return factorial;
    
}

int main(){
    int fact = calcularFactorial(3);
    printf("%d\n", fact);
    return 0;
}