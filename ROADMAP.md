# ROADMAP.md — topic backlog & status

The research program: ~166 topics across 9 tiers, executed in tier order, one topic at a time, per `METHODOLOGY.md`. This file is the **single resume point**: any session picks the next unchecked box. Checked = file exists with `status: complete`.

- Backlog ids are valid edge/wikilink targets before their files exist (`kb.py validate` treats them as *pending*).
- Research surfaces new topics → append them to the right tier with a `(discovered: <source-topic>)` note.
- Live numbers: `python3 tools/kb.py stats`.

**Status:** ✅ Tiers 0–8 complete — 151/151 · 🚧 **Tier 9 (Cognitive Bias Codex) in progress — 8/15** (7 mechanism clusters + index scaffold; framing-anchoring extended). Checkpoint 1 passed 2026-08-17: graph clean, no orphans, retrieval spot-tests green. Tiers 0–7 done: 3 foundations · 23 mechanisms · 68 tactics · 10 dynamics · 12 contexts · 6 profiles · 9 vulnerabilities · 15 defenses · 8 meta/synthesis. Validates with 0 errors; graph + both matrices regenerate clean; 53 safety-flagged files; 79 false-positive contrast concepts. The synthesis finale ([[felt-sense-index]], [[playbooks-compendium]], [[defense-agent-spec]], [[coverage-audit]]) is in, plus a 2026-07-01 QA/maintenance pass (Tier 8). Remaining work: Tier 9 codex integration (below), then maintenance: localize resources beyond US/UK, refresh fast-moving files, thicken causal edges (see [[coverage-audit]]). · last updated 2026-08-04

## Tier 0 — Foundations (meta/, taxonomy/)

- [x] `manipulation-vs-influence` (meta) — the boundary problem: persuasion/influence/manipulation/coercion/deception; covertness, vulnerability-exploitation, asymmetry criteria; legal lines; grey zones
- [x] `epistemic-guardrails` (meta) — concept creep, term inflation, weak constructs registry, base rates, alternative explanations, calibration protocol for the defense agent
- [x] `master-taxonomy` (taxonomy) — the map: entity types, edge semantics, how prior published taxonomies fold in, navigation entry points

## Tier 1 — Mechanisms (mechanisms/) — why it works

- [x] `reciprocity` — obligation engineering: unsolicited gifts/favors/concessions creating debt
- [x] `commitment-consistency` — small yeses to big traps; sunk cost; public commitment lock-in
- [x] `social-proof` — manufactured consensus, "everyone's doing it", testimonials
- [x] `authority` — symbols, titles, uniforms, borrowed credibility, expert posturing
- [x] `liking-similarity` — rapport, mirroring, compliments, "we're alike" as compliance levers
- [x] `scarcity-urgency` — limited time/quantity, exploding offers, FOMO mechanics
- [x] `unity-ingroup` — shared identity ("we"), family/tribe framing, us-vs-them
- [x] `fear-exploitation` — threat inflation, protection rackets, fear-then-relief
- [x] `guilt-leverage` — indebtedness scripts, obligation manufacturing, guilt as compliance fuel
- [x] `shame-leverage` — humiliation, exposure threats, worthiness attacks
- [x] `hope-greed` — jackpot dreams, "opportunity" framing, get-rich/get-loved promises
- [x] `flattery-ego` — strategic praise, status-stroking, "you're special" hooks
- [x] `attachment-needs` — belonging/love/validation hunger as attack surface
- [x] `certainty-needs` — need for closure/answers exploited by confident liars and gurus
- [x] `trust-mechanics` — how trust forms (warmth/competence/integrity cues) and how each cue is faked
- [x] `intermittent-reinforcement` — variable rewards: the strongest behavioral glue (slots, hot-cold partners)
- [x] `emotional-flooding` — overwhelm states (rage, panic, infatuation) that suspend deliberation
- [x] `cognitive-overload-confusion` — complexity, speed, jargon, contradiction as defenses-suppressors
- [x] `information-asymmetry` — gatekeeping, selective disclosure, epistemic dependence
- [x] `framing-anchoring` — reference-point control: first numbers, comparison sets, decoys
- [x] `loss-aversion-endowment` — losses loom larger; trials/possession effects; "don't lose what you have"
- [x] `dissonance-exploitation` — forcing self-justification spirals after small compromises
- [x] `memory-fallibility` — misinformation effect, confident confabulation, history editing substrate

