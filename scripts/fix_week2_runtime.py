from bs4 import BeautifulSoup
from pathlib import Path
p=Path('week02.html')
soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
script=soup.find_all('script')[-1]
js=script.string or script.get_text()
broken="if(data.radio){data.radio.forEach((choice,i)=>{const opts=[...root.querySelectorAll('input[name=\"b'+(i+1)+'\"]')];if(opts[choice]){opts[choice].checked=true;opts[choice].closest('label')?.classList.add('filled-solution')}})});"
good="if(data.radio){data.radio.forEach((choice,i)=>{const opts=[...root.querySelectorAll('input[name=\"b'+(i+1)+'\"]')];if(opts[choice]){opts[choice].checked=true;const lab=opts[choice].closest('label');if(lab)lab.classList.add('filled-solution');}});}" 
if broken not in js:
    raise SystemExit('Expected broken radio-solution code was not found')
js=js.replace(broken,good)
script.string=js
labels={'strategy':'Reading strategy','clues':'Context clue types','signals':'Signal words','core':'Core class practice','families':'Word families','reading':'Applied reading','speaking':'Partner practice','exit':'Exit ticket'}
for sid,text in labels.items():
    sec=soup.find('section',id=sid)
    if sec:
        lab=sec.select_one('.head .label')
        if lab: lab.string=text
for sec in list(soup.find_all('section')):
    note=sec.find('div',class_='note')
    if note and '10-MINUTE REST' in note.get_text():
        sec.decompose(); break
p.write_text(str(soup),encoding='utf-8')
