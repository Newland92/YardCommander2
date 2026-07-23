import tkinter as tk
from tkinter import ttk


class YardCommanderUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Yard Commander Cleanup v2.0")
        self.root.geometry("900x650")

        self.build()

    def build(self):

        title = tk.Label(
            self.root,
            text="Yard Commander Cleanup",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(pady=15)

        # Browser

        browser = ttk.LabelFrame(self.root, text="Browser")
        browser.pack(fill="x", padx=15, pady=10)

        self.browser_status = tk.Label(
            browser,
            text="Not Connected",
            fg="red"
        )

        self.browser_status.pack(anchor="w", padx=10, pady=5)

        self.launch_btn = ttk.Button(
            browser,
            text="Launch Chrome"
        )

        self.launch_btn.pack(side="left", padx=10, pady=10)

        self.reconnect_btn = ttk.Button(
            browser,
            text="Reconnect"
        )

        self.reconnect_btn.pack(side="left", padx=10)

        # Scan

        scan = ttk.LabelFrame(self.root, text="Scan")
        scan.pack(fill="x", padx=15, pady=10)

        self.scan_status = tk.Label(
            scan,
            text="Not Scanned",
            fg="red"
        )

        self.scan_status.pack(anchor="w", padx=10)

        self.scan_btn = ttk.Button(
            scan,
            text="Scan Yard"
        )

        self.scan_btn.pack(side="left", padx=10, pady=10)

        # Cleanup

        cleanup = ttk.LabelFrame(self.root, text="Cleanup")
        cleanup.pack(fill="x", padx=15, pady=10)

        self.preview_btn = ttk.Button(
            cleanup,
            text="Preview Changes"
        )

        self.preview_btn.pack(side="left", padx=10, pady=10)

        self.run_btn = ttk.Button(
            cleanup,
            text="Run Cleanup"
        )

        self.run_btn.pack(side="left", padx=10)

        # Progress

        progress = ttk.LabelFrame(self.root, text="Progress")
        progress.pack(fill="x", padx=15, pady=10)

        self.progress = ttk.Progressbar(
            progress,
            length=700
        )

        self.progress.pack(padx=10, pady=10)

        # Log

        log = ttk.LabelFrame(self.root, text="Log")
        log.pack(fill="both", expand=True, padx=15, pady=10)

        self.log = tk.Text(
            log,
            height=15
        )

        self.log.pack(fill="both", expand=True)

    def run(self):

        self.root.mainloop()