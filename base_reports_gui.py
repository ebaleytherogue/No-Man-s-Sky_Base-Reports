from pathlib import Path
from queue import Empty, Queue
from threading import Thread
from tkinter import filedialog, messagebox

import customtkinter as ctk

from extract_nms_bases import generate_reports


class BaseReportsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("NMS Base Reports")
        self.geometry("700x380")
        self.minsize(600, 380)
        self.grid_columnconfigure(0, weight=1)
        self.events = Queue()
        self.running = False
        self.protocol("WM_DELETE_WINDOW", self.close)

        ctk.CTkLabel(self, text="No Man's Sky Base Reports",
                     font=ctk.CTkFont(size=25, weight="bold")).grid(
                         row=0, column=0, padx=24, pady=(20, 8), sticky="w")
        ctk.CTkOptionMenu(self, values=["Dark", "Light"], width=90,
                          command=ctk.set_appearance_mode).grid(
                              row=0, column=1, padx=24, pady=(20, 8), sticky="e")

        self.input_entry, self.input_button = self.path_field(
            1, "Exported save JSON", self.choose_input)
        self.output_entry, self.output_button = self.path_field(
            3, "Report output folder", self.choose_output)

        self.generate_button = ctk.CTkButton(
            self, text="Generate Reports", command=self.start)
        self.generate_button.grid(row=5, column=0, padx=24, pady=18, sticky="w")
        self.progress = ctk.CTkProgressBar(self)
        self.progress.grid(row=6, column=0, columnspan=2, padx=24, sticky="ew")
        self.progress.set(0)
        self.status = ctk.CTkLabel(
            self, text="Select a save export and an output folder.",
            wraplength=550, justify="left")
        self.status.grid(row=7, column=0, columnspan=2, padx=24, pady=12, sticky="w")

    def path_field(self, row, label, command):
        ctk.CTkLabel(self, text=label).grid(
            row=row, column=0, padx=24, pady=(8, 2), sticky="w")
        entry = ctk.CTkEntry(self)
        entry.grid(row=row + 1, column=0, padx=(24, 8), sticky="ew")
        button = ctk.CTkButton(self, text="Browse…", width=90, command=command)
        button.grid(row=row + 1, column=1, padx=(0, 24), sticky="e")
        return entry, button

    def choose_input(self):
        selected = filedialog.askopenfilename(
            parent=self, filetypes=[("JSON save exports", "*.json"), ("All files", "*.*")])
        if selected:
            self.input_entry.delete(0, "end")
            self.input_entry.insert(0, selected)
            if not self.output_entry.get():
                self.output_entry.insert(0, str(Path(selected).parent / "nms_base_reports"))

    def choose_output(self):
        selected = filedialog.askdirectory(parent=self)
        if selected:
            self.output_entry.delete(0, "end")
            self.output_entry.insert(0, selected)

    def start(self):
        source = self.input_entry.get().strip()
        destination = self.output_entry.get().strip()
        if not source or not Path(source).is_file():
            messagebox.showerror("Select a save", "Choose an existing exported save JSON file.", parent=self)
            return
        if not destination:
            messagebox.showerror("Select an output folder", "Choose where to save the reports.", parent=self)
            return

        self.set_running(True)
        self.status.configure(text="Starting report generation…")
        self.progress.configure(mode="indeterminate")
        self.progress.start()
        Thread(target=self.run_reports, args=(Path(source), Path(destination))).start()
        self.after(80, self.poll)

    def set_running(self, running):
        self.running = running
        for widget in (self.input_entry, self.input_button, self.output_entry,
                       self.output_button, self.generate_button):
            widget.configure(state="disabled" if running else "normal")

    def run_reports(self, source, destination):
        try:
            result = generate_reports(
                source, destination, lambda message: self.events.put(("status", message)))
        except Exception as error:
            self.events.put(("error", str(error) or type(error).__name__))
        else:
            self.events.put(("done", result))

    def poll(self):
        while True:
            try:
                kind, value = self.events.get_nowait()
            except Empty:
                self.after(80, self.poll)
                return
            if kind == "status":
                self.status.configure(text=value)
                continue

            self.progress.stop()
            self.progress.configure(mode="determinate")
            self.progress.set(1 if kind == "done" else 0)
            self.set_running(False)
            if kind == "error":
                self.status.configure(text="Report generation failed.")
                messagebox.showerror("Report generation failed", value, parent=self)
            else:
                csv_path, summary_path, rows, _, _ = value
                self.status.configure(text=(
                    f"Generated {rows:,} report rows.\n"
                    f"{csv_path.name} and {summary_path.name}\n"
                    f"Saved in {csv_path.parent.resolve()}"))
            return

    def close(self):
        if self.running:
            messagebox.showinfo("Generating reports", "Wait for report generation to finish before closing.", parent=self)
        else:
            self.destroy()


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    BaseReportsApp().mainloop()
