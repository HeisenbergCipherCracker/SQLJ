#define PROGRAM "SQLJNG"
#define VERSION 1.4.1
#include <stdio.h>

struct SQLJNG {
    #ifdef PROGRAM
    int count;
    char programop[100]= "NOTE:please consider using and including parameter after ? mark";
    #endif
};