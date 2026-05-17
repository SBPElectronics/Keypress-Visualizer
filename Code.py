import tkinter as tk
from pynput import keyboard, mouse

# Structured QWERTY matrix
KEYBOARD_LAYOUT = [
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
    ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
    ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";"],
    ["shift", "z", "x", "c", "v", "b", "n", "m", "space"]
]

class AestheticOverlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aesthetic Input HUD")
        
        # Dimensions optimized for ultra-sleek spacing
        self.root.geometry("460x215+20+20")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        
        # Windows Chroma Key Transparency Engine
        self.trans_color = "#abcdef" 
        self.root.configure(bg=self.trans_color)
        self.root.attributes("-transparentcolor", self.trans_color)

        # --- LUXURY BRAND DESIGN PALETTE ---
        self.panel_bg = "#121214"         # Slate Obsidian
        self.border_color = "#26262b"     # Subtle Charcoal Border
        
        self.key_idle_bg = "#1a1a1e"      # Deep Matte Keycap
        self.key_idle_fg = "#80808c"      # Low-lit Silver Legend Text
        
        self.key_active_bg = "#ffffff"    # Pure White illumination
        self.key_active_fg = "#0a0a0c"    # Stark contrast text
        
        self.mouse_active_bg = "#ff4757"  # Clean Crimson Highlight for Mouse Clicks
        self.mouse_active_fg = "#ffffff"

        # Text stream buffers
        self.typed_text = ""
        self.char_count = 0

        # Click & Drag Window Hooks
        self.root.bind("<Button-1>", self.start_drag)
        self.root.bind("<B1-Motion>", self.do_drag)

        self.key_buttons = {}
        
        # Build interface (Header -> Live Feed -> Keypad Matrix)
        self.create_header_gui()
        self.create_text_feed_gui()
        self.create_keyboard_gui()

        # Start low-level input hooks
        self.kb_listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
        self.kb_listener.start()

        self.mouse_listener = mouse.Listener(on_click=self.on_mouse_click)
        self.mouse_listener.start()

    # --- SMOOTH DESKTOP NAVIGATION ENGINE ---
    def start_drag(self, event):
        self.x = event.x
        self.y = event.y

    def do_drag(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")

    # --- COMPONENT BUILDERS ---
    def create_header_gui(self):
        # Top utility layout container
        header_frame = tk.Frame(self.root, bg=self.trans_color)
        header_frame.pack(side="top", fill="x", padx=12, pady=(4, 2))
        
        # Wrapper to style borders cleanly in Tkinter
        drag_box = tk.Frame(header_frame, bg=self.border_color, padx=1, pady=1)
        drag_box.pack(side="left")
        
        # Clean brand indicator label acting as the main drag handle
        drag_hint = tk.Label(
            drag_box, 
            text=" ✦  S Y S T E M  M O N I T O R ", 
            bg=self.panel_bg, 
            fg="#6b6b75", 
            font=("Segoe UI", 7, "bold"), 
            padx=10, 
            pady=3
        )
        drag_hint.pack()

        # Premium flat Mouse Status indicators
        mouse_box_r = tk.Frame(header_frame, bg=self.border_color, padx=1, pady=1)
        mouse_box_r.pack(side="right", padx=(3, 0))
        self.right_click_lbl = tk.Label(mouse_box_r, text="R-CLK", width=7, bg=self.key_idle_bg, fg=self.key_idle_fg, font=("Segoe UI", 7, "bold"), pady=3)
        self.right_click_lbl.pack()

        mouse_box_l = tk.Frame(header_frame, bg=self.border_color, padx=1, pady=1)
        mouse_box_l.pack(side="right", padx=3)
        self.left_click_lbl = tk.Label(mouse_box_l, text="L-CLK", width=7, bg=self.key_idle_bg, fg=self.key_idle_fg, font=("Segoe UI", 7, "bold"), pady=3)
        self.left_click_lbl.pack()

    def create_text_feed_gui(self):
        # Clean obsidian input panel
        feed_border = tk.Frame(self.root, bg=self.border_color, padx=1, pady=1)
        feed_border.pack(side="top", fill="x", padx=12, pady=5)
        
        feed_frame = tk.Frame(feed_border, bg=self.panel_bg, height=34)
        feed_frame.pack(fill="x")
        feed_frame.pack_propagate(False) 

        self.feed_label = tk.Label(
            feed_frame, 
            text="SYSTEM IDLE...", 
            font=("Consolas", 10, "bold"), 
            fg="#44444a", 
            bg=self.panel_bg,
            anchor="w"
        )
        self.feed_label.pack(fill="both", expand=True, padx=12)

    def create_keyboard_gui(self):
        # Premium chassis container
        kb_border = tk.Frame(self.root, bg=self.border_color, padx=1, pady=1)
        kb_border.pack(side="top", fill="x", padx=12, pady=(2, 8))
        
        kb_container = tk.Frame(kb_border, bg=self.panel_bg, padx=6, pady=6)
        kb_container.pack(fill="x")

        for row in KEYBOARD_LAYOUT:
            row_frame = tk.Frame(kb_container, bg=self.panel_bg)
            row_frame.pack(side="top", fill="x", pady=2)
            
            for key in row:
                # Scaled widths to make modifiers look proportional and professional
                width = 11 if key == "space" else (6 if key == "shift" else 2)
                
                # Outer key border frame for precision alignment lines
                key_border = tk.Frame(row_frame, bg=self.border_color, padx=1, pady=1)
                key_border.pack(side="left", padx=2, expand=True, fill="both")
                
                lbl = tk.Label(
                    key_border, 
                    text=key.upper(), 
                    width=width, 
                    height=1, 
                    bg=self.key_idle_bg, 
                    fg=self.key_idle_fg,
                    font=("Segoe UI", 8, "bold"),
                    pady=2
                )
                lbl.pack(fill="both", expand=True)
                self.key_buttons[key] = lbl

    # --- ASYNCHRONOUS HOOK NORMALIZERS ---
    def normalize_key(self, key):
        try:
            if key.char is not None:
                return key.char.lower(), key.char
        except AttributeError:
            pass
        
        key_name = str(key).replace("Key.", "")
        if key_name == "space": return "space", " "
        if "shift" in key_name: return "shift", ""
        if key_name == "backspace": return "backspace", "⌫"
        if key_name == "enter": return "enter", " ↵ "
        return None, ""

    # --- ASYNCHRONOUS SYSTEM EVENT PIPELINES ---
    def on_key_press(self, key):
        key_name, char_to_print = self.normalize_key(key)
        if key_name in self.key_buttons:
            self.root.after(0, self.set_key_visual, key_name, True)
        if char_to_print or key_name == "backspace":
            self.root.after(0, self.update_text_feed, key_name, char_to_print)

    def on_key_release(self, key):
        key_name, _ = self.normalize_key(key)
        if key_name in self.key_buttons:
            self.root.after(0, self.set_key_visual, key_name, False)

    def on_mouse_click(self, x, y, button, pressed):
        btn_str = str(button)
        if "left" in btn_str:
            self.root.after(0, self.set_mouse_visual, "left", pressed)
        elif "right" in btn_str:
            self.root.after(0, self.set_mouse_visual, "right", pressed)

    # --- THREAD-SAFE GRAPHICS DISPATCHERS ---
    def set_key_visual(self, key_name, is_pressed):
        lbl = self.key_buttons[key_name]
        if is_pressed:
            lbl.config(bg=self.key_active_bg, fg=self.key_active_fg)
        else:
            lbl.config(bg=self.key_idle_bg, fg=self.key_idle_fg)

    def set_mouse_visual(self, side, is_pressed):
        lbl = self.left_click_lbl if side == "left" else self.right_click_lbl
        if is_pressed:
            lbl.config(bg=self.mouse_active_bg, fg=self.mouse_active_fg)
        else:
            lbl.config(bg=self.key_idle_bg, fg=self.key_idle_fg)

    def update_text_feed(self, key_name, char):
        if key_name == "backspace":
            self.typed_text = self.typed_text[:-1]
        else:
            self.typed_text += char
            self.char_count += 1

        if self.char_count >= 30:
            self.typed_text = ""
            self.char_count = 0

        if not self.typed_text:
            self.feed_label.config(text="SYSTEM IDLE...", fg="#44444a")
        else:
            self.feed_label.config(text=self.typed_text, fg="#ffffff")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AestheticOverlay()
    app.run()
