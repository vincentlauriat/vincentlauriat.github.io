"""Generate Localia's three inline diagrams (trilingual SVG) into <site>/Localia/diagrams/."""
import sys, os
from html import escape

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)


def frt(s):
    return s.replace(" :", "\u00a0:").replace(" ;", "\u00a0;").replace("« ", "«\u00a0").replace(" »", "\u00a0»")


def L(x, y, cls, v, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    if isinstance(v, str):
        return f'<text x="{x}" y="{y}" class="{cls}"{a}>{escape(v)}</text>'
    return "".join(f'<text x="{x}" y="{y}" class="{cls} {l}"{a}>{escape(frt(v[l]) if l == "fr" else v[l])}</text>' for l in ("en", "fr", "zh"))


def arrow_down(x, y1, y2, cls="s"):
    return f'<path class="{cls}" d="M{x} {y1}V{y2}M{x-5} {y2-7}l5 7 5-7"/>'


def svg(name, w, h, body, defs=""):
    head = f'<svg class="dgm" viewBox="0 0 {w} {h}" aria-hidden="true" focusable="false">'
    if defs:
        head += f"<defs>{defs}</defs>"
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(
        f"<!-- Localia diagram, inlined into the page by tools/monograph/build.py. Labels carry .en/.fr/.zh. -->\n"
        f"{head}{body}</svg>\n")


# ── 1. pipeline ──────────────────────────────────────────────────────────
stages = [
    ({"en": "Hardware profile", "fr": "Profil matériel", "zh": "硬體概況"},
     ("m", "chip · RAM · Metal working set"),
     ("c", {"en": "e.g. a 24 GB Mac → 17.8 GB usable by the GPU",
            "fr": "ex. un Mac de 24 Go → 17,8 Go utilisables par le GPU",
            "zh": "例：24 GB 的 Mac → GPU 可用 17.8 GB"})),
    ({"en": "llmfit scoring", "fr": "Score llmfit", "zh": "llmfit 評分"},
     ("m", "llmfit 1.1.20 --max-context 65536 --json"),
     ("c", {"en": "which models fit this hardware, and how fast",
            "fr": "quels modèles tiennent sur ce matériel, à quelle vitesse",
            "zh": "哪些模型放得進這台硬體、速度多快"})),
    ({"en": "Re-quantise + Metal limit", "fr": "Requantification + limite Metal", "zh": "重新量化 + Metal 上限"},
     ("c", {"en": "size and speed recomputed for Q4_K_M",
            "fr": "taille et vitesse recalculées pour Q4_K_M",
            "zh": "依 Q4_K_M 重新計算大小與速度"}),
     ("m", "pool = working set − 1.5 GB")),
    ({"en": "Measured calibration", "fr": "Calibration mesurée", "zh": "實測校準"},
     ("c", {"en": "first load: real tok/s and memory measured",
            "fr": "premier chargement : tok/s et mémoire réels",
            "zh": "首次載入：實測 tok/s 與記憶體"}),
     ("c", {"en": "estimates were ~2× off on an M5",
            "fr": "estimations fausses d'environ 2× sur un M5",
            "zh": "在 M5 上估計值偏差約 2 倍"})),
    ({"en": "Recommendation", "fr": "Recommandation", "zh": "推薦"},
     ("c", {"en": "speed first · under ~15 tok/s flagged slow",
            "fr": "vitesse d'abord · lent sous ~15 tok/s",
            "zh": "速度優先 · 低於約 15 tok/s 標示為慢"}),
     ("c", {"en": "community fine-tunes filtered out",
            "fr": "fine-tunes communautaires écartés",
            "zh": "濾除社群微調版本"})),
]
RX, TOP, STEP = 56, 44, 118
b = [f'<path class="s2" d="M{RX} {TOP+20}V{TOP+STEP*4-20}"/>']
for i, (title, l1, l2) in enumerate(stages):
    y = TOP + STEP * i
    last = i == len(stages) - 1
    if i:
        b.append(f'<path class="s2" d="M{RX-5} {y-27}l5 7 5-7"/>')
    b.append(f'<rect x="{RX-20}" y="{y-20}" width="40" height="40" class="{"fa" if last else "node"}"/>')
    b.append(L(RX, y + 7, "tn" + (" on" if last else ""), str(i + 1), "middle"))
    b.append(L(100, y - 4, "t", title))
    b.append(L(100, y + 20, l1[0], l1[1]))
    b.append(L(100, y + 42, l2[0], l2[1]))
# feedback loop: calibration (4) back into the estimates (3)
y3, y4 = TOP + STEP * 2, TOP + STEP * 3
b.append(f'<path class="loop" d="M{RX-20} {y4}H14V{y3}H{RX-26}"/><path class="loop-h" d="M{RX-33} {y3-6}l7 6-7 6"/>')
svg("pipeline.svg", 560, TOP + STEP * 4 + 64, "".join(b))

# ── 2. local mode ────────────────────────────────────────────────────────
b = []
# switch
b.append('<rect x="24" y="22" width="60" height="30" class="fa"/><rect x="56" y="26" width="24" height="22" class="knob"/>')
b.append(L(100, 36, "t", {"en": "Local mode: on", "fr": "Mode local : activé", "zh": "本機模式：開啟"}))
b.append(L(100, 58, "c", {"en": "one switch, like airplane mode; its scope is a setting",
                          "fr": "un interrupteur, comme le mode avion ; portée réglable",
                          "zh": "一個開關，就像飛航模式；作用範圍可設定"}))
# two scopes
def box(y, h, title, mono, cap, tag=None):
    out = [f'<rect x="24" y="{y}" width="512" height="{h}" class="box"/>']
    out.append(L(44, y + 30, "t", title))
    if tag:
        out.append(L(516, y + 30, "c", tag, "end"))
    out.append(L(44, y + 54, "m", mono))
    out.append(L(44, y + 76, "c", cap))
    return "".join(out)
b.append('<path class="s" d="M24 37H12V278"/><path class="s" d="M12 150H22M15 144l7 6-7 6M12 278H22M15 272l7 6-7 6"/>')
b.append(box(104, 92, {"en": "Localia's sessions", "fr": "Sessions de Localia", "zh": "Localia 的工作階段"},
             "CLAUDE_CONFIG_DIR → Localia/claude-config",
             {"en": "isolated config: your ~/.claude is never touched",
              "fr": "config isolée : votre ~/.claude n'est jamais modifié",
              "zh": "獨立設定：絕不動到你的 ~/.claude"},
             {"en": "default", "fr": "par défaut", "zh": "預設"}))
b.append(L(44, 220, "c it", {"en": "or", "fr": "ou", "zh": "或"}))
b.append(box(232, 92, {"en": "Every claude, in any terminal", "fr": "Chaque claude, dans tout terminal", "zh": "任何終端機裡的每個 claude"},
             "~/.zshrc block → shell/claude.zsh",
             {"en": "reversible shim: backup first, removable in one click",
              "fr": "shim réversible : sauvegarde d'abord, retrait en un clic",
              "zh": "可還原的 shim：先備份，一鍵移除"},
             {"en": "opt-in", "fr": "sur option", "zh": "選用"}))
b.append('<path class="s" d="M536 150H548V344H220V356M536 278H548M215 349l5 7 5-7"/>')
# Claude Code + barred cloud
b.append('<rect x="24" y="364" width="408" height="92" class="box strong"/>')
b.append(L(44, 394, "t", "Claude Code"))
b.append(L(44, 418, "m", "ANTHROPIC_BASE_URL=http://127.0.0.1:…"))
b.append(L(44, 440, "c", {"en": "the model's real context window, up to 65,536",
                          "fr": "la vraie fenêtre du modèle, jusqu'à 65 536",
                          "zh": "模型的實際上下文視窗，最多 65,536"}))
b.append('<path class="s2 dash" d="M432 410H462"/><path class="ac" d="M440 402l14 16M454 402l-14 16"/>')
b.append('<path class="s2" d="M478 414h44a10 10 0 0 0 0-20 14 14 0 0 0-26-6 11 11 0 0 0-18 8 9 9 0 0 0 0 18Z"/>')
b.append(L(500, 440, "c sm", {"en": "no silent", "fr": "pas de repli", "zh": "不會悄悄"}, "middle"))
b.append(L(500, 456, "c sm", {"en": "fallback", "fr": "silencieux", "zh": "改用雲端"}, "middle"))
b.append(arrow_down(220, 456, 500))
# loopback boundary
b.append('<rect x="24" y="500" width="512" height="132" class="bound"/>')
b.append(L(44, 528, "t", {"en": "127.0.0.1 · this Mac only", "fr": "127.0.0.1 · ce Mac seulement", "zh": "127.0.0.1 · 僅限這台 Mac"}))
for x, name, port in ((44, "Ollama", ":11434"), (220, "llama.cpp", ":11435"), (396, "MLX", ":11436")):
    b.append(f'<rect x="{x}" y="546" width="152" height="68" class="box"/>')
    b.append(L(x + 16, 574, "t", name))
    b.append(L(x + 16, 598, "m", port + (" 4-bit" if name == "MLX" else " Q4_K_M")))
svg("localmode.svg", 560, 650, "".join(b))

# ── 3. memory ────────────────────────────────────────────────────────────
X0, U = 40, 20  # 20 units per GB, 24 GB = 480
ws, head, model = 17.8, 1.5, 10
pool = ws - head
b = []
def bar(y, gb, cls):
    return f'<rect x="{X0}" y="{y}" width="{gb*U:.1f}" height="26" class="{cls}"/>'
# row 1: RAM
b.append(L(X0, 36, "t", {"en": "Unified memory · 24 GB", "fr": "Mémoire unifiée · 24 Go", "zh": "統一記憶體 · 24 GB"}))
b.append(bar(48, 24, "box"))
b.append(f'<rect x="{X0+ws*U:.1f}" y="48" width="{(24-ws)*U:.1f}" height="26" class="hatch"/>')
b.append(L(X0 + 24 * U, 94, "c sm", {"en": "beyond the GPU limit", "fr": "hors limite GPU", "zh": "超出 GPU 上限"}, "end"))
# row 2: working set
b.append(L(X0, 134, "t", {"en": "Metal working set · 17.8 GB", "fr": "Working set Metal · 17,8 Go", "zh": "Metal 工作集 · 17.8 GB"}))
b.append(L(X0, 156, "m", "recommendedMaxWorkingSetSize"))
b.append(bar(168, ws, "box"))
b.append(f'<rect x="{X0+pool*U:.1f}" y="168" width="{head*U:.1f}" height="26" class="hatch"/>')
b.append(L(X0 + ws * U + 10, 186, "c sm", {"en": "1.5 GB kept free", "fr": "1,5 Go laissés libres", "zh": "保留 1.5 GB"}))
# pool ticks
for pct in (60, 85, 100):
    x = X0 + pool * U * pct / 100
    if pct < 100:
        b.append(f'<path class="s2" d="M{x:.1f} 240V318"/>')
    b.append(L(f"{x+5:.1f}", 236, "c sm", f"{pct} %") if pct == 100 else L(f"{x:.1f}", 236, "c sm", f"{pct} %", "middle"))
# row 3: model
b.append(bar(270, model, "fa"))
b.append(f'<rect x="{X0+model*U:.1f}" y="270" width="{(pool-model)*U:.1f}" height="26" class="box"/>')
b.append(L(X0, 340, "t", {"en": "Gemma 4 E4B · Q4_K_M · ≈10 GB", "fr": "Gemma 4 E4B · Q4_K_M · ≈10 Go", "zh": "Gemma 4 E4B · Q4_K_M · ≈10 GB"}))
b.append(L(X0, 364, "c", {"en": "fits, with room for the context · ≈19 tok/s estimated",
                          "fr": "tient, avec de la place pour le contexte · ≈19 tok/s estimés",
                          "zh": "放得下，仍有空間給上下文 · 估計約 19 tok/s"}))
# GPU limit line
gx = X0 + pool * U
b.append(f'<path class="ac dash" d="M{gx:.1f} 160V318"/>')
defs = ('<pattern id="lc-hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        '<path d="M0 0V6" style="stroke:var(--ink-2)" stroke-width="1"/></pattern>')
svg("memory.svg", 560, 380, "".join(b), defs)
print("ok")
