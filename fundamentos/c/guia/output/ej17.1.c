#include <stdio.h>

int area(int a, int b) {
    int areaRectangulo=(a*b);
    return areaRectangulo;

}

int main() {
    int rectangulo=area(5,5);
    printf("%d\n", rectangulo);
    return 0;
}



