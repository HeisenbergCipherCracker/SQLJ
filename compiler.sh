#!/bin/bash

# Check if dialog and pip are installed
if ! command -v dialog &> /dev/null || ! command -v pip &> /dev/null; then
    echo "Error: dialog or pip is not installed. Please install them to continue."
    exit 1
fi

# Function to compile and run the command
compile_and_run() {
    echo "Compiling SQLJng.py using PyInstaller..."
    pyinstaller --onefile --noconfirm SQLJng.py
}

# Function to install PyInstaller
install_pyinstaller() {
    echo "Installing PyInstaller..."
    pip install pyinstaller
}

# Function to install Colorama
install_colorama() {
    echo "Installing Colorama..."
    pip install colorama
}

# Main menu
while true; do
    # Show a dialog box with options
    choice=$(dialog --backtitle "SQLJng Compiler" \
                    --title "Main Menu" \
                    --menu "Choose an option:" 14 50 4 \
                    1 "Compile and Run" \
                    2 "Exit" \
                    3 "Install PyInstaller (if not installed)" \
                    4 "Install Dependencies" \
                    2>&1 >/dev/tty)

    # Act on the user's choice
    case $choice in
        1)  # Compile and Run
            compile_and_run
            ;;
        2)  # Exit
            echo "Exiting the SQLJng Compiler."
            exit 0
            ;;
        3)  # Install PyInstaller
            install_pyinstaller
            ;;
        4)  # Install Colorama
            install_colorama
            ;;
        *)  # Invalid option
            echo "Invalid option. Please try again."
            ;;
    esac
done
