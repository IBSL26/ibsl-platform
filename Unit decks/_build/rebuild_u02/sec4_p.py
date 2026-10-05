# -*- coding: utf-8 -*-
# Participant Section 4 (static part). The interactive parts are rendered by u2_tool.js into the *StageP holders.
b41 = P('This is the production section of the unit, and Step 1 is its foundation. With your group, work through the <strong>14 elements of the Strategy2Results® Strategy Definition</strong>. You establish the thinking and logic underneath your organisation\'s strategic position before you express that position concisely.',
        'The elements are interconnected: a strong answer to one element can expose a weakness or contradiction in another. The value you intend to create must be supported by your HOW. Your WHEN must reflect the capabilities you need to build. Your approach to sustaining value must respond to the forces within your operating environment.') \
    + '  <div class="hbox teal"><p><strong>How each element works.</strong> Answer the four questions with <strong>actual strategic choices</strong> and leave broad aspirations out. Select <strong>Generate what this is saying</strong>. Read the result with your group and ask: <em>"Is this what we mean?"</em> Confirm it, or refine it until it says what your group means. Surface the differences in your group before you resolve them: they expose assumptions and trade-offs.</p></div>\n' \
    + '  <div class="hbox"><p><strong>Working as a group.</strong> Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.</p></div>\n' \
    + '  <div class="u2-meta">\n' \
    + '    <div><label class="u2-inlbl" for="org_name">Organisation</label><input class="u2-in" type="text" id="org_name" placeholder="Organisation name"></div>\n' \
    + '    <div><label class="u2-inlbl" for="strategy_period">Strategy period</label><input class="u2-in" type="text" id="strategy_period" placeholder="e.g. 2027–2029"></div>\n' \
    + '  </div>\n' \
    + '  <div class="u2-progress"><div class="u2-progress-top"><span>14-element progress</span><b id="elPctP">0 of 14 confirmed</b></div><div class="u2-bar"><span id="elBarP"></span></div></div>\n' \
    + '  <div class="u2-chips" id="elNavP"></div>\n' \
    + '  <div id="elWorkP"></div>\n' \
    + '  <h4>Producing the Strategy Architecture</h4>\n' \
    + P('When all 14 elements are confirmed, step back from the individual responses and examine them as <strong>one strategic system</strong>.') \
    + '  <div class="quote"><p>"What is this architecture collectively saying about our organisation\'s strategy?"</p></div>\n' \
    + P('The page brings your 14 elements together under five headings: Strategic Position, Strategic Model, Value Architecture, Strategic Navigation and Strategy Discipline. Before you confirm the output, check:') \
    + '  <ul>\n' + ''.join('    <li>%s</li>\n' % c for c in SIX_CHECKS) + '  </ul>\n' \
    + '  <div id="archStageP"></div>\n' \
    + '  <p style="margin-top:14px;">Your confirmed Strategy Architecture is the source for Step 2.</p>\n'

b42 = P('With your Strategy Architecture established, your group now crystallises that thinking into a <strong>Strategy Intent Statement</strong>. The Architecture contains the depth. The Intent must provide the clarity.',
        'Bring forward the four dimensions already established through your architecture. Your group\'s answers appear under each one. Review the four together, deduce <strong>one crisp Strategy Intent Statement</strong> and write it in the box.') \
    + '  <div class="hbox"><p><strong>Protect the Intent from overload.</strong> You may want to carry every important point from the Architecture into the statement. The Architecture already holds that detail. The statement crystallises the ambition. A strong Intent lets a leader understand your organisation\'s strategic position without a paragraph of explanation.</p></div>\n' \
    + '  <div id="intentStageP"></div>\n' \
    + P('Read your statement against your completed Architecture and confirm:') \
    + '  <div class="quote"><p>"Does this statement faithfully express the strategic ambition contained in our Architecture?"</p></div>\n' \
    + P('Where the statement exposes a contradiction in your Architecture, resolve the underlying contradiction before you finalise the Intent. Your confirmed Strategy Intent is the source for Step 3.')

W_DEF = ['The value your organisation has chosen to create and its field of play.',
         'The rationale for those choices and why they matter.',
         'The operating model, capabilities and mechanisms through which the value will be delivered.',
         'The timing, sequencing and strategic moves through which the ambition will be pursued.']
def sip_mirrors():
    return ''.join('  <div class="u2-out"><div class="u2-out-h" style="color:%s;">D%d · %s</div>%s</div>\n'
                   % (DOM_COL[i], i + 1, DOM[i], mirror(sip_st(i + 1), 'Appears here once your group has written this statement in 4.3.')) for i in range(4))
b43 = P('Your Strategy Intent Statement establishes the ambition. Your group now defines what must be <strong>seen, experienced and executed</strong> for that ambition to become reality within the agreed time horizon.') \
    + '  <div class="u2-out"><div class="u2-out-h">Your Strategy Intent Statement</div>' + mirror('intent_statement', 'Complete your Strategy Intent Statement in 4.2.') + '</div>\n' \
    + P('Stand inside the future described by your Strategy Intent and use one central question:') \
    + '  <div class="quote"><p>"If our Strategy Intent is successful, what should we see in practice?"</p></div>\n' \
    + P('Work through the four SiP domains. In each one, answer the three questions, then derive <strong>one statement for that domain</strong> from your answers and write it in. Use the observable indicators from Section 3 to deepen the discussion where useful, and keep each statement focused on your own Strategy Intent.') \
    + '  <div class="hbox teal"><p><strong>Confirm each domain.</strong> After each statement, pause and ask: <em>"Is this what success in this domain should look like if our Strategy Intent is realised?"</em> Refine the statement until your group confirms it. Your SiP comes from your group\'s own definition of success. Generic descriptions of a successful organisation have no place in it.</p></div>\n' \
    + '  <div id="sipStageP"></div>\n' \
    + '  <h4>Test the SiP</h4>\n' \
    + P('When all four statements are confirmed, they appear together, numbered 1 to 4. Read them as <strong>one Success in Practice</strong> and test them:') \
    + '  <ul>\n    <li><strong>Depth:</strong> Is each statement specific enough that you could recognise the condition if you saw it in practice?</li>\n    <li><strong>Balance:</strong> Do the four statements collectively describe enterprise success, or has one perspective become dominant?</li>\n  </ul>\n' \
    + P('Use the <strong>SiP Flammables</strong> from 3.2 as the final balance check. The four confirmed statements together become your organisation\'s <strong>Success in Practice</strong>. Once you have confirmed it, you can print your three outputs as one report: Strategy Architecture → Strategy Intent → Success in Practice.') \
    + '  <div class="hbox"><p><strong>Into your Capstone.</strong> Your three confirmed outputs feed your team\'s Capstone Blueprint. Its Unit 2 section opens once every member of your team has completed this unit, and brings the three outputs in from your page. Your team then reads them together and confirms them.</p></div>\n'
