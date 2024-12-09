void funcChessBoard(int inputNum)
{
    for (int i = 0; i < inputNum; i++) {
        for (int j = 0; j < inputNum; j++) {
            // Print "W" or "B" based on the sum of indices
            if ((i + j) % 2 == 0) {
                printf("W");
            } else {
                printf("B");
            }
            // Print a space after every character except the last in the row
            if (j < inputNum - 1) {
                printf(" ");
            }
        }
        // Print a newline at the end of the row
        printf("\n");
    }
}
