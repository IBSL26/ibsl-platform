# Renames "Capstone Blueprint" to "Capstone S2R Blueprint" (Carol, 27 Oct 2026) in the portal pages,
# scripts, unit decks (slides and notes), deck upload copies and reader manifests. Backs up first.
# Byte-level replace keeps encoding and line endings as found. Safe to run twice (skips done files).
import os, glob, shutil, zipfile
OLD, NEW = b'Capstone Blueprint', b'Capstone S2R Blueprint'
BK = 'Claude outputs/Backups/Blueprint rename 27 Oct'
os.makedirs(BK, exist_ok=True)
def backup(f):
    dst = os.path.join(BK, f.replace('/', ' __ '))
    if not os.path.exists(dst): shutil.copy2(f, dst)
done = []
def fix_bytes(b):
    b2 = b.replace(NEW, b'\0KEEP\0').replace(OLD, NEW).replace(b'\0KEEP\0', NEW)
    return b2, b.count(OLD) - b.count(NEW)
# 1. pages and scripts (Units 10-12 hold none)
for f in sorted(glob.glob('*.html') + glob.glob('*.js')):
    b = open(f, 'rb').read()
    b2, n = fix_bytes(b)
    if b2 != b:
        backup(f); open(f, 'wb').write(b2); done.append((f, n))
# 2. decks: rewrite the slide and notes XML inside each .pptx
def fix_pptx(f):
    zin = zipfile.ZipFile(f); items = []; total = 0
    for info in zin.infolist():
        data = zin.read(info.filename)
        if info.filename.endswith('.xml') and ('ppt/slides/slide' in info.filename or 'ppt/notesSlides/' in info.filename):
            data2, n = fix_bytes(data); total += max(n, 0); data = data2
        items.append((info, data))
    zin.close()
    if not total: return 0
    backup(f)
    tmp = f + '.tmp'
    with zipfile.ZipFile(tmp, 'w') as zout:
        for info, data in items: zout.writestr(info, data, compress_type=info.compress_type)
    os.replace(tmp, f)
    return total
for f in sorted(glob.glob('Unit decks/Unit 0*.pptx')):
    n = fix_pptx(f)
    if n: done.append((f, n))
# 3. deck upload copies: same file as the Unit decks master
pairs = {'01': 'Module-1', '02': 'Module-2', '03': 'Module-2', '04': 'Module-2'}
for f in sorted(glob.glob('Unit decks/Unit 0*.pptx')):
    u = os.path.basename(f)[5:7]
    dst = 'Claude outputs/Deck upload/%s/unit-%s.pptx' % (pairs.get(u, 'Module-3'), u)
    if os.path.exists(dst) and open(dst, 'rb').read() != open(f, 'rb').read() and OLD in b''.join(
            zipfile.ZipFile(dst).read(n) for n in zipfile.ZipFile(dst).namelist() if n.endswith('.xml')):
        backup(dst); shutil.copy2(f, dst); done.append((dst, 'copied from Unit decks'))
# 4. reader manifests (notes text shown in the deck reader)
for f in sorted(glob.glob('Claude outputs/Deck upload/Module-*/unit-0*/manifest.json')):
    b = open(f, 'rb').read(); b2, n = fix_bytes(b)
    if b2 != b: backup(f); open(f, 'wb').write(b2); done.append((f, n))
for d in done: print(*d)
print(len(done), 'files changed')
