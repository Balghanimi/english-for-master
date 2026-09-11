from bs4 import BeautifulSoup
from pathlib import Path

p=Path('week02.html')
soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')

meta=soup.find('meta',attrs={'name':'description'})
if meta:
    meta['content']='Week 2 — Academic Vocabulary in Context: context clues, signal words, general academic examples, inference strategies, word families, and interactive solutions.'

nav=soup.find('nav',attrs={'aria-label':'Week 2 navigation'})
if nav:
    for a in nav.find_all('a'):
        if a.get('href')=='#agenda': a.string='Today’s Roadmap'
    if not nav.find('a',href='#source-practice'):
        mixed=nav.find('a',href='#mixed')
        a=soup.new_tag('a',href='#source-practice'); a.string='Source Practice'
        mixed.insert_after(a)

source=soup.select_one('section .source')
if source:
    source.clear()
    source.append(BeautifulSoup('<strong>Basis for Week 2:</strong> <em>Understanding Vocabulary in Context</em>. Its original sequence is kept: <strong>why context clues matter → four clue types → signal words → reading strategy → guided practice → meaning inference</strong>. General academic examples from the lecture are restored alongside a smaller number of engineering examples. <strong>Word Families</strong> remains a short course extension.','html.parser'))

agenda=soup.find('section',id='agenda')
if agenda:
    agenda.clear()
    agenda.extend(BeautifulSoup('''<div class="head"><div><span class="label">Student roadmap</span><h2>What We Will Do Today</h2></div><p>A simple overview of the lesson — the detailed timing is kept for the instructor.</p></div><div class="grid3"><div class="card"><h3>1. Notice</h3><p>See how surrounding words and sentences can reveal meaning.</p></div><div class="card"><h3>2. Identify</h3><p>Recognise <strong>definition, exemplification, contrast, and general-knowledge</strong> clues.</p></div><div class="card"><h3>3. Use Signals</h3><p>Spot words such as <strong>or, such as, however, unlike, whereas</strong>.</p></div><div class="card"><h3>4. Infer</h3><p>Make a likely meaning from evidence before using a dictionary.</p></div><div class="card"><h3>5. Practise</h3><p>Work with general academic and engineering examples, then check solutions.</p></div><div class="card"><h3>6. Apply</h3><p>Use the same strategy in a short connected reading and your own vocabulary log.</p></div></div><div class="takeaway" style="margin-top:14px"><strong>Main goal:</strong> do not stop at every new word. Read on, locate evidence, infer a meaning, and then verify it if necessary.</div>''','html.parser').contents)

clues=soup.find('section',id='clues')
if clues:
    head=clues.find('div',class_='head')
    if head and head.find('p'): head.find('p').string='These are the four clue types used in the original lecture document.'
    cards=clues.select('.clue-card')
    data=[
      ('1. Definition','The writer explains the word directly, often after a dash, <strong>or</strong>, commas, <strong>is</strong>, or <strong>means</strong>.','The <strong>media</strong> — organisations such as newspapers and television that provide news and information — influence how people receive current events.','Clue: the meaning is given immediately after the word.'),
      ('2. Exemplification','The writer gives examples that show what the word includes.','Symbols can communicate ideas. <strong>For example</strong>, a heart can represent love.','Clue: <strong>for example</strong> introduces an example.'),
      ('3. Contrast','An opposite or different idea helps reveal the meaning.','The teacher considered <strong>eliminating</strong> one question; <strong>however</strong>, he finally decided to keep it.','Clue: <strong>however</strong> contrasts <em>eliminating</em> with <em>keep</em>.'),
      ('4. General Knowledge','Knowledge of the topic or situation helps you interpret the word.','News reports described the <strong>devastation</strong> after a major earthquake and tsunami.','Clue: knowledge of the disaster suggests serious destruction.')]
    for card,d in zip(cards,data):
        card.clear(); card.extend(BeautifulSoup(f'<h3>{d[0]}</h3><p>{d[1]}</p><div class="prompt">{d[2]}</div><span class="small-note">{d[3]}</span>','html.parser').contents)

mixed=soup.find('section',id='mixed')
if mixed:
    mixed.clear()
    mixed.extend(BeautifulSoup('''<div class="head"><div><span class="label">General / real-world examples</span><h2>Context Clues Beyond Engineering</h2></div><p>The original lecture uses ordinary academic and real-life situations. These examples help you practise the skill without depending on specialist knowledge.</p></div><div class="mixed-grid"><div class="mixed-example"><strong>Education — contrast:</strong><br/>Mina felt calm before the exam; <em>however</em>, when she saw the first page, she became <span class="target-word">agitated</span>.<div class="keyline"><strong>Key words:</strong> calm · however · agitated</div></div><div class="mixed-example"><strong>Journalism — examples:</strong><br/>A journalist must be <span class="target-word">versatile</span>. <em>For instance</em>, the job may require writing, interviewing, speaking, researching, and working quickly.<div class="keyline"><strong>Key words:</strong> for instance · many different skills</div></div><div class="mixed-example"><strong>Work — contrast:</strong><br/>His office job was <span class="target-word">sedentary</span>; <em>in contrast</em>, his new reporting job kept him away from his desk most of the day.<div class="keyline"><strong>Key words:</strong> in contrast · away from his desk</div></div><div class="mixed-example"><strong>Everyday technology — example:</strong><br/>Many people prefer <span class="target-word">portable</span> devices, <em>such as</em> phones, tablets, and small music players that can be carried easily.<div class="keyline"><strong>Key words:</strong> such as · carried easily</div></div></div>''','html.parser').contents)

