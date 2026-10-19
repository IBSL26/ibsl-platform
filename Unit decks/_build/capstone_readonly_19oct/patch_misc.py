import sys
d,bc,dout,bcout=sys.argv[1:5]
s=open(d,encoding='utf-8',newline='').read(); CR='\r\n' in s; s=s.replace('\r\n','\n')
def once(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80]); s=s.replace(a,b)
once("      mbt_value: 'Step 4 · Establish the Value Proposition — confirmed',\n","      mbt_value: 'Step 4 · Establish the Value Proposition — confirmed',\n      mbt_verify: '5.3 · Verification ownership — confirmed',\n      mbt_blind: '5.3 · Executive blind spot — confirmed',\n")
once("      kit_mind: 'Leading with Clarity · the 3S Check (Shift, Stake, Step) — confirmed',\n","      kit_profile: 'Leading with Clarity · the two highest-risk OCEAVL dimensions — confirmed',\n      kit_mind: 'Leading with Clarity · the 3S Check (Shift, Stake, Step) — confirmed',\n")
open(dout,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if CR else s)
s=open(bc,encoding='utf-8',newline='').read()
a="mbt_(record|arena|bound|comp|value)$"; assert s.count(a)==1; s=s.replace(a,"mbt_(record|arena|bound|comp|value|verify|blind)$")
a="kit_(team|mind|heart|hands|habit)$"; assert s.count(a)==1; s=s.replace(a,"kit_(team|mind|heart|hands|habit|profile)$")
open(bcout,'w',encoding='utf-8',newline='').write(s)
print('ok')
