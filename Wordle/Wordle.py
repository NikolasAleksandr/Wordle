import tkinter as tk
import random

class Sõnademäng:
    def __init__(self, master):
        self.master = master
        self.master.title("Sõnademäng")
        self.master.configure(bg='pink')
        
        with open("sõnad.txt", "r", encoding="utf-8") as file:
            self.sõnad = file.read().splitlines()
        
        self.uue_mängu_algus()
        
    def uue_mängu_algus(self):
        self.salajane_sõna = random.choice(self.sõnad)
        self.järelejäänud_katsed = 6
        self.arvatud_tähed = ['_' for _ in self.salajane_sõna]
        self.est_alphabet = "aäbcdefghijklmnoõöpqrstuvzšž"
        
        self.kaota_vanad_vidinad()
        self.loo_vidinad()
        
    def kaota_vanad_vidinad(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        
    def loo_vidinad(self):
        self.sõna_silt = tk.Label(self.master, text=" ".join(self.arvatud_tähed), font=("Times New Roman", 30), bg='pink') 
        self.sõna_silt.pack()
        
        self.katsete_silt = tk.Label(self.master, text=f"Järelejäänud katsed: {self.järelejäänud_katsed}", font=("Times New Roman", 24), bg='pink') 
        self.katsete_silt.pack()
        
        self.sisestus = tk.Entry(self.master, font=("Times New Roman", 24))
        self.sisestus.pack()
        
        self.nupp = tk.Button(self.master, text="Esita", command=self.kontrolli_arvamust, font=("Times New Roman", 20), bg='pink')
        self.nupp.pack()
        
        self.tulemuse_silt = tk.Label(self.master, text="", font=("Times New Roman", 20), bg='pink') 
        self.tulemuse_silt.pack()
        
        self.tähestiku_raam = tk.Frame(self.master, bg='pink')
        self.tähestiku_raam.pack()
        
        self.tähestiku_nupud = []
        for täht in self.est_alphabet:
            nupp = tk.Button(self.tähestiku_raam, text=täht, width=3, command=lambda t=täht: self.kontrolli_tähte(t))
            nupp.grid(row=(self.est_alphabet.index(täht)) // 7, column=(self.est_alphabet.index(täht)) % 7)
            self.tähestiku_nupud.append(nupp)
        
    def kontrolli_tähte(self, täht):
        if täht in self.salajane_sõna:
            for i in range(len(self.salajane_sõna)):
                if self.salajane_sõna[i] == täht:
                    if self.arvatud_tähed[i] == '_':
                        self.arvatud_tähed[i] = täht
                        self.sõna_silt.config(text=" ".join(self.arvatud_tähed))
                    self.sõna_silt.config(fg='green' if self.arvatud_tähed[i] == täht else 'blue', font=("Times New Roman", 34))
            self.uuenda_sõna_silt()
        else:
            self.järelejäänud_katsed -= 1
            self. uuenda_katsete_silt()
        
        self.keela_tähe_nupp(täht)
        self.kontrolli_mängu_staatus()
        
    def uuenda_sõna_silt(self):
        self.sõna_silt.config(text=" ".join(self.arvatud_tähed))
        
    def uuenda_katsete_silt(self):
        self.katsete_silt.config(text=f"Järelejäänud katsed: {self.järelejäänud_katsed}")
        
    def keela_tähe_nupp(self, täht):
        self.tähestiku_nupud[self.est_alphabet.index(täht)].config(state=tk.DISABLED)
        
    def kontrolli_arvamust(self):
        arvamus = self.sisestus.get().lower()
        self.sisestus.delete(0, tk.END)
        
        if arvamus == self.salajane_sõna:
            self.tulemuse_silt.config(text="Õnnitleme! Te arvasite õige sõna ära.")
            self.nupp.config(text="Uus mäng", command=self.uue_mängu_algus)
        else:
            self.järelejäänud_katsed -= 1
            self.uuenda_katsete_silt()
            self.kontrolli_mängu_staatus()
        
    def kontrolli_mängu_staatus(self):
        if self.järelejäänud_katsed == 0:
            self.tulemuse_silt.config(text=f"Vabandame, katsed on otsas. Õige sõna oli {self.salajane_sõna}.")
            self.keela_kõik_tähed()
            self.nupp.config(text="Uus mäng", command=self.uue_mängu_algus)
        elif "_" not in self.arvatud_tähed:
            self.tulemuse_silt.config(text="Õnnitleme! Te arvasite õige sõna ära.")
            self.keela_kõik_tähed()
            self.nupp.config(text="Uus mäng", command=self.uue_mängu_algus)
        
    def keela_kõik_tähed(self):
        for nupp in self.tähestiku_nupud:
            nupp.config(state=tk.DISABLED)

def põhifunktsioon():
    juur = tk.Tk()
    mäng = Sõnademäng(juur)
    juur.mainloop()

if __name__ == "__main__":
    põhifunktsioon()