## Tier 2 — Core cross-domain tactics (tactics/) + keystone defenses (defenses/)

- [x] `gaslighting` — systematic reality-denial to destabilize a target's trust in their own perception
- [x] `darvo` — Deny, Attack, Reverse Victim and Offender (Freyd)
- [x] `love-bombing` — overwhelming early affection/attention as accelerant and leverage
- [x] `guilt-tripping` — inducing guilt to control ("after all I've done…")
- [x] `silent-treatment` — punitive withdrawal of contact/affection as control
- [x] `triangulation` — third parties imported as weapons: comparisons, rivals, messengers
- [x] `isolation-tactics` — severing friends/family/finances/information channels
- [x] `projection-blame-shifting` — accusing the target of the manipulator's own behavior; fault relocation
- [x] `victim-posturing` — strategic self-pity to deflect accountability and recruit allies
- [x] `moving-goalposts` — success criteria that shift whenever met
- [x] `circular-conversation` — word salad, topic rotation, exhaustion arguments that never resolve
- [x] `thought-terminating-cliches` — stock phrases that kill examination ("it is what it is", "doubt your doubts")
- [x] `hoovering` — re-contact campaigns to suck a target back after escape
- [x] `smear-campaigns` — preemptive/retaliatory reputation destruction
- [x] `proxy-recruitment` — flying monkeys: third parties deployed to pressure the target
- [x] `negging` — calculated put-downs to lower status and fish for validation
- [x] `future-faking` — vivid promised futures as payment-now leverage
- [x] `breadcrumbing` — minimal intermittent attention to keep a target on the hook
- [x] `double-binds` — engineered no-win choices ("damned either way")
- [x] `history-rewriting` — retroactive narrative editing of events, promises, agreements
- [x] `weaponized-incompetence` — strategic helplessness to offload labor and lower expectations
- [x] `emotional-blackmail` — FOG: fear, obligation, guilt (Forward); if-you-loved-me leverage
- [x] `veiled-threats` — deniable intimidation: hints, jokes, "I'd hate for X to happen"
- [x] `self-harm-threats` — "I'll hurt myself if you leave" as a control mechanism (safety-critical)
- [x] `lying-typologies` — commission, omission, paltering, equivocation, bluffing, BS (Frankfurt)
- [x] `boundary-testing` — probing small violations to map compliance before bigger ones
- [x] `mirroring-false-identity` — manufactured soulmate/ideal-candidate personas
- [x] `pity-plays` — sympathy as the con's strongest card (Stout's "pity play")
- [x] `charm-offensive` — weaponized charisma and impression management
- [x] `manufactured-urgency` — deadline pressure engineered to prevent deliberation (act-now closes)
- [x] `therapy-speak-weaponization` — "boundaries"/"toxic"/"gaslighting" vocabulary misused as control
- [x] `non-apology-patterns` — fauxpologies: "sorry you feel that way", conditional and blame-shifting apologies
- [x] `bad-faith-argumentation` — sealioning, gish gallop, motte-and-bailey, strawman cycles
- [x] `detection-heuristics` (defenses) — the universal screen: pressure+urgency+emotion+isolation+secrecy → audit
- [x] `boundary-scripts` (defenses) — concrete language for setting/holding limits under pressure
- [x] `verification-rituals` (defenses) — callbacks, second opinions, cooling-off periods, independent channels

## Tier 3 — Dynamics (dynamics/) — how it unfolds over time

- [x] `abuse-cycle` — tension → incident → reconciliation → calm (Walker) + critiques of cycle universality
- [x] `trauma-bonding` — attachment to an abuser via intermittent reinforcement + power asymmetry (Dutton & Painter)
- [x] `coercive-control` — the architecture of domination: micro-regulation, surveillance, credible threat (Stark)
- [x] `grooming-sequence` — staged trust-building toward exploitation: selection, access, trust, desensitization, maintenance
- [x] `con-anatomy` — the classic stages: put-up, play, rope, tale, convincer, breakdown, send, touch, blow-off
- [x] `cult-conversion-funnel` — recruitment → love-bomb → escalating commitment → identity replacement (Lifton, Hassan, Singer)
- [x] `radicalization-pipeline` — grievance → ideology → echo chamber → action funnel
- [x] `romance-scam-arc` — profile → grooming → crisis/investment ask → escalation → pig butchering
- [x] `mlm-lifecycle` — recruitment dream → sunk-cost deepening → inventory loading → exit shaming
- [x] `escalation-entrapment` — how exit costs are engineered upward over time (commitments, secrets, dependents, debts)