if not soup.find('section',id='source-practice'):
    sec=BeautifulSoup('''<section id="source-practice"><div class="head"><div><span class="label">From the original lecture</span><h2>Source Practice: Clue Type → Meaning</h2></div><p>The lecture first asks you to identify the clue type, then use that clue to infer the meaning. Try both stages before pressing the solution.</p></div><div class="grid"><div class="task" id="sol-sourceA"><h3>Activity — Identify the Clue Type</h3><ol><li>She was calm before the test. However, after reading the first question, she became <strong>agitated</strong>.<input type="text" placeholder="Clue type + evidence"/></li><li>Journalists need to be <strong>versatile</strong>. For instance, they write, interview, speak, research, and work quickly.<input type="text" placeholder="Clue type + evidence"/></li><li>His old office job was <strong>sedentary</strong>. In contrast, his reporting job kept him away from his desk.<input type="text" placeholder="Clue type + evidence"/></li><li>Many people prefer <strong>portable</strong> devices, such as phones and tablets.<input type="text" placeholder="Clue type + evidence"/></li><li>The organisers <strong>estimated</strong> that more than 10,000 people attended. They were not exactly sure because the crowd was too large to count.<input type="text" placeholder="Clue type + evidence"/></li><li>Most <strong>illiterate</strong> adults in the report — those who cannot read or write — lived outside the main cities.<input type="text" placeholder="Clue type + evidence"/></li></ol><div class="solution-controls"><button class="solution-btn" type="button" onclick="fillSolution('sourceA')">Fill solution</button><button class="clear-btn" type="button" onclick="clearSolution('sourceA')">Clear</button><span class="solution-note">Identify the evidence, not only the answer.</span></div><div class="answer-status" id="status-sourceA"></div></div><div class="task" id="sol-sourceB"><h3>Activity — Infer the Meaning</h3><ol><li><strong>agitated</strong><input type="text" placeholder="likely meaning"/></li><li><strong>versatile</strong><input type="text" placeholder="likely meaning"/></li><li><strong>sedentary</strong><input type="text" placeholder="likely meaning"/></li><li><strong>portable</strong><input type="text" placeholder="likely meaning"/></li><li><strong>estimated</strong><input type="text" placeholder="likely meaning"/></li><li><strong>illiterate</strong><input type="text" placeholder="likely meaning"/></li></ol><div class="solution-controls"><button class="solution-btn" type="button" onclick="fillSolution('sourceB')">Fill solution</button><button class="clear-btn" type="button" onclick="clearSolution('sourceB')">Clear</button><span class="solution-note">Compare your inference with the evidence from Activity A.</span></div><div class="answer-status" id="status-sourceB"></div></div></div></section>''','html.parser').find('section')
    mixed.insert_after(sec)

script=soup.find_all('script')[-1]
js=script.string or script.get_text()
bad="if(data.radio){data.radio.forEach((choice,i)=>{const opts=[...root.querySelectorAll('input[name=\"b'+(i+1)+'\"]')]; if(opts[choice]){opts[choice].checked=true;opts[choice].closest('label')?.classList.add('filled-solution')}})});"
good="if(data.radio){data.radio.forEach((choice,i)=>{const opts=[...root.querySelectorAll('input[name=\"b'+(i+1)+'\"]')];if(opts[choice]){opts[choice].checked=true;const lab=opts[choice].closest('label');if(lab)lab.classList.add('filled-solution');}});}" 
js=js.replace(bad,good)
js=js.replace("el.closest('label')?.classList.remove('filled-solution')","(()=>{const lab=el.closest('label');if(lab)lab.classList.remove('filled-solution')})()")
if 'sourceA:{text' not in js:
    insert="""  sourceA:{text:[\n    'Contrast — “however” contrasts calm with agitated',\n    'Exemplification — “for instance” introduces several different skills',\n    'Contrast — “in contrast” compares sitting at a desk with being away from the desk',\n    'Exemplification — “such as” introduces examples of portable devices',\n    'General knowledge / explanation — not exactly sure; the crowd was too large to count',\n    'Definition — “those who cannot read or write” directly explains illiterate'\n  ]},\n  sourceB:{text:[\n    'very nervous / disturbed / unable to remain calm',\n    'able to do many different kinds of tasks',\n    'involving a lot of sitting and little physical movement',\n    'easy to carry or move',\n    'made a careful approximate guess',\n    'unable to read or write'\n  ]},\n"""
    js=js.replace('  extraA:{text:[',insert+'  extraA:{text:[')
if 'window.fillSolution=fillSolution' not in js:
    js=js.replace("const key='efm-progress-v1'","window.fillSolution=fillSolution;window.clearSolution=clearSolution;\nconst key='efm-progress-v1'")
script.string=js
p.write_text(str(soup),encoding='utf-8')
