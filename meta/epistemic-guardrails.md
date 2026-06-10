---
id: epistemic-guardrails
type: meta
name: Epistemic Guardrails Against Over-Detection
aliases: [false positives, concept creep guardrails, over-detection, calibration]
evidence: established
safety: crisis-escalation
status: complete
last-updated: 2026-06-10
---

# Epistemic Guardrails Against Over-Detection

> This knowledge base must make its user *accurate*, not *alarmed*. A detector tuned only for sensitivity ruins relationships, feeds paranoia, and hands real manipulators a vocabulary to weaponize. These guardrails bind every other file — and the future defense agent — to calibrated conclusions.

## The two failure modes

| | Under-detection | Over-detection |
|---|---|---|
| What happens | Abuse normalized, frog-boiled escalation, exploitation continues | Innocent people accused; ordinary conflict pathologized; relationships destroyed by labels |
| Why it happens | [[betrayal-blindness]], dependence, normalcy bias, gradual [[boundary-testing]] | Concept creep, vivid-case priming, hostile attribution, confirmation bias |
| Who benefits | The manipulator | Also, sometimes, a manipulator ([[therapy-speak-weaponization]], [[victim-posturing]]) |
| Corrective | Recognition content of this KB | **This file** |

Both errors are real and costly. The KB's stance: **maximize discrimination, not detection** — the goal is telling manipulation apart from its innocent look-alikes, not finding as much of it as possible.

## Concept creep: why the vocabulary keeps expanding

Haslam documented that psychology's harm-related concepts — abuse, bullying, trauma, mental disorder, addiction, prejudice — have systematically expanded: **vertically** (admitting ever-milder instances) and **horizontally** (annexing new phenomena). "Concepts that refer to the negative aspects of human experience and behavior have expanded their meanings so that they now encompass a much broader range of phenomena than before" [1]. He warns the trend "runs the risk of pathologizing everyday experience and encouraging a sense of virtuous but impotent victimhood" [1]. Follow-up work ("harm inflation") notes the flip side: some expansion reflects genuine moral progress — recognizing coercive control *was* progress [2]. The guardrail is not "never expand concepts"; it is **know which definition you're using and apply it consistently**.

Related and newer: the **prevalence inflation hypothesis** — awareness campaigns may lead people to interpret normal distress as disorder, with self-labeling becoming self-fulfilling [12]. The manipulation-awareness ecosystem (NarcTok, r/raisedbynarcissists, pop-psych YouTube) plausibly does the same for abuse concepts: roughly half of top TikTok ADHD content is misleading [13], and "narcissist" content economies reward maximal labeling (journalistic accounts) [16].

## Term-inflation case studies

