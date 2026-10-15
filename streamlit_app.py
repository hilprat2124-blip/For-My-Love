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


# =====================================================================
# AUDIO ENGINE — PIANO SUITE (harmonic synthesis + reverb)
# =====================================================================
def inject_audio_engine():
    html = """
    <!DOCTYPE html><html><head><style>body{margin:0;background:transparent;overflow:hidden;}</style></head>
    <body>
    <script>
        (function() {
            const P = window.parent;
            if (P.__lovePianoV1) return;
            P.__lovePianoV1 = true;

            const AudioCtx = P.AudioContext || P.webkitAudioContext;
            P.__loveCtx = new AudioCtx();

            P.__musicVolume = 1.0;
            P.__sfxVolume = 0.85;
            P.__musicRunning = false;
            P.__musicTimer = null;
            P.__musicEnabled = true;
            P.__lastSfxAt = 0;

            // Reverb sederhana pakai ConvolverNode
            function makeReverbIR(ctx, duration, decay) {
                const rate = ctx.sampleRate;
                const length = rate * duration;
                const impulse = ctx.createBuffer(2, length, rate);
                for (let ch = 0; ch < 2; ch++) {
                    const data = impulse.getChannelData(ch);
                    for (let i = 0; i < length; i++) {
                        data[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / length, decay);
                    }
                }
                return impulse;
            }

            const reverbIR = makeReverbIR(P.__loveCtx, 3.5, 3);
            const reverb = P.__loveCtx.createConvolver();
            reverb.buffer = reverbIR;

            const reverbGain = P.__loveCtx.createGain();
            reverbGain.gain.value = 0.35;

            const masterGain = P.__loveCtx.createGain();
            masterGain.gain.value = 1.0;

            reverb.connect(reverbGain);
            reverbGain.connect(masterGain);
            masterGain.connect(P.__loveCtx.destination);

            P.__loveMaster = masterGain;
            P.__loveReverb = reverb;

            // ================================================================
            // PIANO SYNTHESIS — harmonic partials
            // ================================================================
            function playPiano(freq, startTime, duration, volume) {
                const ctx = P.__loveCtx;
                if (ctx.state === 'suspended') ctx.resume().catch(()=>{});

                const harmonics = [
                    { mult: 1, gain: 1.0,  type: 'sine' },
                    { mult: 2, gain: 0.55, type: 'sine' },
                    { mult: 3, gain: 0.30, type: 'sine' },
                    { mult: 4, gain: 0.18, type: 'sine' },
                    { mult: 5, gain: 0.10, type: 'sine' },
                    { mult: 6, gain: 0.06, type: 'sine' },
                ];

                harmonics.forEach(h => {
                    const o = ctx.createOscillator();
                    const g = ctx.createGain();
                    o.type = h.type;
                    o.frequency.value = freq * h.mult;

                    const amp = volume * h.gain;
                    g.gain.setValueAtTime(0.0001, startTime);
                    g.gain.exponentialRampToValueAtTime(amp, startTime + 0.008);
                    g.gain.exponentialRampToValueAtTime(amp * 0.6, startTime + 0.15);
                    g.gain.exponentialRampToValueAtTime(amp * 0.25, startTime + duration * 0.5);
                    g.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

                    o.connect(g);

                    const dryGain = ctx.createGain();
                    dryGain.gain.value = 0.75;
                    g.connect(dryGain);
                    dryGain.connect(masterGain);

                    const wetGain = ctx.createGain();
                    wetGain.gain.value = 0.35;
                    g.connect(wetGain);
                    wetGain.connect(reverb);

                    o.start(startTime);
                    o.stop(startTime + duration + 0.1);
                });
            }

            // ================================================================
            // MUSIK: "River Flows in You" style
            // Progresi: Am - F - C - G
            // ================================================================
            const melody = [
                440.00, 523.25, 659.25, 523.25,
                440.00, 523.25, 698.46, 523.25,
                523.25, 659.25, 783.99, 659.25,
                493.88, 587.33, 739.99, 587.33,
            ];

            const bassLine = [110.00, 87.31, 130.81, 98.00];

            const arpPattern = [
                [220.00, 261.63, 329.63, 261.63],
                [174.61, 220.00, 261.63, 220.00],
                [261.63, 329.63, 392.00, 329.63],
                [196.00, 246.94, 293.66, 246.94],
            ];

            let step = 0;

            function playMeasure(atTime) {
                const vol = P.__musicVolume;
                const barIdx = step % 4;
                const baseTime = atTime;

                playPiano(bassLine[barIdx], baseTime, 3.6, 0.32 * vol);

                const arp = arpPattern[barIdx];
                for (let i = 0; i < arp.length; i++) {
                    playPiano(arp[i], baseTime + i * 0.72, 1.6, 0.16 * vol);
                }

                const startMel = step * 4;
                for (let i = 0; i < 4; i++) {
                    const note = melody[(startMel + i) % melody.length];
                    playPiano(note, baseTime + i * 0.72 + 0.05, 1.8, 0.22 * vol);
                    playPiano(note * 2, baseTime + i * 0.72 + 0.08, 1.2, 0.06 * vol);
                }

                step++;
            }

            function startMusicLoop() {
                if (!P.__musicEnabled || P.__musicRunning) return;
                P.__musicRunning = true;

                function loop() {
                    if (!P.__musicRunning || !P.__musicEnabled) return;
                    const now = P.__loveCtx.currentTime + 0.05;
                    playMeasure(now);
                    P.__musicTimer = setTimeout(loop, 3000);
                }
                loop();
            }

            function stopMusicLoop() {
                P.__musicRunning = false;
                if (P.__musicTimer) { clearTimeout(P.__musicTimer); P.__musicTimer = null; }
            }

            // ================================================================
            // SFX — pakai piano synth juga
            // ================================================================
            function sfxPop() {
                const now = P.__loveCtx.currentTime;
                playPiano(880, now, 0.9, 0.55 * P.__sfxVolume);
                playPiano(1318.51, now + 0.08, 1.0, 0.42 * P.__sfxVolume);
            }

            function sfxDing() {
                const now = P.__loveCtx.currentTime;
                [1174.66, 1479.98, 1760.00].forEach((f, i) => {
                    playPiano(f, now + i * 0.06, 1.3, 0.35 * P.__sfxVolume);
                });
            }

            function sfxChime() {
                const now = P.__loveCtx.currentTime;
                [587.33, 739.99, 880.00, 1174.66, 1479.98, 1760.00].forEach((f, i) => {
                    playPiano(f, now + i * 0.1, 1.8, 0.32 * P.__sfxVolume);
                });
            }

            function sfxReset() {
                const now = P.__loveCtx.currentTime;
                [880, 659.25, 440].forEach((f, i) => {
                    playPiano(f, now + i * 0.09, 0.9, 0.35 * P.__sfxVolume);
                });
            }

            // ================================================================
            // API
            // ================================================================
            P.__lovePlaySfx = function(name) {
                const now = Date.now();
                // Debounce 250ms biar gak double
                if (now - P.__lastSfxAt < 250) return;
                P.__lastSfxAt = now;

                if (P.__loveCtx.state === 'suspended') P.__loveCtx.resume().catch(()=>{});
                try {
                    if (name === 'pop') sfxPop();
                    else if (name === 'ding') sfxDing();
                    else if (name === 'chime') sfxChime();
                    else if (name === 'reset') sfxReset();
                } catch(e) {}
            };

            P.addEventListener('message', function(ev) {
                const data = ev.data;
                if (data && data.__loveSfx) P.__lovePlaySfx(data.__loveSfx);
            });

            function ensureRunning() {
                if (P.__loveCtx.state === 'suspended') P.__loveCtx.resume().catch(()=>{});
            }
            P.__loveStartMusicIfNeeded = function() {
                ensureRunning();
                if (P.__loveCtx.state === 'running') {
                    startMusicLoop();
                } else {
                    setTimeout(() => {
                        ensureRunning();
                        if (P.__loveCtx.state === 'running') startMusicLoop();
                    }, 250);
                }
            };

            P.__loveStartMusicIfNeeded();

            ['click', 'keydown', 'touchstart', 'mousemove', 'scroll'].forEach(ev => {
                P.document.addEventListener(ev, () => P.__loveStartMusicIfNeeded(),
                    { capture: true, passive: true });
            });
            P.addEventListener('focus', () => P.__loveStartMusicIfNeeded());

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
            P.__loveMusicEnabled = function() { return P.__musicEnabled; };
        })();
    </script>
    </body></html>
    """
    components.html(html, height=0)


# =====================================================================
# TRIGGER SFX — kirim SEKALI doang, gak ada retry
# =====================================================================
def trigger_sfx(sfx_name: str):
    if not sfx_name:
        return
    html = f"""
    <!DOCTYPE html><html><head><style>body{{margin:0;background:transparent;}}</style></head>
    <body>
    <script>
        (function() {{
            try {{
                window.parent.postMessage({{ __loveSfx: '{sfx_name}' }}, '*');
            }} catch(e) {{}}
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
            st.session_state.sfx = "ding"
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
