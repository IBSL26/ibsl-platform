# -*- coding: utf-8 -*-
"""Unit 5 participant page: Step 2 opens with the team's two highest-risk OCEAVL dimensions (Capstone 5A). 19 Oct 2026."""
import sys
src,out=sys.argv[1:3]
s=open(src,encoding='utf-8',newline='').read(); CR='\r\n' in s; s=s.replace('\r\n','\n')
def once(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:90]); s=s.replace(a,b)
DIMS=['Openness','Conscientiousness','Extraversion','Agreeableness','Emotional Stability','Values Alignment','Learning Orientation']
once("<li><strong>Step 2 · ACE-IT.</strong> Your group reads its team OCEAVL profile. It then states",
     "<li><strong>Step 2 · ACE-IT.</strong> Your group reads its team OCEAVL profile and names the two dimensions on which the team carries the highest risk for the strategy, with the response to each. It then states")
once("<li>Read the guide in each card. It is the lesson from part 1.3.4.</li><li>For each behaviour,",
     "<li>Name the two dimensions on which your executive team carries the highest risk for the strategy, and the response your team adopts for each.</li><li>Read the guide in each card. It is the lesson from part 1.3.4.</li><li>For each behaviour,")
def sel(n):
    return ('<label class="wp-label" for="s5_risk%d">Dimension %d</label><select class="wp-ta" id="s5_risk%d" style="min-height:0;" onchange="s5In(\'risk%d\',this.value)"><option value="">&ndash; select a dimension &ndash;</option>' % (n,n,n,n)
            + ''.join('<option>%s</option>' % d for d in DIMS) + '</select>'
            '<label class="wp-label" for="s5_resp%d">Response to dimension %d</label><textarea class="wp-ta" id="s5_resp%d" placeholder="The response your team adopts for this dimension..." oninput="s5In(\'resp%d\',this.value)"></textarea>' % (n,n,n,n))
once('<div class="chg-h">The behaviours your group expects from the leadership team</div>',
     '<div class="chg-h">Your team&rsquo;s highest-risk dimensions</div>\n<div class="u5-s5"><div class="u5-s5-g"><p>From your team OCEAVL profile, name the two dimensions on which your executive team carries the highest risk for the strategy, and the response your team adopts for each. The profile above gives the risk and the response for each dimension at your team&rsquo;s level.</p></div>\n'
     + sel(1) + '\n' + sel(2) + '\n</div>\n<div class="chg-h">The behaviours your group expects from the leadership team</div>')
once('var S5=[["shift","Shift","mind"],["stake","Stake","mind"],["step","Step","mind"],',
     'var S5=[["shift","Shift","mind"],["stake","Stake","mind"],["step","Step","mind"],["risk1","Highest-risk dimension 1","profile"],["resp1","Response to dimension 1","profile"],["risk2","Highest-risk dimension 2","profile"],["resp2","Response to dimension 2","profile"],')
once('var S5_NAMES=["Alignment Plan · Mind","Alignment Plan · Habit"];','var S5_NAMES=["Alignment Plan · Team Profile","Alignment Plan · Mind","Alignment Plan · Habit"];')
once('var S5_REC={"mind":"The 3S Check · our Shift, Stake and Step",','var S5_REC={"profile":"Our team profile · the two highest-risk OCEAVL dimensions","mind":"The 3S Check · our Shift, Stake and Step",')
assert s.count("['mind','habit']")==2; s=s.replace("['mind','habit']","['mind','profile','habit']")
once("await u5save('kit_team',s5Text('mind')+'\\n\\n'+s5Text('habit'));","await u5save('kit_team',s5Text('mind')+'\\n\\n'+s5Text('profile')+'\\n\\n'+s5Text('habit'));")
once("S2RTeam.save('kit_team',s5Text('mind')+'\\n\\n'+s5Text('habit'));S2RTeam.save('kit_mind',s5Text('mind'));",
     "S2RTeam.save('kit_team',s5Text('mind')+'\\n\\n'+s5Text('profile')+'\\n\\n'+s5Text('habit'));S2RTeam.save('kit_profile',s5Text('profile'));S2RTeam.save('kit_mind',s5Text('mind'));")
once("/^(__align_work$|kit_(team|mind|habit)$)/","/^(__align_work$|kit_(team|mind|habit|profile)$)/")
open(out,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if CR else s)
print('ok')