## Tier 4a — Context dossiers (contexts/)

- [x] `intimate-relationships` — dating → partnership: prevalence, top tactics, escalation map, legal protections, exit resources
- [x] `family-parents` — abusive/controlling parents and relatives; adult-child dynamics; estrangement decisions
- [x] `workplace-bosses` — abusive supervision, org cover dynamics, HR realities, documentation & exit
- [x] `competitors-business` — FUD, astroturfing, poaching, bad-faith partnerships, espionage-adjacent social engineering
- [x] `sales` — pressure systems by industry; where persuasion ends and deception begins; consumer rights
- [x] `advertising-marketing` — emotional conditioning, targeting, pricing psychology; regulation and self-defense
- [x] `digital-platforms` — attention engineering, dark patterns, algorithmic amplification, parasocial economies
- [x] `scams-fraud` — the fraud landscape: typologies, current trends, reporting channels, recovery scams
- [x] `cults-high-control` — groups: religious, political, commercial (LGATs), wellness; assessment checklists
- [x] `propaganda-politics` — state/movement persuasion machinery; disinformation ecosystems; voter-facing defenses
- [x] `institutions` — gatekeeping abuse: medical dismissal, legal process abuse, financial steering, school/HR betrayal
- [x] `negotiation` — hardball vs manipulation: recognized dirty tricks and counters at the table

## Tier 4b — Domain-specific tactics (tactics/)

- [x] `financial-abuse` — allowances, sabotaged employment, debt-loading, account control in relationships
- [x] `sexual-coercion` — pressure, guilt, obligation framing short of force; consent erosion
- [x] `reactive-abuse-provocation` — baiting a target into reactions used as evidence against them
- [x] `stalkerware-monitoring` — phone checking, location tracking, spyware, account takeover as control
- [x] `parentification` — children conscripted into adult emotional/practical roles
- [x] `golden-child-scapegoat` — engineered sibling role assignment and comparison control
- [x] `conditional-love` — approval rationing contingent on compliance
- [x] `elder-targeting` — isolation, dependency engineering, inheritance/caregiver leverage
- [x] `credit-theft-visibility` — idea appropriation, contribution erasure, visibility starvation at work
- [x] `pip-weaponization` — performance processes as pretext: paper trails, impossible metrics, managed exits
- [x] `we-are-family-rhetoric` — loyalty framing to extract unpaid labor and suppress complaints
- [x] `mobbing` — coordinated workplace ostracism and reputation destruction
- [x] `foot-in-the-door` — small ask → large ask compliance laddering
- [x] `door-in-the-face` — outrageous ask → "concession" to the real ask
- [x] `lowballing` — commitment first, true cost revealed after
- [x] `thats-not-all-decoys` — sweeteners, bundle fog, decoy options steering choice
- [x] `four-square-payment-packing` — car-dealership worksheet games and finance-office add-on stuffing
- [x] `timeshare-playbook` — captive presentations: gift hooks, 90-minute grinds, today-only pricing
- [x] `mlm-recruitment-scripts` — income puffery, lifestyle theater, "be your own boss", warm-market mining
- [x] `dark-patterns-obstruction` — roach motel, forced continuity, cancellation mazes, sneak-into-basket
- [x] `dark-patterns-social-urgency` — fake counters, fake low-stock, confirmshaming, fabricated activity feeds
- [x] `fake-reviews-astroturfing` — manufactured social proof: review farms, sockpuppets, front groups
- [x] `parasocial-influencer-tactics` — manufactured intimacy monetized: hauls, "link in bio", guru funnels
- [x] `phishing-pretexting` — social engineering attacks: urgency+authority impersonation across channels
- [x] `ai-enabled-manipulation` — voice cloning, deepfakes, chatbot romance/investment scams, synthetic personas
- [x] `cold-reading` — Barnum statements, shotgunning, sleight of tongue (psychics, "intuitives", interviewers)
- [x] `affinity-fraud` — exploiting shared faith/ethnicity/community trust networks
- [x] `ponzi-psychology` — why returns-too-good survive scrutiny: exclusivity, redemption theater, social proof
- [x] `fud-competitor-tactics` — fear-uncertainty-doubt against rivals; switching-cost terror; vaporware promises
- [x] `bad-faith-negotiation` — good cop/bad cop, higher authority, nibbling, brinkmanship, false deadlines
- [x] `propaganda-devices` — the classic device set (IPA seven + modern descendants)
- [x] `disinformation-playbooks` — firehose of falsehood, flooding, manufactured consensus, source laundering