- **Gaslighting.** Merriam-Webster's 2022 Word of the Year (lookups +1740%), defined there loosely as "grossly misleading someone … for one's own advantage" [3]. The scholarly construct is far narrower: Sweet's sociological analysis defines it as psychological abuse "aimed at making victims seem or feel 'crazy,' creating a 'surreal' interpersonal environment," and argues it is "rooted in social inequalities, including gender, and executed in power-laden intimate relationships" [4]. **Disagreement + sincere divergent memory ≠ gaslighting** — the [[gaslighting]] construct requires sustained reality-denial within a power relation. Memory science shows two honest people *will* remember the same event differently: the misinformation effect distorts recall in ordinary minds, no malice required [9] ([[memory-divergence]], [[memory-fallibility]]).
- **Narcissist.** Community prevalence of NPD spans roughly **0–6.2%** across studies; a median estimate is ~**1.6%**, with several studies near 0.5–1% (the 6.2% figure is the NESARC lifetime upper end) [8]. The base rate of *diagnosable* NPD is low; the base rate of *occasional self-centered behavior* is ~100%. Casual diagnosis from listicles inverts that arithmetic ([[narcissistic-patterns]] handles the real construct; see also the Goldwater-rule norm against diagnosing people you haven't examined).
- **Trauma / toxic / abuse.** Same creep dynamics [1][16]: when everything is trauma, the word stops discriminating — and people facing *intimate terrorism* get lumped with people facing ordinary friction (next section).

## The weak-construct registry

Constructs this KB grades `contested` or `folk` no matter how often they appear in pop content:

| Construct | Status | What the evidence says | What survives |
|---|---|---|---|
| **Stockholm syndrome** | `contested` | Systematic review found ~12 qualifying papers, mostly case reports; "no validated diagnostic criteria have been described"; absent from diagnostic classifications; likely a media-driven construct shaped by reporting bias [5] | Bonding to captors/abusers under threat *does occur* — modeled better as [[trauma-bonding]] (graded on its own evidence) |
| **Parental alienation *syndrome*** | `contested` | Rejected as a diagnosis (not in DSM-5); the American Psychological Association found "no evidence … of a diagnosable parental alienation syndrome" [10] | Alienating *behaviors* in custody conflict are real and studied [10]; behavior ≠ syndrome |
| **Micro-expression lie detection** | `contested` | Human deception detection averages **54%** against a 50% coin-flip across 206 studies and 24k+ judges [6]; trained-tool claims have not replicated robustly under independent test | Attend to *content inconsistencies and verifiable facts*, not faces |
| **The 7%-38%-55% "rule"** | `folk` (misapplied) | Mehrabian's 1967 studies measured single-word feeling messages with inconsistent cues; his own disclaimer: "Unless a communicator is talking about their feelings or attitudes, these equations are not applicable" [7] | Nonverbal channels matter for *emotional* signals; they are not 93% of meaning |
| **NLP persuasion techniques** | `contested` | Systematic review of the NLP Research Data Base: of 33 ISI-journal studies, 54.5% non-supportive, 18.2% supportive, 27.3% uncertain — with the non-supportive studies methodologically stronger [14] | Rapport and pacing exist as ordinary social skills; the proprietary system is decoration |
| **Body-language decoding ("crossed arms = lying")** | `folk` | Folk cues (gaze aversion, fidgeting) do not validly indicate deception [6] | Baseline *changes* under specific questions are weak leads at best |

Rule for the defense agent: when a user's question is phrased in a weak construct's vocabulary, answer in it (it's what they know) while explicitly mapping it onto the evidence-based construct underneath — and say plainly which parts are unvalidated.

## Base rates: the math of over-detection

Suppose a behavior pattern is shown by 80% of actual manipulators but also by 30% of ordinary stressed/awkward people, and true manipulators are ~5% of the relevant population. Then a person showing the pattern is manipulating with probability:

```
P = (0.80 × 0.05) / (0.80 × 0.05 + 0.30 × 0.95) ≈ 12%
```

A "strong sign" still leaves an ~88% chance of innocence — because the innocent pool is 19× larger. This is base-rate neglect, the classic Kahneman–Tversky result: people predict from resemblance and ignore priors [11]; Meehl & Rosen formalized why low-prevalence conditions + imperfect signs ⇒ mostly false positives [11]. Consequences:

- **Single cues are nearly worthless.** Diagnosticity lives in *conjunctions* (multiple independent signs), *patterns over time*, and *costly signals* (behavior expensive to fake, like how someone acts when you have nothing left to offer).
- **Sampling distorts intuition.** Johnson's IPV typology: general community samples are dominated by **situational couple violence** (mutual conflict escalation without a control structure), while shelter/agency samples are dominated by **intimate terrorism** (violence embedded in coercive control) [15]. Survey data on current relationships contain almost no intimate terrorism at all [15]. Forum-trained intuitions (r/raisedbynarcissists et al.) are *agency-sample* intuitions: vivid, real, and unrepresentative of the general population. Use them for recognition vocabulary, never for prevalence.
- **Severity tiers are not interchangeable.** Most interpersonal friction is not abuse; most difficult people are not dark-triad; most pushy salespeople are not con artists. Each KB file's Caveats section carries its own base-rate note for this reason.

## The perceiver is part of the system

Detection errors aren't only about the other person:

- **Hostile attribution bias** — the robust tendency (meta-analytically linked to aggression) to read ambiguous behavior as intentionally hostile [17]. If you're primed, tired, or hurt, ambiguous behavior *will* look strategic.
- **Exposure priming** — a self-exemplifying entry: the folk "psych-student syndrome" largely fails its own test (controlled studies found students' anxiety about their *own* mental health **decreased** with study, while worry about family members rose; later work found little overall support) [18]. What does survive: misleading awareness content measurably distorts how people label *others* [13], and prevalence-inflation theory predicts exposure shifts interpretation [12]. Treat "a week of NarcTok" as a plausible — not proven — prime: notice recent exposure, then run the differential anyway.
- **Confirmation loops** — once a label is adopted ("my boss is a narcissist"), all subsequent behavior gets coded as evidence; disconfirming behavior becomes "the mask" or "hoovering". A theory that no observation can disconfirm is operating as faith, not inference. Build in disconfirmable predictions ("if I set this boundary and they respect it durably, I update down").
- **Motivated labeling** — labels can serve the labeler: explaining a failed relationship, winning a custody narrative, avoiding one's own contribution. The KB's symmetry rule: run the [[manipulation-audit]] on your own behavior in the same conflict.

## The differential: innocent explanations to rule out first

Before concluding "tactic", check the alternatives (each is a registered contrast concept in `taxonomy/glossary.md`):

1. **Stress, overload, depression** — withdrawal, irritability, and forgetfulness without a control pattern ([[self-protective-distance]] vs [[silent-treatment]]).
2. **Incompetence and disorganization** — harm without design ([[incompetence-not-malice]]; Hanlon's razor, bounded by: pattern + concentrated benefit + concealment defeats the razor).
3. **Honest memory divergence** — the misinformation effect and ordinary forgetting [9] ([[memory-divergence]] vs [[gaslighting]] / [[history-rewriting]]).
4. **Neurodivergent communication** — ADHD forgetting promises ≠ [[future-faking]]; autistic directness ≠ [[negging]]; flat affect ≠ coldness ([[neurodivergent-communication]]). Caveat in both directions: neurodivergence explains *styles*, not *exploitation patterns*; diagnosis is not a license.
5. **Cultural difference** — haggling norms, gift obligations, directness gradients, high-context implication ([[cultural-difference]]).
6. **Legitimate disagreement and advocacy** — someone arguing strongly for their interests, transparently, is negotiating, not manipulating ([[honest-disagreement]], [[hard-bargaining]], [[assertiveness]]).
7. **Your own state** — sleep, conflict history, priming, hostile attribution [17][18].

## Discriminators that actually work

What separates tactics from look-alikes, in rough order of evidential value:

1. **Response to "no"** — persuaders accept or re-argue; manipulators punish, escalate, or re-disguise ([[manipulation-vs-influence]]).
2. **Response to being caught** — repair attempts and changed behavior vs [[darvo]], [[non-apology-patterns]], counter-accusation.
3. **Pattern × time × targets** — one incident with one person is noise; the same move across incidents (and especially across *victims*) is signal.
4. **Benefit asymmetry over time** — track the cumulative flow of money, labor, control, risk, and apologies.
5. **Cross-audience consistency** — masks are audience-specific; compare behavior when witnesses are present vs absent, and toward people with vs without power over them.
6. **Costly-signal behavior** — kindness that persists when you can offer nothing; respect for boundaries that costs them something.
7. **Disconfirmable prediction** — state (privately) what you'd expect to see next under "innocent" vs "tactic"; score it.

## Calibration protocol (binding on the defense agent)

1. **Confidence ladder.** Express conclusions at one of four rungs, never higher than evidence supports: *observation* ("this happened") → *hypothesis* ("this is consistent with X, and with [innocent Y]") → *pattern* ("X has recurred under these conditions; innocent explanations are weakening because…") → *conclusion* ("the pattern, benefit flow, and response-to-no jointly support X").
2. **Always present the strongest innocent explanation** alongside the tactic hypothesis at rungs 1–2 — and what evidence would separate them.
3. **Label behaviors, not people**, until rung 4: "that was a guilt-tripping move", not "they are a manipulator"; trait/disorder language only with its base rates attached [8].
4. **Single incident ⇒ rung 1–2 max.** No identity labels, no relationship verdicts from one data point.
5. **Recommend evidence-gathering before confrontation** at rungs 1–3: [[documentation-practices]], an outside calibrator (friend/therapist with both-sides exposure), and the behavioral tests above.
6. **Severity override (fail-unsafe).** Where the *cost of under-detection is catastrophic* — physical danger signs, [[self-harm-threats]], strangulation, escalating [[coercive-control]], child or elder risk — calibration shifts: act on protective protocols ([[dv-safety-planning]]) without waiting for rung-4 certainty. Over-detection costs reputations; under-detection there costs lives.
7. **Decline armchair diagnosis.** The agent never asserts that a real person *has* NPD/ASPD; it can describe behavior patterns and their typical handling ([[narcissistic-patterns]] caveats govern).

## Caveats — yes, this file has caveats

- **Guardrails can be weaponized too.** "You're overreacting", "you read too much into things", "stop pathologizing me" are standard suppression moves ([[gaslighting]], [[darvo]]). These guardrails are for the *evaluator's internal process*; they are not ammunition the evaluated party gets to cite. If someone systematically uses your epistemic humility against you — punishing every hypothesis you raise while demanding rung-4 proof — **that response pattern is itself data** (see Discriminators 1–2).
- **Don't let the differential become denial.** The innocent-explanation checklist is run *once per hypothesis, honestly* — not repeatedly until the discomfort goes away. [[betrayal-blindness]] (motivated unawareness when dependence is high) is the equal-and-opposite failure, and it is well documented.
- **Forum wisdom is real phenomenology.** Survivor communities supply the best recognition language in existence ("word salad," "flying monkeys") and validated thousands of people the establishment failed. Grading them `folk`/anecdotal is a statement about *evidence type*, not about the people.
- **Haslam's framework is itself debated** (target-article-with-commentaries format; creep as moral progress) [2], and Johnson's typology has empirical critics [15]. The guardrails rest on the *convergence* of these literatures, not any single paper.
- **The IPV gender debate is real and unsettled.** Community surveys find near-symmetric perpetration of situational couple violence (meta-analytically: Archer 2000 [19]), while coercive control / intimate terrorism is heavily asymmetric in agency samples [15]; the Duluth model's gendered framing has documented critics (Dutton & Corvo 2007 — see [[master-taxonomy]] sources). KB files describe tactics gender-neutrally and surface this debate wherever prevalence claims appear.

## Safety notes

The severity override (calibration protocol §6) is the operative rule: when physical danger, strangulation, [[self-harm-threats]], stalking, or escalating [[coercive-control]] enter the picture, stop calibrating and act on protective protocols. Immediate resources — **US:** 911 · National Domestic Violence Hotline 1-800-799-7233 / thehotline.org · 988 Suicide & Crisis Lifeline. **UK:** 999 · National Domestic Abuse Helpline 0808 2000 247 · Samaritans 116 123. Elsewhere: local emergency services; search "domestic violence hotline" + country. The dedicated protocol file is [[dv-safety-planning]] (backlogged; `README.md` carries the standing resource list).

## Evidence & debates

Core pillars are peer-reviewed and replicated where replication exists: concept creep [1][2], the 54% deception-detection ceiling [6], misinformation effect [9], base-rate neglect [11], hostile attribution [17]. Sociological gaslighting [4] is a single landmark study (well-cited, not yet a literature). The prevalence-inflation hypothesis [12] is explicitly a "call to test" — treat as promising, not settled. NPD epidemiology varies by method [8]; the honest statement is the range, not a point.

## Sources

1. Haslam, N. (2016). "Concept Creep: Psychology's Expanding Concepts of Harm and Pathology." *Psychological Inquiry* 27(1), 1–17. https://www.tandfonline.com/doi/full/10.1080/1047840X.2016.1082418
2. Haslam, N., Dakin, B. C., Fabiano, F., et al. (2020). "Harm inflation: Making sense of concept creep." *European Review of Social Psychology* 31(1), 254–286.
3. Merriam-Webster, "Word of the Year 2022: *gaslighting*" (lookups +1740%). https://www.merriam-webster.com/wordplay/word-of-the-year-2022
4. Sweet, P. L. (2019). "The Sociology of Gaslighting." *American Sociological Review* 84(5), 851–875. https://journals.sagepub.com/doi/10.1177/0003122419874843
5. Namnyak, M., et al. (2008). "'Stockholm syndrome': psychiatric diagnosis or urban myth?" *Acta Psychiatrica Scandinavica* 117(1), 4–11. https://pubmed.ncbi.nlm.nih.gov/18028254/
6. Bond, C. F., & DePaulo, B. M. (2006). "Accuracy of Deception Judgments." *Personality and Social Psychology Review* 10(3), 214–234 (54% overall; 47% lies / 61% truths).
7. Mehrabian, A., & Wiener, M. (1967). *JPSP* 6(1), 109–114; Mehrabian, A., & Ferris, S. (1967). *J. Consulting Psychology* 31(3), 248–252; Mehrabian's scope disclaimer: https://en.wikipedia.org/wiki/Albert_Mehrabian
8. Stinson, F. S., et al. (2008). NESARC Wave 2 NPD epidemiology. *J. Clinical Psychiatry* 69(7), 1033–1045; range 0–6.2%, median ≈1.6%: *Focus* review, https://psychiatryonline.org/doi/full/10.1176/appi.focus.20220052; StatPearls NPD, https://www.ncbi.nlm.nih.gov/books/NBK556001/
9. Loftus, E. F. (2005). "Planting misinformation in the human mind: A 30-year investigation." *Learning & Memory* 12(4), 361–366. https://learnmem.cshlp.org/content/12/4/361.full
10. American Psychological Association (2008 statement: "no evidence within the psychological literature of a diagnosable parental alienation syndrome"; the APA simultaneously notes it has no official position); DSM-5 exclusion (American Psychiatric Association — keep the two APAs distinct); Harman, J., Kruk, E., & Hines, D. (2018). "Parental alienating behaviors." *Psychological Bulletin* 144(12), 1275–1299.
11. Kahneman, D., & Tversky, A. (1973). "On the Psychology of Prediction." *Psychological Review* 80(4), 237–251; Meehl, P., & Rosen, A. (1955). "Antecedent probability and the efficiency of psychometric signs." *Psychological Bulletin* 52(3), 194–216.
12. Foulkes, L., & Andrews, J. L. (2023). "…A call to test the prevalence inflation hypothesis." *New Ideas in Psychology* 69, 101010.
13. Yeung, A., Ng, E., & Abi-Jaoude, E. (2022). "TikTok and ADHD." *Canadian Journal of Psychiatry* 67(12).
14. Witkowski, T. (2010). "Thirty-Five Years of Research on Neuro-Linguistic Programming. NLP Research Data Base. State of the Art or Pseudoscientific Decoration?" *Polish Psychological Bulletin* 41(2), 58–66. doi:10.2478/v10059-010-0008-0
15. Johnson, M. P. (1995). *J. Marriage and the Family* 57(2), 283–294 ("patriarchal terrorism" vs "common couple violence"); Johnson (2006). *Violence Against Women* 12(11), 1003–1018 (sampling); Johnson (2008). *A Typology of Domestic Violence* (modern terms); Johnson, Leone & Xu (2014). *Violence Against Women* 20(2) (ex-spouses required); critique: Meier, J., GWU Law (empirical-support challenge).
16. Waldman, K. "The Rise of Therapy-Speak." *The New Yorker* (Mar 2021); "Psychology Terms You're Misusing." *Time* (2023); "NarcTok." *Slate* (Jan 2023).
17. Orobio de Castro, B., et al. (2002). "Hostile Attribution of Intent and Aggressive Behavior: A Meta-Analysis." *Child Development* 73(3), 916–934.
18. Hardy, M. S., & Calhoun, L. G. (1997). "Psychological Distress and the 'Medical Student Syndrome' in Abnormal Psychology Students." *Teaching of Psychology* 24(3), 192–193 (self-directed anxiety *decreased*; family-directed worry rose); Deo, M., & Lymburner, J. (2011). *Teaching of Psychology* 38(3) (little support for the syndrome).
19. Archer, J. (2000). "Sex differences in aggression between heterosexual partners: A meta-analytic review." *Psychological Bulletin* 126(5), 651–680 (cited for the symmetry debate; verification status logged in the bibliography).

## See also

[[manipulation-vs-influence]] · [[master-taxonomy]] · [[manipulation-audit]] · [[detection-heuristics]] · [[betrayal-blindness]] · [[therapy-speak-weaponization]] · [[everyday-manipulators]]
