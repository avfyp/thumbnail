import base64
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Cara pakai:")
    print("python obfuscate.py index.html")
    sys.exit()

src = Path(sys.argv[1])

if not src.exists():
    print("File tidak ditemukan:", src)
    sys.exit(1)

html = src.read_text(encoding="utf-8")
payload = base64.b64encode(html.encode("utf-8")).decode("ascii")

loader = f'''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<script>
(()=>{{
const d="{payload}";
const b=atob(d);
const u=new Uint8Array(b.length);

for(let i=0;i<b.length;i++){{
    u[i]=b.charCodeAt(i);
}}

document.open();
document.write(new TextDecoder().decode(u));
document.close();
}})();
</script>
</head>
<body></body>
</html>'''

out = src.with_name("index-obfuscated.html")
out.write_text(loader, encoding="utf-8")

print("================================")
print(" AVFYP HTML OBFUSCATOR")
print("================================")
print("Input :", src)
print("Output:", out)
print("Ukuran asli :", len(html.encode("utf-8")), "bytes")
print("Ukuran hasil :", len(loader.encode("utf-8")), "bytes")
print()
print("Selesai.")