## Tier 5 — Profiles (profiles/) & Vulnerabilities (vulnerabilities/)

- [x] `narcissistic-patterns` — NPD-informed manipulation signatures (carefully: traits ≠ diagnosis)
- [x] `psychopathic-patterns` — callous-instrumental signatures (Hare); glibness, parasitism, dual masks
- [x] `machiavellianism` — strategic long-game manipulation as trait; workplace expression
- [x] `dark-triad-overview` — measurement, overlap, critiques of pop usage
- [x] `con-artist-typologies` — professional fraud operator patterns and role specialization
- [x] `everyday-manipulators` — situational, non-pathological manipulation: the most common case
- [x] `why-smart-people-fall` — intelligence ≠ immunity; expertise overconfidence; the fraud-victim profile myth
- [x] `crisis-windows` — bereavement, divorce, illness, relocation, job loss as targeting windows
- [x] `loneliness-isolation` — social hunger as attack surface
- [x] `trauma-history-revictimization` — normalized red flags and re-selection dynamics
- [x] `people-pleasing-fawn` — conflict-avoidant compliance and exploitability
- [x] `cognitive-decline-age` — aging, decision fatigue, and financial-exploitation susceptibility
- [x] `optimism-overconfidence` — "it can't happen to me"; bias blind spot
- [x] `scarcity-stress` — financial desperation narrowing judgment (tunneling)
- [x] `betrayal-blindness` — motivated unawareness when dependence is high (Freyd)

## Tier 6 — Defenses & recovery (defenses/)

