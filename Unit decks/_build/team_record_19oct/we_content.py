# -*- coding: utf-8 -*-
"""Unit 2 Section 4 worked example (19 October 2026).
One simulated company runs through the Strategy Architecture, the Strategy Intent Statement and
Success in Practice. Its four SiP statements lead into the SiP statement used in the Unit 3 worked
example, and from there into the Unit 4 Key Results, so one case runs from Unit 2 to Unit 4."""

COMPANY = {
    'name': 'Kestrel Point Services',
    'sector': 'Business services: facilities management and technical maintenance for corporate clients',
    'size': 'About 1,200 employees, eight regional service hubs',
    'period': '2027–2029',
    'problem': 'Kestrel Point wins clients on relationships and loses them on service. Response times vary from team to team, '
               'requests stall in handovers between functions, decisions that involve more than one function wait for escalation, '
               'and margins swing with the cost of rework.',
}

# Element name -> (four answers, what this element is saying). Order follows EL on the page.
ELEMENTS = [
    ('ITERATIVE', [
        'Clients will value speed and consistency above the lowest price.',
        'Quarterly client reviews and monthly service data test that hypothesis.',
        'Two consecutive quarters of falling retention in key accounts would trigger a review.',
        'The executive team revisits its strategic choices every quarter and in full each year.',
    ], 'The strategy rests on one hypothesis, that clients value speed and consistency above the lowest price, and the executive team tests it against service data every quarter.'),
    ('THINKING & LOGIC', [
        'Competing on price, adding new service lines and becoming the most responsive partner.',
        'Key accounts will pay for reliability, and responsiveness can be built without new headcount.',
        'Requests must move between functions without delay, and leaders must decide at the right level.',
        'Client feedback names slow response as the first reason for leaving; price comes third.',
    ], 'Price competition and new service lines were weighed and set aside. The evidence points to responsiveness, which holds only if requests and decisions move across functions without delay.'),
    ('PROCESS', [
        'The executive team, the regional hub managers and five key account clients.',
        'Client feedback, response-time data, margin per contract and the reasons clients left.',
        'Diagnose, choose, test with two hubs, then roll out to all eight.',
        'One strategy log records each decision, the evidence behind it and who agreed it.',
    ], 'The strategy is shaped with the hub managers and key clients, moves from diagnosis to a two-hub test before full roll-out, and every decision is recorded with its evidence.'),
    ('WHAT', [
        'Keeping corporate buildings and their technical systems running without disruption.',
        'Fast, consistent and effortless service that clients can rely on first.',
        'Integrated facilities and technical maintenance, with one client team for each key account.',
        'Once-off construction projects and low-value contracts that absorb leadership attention.',
    ], 'Kestrel Point is in the business of keeping client buildings running, and it chooses to win on fast, consistent and effortless service through one client team per key account.'),
    ('WHY', [
        'To let clients focus on their own business while their buildings simply work.',
        'One call reaches a team that already knows the site and resolves the request.',
        'Responsiveness is what clients reward with renewals and new sites.',
        'Being the partner clients rely on first ties every choice together.',
    ], 'Kestrel Point exists so that clients can focus on their own business, and every choice serves one rationale: to be the partner clients rely on first.'),
    ('HOW', [
        'Integrated client teams supported by one cross-functional operating rhythm.',
        'Request triage, first-contact resolution, cross-functional decision-making and account management.',
        'Weekly cross-functional execution reviews, decision rights at hub level and a single request system.',
        'Specialist subcontractors under shared service standards, and a technology partner for the request system.',
    ], 'Value is delivered through integrated client teams, decision rights at hub level and one weekly cross-functional rhythm, supported by a single request system and partners held to shared standards.'),
    ('WHEN', [
        'First responsiveness, next cross-functional decision-making, then scalable service models.',
        'Hubs move once their response times are stable; contracts that stay below margin are exited.',
        'The request system must be live before hub-level decision rights can work.',
        'That key accounts renew on service quality over the three years of the strategy.',
    ], 'Responsiveness comes first, cross-functional decision-making next and scalable service models last, with the request system in place before decision rights move to the hubs.'),
    ('CREATES VALUE', [
        'Faster resolution, fewer repeat visits and proactive maintenance that prevents breakdowns.',
        'Redesigning service routines and building a proactive engagement model with key accounts.',
        'Site knowledge held in client teams and the request system data.',
        'Clients renew, expand to new sites and refer Kestrel Point to others.',
    ], 'New value comes from faster resolution and maintenance that prevents breakdowns, built on site knowledge held in client teams.'),
    ('DELIVERS VALUE', [
        'Through the client team for the site, reachable through one number and one portal.',
        'The service desk, the client portal and the on-site team.',
        'Requests are acknowledged at once and resolved at first contact wherever possible.',
        'Slow internal handovers and decisions that wait for escalation.',
    ], 'Value reaches clients through one client team, one number and one portal, and the main threat to delivery is slow handovers between functions.'),
    ('SUSTAINS VALUE', [
        'Relationships with key accounts and a track record of consistent service.',
        'The skills of client teams, the request system and service standards.',
        'Functional silos, excessive reporting cycles and contracts that run below margin.',
        'Annual service reviews with each key account and reinvestment in scalable service models.',
    ], 'Value lasts through key account relationships and consistent service, and it is protected by removing silos, cutting reporting that delays action and exiting contracts that run below margin.'),
    ('STAKEHOLDERS', [
        'Corporate clients, employees, subcontractors, the board and the communities around client sites.',
        'Clients receive reliable buildings, employees clear ownership, subcontractors steady work, the board stable margins.',
        'Faster service can conflict with margin when it requires extra visits.',
        'Subcontractors, who carry the service standards on site without shaping them.',
    ], 'The strategy serves clients, employees, subcontractors and the board, and it must hold the tension between faster service and margin while bringing subcontractors into the service standards.'),
    ('NAVIGATING', [
        'Monthly service data per hub and quarterly client reviews.',
        'The weekly execution review turns signals into decisions with named owners.',
        'Clients moving to fewer, larger service partners favour an integrated provider.',
        'Decision rights at hub level and a quarterly review of the strategic choices.',
    ], 'Kestrel Point reads its environment through service data and client reviews, turns signals into owned decisions every week, and uses the client shift to fewer, larger partners to its advantage.'),
    ('THE FORCES', [
        'Low-price competitors and clients who bring maintenance in-house.',
        'Rising labour costs and stricter building safety regulation.',
        'Remote monitoring technology that lets competitors respond faster.',
        'Clients expect greener buildings and lower energy use.',
        'Functional silos and a habit of escalating decisions upwards.',
    ], 'Price competition, labour costs, safety regulation, remote monitoring technology and greener buildings shape the strategy, and the strongest force against it is internal: silos and the habit of escalation.'),
    ('OPERATING ENVIRONMENT', [
        'Facilities and technical services for mid-sized corporate clients in one regional market.',
        'A mature market in which clients are consolidating suppliers.',
        'Building safety regulation, remote monitoring technology and client expectations of greener buildings.',
        'If clients moved to the lowest price as their first choice, the strategy would need to change.',
    ], 'The strategy is set for a mature regional market of mid-sized corporate clients who are consolidating suppliers, and it holds as long as clients put service ahead of price.'),
]

