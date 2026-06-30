import re
import os
import glob

def clean_filename(title):
    # Remove quotes, weird chars, replace spaces with underscores
    title = re.sub(r'[^A-Za-z0-9 ]+', '', title)
    title = title.strip().replace(' ', '_').upper()
    return title

def split_script():
    base_dir = '/data/data/com.termux/files/home/storage/downloads/ADM/novel/02_Webtoon_Script'
    raw_file = os.path.join(base_dir, 'raw_script.txt')
    
    with open(raw_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all episodes using regex
    # Matches "EPISODE 1 - TITLE", "EPISODE 10 - TITLE", etc.
    # Allowing variations in quotes or hyphens
    pattern = r'(EPISODE\s+(\d+)\s*[-–—]\s*([^\n]+))'
    
    matches = list(re.finditer(pattern, content))
    
    if not matches:
        print("No episodes found!")
        return

    episodes = []
    
    for i in range(len(matches)):
        start_idx = matches[i].start()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(content)
        
        ep_text = content[start_idx:end_idx].strip()
        ep_num = int(matches[i].group(2))
        ep_title = matches[i].group(3).strip()
        
        # Clean title for filename
        clean_name = clean_filename(ep_title)
        # Some titles have "(Versi Komik/Dialog Fokus)" which we should strip
        if "VERSI" in clean_name:
            clean_name = clean_name.split("VERSI")[0].strip("_")
            
        filename = f"EPISODE_{ep_num:02d}_{clean_name}.md"
        
        episodes.append({
            'num': ep_num,
            'title': ep_title,
            'filename': filename,
            'text': ep_text
        })
        
    # Sort just in case
    episodes.sort(key=lambda x: x['num'])
    
    # Write files with interlinking
    for i, ep in enumerate(episodes):
        out_path = os.path.join(base_dir, ep['filename'])
        
        body = ep['text']
        
        # Build navigation
        nav = "\n\n---\n### Navigasi\n"
        
        if i > 0:
            prev_ep = episodes[i-1]
            nav += f"⬅️ [[{prev_ep['filename'].replace('.md', '')} | {prev_ep['title']}]]\n"
            
        if i < len(episodes) - 1:
            next_ep = episodes[i+1]
            nav += f"➡️ [[{next_ep['filename'].replace('.md', '')} | {next_ep['title']}]]\n"
            
        # Write to file
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(body + nav)
            
        print(f"Created: {ep['filename']}")
        
    # Create index
    index_path = os.path.join(base_dir, '00_INDEX_WEBTOON.md')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# Indeks Naskah Webtoon: Kael Fury of Zerath\n\n")
        for ep in episodes:
            f.write(f"- [[{ep['filename'].replace('.md', '')} | Episode {ep['num']}: {ep['title']}]]\n")
            
    print("Created: 00_INDEX_WEBTOON.md")
    
if __name__ == '__main__':
    split_script()