- [x] `universal-red-flags` — the master cross-context warning list, ranked by diagnosticity
- [x] `manipulation-audit` — structured self-check protocol when something feels off (the agent's core procedure)
- [x] `gray-rock` — low-information unresponsiveness: how, when, risks (can escalate some abusers)
- [x] `jade-avoidance` — don't Justify, Argue, Defend, Explain; resisting engagement hooks
- [x] `documentation-practices` — contemporaneous records, message preservation, witnesses, legality of recording
- [x] `no-contact-exit-planning` — graded disengagement: limited contact → no contact; relationships/family/jobs/groups
- [x] `dv-safety-planning` — leaving safely is the highest-risk window; professional protocols, hotlines (safety-critical)
- [x] `cult-exit-support` — exit counseling vs deprogramming; identity reconstruction; family do's/don'ts
- [x] `recovery-rebuilding` — self-trust repair, therapy modalities with evidence notes, post-exploitation finances
- [x] `helping-others` — intervening without pushing them deeper (motivational-interviewing stance, ultimatum risks)
- [x] `inoculation-prebunking` — attitudinal vaccines: weakened-dose exposure to tactics (van der Linden, McGuire)
- [x] `organizational-defenses` — procurement gates, hiring screens, anti-fraud controls, speak-up cultures

## Tier 7 — Synthesis (taxonomy/, meta/)

- [x] `playbooks-compendium` (taxonomy) — named multi-tactic sequences cataloged across domains
- [x] `felt-sense-index` (taxonomy) — reverse index: what the target feels → candidate tactics ("confused after every talk" → …)
- [x] `defense-agent-spec` (meta) — system prompt, retrieval strategy, confidence calibration, safety escalation rules
- [x] `coverage-audit` (taxonomy) — final gap analysis: orphan nodes, missing edges, untested scenarios

## Tier 8 — Post-audit maintenance additions (2026-07-01)

Added during a QA/audit pass that also fixed inventory drift, hardened `kb.py` (safety-flag symmetry + phantom-link warnings), resolved 236 Obsidian phantom-links, added ~18 missing graph edges, and backfilled 42 per-topic bibliographies (see [[coverage-audit]]).

- [x] `emergent-insights` (taxonomy/meta) — graph-analysis companion to [[coverage-audit]]: degree distribution, evidence×connectivity cross-tab, the escalation-layer convergence on [[coercive-control]] (discovered: coverage-audit)
- [x] `tone-policing` (tactic) — dismissing a message for its emotional tone instead of its content; the derailing/silencing move (discovered: audit gap-scan)
- [x] `spiritual-abuse` (tactic) — coercive control exerted through religion, scripture, and "God's will" in mainstream families and congregations, short of a full cult (discovered: audit gap-scan)
- [x] `overton-window-shifting` (tactic) — normalizing a once-fringe position by repetition and extreme anchoring so the perceived center drifts (discovered: audit gap-scan)

## Tier 9 — Cognitive Bias Codex integration (mechanisms/, taxonomy/) (started 2026-08-04)

Owner-requested expansion: integrate all **188 unique entries** of the Cognitive Bias Codex (Benson/Manoogian 2016; pinned to Benson's `cognitive-bias-cheat-sheet.json` — the only dual-listed entry is Negativity bias) as clustered mechanism files plus an index. Every codex bias gets a bolded subsection + registered alias on exactly one home file; ~49 entries resolve to existing files (extensions/pointer alias-adds, tracked in [[bias-codex-index]], not as separate roadmap ids). Evidence graded honestly per `METHODOLOGY.md`; known-contested entries flagged inline (backfire effect, hot-hand, Dunning-Kruger mechanism, Google effect, IAT validity).

- [ ] `bias-codex-index` (taxonomy/meta) — pinned 188-entry enumeration; entry → KB-home map with evidence + exploitation-relevance columns; the completeness gate
- [x] `confirmation-bias` — confirmation & expectancy family: selective perception, congruence bias, observer-expectancy, subjective validation, continued influence, Semmelweis reflex, backfire effect (contested), conservatism, belief bias, placebo
- [x] `availability-salience` — availability heuristic, attentional bias, frequency illusion (Baader-Meinhof), negativity bias, Von Restorff/bizarreness/humor/picture-superiority/self-relevance
- [x] `pattern-illusions` — clustering illusion, illusory correlation, gambler's fallacy, hot-hand (contested), pareidolia, anthropomorphism, recency illusion, anecdotal fallacy, illusion of validity, masked-man fallacy
- [x] `probability-blindspots` — representativeness, base-rate fallacy, sample-size insensitivity, conjunction fallacy, subadditivity, survivorship bias, mental accounting, money illusion, denomination effect, zero-sum bias, appeal to probability, identifiable victim effect
- [x] `attribution-errors` — fundamental attribution error, actor-observer, self-serving, defensive/trait/group/ultimate attribution, just-world hypothesis, moral luck, system justification, reactive devaluation
- [x] `stereotyping-essentialism` — stereotyping, implicit associations (IAT validity flagged), prejudice, essentialism, out-group homogeneity, cross-race effect
- [x] `mind-reading-illusions` — illusions of transparency/asymmetric insight/external agency, spotlight effect, curse of knowledge, naïve realism, naïve cynicism, false consensus, extrinsic incentive error
- [x] `self-evaluation-illusions` — Dunning-Kruger (mechanism contested), illusory superiority, hard-easy effect, egocentric bias, illusion of control, restraint bias, moral licensing, social desirability, social comparison bias
- [x] `memory-self-editing` — hindsight bias, outcome bias, rosy retrospection, telescoping, fading affect, positivity effect, peak-end rule, duration neglect, self-consistency bias, misattribution/source confusion, cryptomnesia, leveling & sharpening
- [x] `memory-retrieval-quirks` — serial-position family, spacing/testing/levels-of-processing effects, tip-of-the-tongue, absent-mindedness, Google effect (contested); mostly observer-side lab effects, said plainly
- [ ] `time-distortions` — hyperbolic discounting (present bias), planning fallacy, impact/projection/pessimism bias, declinism, appeal to novelty, pro-innovation bias, time-saving bias, well-traveled-road effect
- [x] `risk-misperception` — normalcy bias, ostrich effect, zero-risk bias, pseudocertainty, omission bias, risk compensation (Peltzman), ambiguity aversion
- [x] `fluency-familiarity` — mere exposure, illusory truth, processing fluency, rhyme-as-reason, processing-difficulty (disfluency), generation effect, IKEA effect, not-invented-here
- [ ] `choice-simplification` — less-is-better, information bias, unit bias, functional fixedness, bike-shedding (Law of Triviality), Delmore effect (folk), Occam's-razor boundary note
