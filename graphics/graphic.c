#include <stdio.h>
#include <windows.h> // Include the Windows API header for Sleep function

void clearScreen() {
    system("cls"); // Clear the screen (for Windows)
}

void printLogo(int x, int y) {
    clearScreen();
    
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord); // Move the cursor to the specified coordinates

    printf("    _____ ____    __        __                 \n");
    printf("  / ___// __ \\  / /        / /     ____  ____ _\n");
    printf("  \\__ \\/ / / / / /   __  / /_____/ __ \\/ __ `/\n");
    printf(" ___/ / /_/ / / /___/ /_/ /_____/ / / / /_/ / \n");
    printf("/____/\\___\\_\\/_____/\\____/     /_/ /_/\\__, /  \n");
    printf("                                        /____/   \n");
}

int main() {
    int screenWidth = 80;
    int screenHeight = 24;

    while (1) {
        for (int x = 1; x <= screenWidth - 37; x++) {
            for (int y = 1; y <= screenHeight - 7; y++) {
                printLogo(x, y);
                Sleep(100); // Sleep for 100 milliseconds (adjust as needed for your desired speed)
            }
        }

        // Rotate the logo by shifting the characters in each line
        char logo[7][37];
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 36; j++) {
                logo[i][j] = logo[i][j + 1];
            }
            logo[i][36] = (i == 0) ? ' ' : logo[i - 1][0];
        }

        // Update the logo with the rotated characters
        clearScreen();
        COORD coord;
        coord.X = 1;
        coord.Y = 1;
        SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 37; j++) {
                putchar(logo[i][j]);
            }
            putchar('\n');
        }
        Sleep(100); // Sleep to control the animation speed
    }

    return 0;
}