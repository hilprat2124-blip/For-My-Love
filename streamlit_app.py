import streamlit as st
import streamlit.components.v1 as components
import random

# ================== KONFIG ==================
st.set_page_config(
    page_title="Untuk Kamu",
    page_icon="🌸",
    layout="centered"
)

# ================== KATA SEMANGAT NUGAS ==================
kata_nugas = [
    "Sayang... aku tahu kamu capek, tapi aku percaya kamu pasti bisa. Semangat ya, cintakuu.",
    "Aku tahu tugas kamu banyak, tapi aku juga tahu kamu sekuat itu. Aku bangga banget sama kamu.",
    "Capek boleh, istirahat dulu juga boleh. Kamu nggak harus selalu kuat setiap saat, yaa... Aku tetap bangga sama kamu, apa pun hasilnya.",
    "Coba nugas sambil bayangin aku lagi nemenin kamu, yaa. Anggap aja aku lagi duduk di samping kamu sambil elus kepala kamu pelan-pelan. 🤍",
    "Kalau udah selesai, aku traktir kamu es krim.",
    "Kalau tugas kamu udah selesai, sini cerita sama aku. Aku mau dengerin semua keluh kesah kamu, terus aku peluk yang lamaaa.",
]

# ================== PARAGRAF CINTA ==================
kalimat_penutup = (
    "Sayang... aku gak tau harus gimana ngejelasin ini semua ke kamu. "
    "Tiap hari rasanya aku makin sayang, makin cinta, makin pengen kamu bahagia terus. "
    "Kamu itu bukan cuma pacar. Kamu udah jadi tempat aku pulang, tempat aku cerita hal-hal random, "
    "Makasih ya udah bertahan, udah sabar, udah sayang sama aku yang menyebalkan ini. "
    "Kita tau hubungan tidak selalu mulus, tapi aku janji bakal terus ada buat kamu, "
    "di hari kamu senang, di hari kamu capek, di hari kamu ngerasa sendirian. "
    "Pokoknya, aku cinta banget banget banget sama kamu. "
    "I LOVE YOU SOOOOOOOOOO MMMMUUUUUUCCCHHHHH SAYANGGGG!!!!!!"
)

