#include <stdio.h>
#include <stdlib.h>

// Define the array_single_int structure
typedef struct {
    int *data; // Pointer to dynamically allocate array
    int size;  // Size of the array
} array_single_int;

// Function to calculate the maximum number of points on a single path
void funcDrop(array_single_int xCoordinate, array_single_int yCoordinate) {
    int maxCount = 0;

    // Count occurrences of x-coordinates
    for (int i = 0; i < xCoordinate.size; i++) {
        int count = 0;
        for (int j = 0; j < xCoordinate.size; j++) {
            if (xCoordinate.data[i] == xCoordinate.data[j]) {
                count++;
            }
        }
        if (count > maxCount) {
            maxCount = count;
        }
    }

    // Count occurrences of y-coordinates
    for (int i = 0; i < yCoordinate.size; i++) {
        int count = 0;
        for (int j = 0; j < yCoordinate.size; j++) {
            if (yCoordinate.data[i] == yCoordinate.data[j]) {
                count++;
            }
        }
        if (count > maxCount) {
            maxCount = count;
        }
    }

    // Print the result
    printf("%d\n", maxCount);
}

int main() {
    array_single_int xCoordinate;
    array_single_int yCoordinate;

    // Input for xCoordinate
    scanf("%d", &xCoordinate.size);
    xCoordinate.data = (int *)malloc(sizeof(int) * xCoordinate.size);
    for (int idx = 0; idx < xCoordinate.size; idx++) {
        scanf("%d", &xCoordinate.data[idx]);
    }

    // Input for yCoordinate
    scanf("%d", &yCoordinate.size);
    yCoordinate.data = (int *)malloc(sizeof(int) * yCoordinate.size);
    for (int idx = 0; idx < yCoordinate.size; idx++) {
        scanf("%d", &yCoordinate.data[idx]);
    }

    funcDrop(xCoordinate, yCoordinate);

    // Free allocated memory
    free(xCoordinate.data);
    free(yCoordinate.data);

    return 0;
}
