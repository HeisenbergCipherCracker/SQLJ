#define PROGRAM "SQLJNG"
#define VERSION "1.4.1"
#include <stdio.h>

struct SQLJNG {
#ifdef PROGRAM
    int count;
    char programop[100]; // Use an array for storing strings
#endif
};

int main() {
#ifdef PROGRAM
    struct SQLJNG sqljng;

    // You can initialize or manipulate the programop array as needed.
    // For example:
    sqljng.count = 5;
    snprintf(sqljng.programop, sizeof(sqljng.programop), "NOTE: please consider using and including parameter after ? mark");

    // Debugging: Print the values to check if they are set correctly.
    printf("Count: %d\n", sqljng.count);
    printf("Program Op: %s\n", sqljng.programop);
#endif

    return 0;
}
