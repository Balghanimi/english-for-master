from bs4 import BeautifulSoup
from pathlib import Path

src=Path('week02.html')
out=Path('week02.html')
html=src.read_text(encoding='utf-8')
soup=BeautifulSoup(html,'html.parser')

meta=soup.find('meta',attrs={'name':'description'})
if meta:
    meta['content']='Week 2 — Academic Vocabulary in Context: context clues, key words, mixed academic examples, strategic inference, word families, and interactive solutions.'
source=soup.find('div',class_='source')
if source:
    source.clear()
    source.append(BeautifulSoup('<strong>Basis for Week 2:</strong> the course handout <em>Understanding Vocabulary in Context</em>. The core sequence is retained: <strong>context clues → clue types → signal words → reading strategy → practice</strong>. The page uses both <strong>Electrical Engineering</strong> and <strong>mixed academic / real-world contexts</strong>. The <strong>Word Families</strong> section is a course extension to support MSc reading.', 'html.parser'))

style=soup.find('style')
extra_css='''\n.keyword-bank{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.keyword-item{padding:12px;border:1px solid var(--line);border-radius:11px;background:#fbfdfb}.keyword-item b{display:block;color:var(--navy);margin-bottom:3px}.keyword-item span{font-size:13px;color:var(--muted)}.mixed-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}.mixed-example{padding:14px;border:1px solid var(--line);border-left:5px solid var(--kufa-blue,#276f97);border-radius:10px;background:#f8fbfc}.mixed-example:nth-child(2n){border-left-color:var(--kufa-gold,#c6a15b)}.solution-controls{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:11px}.solution-btn,.clear-btn{appearance:none;border:1.5px solid var(--kufa-green,#1f6b4a);border-radius:9px;padding:8px 11px;font:800 12px system-ui;cursor:pointer}.solution-btn{background:var(--kufa-green,#1f6b4a);color:#fff}.solution-btn:hover{filter:brightness(.94)}.clear-btn{background:#fff;color:#15563b}.solution-note{font:700 11px system-ui;color:#4b5c53}.filled-solution{background:#eef8f2!important;border-color:#76aa89!important}.keyline{margin-top:8px;padding:9px 11px;border-radius:9px;background:#f7f1df;border:1px solid #dbc792;color:#5b4427;font-size:13px}.answer-status{margin-top:8px;font:700 12px system-ui;color:#15563b}.answer-status:empty{display:none}\n@media(max-width:900px){.keyword-bank{grid-template-columns:1fr 1fr}}@media(max-width:680px){.keyword-bank,.mixed-grid{grid-template-columns:1fr}}\n'''
if extra_css.strip() not in style.get_text():
    style.append(extra_css)

nav=soup.find('nav',attrs={'aria-label':'Week 2 navigation'})
if nav and not nav.find('a',href='#keywords'):
    links=nav.find_all('a',recursive=False)
    outcomes_link=next((a for a in links if a.get('href')=='#outcomes'),None)
    if outcomes_link:
        outcomes_link.insert_after(BeautifulSoup('<a href="#keywords">Key Words</a>','html.parser').a)
    links=nav.find_all('a',recursive=False)
    clue_link=next((a for a in links if a.get('href')=='#clues'),None)
    if clue_link:
        clue_link.insert_after(BeautifulSoup('<a href="#mixed">Mixed Examples</a>','html.parser').a)

outcomes=soup.find('section',id='outcomes')
keyword_html='''
<section id="keywords"><div class="head"><div><span class="label">Week 2 reference</span><h2>Key Words for Vocabulary in Context</h2></div><p>These terms are the language you need to talk about how you inferred a meaning.</p></div>
<div class="keyword-bank">
<div class="keyword-item"><b>context</b><span>the words and ideas surrounding a word</span></div>
<div class="keyword-item"><b>context clue</b><span>evidence that helps reveal a meaning</span></div>
<div class="keyword-item"><b>infer</b><span>reach a likely meaning from evidence</span></div>
<div class="keyword-item"><b>inference</b><span>the meaning or conclusion you infer</span></div>
<div class="keyword-item"><b>definition</b><span>a direct explanation of meaning</span></div>
<div class="keyword-item"><b>exemplification</b><span>examples that clarify a category or idea</span></div>
<div class="keyword-item"><b>contrast</b><span>an opposite or different idea used as a clue</span></div>
<div class="keyword-item"><b>signal word</b><span>a word such as <em>however</em> or <em>such as</em> that points to a clue</span></div>
<div class="keyword-item"><b>provisional</b><span>temporary; acceptable until more evidence is available</span></div>
<div class="keyword-item"><b>word family</b><span>related forms such as <em>analyse, analysis, analytical</em></span></div>
<div class="keyword-item"><b>evidence</b><span>the exact phrase, example, number, or contrast supporting your guess</span></div>
<div class="keyword-item"><b>verify</b><span>check your inferred meaning after you have made a guess</span></div>
</div><div class="keyline"><strong>Useful answer frame:</strong> “I infer that <strong>_____</strong> means <strong>_____</strong> because <strong>_____</strong> provides a <strong>definition / example / contrast / general-knowledge</strong> clue.”</div></section>
'''
if outcomes and not soup.find('section',id='keywords'):
    outcomes.insert_after(BeautifulSoup(keyword_html,'html.parser'))