INTENT = ('By the end of 2029, Kestrel Point will be the service partner its corporate clients rely on first, '
          'delivering fast, consistent and effortless facilities and technical service through integrated client teams '
          'and one cross-functional operating rhythm, building responsiveness first and scalable service models after.')

INTENT_HOW = [
    'WHAT gave the ambition: fast, consistent and effortless service that clients rely on first.',
    'WHY gave the reason it holds together: clients reward responsiveness with renewals and new sites.',
    'HOW gave the mechanism: integrated client teams and one cross-functional operating rhythm.',
    'WHEN gave the order: responsiveness first, scalable service models after, within 2027–2029.',
]

# Domain -> (three answers, statement)
SIP = [
    ([
        'Clients reach a team that knows their site, and requests are acknowledged at once.',
        'Most requests are resolved at first contact, and key accounts are engaged before problems surface.',
        'Response times fall and first-contact resolution rises in every hub.',
    ], 'Every client experiences fast, consistent and effortless service: requests are acknowledged at once, most are resolved at first contact, and key accounts are engaged before problems surface.'),
    ([
        'Integrated client teams and a single request system work in every hub.',
        'Decisions are taken at hub level within a day, and handovers between functions run without delay.',
        'Cross-functional decision time falls, and management reports are limited to those that drive action.',
    ], 'Kestrel Point moves quickly from insight to action across functions: decisions are taken at the right level within a day, handovers run without delay, and reporting is limited to what drives action.'),
    ([
        'Every leader can say how their work serves the promise to be the partner clients rely on first.',
        'Teams resolve issues across functions without escalation and own enterprise priorities together.',
        'Escalations fall, and cross-functional work is visible in every weekly review.',
    ], 'People hold shared ownership of enterprise priorities: teams work across functions without escalation, and every leader can name how their work serves the client promise.'),
    ([
        'Margins hold steady, and growth comes from retained and expanded key accounts.',
        'The first-choice integrated service partner for mid-sized corporate clients in the region.',
        'Key account retention, margin per contract and leadership time spent on high-value work.',
    ], 'Scalable, efficient service models strengthen enterprise performance: margins hold steady, growth comes from retained and expanded key accounts, and leadership attention goes to high-value work.'),
]

SIP_TEST = [
    ('Depth', 'Each statement names conditions a leader could observe in a hub: acknowledgement at once, decisions within a day, fewer escalations, steady margins.'),
    ('Balance', 'Customer, operational, people and enterprise success each carry their own statement, so no one perspective defines success for the whole organisation.'),
]
