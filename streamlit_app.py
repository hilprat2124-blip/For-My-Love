from flask import Flask, render_template
import random

app = Flask(__name__)

# Kata-kata semangat & sayang
kata_semangat = [
    "Semangat ya sayangku! Kamu pasti bisa melewati hari ini! 💪💖",
    "Jangan lupa makan ya cantik, aku gak mau kamu sakit 🥺🍜",
    "Kamu itu kuat, hebat, dan luar biasa! Aku bangga sama kamu 🌟",
    "Kalau capek, istirahat ya. Aku selalu ada buat kamu 💕",
    "Hari ini boleh sedih, besok harus senyum lagi ya sayang 😊",
    "Kamu tuh kayak kopi, bikin hari-hariku jadi lebih hidup ☕💗",
    "Semangat kerjanya! Nanti aku traktir kamu ya 🍰",
    "Kamu adalah alasan aku senyum sendiri kayak orang gila 😆💘",
    "Aku sayang kamu lebih dari kemarin, tapi kurang dari besok 💌",
    "Jangan overthinking ya, aku cuma cinta sama kamu kok 🥰",
    "Kamu cantik, pinter, dan menggemaskan. Paket lengkap! 🎀",
    "Kalau dunia jahat sama kamu, aku lawan! 😤💗",
    "Semangat terus ya, aku selalu support kamu dari sini 📣💖",
    "Kamu itu bunga, dan aku lebahnya. Eh, gombal ya? Hehe 🐝🌸",
    "Aku gak butuh kopi, aku butuh kamu tiap pagi ☕💕",
]

# Alasan sayang (untuk halaman random)
alasan_sayang = [
    "Aku sayang kamu karena senyum kamu bikin dunia aku terang ✨",
    "Aku sayang kamu karena kamu selalu dengerin cerita aku 🎧💗",
    "Aku sayang kamu karena kamu sabar banget sama aku 😌💖",
    "Aku sayang kamu karena kamu wangi dan bikin aku nyaman 🌸",
    "Aku sayang kamu karena kamu pinter masak (walau kadang gosong) 🍳😆",
    "Aku sayang kamu karena kamu tuh home aku 🏡💕",
    "Aku sayang kamu karena kamu gak pernah bosen sama aku 🥺",
    "Aku sayang kamu karena kamu ganteng/cantik banget 😍",
]

@app.route("/")
def home():
    pesan = random.choice(kata_semangat)
    alasan = random.choice(alasan_sayang)
    return render_template("index.html", pesan=pesan, alasan=alasan)

if __name__ == "__main__":
    app.run(debug=True)
