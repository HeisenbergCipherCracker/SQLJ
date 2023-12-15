#define PROGRAM "SQLJ-ng"
#define VERSION "1.4.1"
#define FILENAME "info.c"

#ifndef PROGRAM
    #error "PROGRAM is not defined"
#endif

#ifndef VERSION
    #error "VERSION is not defined"
#endif

#ifndef FILENAME
    #error "FILENAME is not defined"
#endif

#include <stdio.h>

int main() {
    #if !defined(VERSION) || !defined(FILENAME)
        #error "VERSION or FILENAME is not defined"
    #endif

    #if defined(VERSION) && defined(FILENAME)
    #if VERSION >= 1.4.1
        printf("Program: %s\nVersion: %s\nFilename: %s\n", PROGRAM, VERSION, FILENAME);
    #else
        printf("Program is outdated");
    #endif
    #endif

    return 0;
}
