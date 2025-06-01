import ttkbootstrap as ttkb

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Konverter Suhu")
        self.root.geometry("400x250")

        ttkb.Label(root, text="Masukkan Nilai Suhu:").pack(pady=5)
        self.entry_nilai = ttkb.Entry(root, bootstyle="danger")  # Background merah
        self.entry_nilai.pack()

        ttkb.Label(root, text="Dari Satuan:").pack(pady=5)
        self.combo_dari = ttkb.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
        self.combo_dari.pack()

        ttkb.Button(root, text="Konversi", command=self.hitung, bootstyle="success").pack(pady=10)

        self.hasil = ttkb.StringVar()
        ttkb.Label(root, textvariable=self.hasil, bootstyle="primary").pack(pady=5)

    def hitung(self):
        try:
            val = float(self.entry_nilai.get())
            unit = self.combo_dari.get()

            if unit == "Celsius":
                f = (val * 9/5) + 32
                k = val + 273.15
                self.hasil.set(f"{val}°C = {f:.2f}°F | {k:.2f} K")
            elif unit == "Fahrenheit":
                c = (val - 32) * 5/9
                k = c + 273.15
                self.hasil.set(f"{val}°F = {c:.2f}°C | {k:.2f} K")
            elif unit == "Kelvin":
                c = val - 273.15
                f = (c * 9/5) + 32
                self.hasil.set(f"{val} K = {c:.2f}°C | {f:.2f}°F")
            else:
                self.hasil.set("Pilih satuan suhu yang valid!")
        except Exception:
            self.hasil.set("Input tidak valid!")

if __name__ == "__main__":
    app = ttkb.Window(themename="superhero")
    MainApp(app)
    app.mainloop()
