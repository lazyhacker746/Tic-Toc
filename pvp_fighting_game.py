import customtkinter as ctk
import tkinter.messagebox as messagebox
import random

class PvPFightingGame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PvP Fighting Game")
        self.geometry("600x650")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Game state
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

        # Title
        self.title_label = ctk.CTkLabel(self, text="PvP Fighting Game", font=("Helvetica", 28, "bold"))
        self.title_label.pack(pady=18)

        # Current turn status
        self.status_label = ctk.CTkLabel(self, text="Player 1's turn", font=("Helvetica", 16))
        self.status_label.pack(pady=8)

        # Health bars frame
        self.health_frame = ctk.CTkFrame(self)
        self.health_frame.pack(pady=12, padx=20, fill="x")
        
        # Player 1 Health
        self.p1_label = ctk.CTkLabel(self.health_frame, text="Player 1", font=("Helvetica", 14, "bold"))
        self.p1_label.grid(row=0, column=0, padx=10, pady=5)
        self.p1_hp_label = ctk.CTkLabel(self.health_frame, text="HP: 100/100", font=("Helvetica", 12))
        self.p1_hp_label.grid(row=1, column=0, padx=10)
        self.p1_health_bar = ctk.CTkProgressBar(self.health_frame, width=200, height=20)
        self.p1_health_bar.grid(row=2, column=0, padx=10, pady=5)
        self.p1_health_bar.set(1.0)

        # VS Label
        self.vs_label = ctk.CTkLabel(self.health_frame, text="VS", font=("Helvetica", 16, "bold"))
        self.vs_label.grid(row=1, column=1, padx=20)

        # Player 2 Health
        self.p2_label = ctk.CTkLabel(self.health_frame, text="Player 2", font=("Helvetica", 14, "bold"))
        self.p2_label.grid(row=0, column=2, padx=10, pady=5)
        self.p2_hp_label = ctk.CTkLabel(self.health_frame, text="HP: 100/100", font=("Helvetica", 12))
        self.p2_hp_label.grid(row=1, column=2, padx=10)
        self.p2_health_bar = ctk.CTkProgressBar(self.health_frame, width=200, height=20)
        self.p2_health_bar.grid(row=2, column=2, padx=10, pady=5)
        self.p2_health_bar.set(1.0)

        # Combat Arena
        self.arena_frame = ctk.CTkFrame(self)
        self.arena_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Fighter representations
        self.fighter_frame = ctk.CTkFrame(self.arena_frame)
        self.fighter_frame.pack(pady=20, fill="x")
        
        self.fighter1_label = ctk.CTkLabel(self.fighter_frame, text="🥊", font=("Helvetica", 60))
        self.fighter1_label.grid(row=0, column=0, padx=50)
        
        self.battle_label = ctk.CTkLabel(self.fighter_frame, text="⚔️", font=("Helvetica", 40))
        self.battle_label.grid(row=0, column=1, padx=30)
        
        self.fighter2_label = ctk.CTkLabel(self.fighter_frame, text="🥊", font=("Helvetica", 60))
        self.fighter2_label.grid(row=0, column=2, padx=50)

        # Action Buttons
        self.action_frame = ctk.CTkFrame(self.arena_frame)
        self.action_frame.pack(pady=20)
        
        self.attack_btn = ctk.CTkButton(
            self.action_frame, text="Basic Attack\n(15-25 DMG)", 
            command=self.basic_attack, width=120, height=60,
            font=("Helvetica", 12, "bold")
        )
        self.attack_btn.grid(row=0, column=0, padx=10, pady=5)
        
        self.heavy_btn = ctk.CTkButton(
            self.action_frame, text="Heavy Attack\n(25-35 DMG)", 
            command=self.heavy_attack, width=120, height=60,
            font=("Helvetica", 12, "bold"), fg_color="#E17055"
        )
        self.heavy_btn.grid(row=0, column=1, padx=10, pady=5)
        
        self.block_btn = ctk.CTkButton(
            self.action_frame, text="Block\n(50% DMG Reduction)", 
            command=self.block_action, width=120, height=60,
            font=("Helvetica", 12, "bold"), fg_color="#6C5CE7"
        )
        self.block_btn.grid(row=1, column=0, padx=10, pady=5)
        
        self.special_btn = ctk.CTkButton(
            self.action_frame, text="Special Move\n(40-50 DMG)", 
            command=self.special_attack, width=120, height=60,
            font=("Helvetica", 12, "bold"), fg_color="#00B894"
        )
        self.special_btn.grid(row=1, column=1, padx=10, pady=5)

        # Action log
        self.log_frame = ctk.CTkFrame(self)
        self.log_frame.pack(pady=10, padx=20, fill="x")
        self.log_label = ctk.CTkLabel(self.log_frame, text="Game Log", font=("Helvetica", 14, "bold"))
        self.log_label.pack(pady=5)
        self.last_action = ctk.CTkLabel(self.log_frame, text="Game started! Player 1's turn.", font=("Helvetica", 12))
        self.last_action.pack(pady=5)

        # Score & Reset
        self.score_frame = ctk.CTkFrame(self)
        self.score_frame.pack(pady=10)
        self.p1_score = ctk.CTkLabel(self.score_frame, text="Player 1 Wins: 0", font=("Helvetica", 14, "bold"))
        self.p1_score.grid(row=0, column=0, padx=20)
        self.p2_score = ctk.CTkLabel(self.score_frame, text="Player 2 Wins: 0", font=("Helvetica", 14, "bold"))
        self.p2_score.grid(row=0, column=1, padx=20)

        self.reset_btn = ctk.CTkButton(self, text="New Fight", command=self.reset_game, width=150)
        self.reset_btn.pack(pady=15)

        self.update_ui()

    def basic_attack(self):
        if self.game_over:
            return
        damage = random.randint(15, 25)
        self.deal_damage(damage)
        self.log_action(f"{self.current_player} used Basic Attack! Dealt {damage} damage.")
        self.end_turn()

    def heavy_attack(self):
        if self.game_over:
            return
        
        # Check cooldown
        if (self.current_player == "Player 1" and self.player1_heavy_cooldown > 0) or \
           (self.current_player == "Player 2" and self.player2_heavy_cooldown > 0):
            messagebox.showwarning("Cooldown", "Heavy Attack is on cooldown!")
            return
            
        damage = random.randint(25, 35)
        self.deal_damage(damage)
        
        # Set cooldown
        if self.current_player == "Player 1":
            self.player1_heavy_cooldown = 2
        else:
            self.player2_heavy_cooldown = 2
            
        self.log_action(f"{self.current_player} used Heavy Attack! Dealt {damage} damage.")
        self.end_turn()

    def block_action(self):
        if self.game_over:
            return
        
        if self.current_player == "Player 1":
            self.player1_blocking = True
        else:
            self.player2_blocking = True
            
        self.log_action(f"{self.current_player} is now blocking!")
        self.end_turn()

    def special_attack(self):
        if self.game_over:
            return
        
        # Check uses remaining
        if (self.current_player == "Player 1" and self.player1_special_uses <= 0) or \
           (self.current_player == "Player 2" and self.player2_special_uses <= 0):
            messagebox.showwarning("No Uses", "No special moves remaining!")
            return
            
        damage = random.randint(40, 50)
        self.deal_damage(damage)
        
        # Decrease uses
        if self.current_player == "Player 1":
            self.player1_special_uses -= 1
        else:
            self.player2_special_uses -= 1
            
        self.log_action(f"{self.current_player} used Special Move! Dealt {damage} damage.")
        self.end_turn()

    def deal_damage(self, damage):
        target_player = "Player 2" if self.current_player == "Player 1" else "Player 1"
        
        # Apply blocking reduction
        if (target_player == "Player 1" and self.player1_blocking) or \
           (target_player == "Player 2" and self.player2_blocking):
            damage = damage // 2
            self.log_action(f"{target_player} blocked! Damage reduced to {damage}.")
        
        # Deal damage
        if target_player == "Player 1":
            self.player1_hp = max(0, self.player1_hp - damage)
            self.player1_blocking = False
        else:
            self.player2_hp = max(0, self.player2_hp - damage)
            self.player2_blocking = False
        
        # Check for game over
        if self.player1_hp <= 0 or self.player2_hp <= 0:
            self.handle_game_end()

    def end_turn(self):
        # Reduce cooldowns
        if self.player1_heavy_cooldown > 0:
            self.player1_heavy_cooldown -= 1
        if self.player2_heavy_cooldown > 0:
            self.player2_heavy_cooldown -= 1
        
        # Reset blocking for other player
        if self.current_player == "Player 1":
            self.player2_blocking = False
        else:
            self.player1_blocking = False
        
        # Switch turn
        self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"
        self.update_ui()

    def handle_game_end(self):
        self.game_over = True
        winner = "Player 1" if self.player2_hp <= 0 else "Player 2"
        self.scores[winner] += 1
        
        self.status_label.configure(text=f"{winner} wins!")
        self.log_action(f"Game Over! {winner} wins!")
        messagebox.showinfo("Game Over", f"{winner} wins the fight!")
        
        # Disable action buttons
        for button in [self.attack_btn, self.heavy_btn, self.block_btn, self.special_btn]:
            button.configure(state="disabled")
        
        self.update_scoreboard()

    def update_ui(self):
        # Update health bars and labels
        p1_percentage = self.player1_hp / self.max_hp
        p2_percentage = self.player2_hp / self.max_hp
        
        self.p1_health_bar.set(p1_percentage)
        self.p2_health_bar.set(p2_percentage)
        
        self.p1_hp_label.configure(text=f"HP: {self.player1_hp}/{self.max_hp}")
        self.p2_hp_label.configure(text=f"HP: {self.player2_hp}/{self.max_hp}")
        
        # Update turn status
        if not self.game_over:
            self.status_label.configure(text=f"{self.current_player}'s turn")
        
        # Update button states based on cooldowns and uses
        if not self.game_over:
            # Enable all buttons by default
            for button in [self.attack_btn, self.heavy_btn, self.block_btn, self.special_btn]:
                button.configure(state="normal")
            
            # Disable heavy attack if on cooldown
            if (self.current_player == "Player 1" and self.player1_heavy_cooldown > 0) or \
               (self.current_player == "Player 2" and self.player2_heavy_cooldown > 0):
                self.heavy_btn.configure(state="disabled")
            
            # Disable special if no uses left
            if (self.current_player == "Player 1" and self.player1_special_uses <= 0) or \
               (self.current_player == "Player 2" and self.player2_special_uses <= 0):
                self.special_btn.configure(state="disabled")
        
        # Update button text with cooldowns/uses
        heavy_text = "Heavy Attack\n(25-35 DMG)"
        special_text = "Special Move\n(40-50 DMG)"
        
        if self.current_player == "Player 1":
            if self.player1_heavy_cooldown > 0:
                heavy_text = f"Heavy Attack\n(Cooldown: {self.player1_heavy_cooldown})"
            special_text = f"Special Move\n(Uses: {self.player1_special_uses})"
        else:
            if self.player2_heavy_cooldown > 0:
                heavy_text = f"Heavy Attack\n(Cooldown: {self.player2_heavy_cooldown})"
            special_text = f"Special Move\n(Uses: {self.player2_special_uses})"
        
        self.heavy_btn.configure(text=heavy_text)
        self.special_btn.configure(text=special_text)

    def update_scoreboard(self):
        self.p1_score.configure(text=f"Player 1 Wins: {self.scores['Player 1']}")
        self.p2_score.configure(text=f"Player 2 Wins: {self.scores['Player 2']}")

    def log_action(self, message):
        self.last_action.configure(text=message)

    def reset_game(self):
        self.current_player = "Player 1"
        self.player1_hp = 100
        self.player2_hp = 100
        self.game_over = False
        
        # Reset cooldowns and uses
        self.player1_heavy_cooldown = 0
        self.player2_heavy_cooldown = 0
        self.player1_special_uses = 3
        self.player2_special_uses = 3
        self.player1_blocking = False
        self.player2_blocking = False
        
        # Enable action buttons
        for button in [self.attack_btn, self.heavy_btn, self.block_btn, self.special_btn]:
            button.configure(state="normal")
        
        self.log_action("New fight started! Player 1's turn.")
        self.update_ui()

if __name__ == "__main__":
    app = PvPFightingGame()
    app.mainloop()