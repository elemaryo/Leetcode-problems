#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//https://www.youtube.com/watch?v=PsjZDnd2Fus&ab_channel=nexTRIE

int *reverseArray(int a_count, int *a, int *result_count)
{
    int middle = a_count / 2;
    for (int i = 0; i < middle; i++)
    {
        int temp = a[i];
        a[i] = a[a_count - 1 - i];
        a[a_count - 1 - i] = temp;
    }

    *result_count = a_count;

    return a;
}