clues=soup.find('section',id='clues')
mixed_html='''
<section id="mixed"><div class="head"><div><span class="label">Mixed academic contexts</span><h2>Context Clues Beyond Electrical Engineering</h2></div><p>Vocabulary-in-context is a general academic reading skill. These examples deliberately come from different fields.</p></div>
<div class="mixed-grid">
<div class="mixed-example"><strong>Public health — definition:</strong><br/>A disease is <span class="target-word">endemic</span>, <em>meaning that it is regularly present in a particular population or region</em>.<div class="keyline"><strong>Key words:</strong> meaning that · regularly present</div></div>
<div class="mixed-example"><strong>Environmental science — exemplification:</strong><br/><span class="target-word">Arid</span> environments, <em>such as deserts and very dry plateaus</em>, receive little rainfall.<div class="keyline"><strong>Key words:</strong> such as · deserts · dry</div></div>
<div class="mixed-example"><strong>Economics — contrast:</strong><br/>Consumer demand was <span class="target-word">buoyant</span> in the first quarter; <em>however</em>, it weakened considerably later in the year.<div class="keyline"><strong>Key words:</strong> however · weakened later</div></div>
<div class="mixed-example"><strong>Computing — numerical context:</strong><br/>The added processing delay was <span class="target-word">negligible</span>: only 2 ms compared with a total response time of 480 ms.<div class="keyline"><strong>Key words:</strong> only 2 ms · compared with 480 ms</div></div>
</div></section>
'''
if clues and not soup.find('section',id='mixed'):
    clues.insert_after(BeautifulSoup(mixed_html,'html.parser'))

def task_by_heading(text):
    h=soup.find(['h3','h2'],string=lambda x: x and text in x)
    if not h: return None
    return h.find_parent(['div','section'])

def add_controls(container, group):
    if not container or container.find('button',onclick=f"fillSolution('{group}')"):
        return
    note=container.find('div',class_='student-answer-note')
    controls=BeautifulSoup(f'''<div class="solution-controls"><button type="button" class="solution-btn" onclick="fillSolution('{group}')">Fill solution</button><button type="button" class="clear-btn" onclick="clearSolution('{group}')">Clear</button><span class="solution-note">Try the task first, then use the solution.</span></div><div class="answer-status" id="status-{group}"></div>''','html.parser')
    if note:
        note.string='Interactive solution available below.'
        note.insert_after(controls)
    else:
        container.append(controls)

for key, heading in [
    ('warmup','Warm-Up — Do Not Use a Dictionary'),
    ('signal','Signal Hunt'),
    ('activityA','Activity A — Identify the Clue Type'),
    ('activityB','Activity B — Infer the Meaning'),
    ('activityC','Activity C — Choose the Correct Family Member'),
    ('extraA','Extra A — Context-Clue Challenge'),
    ('extraB','Extra B — Build a Word Family')]:
    c=task_by_heading(heading)
    if c:
        c['id']=f'sol-{key}'
        add_controls(c,key)

reading=soup.find('section',id='reading')
if reading:
    reading['data-solution-group']='reading'
    add_controls(reading,'reading')

core=soup.find('section',id='core')
if core:
    banner=core.find('div',class_='core-banner')
    if banner and not core.find('div',class_='keyline'):
        banner.insert_after(BeautifulSoup('<div class="keyline"><strong>How the solution buttons work:</strong> press <strong>Fill solution</strong> after attempting an activity. The answer and the key clue/evidence are inserted directly into the fields. Press <strong>Clear</strong> to try again.</div>','html.parser'))

for script in soup.find_all('script'):
    script.extract()

