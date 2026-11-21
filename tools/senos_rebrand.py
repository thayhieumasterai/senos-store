"""Turn upstream's Javis Store text into SenOS's (run from the repo root). Safe to run again after every sync.

Kept as-is, because installed SenOS and the zips depend on them: pack ids (javis.*), manifest file names
(javis-pack.yaml), tool names (javis_*), the zips in dist/ (their sha256 is in index.json), and packs/ sources.
Changed: the repo address, the index marker and store name, and the brand word in docs and in index text.
The workflow .github/workflows/dong-bo-javis.yml runs this after merging upstream.
"""
import json, pathlib, re

ROOT = pathlib.Path(".")
URLS = [("blogminhquy/javis-store", "thayhieumasterai/senos-store"),
        ("blogminhquy/javis-os", "thayhieumasterai/senos-os"),
        ("javis-store-bot", "senos-store-bot"),
        ("javis-store-soi", "senos-store-soi"),
        ("javis-pack-index", "senos-pack-index")]
WORD = [(re.compile(r"\bJavis OS\b"), "SenOS"), (re.compile(r"\bJavis Store\b"), "Kho SenOS"),
        (re.compile(r"\bJavis\b"), "SenOS")]
CREDIT_START = "> Kho này bắt nguồn từ"
CREDIT = (CREDIT_START + " [Javis Store](https://github.com/blogminhquy/javis-store) của Nguyễn Minh Quý. "
          "Mã gói (`javis.*`) được giữ nguyên để mọi gói cài và chạy đúng trên SenOS.")
SKIP_TOP = ("dist", "packs", "mcp", "mcp-nguon", ".git")


def words(s):
    for rx, b in WORD:
        s = rx.sub(b, s)
    return s


def urls(s):
    for a, b in URLS:
        s = s.replace(a, b)
    return s


# Store tests run against the SenOS app (kiem-tra.yml checks out senos-os): the names the APP owns are SenOS's there.
# Names the packs own (javis.gate, javis-gate, JAVIS_OS_DIR = where the app is checked out) stay.
HOST_IN_TESTS = [(re.compile(r"\bJAVIS_(STATE_DIR|REQUIRE_LOGIN|API_STREAM_TOOLS)\b"), r"SENOS_\1"),
                 (re.compile(r"\bjavis_chat_"), "senos_chat_"), (re.compile(r"JAVIS GATE"), "SENOS GATE")]


def host_names(s):
    for rx, b in HOST_IN_TESTS:
        s = rx.sub(b, s)
    return s


def prose(s):
    """Docs: URLs and brand words, but never on the credit line (it names where the store comes from)."""
    return "\n".join(ln if ln.startswith(CREDIT_START) else words(urls(ln)) for ln in s.split("\n"))


changed = 0
for p in ROOT.rglob("*"):
    # the sync workflow names upstream's repo on purpose; this script and the index are handled on their own
    if (not p.is_file() or p.parts[0] in SKIP_TOP or p.name in ("index.json", "senos_rebrand.py", "dong-bo-javis.yml")):
        continue
    if p.suffix not in (".md", ".py", ".yml", ".yaml", ".json", ".txt"):
        continue
    s = p.read_text(encoding="utf-8")
    t = prose(s) if p.suffix == ".md" or p.parts[0] == "huong-dan" else urls(s)
    if p.parts[0] == "tests" and p.suffix == ".py":
        t = host_names(t)
    if t != s:
        p.write_text(t, encoding="utf-8", newline="\n")
        changed += 1

# index: marker, store block, brand word in the human text fields only (ids, urls, hashes untouched)
KEEP = ("id", "url", "sha256", "replaces", "requires", "pairs", "connector", "connectors")


def walk(v, key=""):
    if isinstance(v, dict):
        return {k: walk(x, k) for k, x in v.items()}
    if isinstance(v, list):
        return [walk(x, key) for x in v]
    if isinstance(v, str) and key not in KEEP:
        return words(urls(v))
    return v


ip = ROOT / "index.json"
raw = ip.read_text(encoding="utf-8")
idx = json.loads(raw)
idx["format"] = "senos-pack-index"
idx["store"] = {"name": "Kho cài đặt SenOS", "url": "https://github.com/thayhieumasterai/senos-store"}
idx["_doc"] = words(urls(idx.get("_doc", "")))
idx["packs"] = walk(idx["packs"])
out = json.dumps(idx, ensure_ascii=False, indent=2) + "\n"
if out != raw:
    ip.write_text(out, encoding="utf-8", newline="\n")
    changed += 1

rp = ROOT / "README.md"
r = rp.read_text(encoding="utf-8")
if CREDIT_START not in r:
    first, rest = r.split("\n", 1)
    rp.write_text(first + "\n\n" + CREDIT + "\n" + rest, encoding="utf-8", newline="\n")
    changed += 1
print("files changed:", changed)
