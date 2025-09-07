#!/usr/bin/env python3
"""
Game Launcher - Choose between Tic-Tac-Toe and PvP Fighting Game
"""

import sys
import os

def main():
    print("=" * 50)
    print("         GAME LAUNCHER")
    print("=" * 50)
    print()
    print("Choose a game to play:")
    print("1. PvP Fighting Game (NEW!)")
    print("2. Tic-Tac-Toe (Original)")
    print("3. Run Tests")
    print("4. Exit")
    print()
    
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\nLaunching PvP Fighting Game...")
            os.system("python3 pvp_fighting_game.py")
            break
        elif choice == "2":
            print("\nLaunching Tic-Tac-Toe...")
            os.system("python3 tictactoe_ai_customtkinter_Version1.py")
            break
        elif choice == "3":
            print("\nRunning Fighting Game Tests...")
            os.system("python3 test_fighting_game.py")
            print("\nPress Enter to continue...")
            input()
        elif choice == "4":
            print("\nGoodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()