script_text=r'''
const solutionMap={
  warmup:{text:[
    'attenuated = reduced / made weaker; evidence: amplitude fell from 5.0 V to 1.4 V',
    'intermittent = occurring sometimes, not continuously; evidence: appeared in 3 start-ups but was absent in the others',
    'negligible = too small to be important; evidence: 0.02 A compared with 8 A rated current',
    'transparent = allowing objects to be seen through it; evidence: internal wiring can be seen without opening the enclosure'
  ]},
  signal:{text:['or → definition','such as → exemplification','however → contrast','unlike → contrast']},
  activityA:{text:[
    'Definition — “is a resistor whose resistance changes strongly with temperature”',
    'Exemplification — “for instance solar and wind power”',
    'Contrast — “steady at first; however ... erratic” + “changed unpredictably”',
    'General knowledge / contextual result — “it cracked when it was bent” shows brittle = easily broken',
    'Definition — “that is, a second sensor installed as backup”',
    'Contrast — “whereas” contrasts smooth with distorted'
  ]},
  activityB:{text:[
    '4.8 s versus 0.7 s, introduced with “whereas”',
    '“meaning that water cannot pass through it”',
    '“for example, the same waveform repeated every 20 ms”',
    '“in contrast” + the second battery retained 94%; degradation therefore means loss of performance/capacity',
    '“because an exact measurement was not available” indicates an approximate calculation or guess'
  ],radio:[0,0,0,1,1]},
  activityC:{text:['regulation','stable','varied','analysis','approximately','variable']},
  reading:{text:[
    'occurring only sometimes / not continuously','four of twenty start-ups; absent during the remaining trials',
    'reduce / lessen','ripple decreased from 6.1% to 2.0% after the filter was added',
    'difference from a reference value','definition clue: “or difference between the measured and reference voltage”',
    'able to maintain acceptable performance under changing conditions','contrast: earlier controller became unstable; revised controller maintained performance across three loads',
    'about / close to, not exactly','numerical context: values ranged from 4.8 A to 5.2 A around 5 A'
  ]},
  extraA:{text:[
    'ductile = able to be drawn into wire without breaking; exemplification: “for example ... drawn into a thin wire”',
    'erratic = inconsistent / unpredictable; contrast: “however ... consistent and predictable”',
    'dielectric = an insulating material between conductors; definition: “that is ...”',
    'corroded = chemically deteriorated / oxidised; context: rust-like deposits + poor contact',
    'transducer = device that converts a physical quantity into an electrical signal; examples: thermocouples and piezoelectric sensors',
    'efficient = achieving the same task with less input/power; contrast: 12 W versus 7 W for the same task'
  ]},
  extraB:{text:['variation','vary','variable','stability','stabilise','stable','analysis','analyse','analytical','regulation','regulate','regulated']}
};
function groupRoot(group){return group==='reading'?document.querySelector('#reading'):document.querySelector('#sol-'+group)}
function fillSolution(group){
  const root=groupRoot(group),data=solutionMap[group];if(!root||!data)return;
  const textInputs=[...root.querySelectorAll('input[type="text"], textarea')];
  (data.text||[]).forEach((v,i)=>{if(textInputs[i]){textInputs[i].value=v;textInputs[i].classList.add('filled-solution')}});
  if(data.radio){data.radio.forEach((choice,i)=>{const opts=[...root.querySelectorAll('input[name="b'+(i+1)+'"]')];if(opts[choice]){opts[choice].checked=true;opts[choice].closest('label')?.classList.add('filled-solution')}})});
  const status=document.getElementById('status-'+group);if(status)status.textContent='Solution filled. Compare it with your own answer and identify the clue words.';
}
function clearSolution(group){
  const root=groupRoot(group);if(!root)return;
  root.querySelectorAll('input[type="text"], textarea').forEach(el=>{el.value='';el.classList.remove('filled-solution')});
  root.querySelectorAll('input[type="radio"]').forEach(el=>{el.checked=false;el.closest('label')?.classList.remove('filled-solution')});
  const status=document.getElementById('status-'+group);if(status)status.textContent='';
}
const key='efm-progress-v1',completeBtn=document.getElementById('complete');let a=[];try{a=JSON.parse(localStorage.getItem(key)||'[]')}catch(e){}
function renderCompletion(){if(!completeBtn)return;if(a.includes(2)){completeBtn.textContent='Week 2 Completed ✓';completeBtn.classList.add('done')}else{completeBtn.textContent='Mark Week 2 Complete';completeBtn.classList.remove('done')}}
if(completeBtn){completeBtn.onclick=()=>{a=a.includes(2)?a.filter(x=>x!==2):[...a,2];localStorage.setItem(key,JSON.stringify(a));renderCompletion()};renderCompletion()}
'''
script=soup.new_tag('script')
script.string=script_text
soup.body.append(script)

for note in soup.find_all('div',class_='student-answer-note'):
    if 'reviewed in class' in note.get_text().lower() or 'does not contain' in note.get_text().lower() or 'several valid' in note.get_text().lower():
        note.string='Interactive solution available below.'

out.write_text(str(soup),encoding='utf-8')
print('Updated',out)
