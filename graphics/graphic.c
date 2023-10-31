#include <stdio.h>
#include <windows.h>

void clearScreen() {
    system("cls");
}

void gotoxy(int x, int y) {
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

int main() {
    int x = 0;
    int direction = 1;
    const char* sqljng = "SQLJ-ng";

    while (1) {
        clearScreen();
        gotoxy(x, 10);
        printf("%s", sqljng);
        Sleep(100);  // Adjust the animation speed

        x += direction;
        if (x >= 70 || x < 0) {
            direction *= -1; // Reverse direction at screen edges
        }
    }

    return 0;
}
