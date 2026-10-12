import json
import tkinter as tk
from tkinter import ttk
from agent import process_instruction

class App:
    def __init__(self, root):
        self.root = root
        root.title("Advertising Agent — Draft Only")
        root.geometry("900x700")
        frame = ttk.Frame(root, padding=16)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="E-commerce Advertising Agent", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        ttk.Label(frame, text="Paste a JSON task below and click Run. This local demo never publishes ads.", wraplength=820).pack(anchor="w", pady=(5,12))
        ttk.Label(frame, text="Instruction / JSON input").pack(anchor="w")
        self.input = tk.Text(frame, height=11, wrap="word", font=("Consolas", 10))
        self.input.pack(fill="x", pady=5)
        self.load_product()
        row = ttk.Frame(frame); row.pack(fill="x", pady=6)
        ttk.Button(row, text="Run", command=self.run).pack(side="left")
        ttk.Button(row, text="Product Example", command=self.load_product).pack(side="left", padx=8)
        ttk.Button(row, text="Echo Example", command=self.load_echo).pack(side="left")
        ttk.Button(row, text="Clear", command=self.clear).pack(side="right")
        ttk.Label(frame, text="Result (JSON)").pack(anchor="w", pady=(8,0))
        self.output = tk.Text(frame, height=12, wrap="word", font=("Consolas", 10), state="disabled")
        self.output.pack(fill="both", expand=True, pady=5)
        self.status = tk.StringVar(value="Ready — draft only.")
        ttk.Label(frame, textvariable=self.status).pack(anchor="w")
    def set_output(self, value):
        self.output.configure(state="normal"); self.output.delete("1.0","end")
        self.output.insert("1.0", value); self.output.configure(state="disabled")
    def load_product(self):
        data = {"customer_code":"BD-2026-10-12-13","product":"Training desk lamp","price":1325,"approved_claim":"Aluminium body"}
        self.input.delete("1.0","end"); self.input.insert("1.0", json.dumps(data, indent=2))
    def load_echo(self):
        data = {"action":"echo","customer_code":"BD-13","budget":19750}
        self.input.delete("1.0","end"); self.input.insert("1.0", json.dumps(data, indent=2))
    def clear(self):
        self.input.delete("1.0","end"); self.set_output(""); self.status.set("Cleared — nothing published.")
    def run(self):
        raw = self.input.get("1.0","end").strip()
        try:
            data = json.loads(raw) if raw else {}
            result = process_instruction(data)
        except json.JSONDecodeError:
            result = {"error":"invalid_json","message":"Please enter a valid JSON object. Use an example button."}
        self.set_output(json.dumps(result, ensure_ascii=False, indent=2))
        self.status.set("Completed locally — draft only; no external action taken.")

if __name__ == "__main__":
    root = tk.Tk()
    try: ttk.Style().theme_use("vista")
    except tk.TclError: pass
    App(root)
    root.mainloop()
