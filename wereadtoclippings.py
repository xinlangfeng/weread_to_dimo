import datetime


def generate_my_clippings(notes):
    clippings = []
    current_time = datetime.datetime.now()
    time_str = current_time.strftime("%Y年%m月%d日%A %p %I:%M:%S")
    for note in notes:
        title = note['title']
        content = note['content']
        clippings.append(f"{title}\n - 您在位置 #1-1的标注 | 添加于 {time_str} \n \n {content} \n==========")
    return '\n'.join(clippings)

def parse_notes(text):
    lines = text.split('\n')
    notes = []
    for i, line in enumerate(lines):
        if line.startswith('《'):
            title = line.replace('《','')
            title = title.replace('》','')
        if line.startswith('>>'):
            content_line = i
            content = lines[content_line].split('>>')[1].strip()
            notes.append({
                'title': title,
                'content': content
            })
    return notes

if __name__ == '__main__':
    with open('note.txt', 'r',encoding='utf-8') as f:
        notes_text = f.read()
    notes = parse_notes(notes_text)    
    clippings = generate_my_clippings(notes)
    with open('my_clippings.txt', 'w',encoding='utf-8') as f:
        f.write(clippings)
