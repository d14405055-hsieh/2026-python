import random
import tkinter as tk
from collections import Counter, defaultdict, namedtuple
from tkinter import messagebox, ttk

General = namedtuple(
    "General",
    ["faction", "name", "hp", "atk", "def_", "spd", "is_leader", "skill"],
)


class Unit:
    def __init__(self, general):
        self.general = general
        self.hp = general.hp
        self.defending = False

    @property
    def alive(self):
        return self.hp > 0

    @property
    def hp_percent(self):
        return max(0, int(self.hp / self.general.hp * 100))


class ChibiWarlordsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("三國武將 PK - 赤壁戰役")
        self.root.geometry("1440x900")
        self.root.minsize(1240, 800)

        self.generals = {}
        self.ally_units = []
        self.enemy_units = []
        self.turn_order = []
        self.turn_index = 0
        self.current_actor = None
        self.animating = False

        self.stats = {
            "damage": Counter(),
            "losses": defaultdict(int),
        }
        self.potions = defaultdict(lambda: 1)

        self.hp_vars = {}
        self.state_vars = {}
        self.name_labels = {}
        self.target_var = tk.StringVar()
        self.mode_var = tk.StringVar(value="新手模式")
        self.battle_mode = tk.StringVar(value="單人模式")

        self.sprite_items = {}
        self.sprite_positions = {}
        self.idle_dir = {}
        self.arena_hud_items = {}

        self.mode_settings = {
            "player_damage": 1.15,
            "enemy_damage": 0.9,
            "potions": 2,
            "ai_delay": 900,
            "auto_player": False,
            "enemy_aggressive": 0.45,
            "enemy_critical": 0.10,
        }

        self.load_generals("generals.txt")
        ally_names, enemy_names = self.load_battle_config("battles.txt")
        self.setup_ui()
        self.bind_hotkeys()
        self.reset_battle(ally_names, enemy_names)
        self.animate_idle()

    def load_generals(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line == "EOF":
                    if line == "EOF":
                        break
                    continue
                faction, name, hp, atk, def_, spd, is_leader, skill = line.split()
                self.generals[name] = General(
                    faction=faction,
                    name=name,
                    hp=int(hp),
                    atk=int(atk),
                    def_=int(def_),
                    spd=int(spd),
                    is_leader=(is_leader == "True"),
                    skill=skill,
                )

    def load_battle_config(self, filename):
        ally_names = []
        enemy_names = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line == "EOF":
                    if line == "EOF":
                        break
                    continue
                parts = line.split()
                if parts[0] == "ALLY":
                    ally_names = parts[1:]
                elif parts[0] == "ENEMY":
                    enemy_names = parts[1:]
        return ally_names, enemy_names

    def setup_ui(self):
        bg = tk.Canvas(self.root, highlightthickness=0)
        bg.pack(fill="both", expand=True)
        self.draw_background(bg)

        main = tk.Frame(bg, bg="#101f34")
        bg.create_window(720, 450, window=main, width=1400, height=860)

        title = tk.Label(
            main,
            text="赤壁戰役 Online - 武將決戰",
            fg="#f8e9b0",
            bg="#101f34",
            font=("Microsoft JhengHei", 26, "bold"),
        )
        title.pack(pady=(10, 6))

        top_bar = tk.Frame(main, bg="#101f34")
        top_bar.pack(fill="x", padx=16, pady=(0, 8))

        tk.Label(
            top_bar,
            text="遊戲模式",
            bg="#101f34",
            fg="#cfe6ff",
            font=("Microsoft JhengHei", 11),
        ).pack(side="left")

        self.mode_combo = ttk.Combobox(
            top_bar,
            textvariable=self.mode_var,
            state="readonly",
            width=12,
            values=["新手模式", "老手模式", "AI自動模式", "雙人對戰"],
            font=("Microsoft JhengHei", 10),
        )
        self.mode_combo.pack(side="left", padx=(8, 8))
        self.mode_combo.bind("<<ComboboxSelected>>", self.on_mode_change)

        ttk.Button(top_bar, text="規則說明", command=self.show_rules).pack(side="left", padx=4)
        ttk.Button(top_bar, text="重新開局", command=self.restart_game).pack(side="right")

        body = tk.Frame(main, bg="#101f34")
        body.pack(fill="both", expand=True, padx=16, pady=4)

        ally_panel = tk.Frame(body, bg="#0d192b", width=280, bd=1, relief="solid")
        ally_panel.pack(side="left", fill="y", padx=(0, 10))
        ally_panel.pack_propagate(False)

        tk.Label(
            ally_panel,
            text="蜀吳聯軍",
            fg="#d6ffd0",
            bg="#0d192b",
            font=("Microsoft JhengHei", 15, "bold"),
        ).pack(pady=(8, 8))

        self.ally_frame = tk.Frame(ally_panel, bg="#0d192b")
        self.ally_frame.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        field = tk.Frame(body, bg="#101f34")
        field.pack(side="left", fill="both", expand=True)

        self.battle_canvas = tk.Canvas(
            field,
            width=780,
            height=520,
            bg="#162a45",
            highlightthickness=1,
            highlightbackground="#2f4a73",
        )
        self.battle_canvas.pack(fill="both", expand=True, pady=(0, 10))
        self.draw_battle_arena()

        right_panel = tk.Frame(body, bg="#0d192b", width=300, bd=1, relief="solid")
        right_panel.pack(side="left", fill="y", padx=(10, 0))
        right_panel.pack_propagate(False)

        tk.Label(
            right_panel,
            text="曹魏陣營",
            fg="#ffd0d0",
            bg="#0d192b",
            font=("Microsoft JhengHei", 15, "bold"),
        ).pack(pady=(8, 8))

        self.enemy_frame = tk.Frame(right_panel, bg="#0d192b")
        self.enemy_frame.pack(fill="x", padx=8, pady=(0, 8))

        rule_card = tk.Label(
            right_panel,
            text=(
                "快速上手\n"
                "1. 速度高先手\n"
                "2. 先打倒 3 名魏將獲勝\n"
                "3. 防禦可減半下一擊\n"
                "4. 每名武將可補給有限次\n"
                "5. 武將技有專屬特效\n"
                "6. 雙人對戰時，1P用WASD，2P用方向鍵\n"
                "單人鍵盤: 1攻 2技 3防 4補 Tab換目標"
            ),
            justify="left",
            bg="#1a2740",
            fg="#d7ebff",
            padx=12,
            pady=8,
            width=26,
            wraplength=250,
            font=("Microsoft JhengHei", 10),
        )
        rule_card.pack(fill="x", padx=10, pady=(6, 8))

        tk.Label(
            right_panel,
            text="戰鬥紀錄",
            bg="#0b1728",
            fg="#f3f7ff",
            font=("Microsoft JhengHei", 14, "bold"),
        ).pack(pady=(2, 6))

        self.log_box = tk.Text(
            right_panel,
            width=32,
            height=12,
            bg="#09111d",
            fg="#d7f0ff",
            insertbackground="#d7f0ff",
            font=("Consolas", 10),
            state="disabled",
            wrap="word",
        )
        self.log_box.pack(padx=10)

        control = tk.Frame(main, bg="#0c1728", bd=1, relief="solid")
        control.pack(fill="x", padx=16, pady=(6, 12))

        self.turn_label = tk.Label(
            control,
            text="",
            fg="#ffe9ad",
            bg="#0c1728",
            font=("Microsoft JhengHei", 13, "bold"),
        )
        self.turn_label.pack(anchor="w", padx=12, pady=(8, 8))

        control_bar = tk.Frame(control, bg="#0c1728")
        control_bar.pack(fill="x", padx=12, pady=(0, 6))

        tk.Label(
            control_bar,
            text="目標",
            bg="#0c1728",
            fg="#d7e8ff",
            font=("Microsoft JhengHei", 11),
        ).pack(side="left")

        self.target_combo = ttk.Combobox(
            control_bar,
            textvariable=self.target_var,
            width=12,
            state="readonly",
            font=("Microsoft JhengHei", 11),
        )
        self.target_combo.pack(side="left", padx=(8, 16))

        self.attack_btn = ttk.Button(control_bar, text="普通攻擊", command=self.player_attack)
        self.skill_btn = ttk.Button(control_bar, text="必殺技", command=self.player_skill)
        self.defend_btn = ttk.Button(control_bar, text="防禦", command=self.player_defend)
        self.heal_btn = ttk.Button(control_bar, text="補給", command=self.player_heal)

        self.attack_btn.pack(side="left", padx=4)
        self.skill_btn.pack(side="left", padx=4)
        self.defend_btn.pack(side="left", padx=4)
        self.heal_btn.pack(side="left", padx=4)

        hint_row = tk.Frame(control, bg="#0c1728")
        hint_row.pack(fill="x", padx=12, pady=(0, 10))

        tk.Label(
            hint_row,
            text="單人: 1攻 2技 3防 4補；雙人: WASD / 方向鍵",
            bg="#0c1728",
            fg="#96b7d9",
            font=("Microsoft JhengHei", 10),
            anchor="w",
        ).pack(side="left", fill="x")

    def draw_background(self, canvas):
        for i in range(48):
            color = f"#{8 + i:02x}{22 + i:02x}{42 + i:02x}"
            canvas.create_rectangle(0, i * 18, 1500, i * 18 + 18, fill=color, outline="")
        canvas.create_oval(-100, -80, 360, 280, fill="#f5cb70", outline="", stipple="gray25")
        canvas.create_polygon(0, 620, 330, 350, 600, 620, fill="#1a2f4d", outline="")
        canvas.create_polygon(360, 620, 760, 280, 1130, 620, fill="#173453", outline="")
        canvas.create_polygon(840, 620, 1160, 380, 1500, 620, fill="#122a45", outline="")

    def draw_battle_arena(self):
        c = self.battle_canvas
        c.delete("all")
        w = 760
        h = 500
        c.create_rectangle(0, 0, w, h, fill="#1b3457", outline="")
        for i in range(26):
            shade = 32 + i
            c.create_rectangle(0, i * 13, w, i * 13 + 13, fill=f"#{shade:02x}{56 + i:02x}{84 + i:02x}", outline="")

        c.create_polygon(0, 350, 240, 220, 420, 350, fill="#2b4665", outline="")
        c.create_polygon(220, 350, 460, 210, 700, 350, fill="#2a415f", outline="")
        c.create_rectangle(0, 350, w, h, fill="#6b533f", outline="")

        for i in range(140):
            x = random.randint(40, 720)
            y = random.randint(120, 334)
            c.create_line(x, y, x + random.randint(-2, 2), y + 8, fill="#2e2b22")

        for i in range(45):
            x = random.randint(18, 360)
            y = random.randint(240, 335)
            c.create_oval(x, y, x + 5, y + 5, fill="#c1b9a8", outline="")
            c.create_line(x + 2, y + 3, x + 2, y + 12, fill="#5a4f41")
        for i in range(45):
            x = random.randint(390, 742)
            y = random.randint(240, 335)
            c.create_oval(x, y, x + 5, y + 5, fill="#c1b9a8", outline="")
            c.create_line(x + 2, y + 3, x + 2, y + 12, fill="#5a4f41")

        c.create_text(380, 28, text="赤壁主戰場", fill="#f6e6b2", font=("Microsoft JhengHei", 18, "bold"))
        c.create_text(108, 62, text="蜀吳", fill="#d6ffd0", font=("Microsoft JhengHei", 13, "bold"))
        c.create_text(652, 62, text="曹魏", fill="#ffd0d0", font=("Microsoft JhengHei", 13, "bold"))

        left_frame = c.create_rectangle(36, 72, 320, 110, fill="#0a1320", outline="#315b86", width=2)
        right_frame = c.create_rectangle(440, 72, 724, 110, fill="#0a1320", outline="#86535a", width=2)
        left_bar = c.create_rectangle(44, 84, 310, 98, fill="#4fc06f", outline="")
        right_bar = c.create_rectangle(448, 84, 716, 98, fill="#d65c63", outline="")
        left_text = c.create_text(177, 91, text="蜀吳聯軍 100%", fill="#ecfff1", font=("Microsoft JhengHei", 10, "bold"))
        right_text = c.create_text(582, 91, text="曹魏軍 100%", fill="#fff0f0", font=("Microsoft JhengHei", 10, "bold"))

        self.arena_hud_items = {
            "left_frame": left_frame,
            "right_frame": right_frame,
            "left_bar": left_bar,
            "right_bar": right_bar,
            "left_text": left_text,
            "right_text": right_text,
        }

    def update_arena_hud(self):
        if not self.arena_hud_items:
            return

        ally_total = sum(u.general.hp for u in self.ally_units)
        ally_now = sum(max(0, u.hp) for u in self.ally_units)
        enemy_total = sum(u.general.hp for u in self.enemy_units)
        enemy_now = sum(max(0, u.hp) for u in self.enemy_units)

        ally_ratio = 0 if ally_total == 0 else ally_now / ally_total
        enemy_ratio = 0 if enemy_total == 0 else enemy_now / enemy_total

        self.battle_canvas.coords(self.arena_hud_items["left_bar"], 44, 84, 44 + int(266 * ally_ratio), 98)
        self.battle_canvas.coords(self.arena_hud_items["right_bar"], 448, 84, 448 + int(268 * enemy_ratio), 98)
        self.battle_canvas.itemconfigure(
            self.arena_hud_items["left_text"],
            text=f"蜀吳聯軍 {int(ally_ratio * 100)}%",
        )
        self.battle_canvas.itemconfigure(
            self.arena_hud_items["right_text"],
            text=f"曹魏軍 {int(enemy_ratio * 100)}%",
        )

    def on_mode_change(self, _event=None):
        self.apply_mode_settings()
        self.log(f"已切換到 {self.mode_var.get()}。")

    def apply_mode_settings(self):
        mode = self.mode_var.get()
        if mode == "新手模式":
            self.mode_settings = {
                "player_damage": 1.15,
                "enemy_damage": 0.88,
                "potions": 2,
                "ai_delay": 900,
                "auto_player": False,
                "enemy_aggressive": 0.45,
                "enemy_critical": 0.10,
            }
        elif mode == "老手模式":
            self.mode_settings = {
                "player_damage": 0.90,
                "enemy_damage": 1.30,
                "potions": 1,
                "ai_delay": 420,
                "auto_player": False,
                "enemy_aggressive": 0.82,
                "enemy_critical": 0.35,
            }
        elif mode == "AI自動模式":
            self.mode_settings = {
                "player_damage": 1.0,
                "enemy_damage": 1.0,
                "potions": 1,
                "ai_delay": 650,
                "auto_player": True,
                "enemy_aggressive": 0.55,
                "enemy_critical": 0.18,
            }
        else:
            self.mode_settings = {
                "player_damage": 1.0,
                "enemy_damage": 1.0,
                "potions": 1,
                "ai_delay": 0,
                "auto_player": False,
                "enemy_aggressive": 0.55,
                "enemy_critical": 0.18,
            }

    def show_rules(self):
        text = (
            "【遊戲規則】\n"
            "1. 每回合依速度值高低決定先後手。\n"
            "2. 你操作蜀吳聯軍，擊倒所有魏將即勝利。\n"
            "3. 普攻穩定，必殺技較強但效果因武將不同。\n"
            "4. 防禦可讓下一次受傷減半。\n"
            "5. 補給每名武將有次數限制。\n"
            "6. AI自動模式會由電腦代你操作我方。\n"
            "7. 雙人對戰時，1號玩家控制蜀吳聯軍，2號玩家控制曹魏軍。\n\n"
            "【操作方式】\n"
            "滑鼠: 點擊按鈕與目標。\n"
            "鍵盤: 1普通攻擊、2必殺技、3防禦、4補給、Tab切換目標。\n"
            "雙人對戰: 1P=W A S D，2P=方向鍵。\n"
            "其他: H開啟規則、R重新開局、M切換模式。"
        )
        messagebox.showinfo("規則說明", text)

    def bind_hotkeys(self):
        self.root.bind("1", lambda _e: self.player_attack())
        self.root.bind("2", lambda _e: self.player_skill())
        self.root.bind("3", lambda _e: self.player_defend())
        self.root.bind("4", lambda _e: self.player_heal())
        self.root.bind("<Tab>", self.hotkey_next_target)
        self.root.bind("w", lambda _e: self.dual_hotkey("player1", "attack"))
        self.root.bind("W", lambda _e: self.dual_hotkey("player1", "attack"))
        self.root.bind("a", lambda _e: self.dual_hotkey("player1", "skill"))
        self.root.bind("A", lambda _e: self.dual_hotkey("player1", "skill"))
        self.root.bind("s", lambda _e: self.dual_hotkey("player1", "defend"))
        self.root.bind("S", lambda _e: self.dual_hotkey("player1", "defend"))
        self.root.bind("d", lambda _e: self.dual_hotkey("player1", "heal"))
        self.root.bind("D", lambda _e: self.dual_hotkey("player1", "heal"))
        self.root.bind("<Up>", lambda _e: self.dual_hotkey("player2", "attack"))
        self.root.bind("<Left>", lambda _e: self.dual_hotkey("player2", "skill"))
        self.root.bind("<Down>", lambda _e: self.dual_hotkey("player2", "defend"))
        self.root.bind("<Right>", lambda _e: self.dual_hotkey("player2", "heal"))
        self.root.bind("r", lambda _e: self.restart_game())
        self.root.bind("R", lambda _e: self.restart_game())
        self.root.bind("h", lambda _e: self.show_rules())
        self.root.bind("H", lambda _e: self.show_rules())
        self.root.bind("m", self.hotkey_cycle_mode)
        self.root.bind("M", self.hotkey_cycle_mode)

    def hotkey_next_target(self, event=None):
        enemies = self.target_combo.cget("values")
        if not enemies:
            return "break"
        current = self.target_var.get()
        if current not in enemies:
            self.target_var.set(enemies[0])
            return "break"
        idx = enemies.index(current)
        self.target_var.set(enemies[(idx + 1) % len(enemies)])
        return "break"

    def hotkey_cycle_mode(self, event=None):
        modes = ["新手模式", "老手模式", "AI自動模式", "雙人對戰"]
        current = self.mode_var.get()
        idx = modes.index(current) if current in modes else 0
        next_mode = modes[(idx + 1) % len(modes)]
        self.mode_var.set(next_mode)
        self.on_mode_change()

    def is_duel_mode(self):
        return self.mode_var.get() == "雙人對戰"

    def get_target_group_for_actor(self, actor):
        if self.is_duel_mode():
            return self.enemy_units if actor in self.ally_units else self.ally_units
        return self.enemy_units

    def update_target_options(self):
        actor = self.current_actor
        if not actor:
            return
        target_group = self.get_target_group_for_actor(actor)
        targets = [u.general.name for u in target_group if u.alive]
        self.target_combo["values"] = targets
        if self.target_var.get() not in targets and targets:
            self.target_var.set(targets[0])

    def dual_hotkey(self, player_tag, action):
        if not self.is_duel_mode():
            return
        if player_tag == "player1" and self.current_actor in self.ally_units:
            self.handle_action(action)
        elif player_tag == "player2" and self.current_actor in self.enemy_units:
            self.handle_action(action)

    def handle_action(self, action):
        if action == "attack":
            self.player_attack()
        elif action == "skill":
            self.player_skill()
        elif action == "defend":
            self.player_defend()
        elif action == "heal":
            self.player_heal()

    def reset_battle(self, ally_names, enemy_names):
        self.apply_mode_settings()
        self.stats["damage"].clear()
        self.stats["losses"].clear()
        self.potions.clear()

        self.ally_units = [Unit(self.generals[name]) for name in ally_names if name in self.generals]
        self.enemy_units = [Unit(self.generals[name]) for name in enemy_names if name in self.generals]
        self.turn_order = []
        self.turn_index = 0
        self.current_actor = None
        self.animating = False

        for unit in self.ally_units + self.enemy_units:
            self.potions[unit.general.name] = self.mode_settings["potions"]

        self.build_cards()
        self.draw_battle_sprites()
        if self.is_duel_mode():
            self.log_box_set("戰役開始，目前模式：雙人對戰（1P=WASD，2P=方向鍵）。")
        else:
            self.log_box_set(f"戰役開始，目前模式：{self.mode_var.get()}。")
        self.start_round()

    def build_cards(self):
        for w in self.enemy_frame.winfo_children():
            w.destroy()
        for w in self.ally_frame.winfo_children():
            w.destroy()

        self.hp_vars.clear()
        self.state_vars.clear()
        self.name_labels.clear()

        for u in self.enemy_units:
            self.create_card(self.enemy_frame, u, enemy=True)
        for u in self.ally_units:
            self.create_card(self.ally_frame, u, enemy=False)

        self.refresh_ui()

    def create_card(self, parent, unit, enemy):
        side_bg = "#3b1e2e" if enemy else "#1f3a2f"
        fg_name = "#ffd8df" if enemy else "#dafedb"

        card = tk.Frame(parent, bg=side_bg, bd=1, relief="groove")
        card.pack(fill="x", padx=2, pady=4)

        top = tk.Frame(card, bg=side_bg)
        top.pack(fill="x", padx=8, pady=(6, 2))

        avatar = tk.Canvas(top, width=26, height=26, bg=side_bg, highlightthickness=0)
        avatar.pack(side="left", padx=(0, 6))
        avatar.create_oval(2, 2, 24, 24, fill="#efcfaa", outline="#222")
        avatar.create_rectangle(7, 14, 19, 24, fill="#6aa6d8" if not enemy else "#bf6f7f", outline="")

        name_text = f"{unit.general.name} ({unit.general.faction})"
        if unit.general.is_leader:
            name_text += " 軍師"

        name_label = tk.Label(
            top,
            text=name_text,
            bg=side_bg,
            fg=fg_name,
            font=("Microsoft JhengHei", 11, "bold"),
        )
        name_label.pack(side="left", padx=(0, 4))

        stat = tk.Label(
            top,
            text=f"攻{unit.general.atk} 防{unit.general.def_} 速{unit.general.spd}",
            bg=side_bg,
            fg="#e7edf8",
            font=("Microsoft JhengHei", 10),
        )
        stat.pack(side="right")

        hp_var = tk.StringVar(value=f"HP: {unit.hp}/{unit.general.hp}")
        tk.Label(
            card,
            textvariable=hp_var,
            bg=side_bg,
            fg="#fff3bd",
            font=("Consolas", 10),
        ).pack(anchor="w", padx=8)

        bar = ttk.Progressbar(card, maximum=100, value=unit.hp_percent)
        bar.pack(fill="x", padx=8, pady=(2, 4))

        state_var = tk.StringVar(value="待命")
        tk.Label(
            card,
            textvariable=state_var,
            bg=side_bg,
            fg="#d9f2ff",
            font=("Microsoft JhengHei", 10),
        ).pack(anchor="w", padx=8, pady=(0, 6))

        self.hp_vars[unit.general.name] = (hp_var, bar)
        self.state_vars[unit.general.name] = state_var
        self.name_labels[unit.general.name] = name_label

    def draw_battle_sprites(self):
        self.draw_battle_arena()
        self.sprite_items.clear()
        self.sprite_positions.clear()
        self.idle_dir.clear()

        enemy_points = [(592, 224), (688, 278), (548, 306)]
        ally_points = [(180, 236), (95, 286), (232, 318)]

        for unit, pos in zip(self.enemy_units, enemy_points):
            self.create_sprite(unit, pos[0], pos[1], enemy=True)
        for unit, pos in zip(self.ally_units, ally_points):
            self.create_sprite(unit, pos[0], pos[1], enemy=False)

    def create_sprite(self, unit, x, y, enemy):
        c = self.battle_canvas
        body_color = "#b94e62" if enemy else "#4aa05f"
        cape_color = "#f3c06a" if enemy else "#8ac6ff"
        sword_color = "#d6d6d6"
        aura_color = "#ed7388" if enemy else "#74e0a1"

        aura = c.create_oval(x - 30, y - 34, x + 30, y + 30, outline=aura_color, width=2)
        shadow = c.create_oval(x - 26, y + 30, x + 26, y + 42, fill="#0f1f34", outline="")
        body = c.create_rectangle(x - 18, y - 2, x + 18, y + 30, fill=body_color, outline="#111")
        head = c.create_oval(x - 12, y - 24, x + 12, y, fill="#f2d2ad", outline="#222")
        cape = c.create_polygon(x - 18, y + 4, x - 29, y + 26, x - 18, y + 30, fill=cape_color, outline="")
        weapon = c.create_line(x + 16, y + 8, x + 36, y - 16, fill=sword_color, width=3)
        name = c.create_text(x, y + 54, text=unit.general.name, fill="#f7f7f7", font=("Microsoft JhengHei", 10, "bold"))

        self.sprite_items[unit.general.name] = [aura, shadow, body, head, cape, weapon, name]
        self.sprite_positions[unit.general.name] = [x, y]
        self.idle_dir[unit.general.name] = 1

    def animate_idle(self):
        if self.sprite_items and not self.animating:
            for name, items in self.sprite_items.items():
                unit = self.find_unit(name, self.ally_units + self.enemy_units)
                if not unit or not unit.alive:
                    continue
                dy = self.idle_dir[name]
                for item in items[2:6]:
                    self.battle_canvas.move(item, 0, dy)
                self.battle_canvas.move(items[6], 0, dy)
                self.sprite_positions[name][1] += dy
                self.idle_dir[name] = -dy
        self.root.after(260, self.animate_idle)

    def living_allies(self):
        return [u for u in self.ally_units if u.alive]

    def living_enemies(self):
        return [u for u in self.enemy_units if u.alive]

    def all_living_units(self):
        return [u for u in self.ally_units + self.enemy_units if u.alive]

    def start_round(self):
        self.turn_order = sorted(self.all_living_units(), key=lambda x: x.general.spd, reverse=True)
        self.turn_index = 0
        self.next_turn()

    def next_turn(self):
        if self.check_victory():
            return
        if self.animating:
            self.root.after(120, self.next_turn)
            return

        if not self.turn_order or self.turn_index >= len(self.turn_order):
            self.start_round()
            return

        actor = self.turn_order[self.turn_index]
        if not actor.alive:
            self.turn_index += 1
            self.next_turn()
            return

        actor.defending = False
        self.current_actor = actor
        is_ally = actor in self.ally_units
        if self.is_duel_mode():
            team_text = "1P" if is_ally else "2P"
        else:
            team_text = "我方" if is_ally else "敵方"
        self.turn_label.config(text=f"{team_text}回合：{actor.general.name}")

        for state_var in self.state_vars.values():
            if state_var.get() == "行動中":
                state_var.set("待命")
        self.state_vars[actor.general.name].set("行動中")

        if is_ally:
            self.update_target_options()
            if self.mode_settings["auto_player"]:
                self.enable_player_controls(False)
                self.log(f"AI 代打：{actor.general.name} 思考中...")
                self.root.after(self.mode_settings["ai_delay"], self.auto_player_action)
            elif self.is_duel_mode():
                self.enable_player_controls(False)
                self.log(f"1P 行動：{actor.general.name}，請使用 WASD。")
            else:
                self.enable_player_controls(True)
                self.log(f"{actor.general.name} 準備出手。")
        else:
            self.update_target_options()
            if self.is_duel_mode():
                self.enable_player_controls(False)
                self.log(f"2P 行動：{actor.general.name}，請使用方向鍵。")
            else:
                self.enable_player_controls(False)
                self.root.after(self.mode_settings["ai_delay"], self.ai_action)

    def enable_player_controls(self, enabled):
        state = "normal" if enabled else "disabled"
        self.attack_btn.config(state=state)
        self.skill_btn.config(state=state)
        self.defend_btn.config(state=state)
        self.heal_btn.config(state=state)
        self.target_combo.config(state="readonly" if enabled else "disabled")

    def find_unit(self, name, group):
        for u in group:
            if u.general.name == name:
                return u
        return None

    def animate_actor_dash(self, name, forward=18):
        items = self.sprite_items.get(name)
        if not items:
            return
        for item in items[2:7]:
            self.battle_canvas.move(item, forward, 0)
        self.root.after(110, lambda: self.animate_actor_return(name, -forward))

    def animate_actor_return(self, name, backward):
        items = self.sprite_items.get(name)
        if not items:
            return
        for item in items[2:7]:
            self.battle_canvas.move(item, backward, 0)

    def play_hit_effect(self, attacker_name, defender_name, color="#ffd166"):
        if attacker_name not in self.sprite_positions or defender_name not in self.sprite_positions:
            return
        self.animating = True
        c = self.battle_canvas
        ax, ay = self.sprite_positions[attacker_name]
        dx, dy = self.sprite_positions[defender_name]
        slash = c.create_line(ax, ay - 4, dx, dy - 8, fill=color, width=5)
        flash = c.create_oval(dx - 28, dy - 28, dx + 28, dy + 28, outline=color, width=4)
        self.animate_actor_dash(attacker_name, 16 if ax < dx else -16)
        self.root.after(140, lambda: c.delete(slash))
        self.root.after(220, lambda: c.delete(flash))
        self.root.after(260, lambda: self.set_animating(False))

    def play_fire_effect(self, targets):
        self.animating = True
        c = self.battle_canvas
        particles = []
        for target in targets:
            if target.general.name not in self.sprite_positions:
                continue
            x, y = self.sprite_positions[target.general.name]
            for _ in range(8):
                px = random.randint(x - 20, x + 20)
                py = random.randint(y - 22, y + 10)
                p = c.create_oval(px, py, px + 7, py + 7, fill="#ff8c42", outline="")
                particles.append(p)
        self.root.after(180, lambda: self.clear_particles(particles))

    def play_heal_effect(self, target_name):
        if target_name not in self.sprite_positions:
            return
        self.animating = True
        c = self.battle_canvas
        x, y = self.sprite_positions[target_name]
        ring1 = c.create_oval(x - 14, y - 14, x + 14, y + 14, outline="#7dffaf", width=3)
        ring2 = c.create_oval(x - 24, y - 24, x + 24, y + 24, outline="#7dffaf", width=2)
        mark = c.create_text(x, y - 34, text="+", fill="#c6ffd8", font=("Consolas", 24, "bold"))
        self.root.after(180, lambda: c.delete(ring1))
        self.root.after(240, lambda: c.delete(ring2))
        self.root.after(280, lambda: c.delete(mark))
        self.root.after(320, lambda: self.set_animating(False))

    def play_ultimate_animation(self, title, color):
        self.animating = True
        c = self.battle_canvas
        w = int(c.cget("width"))
        h = int(c.cget("height"))
        veil = c.create_rectangle(0, 0, w, h, fill="#000000", stipple="gray50", outline="")
        text = c.create_text(w // 2, h // 2, text=title, fill=color, font=("Microsoft JhengHei", 38, "bold"))
        line = c.create_line(w // 2 - 250, h // 2 + 50, w // 2 + 250, h // 2 + 50, fill=color, width=5)
        self.root.after(420, lambda: c.delete(veil))
        self.root.after(420, lambda: c.delete(text))
        self.root.after(420, lambda: c.delete(line))
        self.root.after(460, lambda: self.set_animating(False))

    def clear_particles(self, particles):
        for p in particles:
            self.battle_canvas.delete(p)
        self.set_animating(False)

    def set_animating(self, value):
        self.animating = value

    def apply_damage(self, attacker, defender, multiplier=1.0, note="普通攻擊", effect_color="#ffd166"):
        if attacker in self.ally_units:
            mode_bonus = self.mode_settings["player_damage"]
        else:
            mode_bonus = self.mode_settings["enemy_damage"]

        base = int(attacker.general.atk * multiplier * mode_bonus)
        damage = max(1, base - defender.general.def_ // 2)
        if defender.defending:
            damage = max(1, damage // 2)

        defender.hp = max(0, defender.hp - damage)
        self.stats["damage"][attacker.general.name] += damage
        self.stats["losses"][defender.general.name] += damage

        self.play_hit_effect(attacker.general.name, defender.general.name, color=effect_color)
        self.log(f"{attacker.general.name} 使用{note}，對 {defender.general.name} 造成 {damage} 傷害。")
        if not defender.alive:
            self.log(f"{defender.general.name} 倒下了。")

    def heal_unit(self, source, target, amount, note="治療"):
        old = target.hp
        target.hp = min(target.general.hp, target.hp + amount)
        gain = target.hp - old
        self.play_heal_effect(target.general.name)
        self.log(f"{source.general.name} 使用{note}，{target.general.name} 回復 {gain} HP。")

    def player_attack(self):
        target_name = self.target_var.get()
        target_group = self.get_target_group_for_actor(self.current_actor)
        target = self.find_unit(target_name, target_group)
        if not self.current_actor or not target or not target.alive or self.animating:
            return
        self.apply_damage(self.current_actor, target, note="普通攻擊")
        self.end_actor_turn()

    def player_skill(self):
        actor = self.current_actor
        if not actor or self.animating:
            return

        skill = actor.general.skill
        if skill == "fire":
            self.play_ultimate_animation("火鳳燎原", "#ff9e4d")
            enemies = [u for u in self.get_target_group_for_actor(actor) if u.alive]
            self.root.after(500, lambda: self.play_fire_effect(enemies))
            for enemy in enemies:
                self.apply_damage(actor, enemy, multiplier=0.9, note="火攻", effect_color="#ff8c42")
        elif skill in ("strategy", "command"):
            self.play_ultimate_animation("八陣回春", "#8bffbb")
            friends = self.ally_units if actor in self.ally_units else self.enemy_units
            friends = [u for u in friends if u.alive]
            for ally in friends:
                self.heal_unit(actor, ally, amount=14, note="軍略")
        else:
            target_name = self.target_var.get()
            target_group = self.get_target_group_for_actor(actor)
            target = self.find_unit(target_name, target_group)
            if target and target.alive:
                self.play_ultimate_animation("無雙斬", "#ffe187")
                self.apply_damage(actor, target, multiplier=1.55, note="必殺技", effect_color="#ffe187")

        self.end_actor_turn()

    def player_defend(self):
        if not self.current_actor or self.animating:
            return
        self.current_actor.defending = True
        self.log(f"{self.current_actor.general.name} 進入防禦姿態，下一次受傷減半。")
        self.end_actor_turn()

    def player_heal(self):
        actor = self.current_actor
        if not actor or self.animating:
            return
        if self.potions[actor.general.name] <= 0:
            self.log(f"{actor.general.name} 的補給已用完。")
            return
        self.potions[actor.general.name] -= 1
        self.heal_unit(actor, actor, amount=28, note="戰地補給")
        self.end_actor_turn()

    def auto_player_action(self):
        actor = self.current_actor
        if not actor or not actor.alive:
            self.end_actor_turn()
            return

        enemies = self.living_enemies()
        if not enemies:
            self.end_actor_turn()
            return

        low_hp = actor.hp_percent < 35 and self.potions[actor.general.name] > 0
        if low_hp:
            self.player_heal()
            return

        if random.random() < 0.45:
            target = min(enemies, key=lambda x: x.hp)
            self.target_var.set(target.general.name)
            self.player_skill()
        else:
            target = random.choice(enemies)
            self.target_var.set(target.general.name)
            self.player_attack()

    def ai_action(self):
        actor = self.current_actor
        if not actor or not actor.alive:
            self.end_actor_turn()
            return

        targets = self.living_allies()
        if not targets:
            self.end_actor_turn()
            return

        choice = random.random()
        if choice < 0.2:
            actor.defending = True
            self.log(f"{actor.general.name} 採取防禦姿態。")
        elif choice < 0.48 and actor.general.skill in ("command", "strategy"):
            allies = [u for u in self.enemy_units if u.alive]
            heal_target = min(allies, key=lambda x: x.hp_percent)
            self.heal_unit(actor, heal_target, 14, note="軍略")
        elif choice < self.mode_settings["enemy_aggressive"] and actor.general.skill == "fire":
            self.play_ultimate_animation("烈焰突襲", "#ff8452")
            self.play_fire_effect(targets)
            for t in targets:
                self.apply_damage(actor, t, multiplier=0.8, note="火攻", effect_color="#ff8c42")
        else:
            target = random.choice(targets)
            critical = self.mode_settings.get("enemy_critical", 0)
            multi = 1.35 if actor.general.skill in ("slash", "spear") and random.random() < 0.5 else 1.0
            if random.random() < critical:
                multi *= 1.55
            note = "突擊" if multi > 1 else "普通攻擊"
            color = "#ffaf66" if multi > 1 else "#ffd166"
            self.apply_damage(actor, target, multiplier=multi, note=note, effect_color=color)

        self.end_actor_turn()

    def end_actor_turn(self):
        self.refresh_ui()
        if self.check_victory():
            return
        self.turn_index += 1
        self.root.after(480, self.next_turn)

    def refresh_ui(self):
        for unit in self.ally_units + self.enemy_units:
            hp_var, bar = self.hp_vars[unit.general.name]
            hp_var.set(f"HP: {unit.hp}/{unit.general.hp}")
            bar["value"] = unit.hp_percent

            if not unit.alive:
                self.state_vars[unit.general.name].set("陣亡")
                self.name_labels[unit.general.name].config(fg="#8a8f9b")
                for item in self.sprite_items.get(unit.general.name, []):
                    if item != self.sprite_items[unit.general.name][1]:
                        self.battle_canvas.itemconfigure(item, state="hidden")
            elif unit.defending:
                self.state_vars[unit.general.name].set("防禦")
            elif self.state_vars[unit.general.name].get() != "行動中":
                self.state_vars[unit.general.name].set("待命")

        self.update_arena_hud()
        self.update_target_options()

    def check_victory(self):
        if not self.living_enemies():
            self.finish_battle(player_win=True)
            return True
        if not self.living_allies():
            self.finish_battle(player_win=False)
            return True
        return False

    def finish_battle(self, player_win):
        self.enable_player_controls(False)
        self.turn_label.config(text="戰役結束")

        total_damage = sum(self.stats["damage"].values())
        ranking = self.stats["damage"].most_common(3)
        rank_text = "、".join([f"{n}:{d}" for n, d in ranking]) if ranking else "無"

        if player_win:
            self.log("蜀吳聯軍獲勝，赤壁大捷。")
            message = "你獲勝了。"
        else:
            self.log("魏軍獲勝，戰線潰敗。")
            message = "你落敗了。"

        message += f"\n總傷害: {total_damage}\n前三名輸出: {rank_text}\n模式: {self.mode_var.get()}"
        messagebox.showinfo("戰役結果", message)

    def restart_game(self):
        ally_names = [u.general.name for u in self.ally_units]
        enemy_names = [u.general.name for u in self.enemy_units]
        self.reset_battle(ally_names, enemy_names)

    def log(self, text):
        self.log_box.config(state="normal")
        self.log_box.insert("end", f"{text}\n")
        self.log_box.see("end")
        self.log_box.config(state="disabled")

    def log_box_set(self, text):
        self.log_box.config(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.insert("end", f"{text}\n")
        self.log_box.config(state="disabled")


if __name__ == "__main__":
    random.seed()
    root = tk.Tk()
    app = ChibiWarlordsGame(root)
    root.mainloop()
