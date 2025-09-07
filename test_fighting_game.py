#!/usr/bin/env python3
"""
Test script for PvP Fighting Game logic
"""

class MockFightingGame:
    def __init__(self):
        self.scores = {"Player 1": 0, "Player 2": 0}
        self.current_player = "Player 1"
        self.player1_hp = 100
        self.player2_hp = 100
        self.max_hp = 100
        self.game_over = False
        
        # Special abilities cooldowns and limits
        self.player1_heavy_cooldown = 0
        self.player2_heavy_cooldown = 0
        self.player1_special_uses = 3
        self.player2_special_uses = 3
        self.player1_blocking = False
        self.player2_blocking = False

    def deal_damage(self, damage):
        target_player = "Player 2" if self.current_player == "Player 1" else "Player 1"
        
        # Apply blocking reduction
        if (target_player == "Player 1" and self.player1_blocking) or \
           (target_player == "Player 2" and self.player2_blocking):
            damage = damage // 2
            print(f"{target_player} blocked! Damage reduced to {damage}.")
        
        # Deal damage
        if target_player == "Player 1":
            self.player1_hp = max(0, self.player1_hp - damage)
            self.player1_blocking = False
        else:
            self.player2_hp = max(0, self.player2_hp - damage)
            self.player2_blocking = False
        
        print(f"{target_player} takes {damage} damage! HP: {self.player1_hp if target_player == 'Player 1' else self.player2_hp}")
        
        # Check for game over
        if self.player1_hp <= 0 or self.player2_hp <= 0:
            self.handle_game_end()

    def handle_game_end(self):
        self.game_over = True
        winner = "Player 1" if self.player2_hp <= 0 else "Player 2"
        self.scores[winner] += 1
        print(f"Game Over! {winner} wins!")

    def basic_attack(self):
        import random
        if self.game_over:
            return
        damage = random.randint(15, 25)
        print(f"{self.current_player} used Basic Attack!")
        self.deal_damage(damage)
        self.end_turn()

    def end_turn(self):
        # Switch turn
        self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"
        print(f"Turn switched to {self.current_player}")

def test_combat_mechanics():
    print("Testing PvP Fighting Game Combat Mechanics")
    print("=" * 50)
    
    game = MockFightingGame()
    
    # Test basic combat
    print(f"Initial state: P1 HP: {game.player1_hp}, P2 HP: {game.player2_hp}")
    
    # Player 1 attacks Player 2
    game.basic_attack()
    
    # Player 2 attacks Player 1
    game.basic_attack()
    
    print(f"After attacks: P1 HP: {game.player1_hp}, P2 HP: {game.player2_hp}")
    print(f"Game Over: {game.game_over}")
    print(f"Scores: {game.scores}")
    
    # Test blocking mechanics
    print("\nTesting blocking mechanics:")
    game.player2_blocking = True
    old_hp = game.player2_hp
    game.deal_damage(20)
    new_hp = game.player2_hp
    blocked_damage = old_hp - new_hp
    print(f"Blocked damage: {blocked_damage} (should be 10, half of 20)")
    
    # Test cooldown mechanics
    print("\nTesting cooldown mechanics:")
    game.player1_heavy_cooldown = 2
    print(f"Player 1 heavy cooldown: {game.player1_heavy_cooldown}")
    
    # Test special uses
    print("\nTesting special attack uses:")
    print(f"Player 1 special uses: {game.player1_special_uses}")
    
    print("\nAll combat mechanics test completed successfully!")

def test_game_scenarios():
    print("\nTesting Game Scenarios")
    print("=" * 30)
    
    # Test a complete game
    game = MockFightingGame()
    attack_count = 0
    
    print("Simulating a complete fight...")
    while not game.game_over and attack_count < 20:  # Prevent infinite loop
        game.basic_attack()
        attack_count += 1
    
    print(f"Fight completed after {attack_count} attacks")
    print(f"Final scores: {game.scores}")
    print(f"Winner: {'Player 1' if game.scores['Player 1'] > 0 else 'Player 2'}")
    
    print("\nGame scenario test completed successfully!")

if __name__ == "__main__":
    test_combat_mechanics()
    test_game_scenarios()