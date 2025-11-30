#include <stdio.h>

int promedioArray(int array[],int tam) {
    int total = 0;
    for (int i = 0; i < tam; i++) {
        total += array[i];
    }
    int promedio=total/tam;
    return promedio;

}

int main() {
    int numeros[] = {1,2,3,4};
    int tam = sizeof(numeros) / sizeof(numeros[0]);
    int promedio = promedioArray(numeros,tam);
    printf("%d\n",promedio);
    return 0;
}