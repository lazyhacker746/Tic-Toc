# Tic-Toc

## PvP Fighting Game

A turn-based Player vs Player fighting game built with Python and CustomTkinter.

### Features

- **Turn-based combat** between two players
- **Multiple attack types**:
  - Basic Attack (15-25 damage)
  - Heavy Attack (25-35 damage, 2-turn cooldown)
  - Block (reduces incoming damage by 50%)
  - Special Move (40-50 damage, limited to 3 uses per fight)
- **Visual health bars** showing real-time HP
- **Combat mechanics**:
  - Each player starts with 100 HP
  - Turn-based system with alternating players
  - Blocking reduces damage by half
  - Cooldowns and limited uses for powerful moves
- **Score tracking** for multiple fights
- **Modern GUI** with CustomTkinter

### How to Play

1. **Install dependencies**: 
   ```bash
   pip install -r requirements.txt
   # OR manually: pip install customtkinter
   ```
2. **Launch games**: 
   ```bash
   python3 game_launcher.py  # Game selection menu
   # OR directly: python3 pvp_fighting_game.py
   ```
3. **Take turns** using the action buttons:
   - **Basic Attack**: Always available, moderate damage
   - **Heavy Attack**: High damage but has cooldown
   - **Block**: Protect against next attack (50% damage reduction)
   - **Special Move**: Highest damage but limited uses
4. **Win condition**: Reduce opponent's HP to 0
5. **Play multiple rounds** and track your wins!

### Game Mechanics

- **Health System**: 100 HP per player
- **Damage Ranges**: 
  - Basic: 15-25 damage
  - Heavy: 25-35 damage (2-turn cooldown)
  - Special: 40-50 damage (3 uses per fight)
- **Blocking**: Reduces any incoming damage by 50%
- **Turn System**: Players alternate, with visual indicators
- **Score System**: Tracks wins across multiple fights

### Files

- `pvp_fighting_game.py` - Main fighting game application
- `tictactoe_ai_customtkinter_Version1.py` - Original Tic-Tac-Toe game
- `game_launcher.py` - Game selection menu
- `test_fighting_game.py` - Test suite for combat mechanics
- `requirements.txt` - Python dependencies

### Testing

Run the test suite to verify combat mechanics:
```bash
python3 test_fighting_game.py
```

Enjoy the fight! 🥊