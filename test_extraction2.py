import fitz
path = "/Users/cemkaya/Documents/Ebooks_important/Practical Guide to LTE-A VoLTE and IoT Paving the way towards 5G.pdf"
doc = fitz.open(path)
print(f"Total pages: {doc.page_count}")
for page_num in range(min(5, doc.page_count)):
    page = doc.load_page(page_num)
    blocks = page.get_text('blocks')
    print(f"Page {page_num} has {len(blocks)} blocks.")
    for i, b in enumerate(blocks[:3]):
        print(f"  Block {i}: type={b[6]}, coords=({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}), text='{b[4].strip()[:50]}...'")
doc.close()
