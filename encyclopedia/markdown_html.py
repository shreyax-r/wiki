import re

def simple_markdown_to_html(md_text):
    html = []
    in_list = False
    lines = md_text.split('\n')

    for line in lines:
        line = line.strip()

        # Headings
        match = re.match(r'^(#{1,6})\s*(.*)', line)
        if match:
            level = len(match.group(1))
            content = match.group(2)
            html.append(f'<h{level}>{content}</h{level}>')
            continue


        # Unordered list
        if line.startswith('* '):
            if not in_list:
                html.append('<ul>')
                in_list = True
            html.append(f'<li>{line[2:].strip()}</li>')
            continue
        else:
            if in_list:
                html.append('</ul>')
                in_list = False

        # Bold (**bold**)
        line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)

        # Links [text](url)
        line = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', line)

        if line:
            html.append(f'<p>{line}</p>')

    if in_list:
        html.append('</ul>')

    return '\n'.join(html)