# ================== CSS ==================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=Nunito:wght@400;600;700&display=swap');

    .stApp {
        background: linear-gradient(160deg, #ffe9f0 0%, #ffd9e6 55%, #ffc7db 100%);
        font-family: 'Nunito', sans-serif;
    }

    #MainMenu, footer, header {visibility: hidden;}

    .judul {
        text-align: center;
        font-family: 'Caveat', cursive;
        color: #d6336c;
        font-size: 2.6em;
        margin-bottom: 0;
        letter-spacing: 0.5px;
        animation: fadeDown 0.9s ease-out;
    }

    .subjudul {
        text-align: center;
        color: #e0709a;
        font-size: 0.98em;
        margin-top: 0;
        margin-bottom: 28px;
        font-style: italic;
        animation: fadeDown 1.2s ease-out;
    }

    @keyframes fadeDown {
        from { opacity: 0; transform: translateY(-12px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .box-wrap {
        display: flex;
        justify-content: center;
        margin: 20px 0 30px 0;
        animation: floatY 3.2s ease-in-out infinite;
    }

    @keyframes floatY {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    .box {
        width: 170px;
        height: 170px;
        background: linear-gradient(145deg, #ffb3cc, #ff7fae);
        border-radius: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 4em;
        box-shadow: 0 18px 40px rgba(214, 51, 108, 0.35),
                    inset 0 -6px 12px rgba(255, 255, 255, 0.4);
        border: 3px solid rgba(255, 255, 255, 0.7);
        position: relative;
        animation: shake 2.6s ease-in-out infinite;
    }

    @keyframes shake {
        0%, 100% { transform: rotate(0deg); }
        15% { transform: rotate(-4deg); }
        30% { transform: rotate(4deg); }
        45% { transform: rotate(-3deg); }
        60% { transform: rotate(0deg); }
    }

    .pesan-card {
        background: rgba(255, 255, 255, 0.96);
        border-radius: 22px;
        padding: 34px 28px;
        margin: 18px auto;
        max-width: 560px;
        text-align: center;
        color: #b02a5b;
        font-size: 1.18em;
        font-weight: 600;
        line-height: 1.75;
        box-shadow: 0 12px 32px rgba(214, 51, 108, 0.15),
                    0 0 0 3px rgba(255, 179, 204, 0.6);
        position: relative;
        animation: cardIn 0.7s cubic-bezier(0.22, 1, 0.36, 1);
    }

    .pesan-card::before {
        content: "❝";
        position: absolute;
        top: 6px;
        left: 18px;
        font-size: 2.2em;
        color: #ffb3cc;
        font-family: Georgia, serif;
        line-height: 1;
    }

    @keyframes cardIn {
        0% { opacity: 0; transform: translateY(18px) scale(0.94); filter: blur(4px); }
        60% { filter: blur(0); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }

    .counter {
        text-align: center;
        color: #d6336c;
        font-size: 0.88em;
        font-style: italic;
        margin-top: 12px;
        opacity: 0.85;
        animation: fadeDown 0.9s ease-out;
    }

    .stButton > button {
        background: linear-gradient(135deg, #ff7fae, #d6336c) !important;
        color: #fff !important;
        border: none !important;
        padding: 14px 26px !important;
        border-radius: 999px !important;
        font-size: 1.02em !important;
        font-weight: 700 !important;
        letter-spacing: 0.3px !important;
        box-shadow: 0 8px 22px rgba(214, 51, 108, 0.35) !important;
        transition: all 0.28s cubic-bezier(0.22, 1, 0.36, 1) !important;
        width: 100% !important;
        font-family: 'Nunito', sans-serif !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) scale(1.015);
        box-shadow: 0 14px 30px rgba(214, 51, 108, 0.5) !important;
        background: linear-gradient(135deg, #ff8fbb, #e03d7a) !important;
    }

    .stButton > button:active {
        transform: translateY(-1px) scale(0.99);
    }

    .footer {
        text-align: center;
        color: #d6336c;
        font-size: 0.85em;
        margin-top: 32px;
        opacity: 0.7;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)


# ================== SESSION STATE ==================
if "step" not in st.session_state:
    st.session_state.step = 0

if "pesan_sekarang" not in st.session_state:
    st.session_state.pesan_sekarang = ""

if "sisa_pesan" not in st.session_state:
    pool = kata_nugas.copy()
    random.shuffle(pool)
    st.session_state.sisa_pesan = pool

if "key_pesan" not in st.session_state:
    st.session_state.key_pesan = 0

if "sfx" not in st.session_state:
    st.session_state.sfx = ""


def ambil_pesan_baru():
    if not st.session_state.sisa_pesan:
        st.session_state.step = 99
        return
    st.session_state.pesan_sekarang = st.session_state.sisa_pesan.pop()
    st.session_state.key_pesan += 1


def reset_semua():
    st.session_state.step = 0
    st.session_state.pesan_sekarang = ""
    st.session_state.key_pesan = 0
    pool = kata_nugas.copy()
    random.shuffle(pool)
    st.session_state.sisa_pesan = pool


# ================== AUDIO ENGINE (nempel di window.parent) ==================
def inject_audio_engine():
    html = """
    <!DOCTYPE html><html><head><style>body{margin:0;background:transparent;overflow:hidden;}</style></head>
    <body>
    <script>
        (function() {
            const P = window.parent;

            // =====================================================
            // Pasang audio engine SEKALI di parent, gak kehapus rerun
            // =====================================================
            if (P.__loveAudioInstalled) {
                // Sudah terpasang. Coba resume kalau suspended (auto-play friendly)
                if (P.__loveCtx && P.__loveCtx.state === 'suspended') {
                    P.__loveCtx.resume().catch(()=>{});
                }
                // Pastikan musik nyala
                if (P.__loveStartMusicIfNeeded) P.__loveStartMusicIfNeeded();
                return;
            }
            P.__loveAudioInstalled = true;

            const AudioCtx = P.AudioContext || P.webkitAudioContext;
            P.__loveCtx = new AudioCtx();

            // Volume master
            P.__musicVolume = 1.0;   // musik lebih keras
            P.__sfxVolume = 0.7;     // SFX juga dinaikin biar kedengeran jelas

            // State musik
            P.__musicRunning = false;
            P.__musicTimer = null;
            P.__musicEnabled = true;
            P.__chordIdx = 0;
            P.__melodyIdx = 0;

            // =====================================================
            // PLAY NOTE — pakai ADSR biar suara piano-ish, lembut
            // =====================================================
            function playNote(freq, startTime, duration, volume, type) {
                const ctx = P.__loveCtx;
                if (ctx.state === 'suspended') ctx.resume();
                const o = ctx.createOscillator();
                const g = ctx.createGain();
                o.type = type || 'sine';
                o.frequency.value = freq;
                // attack lembut
                g.gain.setValueAtTime(0.0001, startTime);
                g.gain.exponentialRampToValueAtTime(volume, startTime + 0.12);
                g.gain.exponentialRampToValueAtTime(volume * 0.5, startTime + duration * 0.4);
                g.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);
                o.connect(g); g.connect(ctx.destination);
                o.start(startTime);
                o.stop(startTime + duration + 0.2);
            }

            // =====================================================
            // MUSIK ROMANTIS — Canon in D progression
            // D - A - Bm - F#m - G - D - G - A
            // Ini progresi paling "menyentuh hati" di dunia musik klasik
            // =====================================================
            const canonChords = [
                // [bass, chord tones..., melody note]
                [146.83, 293.66, 369.99, 440.00, 587.33],   // D major
                [110.00, 277.18, 329.63, 440.00, 554.37],   // A major
                [123.47, 293.66, 369.99, 493.88, 587.33],   // B minor
                [92.50,  277.18, 369.99, 440.00, 554.37],   // F# minor
                [98.00,  293.66, 392.00, 493.88, 587.33],   // G major
                [146.83, 293.66, 369.99, 440.00, 587.33],   // D major
                [98.00,  293.66, 392.00, 493.88, 587.33],   // G major
                [110.00, 277.18, 329.63, 440.00, 554.37],   // A major
            ];

            // Melodi Canon in D yang lembut (dalam D major)
            const melodyNotes = [
                440.00, 493.88, 554.37, 587.33,  // A4 B4 C#5 D5
                659.25, 587.33, 554.37, 493.88,  // E5 D5 C#5 B4
                440.00, 493.88, 554.37, 587.33,  // A4 B4 C#5 D5
                659.25, 587.33, 554.37, 493.88,  // E5 D5 C#5 B4
                440.00, 493.88, 554.37, 587.33,  // A4 B4 C#5 D5
                659.25, 587.33, 554.37, 493.88,  // E5 D5 C#5 B4
                440.00, 493.88, 554.37, 587.33,  // A4 B4 C#5 D5
                659.25, 587.33, 493.88, 440.00,  // E5 D5 B4 A4
            ];

            function playChord(atTime, chord) {
                const bass = chord[0];
                const tones = chord.slice(1);
                const vol = P.__musicVolume;

                // Bass (panjang, lembut)
                playNote(bass, atTime, 4.5, 0.14 * vol, 'sine');

                // Chord tones (lembut, sedikit reverb feel)
                tones.forEach((f, i) => {
                    playNote(f, atTime + i * 0.04, 4.0, 0.075 * vol, 'sine');
                });

                // Melodi tinggi — bikin terasa "menyentuh"
                const mel = melodyNotes[P.__melodyIdx % melodyNotes.length];
                playNote(mel, atTime + 0.5, 3.5, 0.11 * vol, 'triangle');
                playNote(mel * 1.5, atTime + 1.8, 2.0, 0.05 * vol, 'sine');

                P.__melodyIdx++;
            }

            function startMusicLoop() {
                if (!P.__musicEnabled || P.__musicRunning) return;
                P.__musicRunning = true;

                function loop() {
                    if (!P.__musicRunning || !P.__musicEnabled) return;
                    const now = P.__loveCtx.currentTime + 0.05;
                    const chord = canonChords[P.__chordIdx % canonChords.length];
                    playChord(now, chord);
                    P.__chordIdx++;
                    // tiap chord 3.2 detik → tempo Canon in D yang tenang
                    P.__musicTimer = setTimeout(loop, 3200);
                }
                loop();
            }

            function stopMusicLoop() {
                P.__musicRunning = false;
                if (P.__musicTimer) { clearTimeout(P.__musicTimer); P.__musicTimer = null; }
            }

            // =====================================================
            // SFX — semua dibikin lebih "manis" & jelas
            // =====================================================
            function sfxPop() {
                const ctx = P.__loveCtx;
                if (ctx.state === 'suspended') ctx.resume();
                const now = ctx.currentTime;
                const o = ctx.createOscillator();
                const g = ctx.createGain();
                o.type = 'sine';
                o.frequency.setValueAtTime(440, now);
                o.frequency.exponentialRampToValueAtTime(1200, now + 0.2);
                g.gain.setValueAtTime(0.0001, now);
                g.gain.exponentialRampToValueAtTime(0.5 * P.__sfxVolume, now + 0.02);
                g.gain.exponentialRampToValueAtTime(0.0001, now + 0.6);
                o.connect(g); g.connect(ctx.destination);
                o.start(now); o.stop(now + 0.65);
            }

            function sfxDing() {
                const ctx = P.__loveCtx;
                if (ctx.state === 'suspended') ctx.resume();
                const now = ctx.currentTime;
                // 3 nada manis: E6, G6, B6 — bikin feel "hati hangat"
                [1318.51, 1567.98, 1975.53].forEach((f, i) => {
                    const o = ctx.createOscillator();
                    const g = ctx.createGain();
                    o.type = 'sine';
                    o.frequency.value = f;
                    const t = now + i * 0.07;
                    g.gain.setValueAtTime(0.0001, t);
                    g.gain.exponentialRampToValueAtTime(0.4 * P.__sfxVolume, t + 0.02);
                    g.gain.exponentialRampToValueAtTime(0.0001, t + 0.85);
                    o.connect(g); g.connect(ctx.destination);
                    o.start(t); o.stop(t + 0.9);
                });
            }

            function sfxChime() {
                const ctx = P.__loveCtx;
                if (ctx.state === 'suspended') ctx.resume();
                const now = ctx.currentTime;
                // arpeggio naik — D5 F#5 A5 D6 F#6
                [587.33, 739.99, 880.00, 1174.66, 1479.98].forEach((f, i) => {
                    const o = ctx.createOscillator();
                    const g = ctx.createGain();
                    o.type = 'sine';
                    o.frequency.value = f;
                    const t = now + i * 0.11;
                    g.gain.setValueAtTime(0.0001, t);
                    g.gain.exponentialRampToValueAtTime(0.42 * P.__sfxVolume, t + 0.03);
                    g.gain.exponentialRampToValueAtTime(0.0001, t + 1.5);
                    o.connect(g); g.connect(ctx.destination);
                    o.start(t); o.stop(t + 1.6);
                });
            }

            function sfxReset() {
                const ctx = P.__loveCtx;
                if (ctx.state === 'suspended') ctx.resume();
                const now = ctx.currentTime;
                [880, 587.33].forEach((f, i) => {
                    const o = ctx.createOscillator();
                    const g = ctx.createGain();
                    o.type = 'sine';
                    o.frequency.value = f;
                    const t = now + i * 0.1;
                    g.gain.setValueAtTime(0.0001, t);
                    g.gain.exponentialRampToValueAtTime(0.35 * P.__sfxVolume, t + 0.02);
                    g.gain.exponentialRampToValueAtTime(0.0001, t + 0.5);
                    o.connect(g); g.connect(ctx.destination);
                    o.start(t); o.stop(t + 0.55);
                });
            }

            // =====================================================
            // AUTO-PLAY LOGIC
            // =====================================================
            // Strategi:
            //   1) Coba langsung play — kalau browser izinin (user udah pernah interaksi
            //      di domain Streamlit sebelumnya), musik langsung nyala.
            //   2) Kalau diblokir, pasang listener click/key/touch SEKALI di parent —
            //      begitu user gerak dikit, musik langsung nyala.
            function ensureRunning() {
                if (P.__loveCtx.state === 'suspended') {
                    P.__loveCtx.resume().catch(()=>{});
                }
            }

            P.__loveStartMusicIfNeeded = function() {
                ensureRunning();
                if (P.__loveCtx.state === 'running') {
                    startMusicLoop();
                } else {
                    // coba lagi sebentar
                    setTimeout(() => {
                        ensureRunning();
                        if (P.__loveCtx.state === 'running') startMusicLoop();
                    }, 200);
                }
            };

            // Coba auto-play langsung
            P.__loveStartMusicIfNeeded();

            // Fallback: pasang listener di parent — begitu user interaksi apapun, nyala
            ['click', 'keydown', 'touchstart', 'mousemove', 'scroll'].forEach(ev => {
                P.document.addEventListener(ev, function once() {
                    P.__loveStartMusicIfNeeded();
                    // jangan remove, biar kalau keburu suspended bisa dipicu lagi
                }, { capture: true, passive: true });
            });

            // Juga di window parent sendiri (kalau user interaksi di luar iframe)
            P.addEventListener('focus', () => P.__loveStartMusicIfNeeded());

            // =====================================================
            // API BUAT IFRAME STREAMLIT
            // =====================================================
            P.__lovePlaySfx = function(name) {
                ensureRunning();
                // delay dikit biar audio ctx siap
                setTimeout(() => {
                    if (name === 'pop') sfxPop();
                    else if (name === 'ding') sfxDing();
                    else if (name === 'chime') sfxChime();
                    else if (name === 'reset') sfxReset();
                }, 30);
            };

            P.__loveToggleMusic = function() {
                P.__musicEnabled = !P.__musicEnabled;
                if (P.__musicEnabled) {
                    ensureRunning();
                    startMusicLoop();
                } else {
                    stopMusicLoop();
                }
                return P.__musicEnabled;
            };

            P.__loveMusicEnabled = function() {
                return P.__musicEnabled;
            };
        })();
    </script>
    </body></html>
    """
    components.html(html, height=0)


# ================== TRIGGER SFX (dipanggil setiap rerun kalau ada sfx) ==================
def trigger_sfx(sfx_name: str):
    if not sfx_name:
        return
    html = f"""
    <!DOCTYPE html><html><head><style>body{{margin:0;background:transparent;}}</style></head>
    <body>
    <script>
        (function() {{
            const P = window.parent;
            function fire() {{
                if (typeof P.__lovePlaySfx === 'function') {{
                    P.__lovePlaySfx('{sfx_name}');
                }} else {{
                    // engine belum siap, coba lagi
                    setTimeout(fire, 80);
                }}
            }}
            // sedikit delay biar rerun selesai & audio ctx siap
            setTimeout(fire, 120);
        }})();
    </script>
    </body></html>
    """
    components.html(html, height=0)


# ================== TOMBOL MUSIK ==================
def render_music_toggle():
    html = """
    <!DOCTYPE html><html><head>
    <style>
        body { margin:0; padding:0; background:transparent; overflow:hidden; }
        #musicToggle {
            position: fixed;
            top: 12px;
            right: 12px;
            background: rgba(255,255,255,0.95);
            border: 2px solid #ffb3cc;
            color: #d6336c;
            border-radius: 999px;
            padding: 8px 16px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 4px 14px rgba(214,51,108,0.3);
            z-index: 999999;
            font-family: 'Nunito', sans-serif;
            transition: transform 0.2s;
        }
        #musicToggle:hover { transform: scale(1.06); background:#fff; }
    </style>
    </head>
    <body>
    <button id="musicToggle">🔊 Musik</button>
    <script>
        const btn = document.getElementById('musicToggle');
        const P = window.parent;

        function refresh() {
            if (typeof P.__loveMusicEnabled === 'function') {
                btn.textContent = P.__loveMusicEnabled() ? '🔊 Musik' : '🔇 Musik';
            }
        }

        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (typeof P.__loveToggleMusic === 'function') {
                P.__loveToggleMusic();
                setTimeout(refresh, 100);
            }
        });

        setInterval(refresh, 1000);
        refresh();
    </script>
    </body></html>
    """
    components.html(html, height=0)


# ================== PASANG AUDIO ENGINE ==================
inject_audio_engine()
render_music_toggle()

# Trigger SFX yang diminta (kalau ada) — INI YANG BIKIN SFX BUNYI DI SETIAP NEXT
if st.session_state.sfx:
    trigger_sfx(st.session_state.sfx)
    st.session_state.sfx = ""


# ================== HALAMAN 0: AWAL ==================
if st.session_state.step == 0:
    st.markdown('<div class="judul">Hai, kamu 🌸</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subjudul">aku nitipin sesuatu di kotak ini. '
        'buka pelan-pelan ya, jangan sekaligus.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="box-wrap"><div class="box">🎁</div></div>',
        unsafe_allow_html=True
    )

    if st.button("Buka kotaknya 💌"):
        st.session_state.step = 1
        ambil_pesan_baru()
        st.session_state.sfx = "pop"
        st.rerun()


# ================== HALAMAN 1: BUKA KOTAK ==================
elif st.session_state.step == 1:
    st.markdown('<div class="judul">Sebuah pesan untukmu</div>', unsafe_allow_html=True)

    st.markdown(
        f'<div class="pesan-card" key="p{st.session_state.key_pesan}">'
        f'{st.session_state.pesan_sekarang}</div>',
        unsafe_allow_html=True
    )

    sisa = len(st.session_state.sisa_pesan)
    total = len(kata_nugas)
    sudah = total - sisa

    st.markdown(
        f'<div class="counter">kotak yang sudah kamu buka — {sudah} dari {total} 🌸</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if sisa > 0:
        if st.button("Lanjut, buka kotak berikutnya 🌷"):
            ambil_pesan_baru()
            st.session_state.sfx = "ding"   # <== SFX SETIAP NEXT
            st.rerun()
    else:
        st.markdown(
            '<div class="counter">kotaknya sudah habis... '
            'tapi masih ada satu hal lagi untukmu</div>',
            unsafe_allow_html=True
        )
        if st.button("Buka yang terakhir ✨"):
            st.session_state.step = 99
            st.session_state.sfx = "chime"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Ulang dari awal"):
        reset_semua()
        st.session_state.sfx = "reset"
        st.rerun()


# ================== HALAMAN 99: SURPRISE ==================
elif st.session_state.step == 99:

    html_surprise = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=Nunito:wght@400;600;700&display=swap');
        html, body {{ margin:0; padding:0; background:transparent; font-family:'Nunito',sans-serif; overflow:hidden; }}
        #fireworks {{ position:fixed; top:0; left:0; width:100%; height:100%; z-index:0; pointer-events:none; }}
        .petal {{ position:fixed; top:-30px; font-size:18px; opacity:0; animation:petalFall linear forwards; z-index:1; pointer-events:none; }}
        @keyframes petalFall {{
            0% {{ opacity:0; transform:translateY(-20px) rotate(0deg); }}
            10% {{ opacity:0.9; }}
            90% {{ opacity:0.9; }}
            100% {{ opacity:0; transform:translateY(105vh) rotate(360deg); }}
        }}
        .konten {{
            position:relative; z-index:3;
            background:rgba(255,255,255,0.96);
            border-radius:26px;
            padding:40px 34px;
            margin:24px auto;
            max-width:640px;
            box-shadow:0 22px 55px rgba(214,51,108,0.28), 0 0 0 3px rgba(255,179,204,0.55);
            text-align:center;
            animation:popIn 1.1s cubic-bezier(0.22,1,0.36,1);
        }}
        @keyframes popIn {{
            0% {{ opacity:0; transform:scale(0.82) translateY(20px); filter:blur(6px); }}
            60% {{ filter:blur(0); }}
            100% {{ opacity:1; transform:scale(1) translateY(0); }}
        }}
        .judul-surprise {{
            font-family:'Caveat', cursive;
            font-size:2.4em;
            color:#d6336c;
            margin-bottom:6px;
            letter-spacing:0.5px;
            animation:heartbeat 2.4s ease-in-out infinite;
        }}
        @keyframes heartbeat {{
            0%, 100% {{ transform:scale(1); }}
            20% {{ transform:scale(1.06); }}
            40% {{ transform:scale(1); }}
            60% {{ transform:scale(1.04); }}
        }}
        .garis {{
            width:60px; height:3px;
            background:linear-gradient(90deg, transparent, #ff7fae, transparent);
            margin:14px auto 22px auto;
            border-radius:3px;
            animation:fadeIn 1.6s ease-out;
        }}
        @keyframes fadeIn {{ from {{ opacity:0; width:0; }} to {{ opacity:1; width:60px; }} }}
        .paragraf {{
            color:#a1255a;
            font-size:1.06em;
            line-height:1.95;
            text-align:left;
            font-weight:500;
            opacity:0;
            animation:fadeUp 1.4s ease-out 0.6s forwards;
        }}
        @keyframes fadeUp {{ from {{ opacity:0; transform:translateY(14px); }} to {{ opacity:1; transform:translateY(0); }} }}
        .ttd {{
            margin-top:28px;
            color:#d6336c;
            font-family:'Caveat', cursive;
            font-size:1.5em;
            text-align:right;
            opacity:0;
            animation:fadeUp 1.4s ease-out 1.6s forwards;
        }}
    </style>
    </head>
    <body>
    <canvas id="fireworks"></canvas>
    <div class="konten">
        <div class="judul-surprise">Untuk kamu 🌸</div>
        <div class="garis"></div>
        <div class="paragraf">{kalimat_penutup}</div>
        <div class="ttd">— dari aku, yang sayang banget sama kamu</div>
    </div>
    <script>
        const petals = ['🌸','🌷','💗','✨','🩷'];
        function spawnPetal() {{
            const el = document.createElement('div');
            el.className = 'petal';
            el.textContent = petals[Math.floor(Math.random() * petals.length)];
            el.style.left = Math.random() * 100 + 'vw';
            el.style.fontSize = (Math.random() * 8 + 14) + 'px';
            const dur = Math.random() * 5 + 7;
            el.style.animationDuration = dur + 's';
            document.body.appendChild(el);
            setTimeout(() => el.remove(), dur * 1000 + 500);
        }}
        setInterval(spawnPetal, 700);

        const canvas = document.getElementById('fireworks');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        window.addEventListener('resize', () => {{
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }});
        const particles = [];
        const colors = ['#ff7fae','#d6336c','#ffb3cc','#ffd9a0','#ffe8b0','#ffffff','#f9a8c9','#e8879f'];
        function createFirework(x, y) {{
            const count = 45 + Math.floor(Math.random() * 25);
            const baseHue = colors[Math.floor(Math.random() * colors.length)];
            for (let i = 0; i < count; i++) {{
                const angle = (Math.PI * 2 * i) / count + Math.random() * 0.15;
                const speed = Math.random() * 4.5 + 1.8;
                particles.push({{
                    x, y,
                    vx: Math.cos(angle) * speed,
                    vy: Math.sin(angle) * speed,
                    life: 1,
                    decay: 0.012 + Math.random() * 0.008,
                    color: Math.random() < 0.7 ? baseHue : colors[Math.floor(Math.random()*colors.length)],
                    size: Math.random() * 2.2 + 1.4
                }});
            }}
        }}
        function animate() {{
            ctx.fillStyle = 'rgba(255,233,240,0.18)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            for (let i = particles.length - 1; i >= 0; i--) {{
                const p = particles[i];
                p.x += p.vx; p.y += p.vy;
                p.vy += 0.05;
                p.vx *= 0.985; p.vy *= 0.985;
                p.life -= p.decay;
                if (p.life <= 0) {{ particles.splice(i, 1); continue; }}
                ctx.globalAlpha = Math.max(p.life, 0);
                ctx.fillStyle = p.color;
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);
                ctx.fill();
            }}
            ctx.globalAlpha = 1;
            requestAnimationFrame(animate);
        }}
        animate();
        setInterval(() => {{
            createFirework(Math.random() * canvas.width, Math.random() * canvas.height * 0.6 + 40);
        }}, 1400);
        setTimeout(() => createFirework(canvas.width * 0.5, canvas.height * 0.28), 400);
        setTimeout(() => createFirework(canvas.width * 0.28, canvas.height * 0.45), 900);
        setTimeout(() => createFirework(canvas.width * 0.72, canvas.height * 0.38), 1400);
    </script>
    </body>
    </html>
    """
    components.html(html_surprise, height=780, scrolling=False)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Ulang dari awal ya"):
        reset_semua()
        st.session_state.sfx = "reset"
        st.rerun()


# ================== FOOTER ==================
st.markdown(
    '<div class="footer">dibuat sambil mikirin kamu terus</div>',
    unsafe_allow_html=True
)
