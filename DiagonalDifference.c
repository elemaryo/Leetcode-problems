#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int diagonalDifference(int arr_rows, int arr_columns, int** arr) {
    int leftD = 0;
    int rightD = 0;
    for (int i = 0; i < arr_rows; i++){
        leftD += arr[i][i];
        rightD += arr[i][arr_rows - i - 1];
    }
    int absoluteSum = abs(rightD-leftD);
    return absoluteSum;
}
