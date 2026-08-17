---
id: bias-codex-index
type: meta
name: Cognitive Bias Codex Index
aliases: [cognitive bias codex, bias codex, cognitive bias cheat sheet, benson codex]
status: researching
last-updated: 2026-08-04
---

# Cognitive Bias Codex Index

> The complete Cognitive Bias Codex (Benson/Manoogian 2016) mapped entry-by-entry to its home in
> this knowledge base — 189 listed entries, 188 unique biases, every one resolvable by name.

## How to read this index

**Provenance & pinning.** The authoritative enumeration is Buster Benson's
`cognitive-bias-cheat-sheet.json` (fetched 2026-08-04 from the `busterbenson/public` GitHub
repository) [1] — the data behind John Manoogian III's codex poster [2], derived from Wikipedia's
*List of cognitive biases* circa 2016 [3]. Benson's essay says "175 biases"; the JSON/poster carry
189 listed slots and 188 unique names (**Negativity bias** is listed under both Q1.2 and Q4.2).
Wikipedia's list has drifted since and is *not* the target. The codex lists several synonym pairs as
separate entries (Forer/Barnum, Frequency illusion/Baader-Meinhof, Risk compensation/Peltzman,
Bike-shedding/Law of Triviality, the four observer-expectancy variants…); each keeps its own row here,
mapped to a shared home.

**Columns.** *KB home* is the one file that owns the concept (one concept, one file); the wikilink
resolves once Tier 9 completes. *Evidence* grades the individual bias per `METHODOLOGY.md`
(established | supported | clinical | folk | contested). *Relevance* says what the bias means for a
defense KB:

- **lever** — tactics actively pull it; expect `exploits:` edges.
- **amplifier** — worsens other levers' effects (mostly target-side vulnerability).
- **observer-side** — biases the *defender's* judgment; feeds [[epistemic-guardrails]], not tactics.
- **not-a-lever** — no meaningful exploitation angle; included for completeness and said plainly.

Rows marked … are provisional until their home file's topic completes (see `ROADMAP.md` Tier 9).
Confusable names: **recency illusion** (linguistics; → [[pattern-illusions]]) is not the **recency
effect** (memory serial position; → [[memory-retrieval-quirks]]); **observer effect** here is the
expectancy effect, not the physics concept.

## 1. Too Much Information (42 entries)


### We notice things already primed in memory or repeated often.

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Availability heuristic | [[availability-salience]] | established | lever |
| Attentional bias | [[availability-salience]] | supported | amplifier |
| Illusory truth effect | [[fluency-familiarity]] | established | lever |
| Mere exposure effect | [[fluency-familiarity]] | established | lever |
| Context effect | [[memory-retrieval-quirks]] | contested | not-a-lever |
| Cue-dependent forgetting | [[memory-retrieval-quirks]] | established | not-a-lever |
| Mood-congruent memory bias | [[memory-retrieval-quirks]] | supported | amplifier |
| Frequency illusion | [[availability-salience]] | folk | observer-side |
| Baader-Meinhof Phenomenon | [[availability-salience]] | folk | observer-side |
| Empathy gap | [[emotional-flooding]] | established | lever |
| Omission bias | [[risk-misperception]] | … | … |
| Base rate fallacy | [[probability-blindspots]] | established | lever |

### Bizarre/funny/visually-striking/anthropomorphic things stick out more than non-bizarre/unfunny things.

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Bizarreness effect | [[availability-salience]] | supported | lever |
| Humor effect | [[availability-salience]] | supported | lever |
| Von Restorff effect | [[availability-salience]] | established | lever |
| Picture superiority effect | [[availability-salience]] | established | lever |
| Self-relevance effect | [[availability-salience]] | established | lever |
| Negativity bias *(dual-listed: Q1.2 + Q4.2)* | [[availability-salience]] | established | lever |

### We notice when something has changed.

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Anchoring | [[framing-anchoring]] | established | lever |
| Conservatism | [[confirmation-bias]] | established | amplifier |
| Contrast effect | [[framing-anchoring]] | established | lever |
| Distinction bias | [[framing-anchoring]] | supported | lever |
| Focusing effect | [[framing-anchoring]] | supported | lever |
| Framing effect | [[framing-anchoring]] | established | lever |
| Money illusion | [[probability-blindspots]] | established | lever |
| Weber–Fechner law | [[framing-anchoring]] | established | lever |

### We are drawn to details that confirm our own existing beliefs

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Confirmation bias | [[confirmation-bias]] | established | lever |
| Congruence bias | [[confirmation-bias]] | supported | lever |
| Post-purchase rationalization | [[dissonance-exploitation]] | … | … |
| Choice-supportive bias | [[dissonance-exploitation]] | … | … |
| Selective perception | [[confirmation-bias]] | supported | amplifier |
| Observer-expectancy effect | [[confirmation-bias]] | established | lever |
| Experimenter's bias | [[confirmation-bias]] | established | lever |
| Observer effect | [[confirmation-bias]] | established | lever |
| Expectation bias | [[confirmation-bias]] | established | lever |
| Ostrich effect | [[risk-misperception]] | … | … |
| Subjective validation | [[confirmation-bias]] | established | lever |
| Continued influence effect | [[confirmation-bias]] | established | lever |
| Semmelweis reflex | [[confirmation-bias]] | folk | observer-side |

### We notice flaws in others more easily than flaws in ourselves.

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Bias blind spot | [[optimism-overconfidence]] | supported | amplifier |
| Naïve cynicism | [[mind-reading-illusions]] | supported | observer-side |
| Naïve realism | [[mind-reading-illusions]] | established | amplifier |

## 2. Not Enough Meaning (63 entries)


### We find stories and patterns even in sparse data

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Confabulation | [[memory-fallibility]] | established | lever |
| Clustering illusion | [[pattern-illusions]] | established | lever |
| Insensitivity to sample size | [[probability-blindspots]] | established | lever |
| Neglect of probability | [[probability-blindspots]] | contested | lever |
| Anecdotal fallacy | [[pattern-illusions]] | n/a (logic, not empirics) | lever |
| Illusion of validity | [[pattern-illusions]] | supported | lever |
| Masked man fallacy | [[pattern-illusions]] | n/a (logic, not empirics) | not-a-lever |
| Recency illusion | [[pattern-illusions]] | folk | observer-side |
| Gambler's fallacy | [[pattern-illusions]] | established | lever |
| Hot-hand fallacy | [[pattern-illusions]] | contested | lever |
| Illusory correlation | [[pattern-illusions]] | established | lever |
| Pareidolia | [[pattern-illusions]] | established | lever |
| Anthropomorphism | [[pattern-illusions]] | established | lever |

### We fill in characteristics from stereotypes, generalities, and prior histories

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Group attribution error | [[attribution-errors]] | supported | lever |
| Ultimate attribution error | [[attribution-errors]] | supported | lever |
| Stereotyping | [[stereotyping-essentialism]] | established | lever |
| Essentialism | [[stereotyping-essentialism]] | established | lever |
| Functional fixedness | [[choice-simplification]] | … | … |
| Moral credential effect | [[self-evaluation-illusions]] | contested | lever |
| Just-world hypothesis | [[attribution-errors]] | established | amplifier |
| Argument from fallacy | [[confirmation-bias]] | n/a (logic, not empirics) | lever |
| Authority bias | [[authority]] | established | lever |
| Automation bias | [[authority]] | … | … |
| Bandwagon effect | [[social-proof]] | established | lever |
| Placebo effect | [[confirmation-bias]] | established | lever |

### We imagine things and people we're familiar with or fond of as better

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Out-group homogeneity bias | [[stereotyping-essentialism]] | established | amplifier |
| Cross-race effect | [[stereotyping-essentialism]] | established | observer-side |
| In-group bias | [[unity-ingroup]] | established | lever |
| Halo effect | [[liking-similarity]] | established | lever |
| Cheerleader effect | [[liking-similarity]] | … | … |
| Positivity effect | [[memory-self-editing]] | established | amplifier |
| Not invented here | [[fluency-familiarity]] | folk | observer-side |
| Reactive devaluation | [[attribution-errors]] | supported | lever |
| Well-traveled road effect | [[time-distortions]] | … | … |

### We simplify probabilities and numbers to make them easier to think about

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Mental accounting | [[probability-blindspots]] | established | lever |
| Appeal to probability fallacy | [[probability-blindspots]] | n/a (logic, not empirics) | lever |
| Normalcy bias | [[risk-misperception]] | … | … |
| Murphy's Law | [[probability-blindspots]] | folk | observer-side |
| Zero sum bias | [[probability-blindspots]] | supported | lever |
| Survivorship bias | [[probability-blindspots]] | established | lever |
| Subadditivity effect | [[probability-blindspots]] | established | lever |
| Denomination effect | [[probability-blindspots]] | supported | lever |
| Magic number 7+-2 | [[cognitive-overload-confusion]] | … | … |

### We think we know what other people are thinking

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Illusion of transparency | [[mind-reading-illusions]] | supported | lever |
| Curse of knowledge | [[mind-reading-illusions]] | established | lever |
| Spotlight effect | [[mind-reading-illusions]] | supported | amplifier |
| Extrinsic incentive error | [[mind-reading-illusions]] | supported | observer-side |
| Illusion of external agency | [[mind-reading-illusions]] | supported | lever |
| Illusion of asymmetric insight | [[mind-reading-illusions]] | supported | lever |

### We project our current mindset and assumptions onto the past and future

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Telescoping effect | [[memory-self-editing]] | established | observer-side |
| Rosy retrospection | [[memory-self-editing]] | supported | lever |
| Hindsight bias | [[memory-self-editing]] | established | lever |
| Outcome bias | [[memory-self-editing]] | established | lever |
| Moral luck | [[attribution-errors]] | supported | observer-side |
| Declinism | [[time-distortions]] | … | … |
| Impact bias | [[time-distortions]] | … | … |
| Pessimism bias | [[time-distortions]] | … | … |
| Planning fallacy | [[time-distortions]] | … | … |
| Time-saving bias | [[time-distortions]] | … | … |
| Pro-innovation bias | [[time-distortions]] | … | … |
| Projection bias | [[time-distortions]] | … | … |
| Restraint bias | [[self-evaluation-illusions]] | supported | lever |
| Self-consistency bias | [[memory-self-editing]] | supported | lever |

## 3. Need To Act Fast (53 entries)


### To act, we must be confident we can make an impact and feel what we do is important

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Overconfidence effect | [[optimism-overconfidence]] | supported | amplifier |
| Social desirability bias | [[self-evaluation-illusions]] | established | lever |
| Third-person effect | [[optimism-overconfidence]] | supported | amplifier |
| False consensus effect | [[mind-reading-illusions]] | established | lever |
| Hard-easy effect | [[self-evaluation-illusions]] | contested | observer-side |
| Lake Wobegone effect | [[self-evaluation-illusions]] | established | lever |
| Dunning-Kruger effect | [[self-evaluation-illusions]] | established | lever |
| Egocentric bias | [[self-evaluation-illusions]] | established | lever |
| Optimism bias | [[optimism-overconfidence]] | supported | amplifier |
| Forer effect | [[cold-reading]] | established | lever |
| Barnum effect | [[cold-reading]] | established | lever |
| Self-serving bias | [[attribution-errors]] | established | lever |
| Actor-observer bias | [[attribution-errors]] | contested | observer-side |
| Illusion of control | [[self-evaluation-illusions]] | supported | lever |
| Illusory superiority | [[self-evaluation-illusions]] | established | lever |
| Fundamental attribution error | [[attribution-errors]] | established | lever |
| Defensive attribution hypothesis | [[attribution-errors]] | supported | amplifier |
| Trait ascription bias | [[attribution-errors]] | supported | observer-side |
| Effort justification | [[commitment-consistency]] | established | lever |
| Risk compensation | [[risk-misperception]] | … | … |
| Peltzman effect | [[risk-misperception]] | … | … |

### To stay focused, we favor the immediate, relatable thing in front of us

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Hyperbolic discounting | [[time-distortions]] | … | … |
| Appeal to novelty | [[time-distortions]] | … | … |
| Identifiable victim effect | [[probability-blindspots]] | contested | lever |

### To get anything done, we tend to complete things we've invested time & energy in.

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Sunk cost fallacy | [[commitment-consistency]] | established | lever |
| Irrational escalation | [[commitment-consistency]] | established | lever |
| Escalation of commitment | [[commitment-consistency]] | established | lever |
| Generation effect | [[fluency-familiarity]] | established | lever |
| Loss aversion | [[loss-aversion-endowment]] | established | lever |
| IKEA effect | [[fluency-familiarity]] | supported | lever |
| Unit bias | [[choice-simplification]] | … | … |
| Zero-risk bias | [[risk-misperception]] | … | … |
| Disposition effect | [[loss-aversion-endowment]] | … | … |
| Pseudocertainty effect | [[risk-misperception]] | … | … |
| Processing difficulty effect | [[fluency-familiarity]] | contested | not-a-lever |
| Endowment effect | [[loss-aversion-endowment]] | established | lever |
| Backfire effect | [[confirmation-bias]] | contested | observer-side |

### To avoid mistakes, we tend to preserve our autonomy and group status, and avoid irreversible decisions.

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| System justification | [[attribution-errors]] | contested | amplifier |
| Reverse psychology | [[scarcity-urgency]] | supported | lever |
| Reactance | [[scarcity-urgency]] | established | lever |
| Decoy effect | [[framing-anchoring]] | supported | lever |
| Social comparison bias | [[self-evaluation-illusions]] | supported | amplifier |
| Status quo bias | [[loss-aversion-endowment]] | established | lever |

### We favor options that appear simple or have more complete information over more complex, ambiguous options.

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Ambiguity bias | [[risk-misperception]] | … | … |
| Information bias | [[choice-simplification]] | … | … |
| Belief bias | [[confirmation-bias]] | established | lever |
| Rhyme as reason effect | [[fluency-familiarity]] | supported | lever |
| Bike-shedding effect | [[choice-simplification]] | … | … |
| Law of Triviality | [[choice-simplification]] | … | … |
| Delmore effect | [[choice-simplification]] | … | … |
| Conjunction fallacy | [[probability-blindspots]] | established | lever |
| Occam's razor | [[choice-simplification]] | … | … |
| Less-is-better effect | [[choice-simplification]] | … | … |

## 4. What Should We Remember? (31 entries)


### We edit and reinforce some memories after the fact

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Misattribution of memory | [[memory-self-editing]] | established | lever |
| Source confusion | [[memory-self-editing]] | established | lever |
| Cryptomnesia | [[memory-self-editing]] | supported | not-a-lever |
| False memory | [[memory-fallibility]] | established | lever |
| Suggestibility | [[memory-fallibility]] | established | lever |
| Spacing effect | [[memory-retrieval-quirks]] | established | not-a-lever |

### We discard specifics to form generalities

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Implicit associations | [[stereotyping-essentialism]] | contested | observer-side |
| Implicit stereotypes | [[stereotyping-essentialism]] | contested | observer-side |
| Stereotypical bias | [[stereotyping-essentialism]] | contested | observer-side |
| Prejudice | [[stereotyping-essentialism]] | established | lever |
| Negativity bias *(dual-listed: Q1.2 + Q4.2)* | [[availability-salience]] | established | lever |
| Fading affect bias | [[memory-self-editing]] | established | lever |

### We reduce events and lists to their key elements

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Peak–end rule | [[memory-self-editing]] | contested | lever |
| Leveling and sharpening | [[memory-self-editing]] | contested | amplifier |
| Misinformation effect | [[memory-fallibility]] | established | lever |
| Serial recall effect | [[memory-retrieval-quirks]] | established | lever |
| List-length effect | [[memory-retrieval-quirks]] | contested | not-a-lever |
| Duration neglect | [[memory-self-editing]] | established | amplifier |
| Modality effect | [[memory-retrieval-quirks]] | established | not-a-lever |
| Memory inhibition | [[memory-retrieval-quirks]] | supported | lever |
| Primacy effect | [[memory-retrieval-quirks]] | established | lever |
| Recency effect | [[memory-retrieval-quirks]] | established | lever |
| Part-list cueing effect | [[memory-retrieval-quirks]] | supported | not-a-lever |
| Serial position effect | [[memory-retrieval-quirks]] | established | lever |
| Suffix effect | [[memory-retrieval-quirks]] | established | not-a-lever |

### We store memories differently based on how they were experienced

| Codex entry | KB home | Evidence | Relevance |
|---|---|---|---|
| Levels of processing effect | [[memory-retrieval-quirks]] | established | not-a-lever |
| Absent-mindedness | [[memory-retrieval-quirks]] | established | observer-side |
| Testing effect | [[memory-retrieval-quirks]] | established | not-a-lever |
| Next-in-line effect | [[memory-retrieval-quirks]] | supported | not-a-lever |
| Google effect | [[memory-retrieval-quirks]] | contested | not-a-lever |
| Tip of the tongue phenomenon | [[memory-retrieval-quirks]] | established | observer-side |
## Caveats

The codex is a **mnemonic, not a mechanistic taxonomy** [4]. Its four "problems" group biases by
the situation that evokes them, not by shared cognitive machinery — several entries appear under a
quadrant that fits one demonstration of the effect rather than its best explanation. Its evidential
status is wildly uneven: it sits replicated meta-analytic effects (anchoring, loss aversion) beside
single-study curiosities, folk labels (Murphy's Law, Delmore effect), one entry that is not a bias
at all (Occam's razor), and several constructs whose standard interpretation later failed or shrank
under replication (backfire effect, hot-hand *fallacy*, Google effect, the Dunning-Kruger
metacognitive story, IAT-based implicit association claims). This KB does not launder that
unevenness: each entry is graded individually, and contested entries are flagged in their home
file's Evidence base section. Treat the codex as a checklist of *names people search for*, not as
188 established facts.

## Sources

1. Benson, B. `cognitive-bias-cheat-sheet.json`, `busterbenson/public` GitHub repository.
   https://raw.githubusercontent.com/busterbenson/public/master/cognitive-bias-cheat-sheet.json
   (fetched 2026-08-04).
2. Manoogian, J. III & Benson, B. (2016). *The Cognitive Bias Codex* (poster). CC BY-SA 4.0.
3. Benson, B. (2016). "Cognitive bias cheat sheet." *Better Humans* (Medium), Sept 1, 2016.
4. Wikipedia, *List of cognitive biases* — noting its own inclusion-criteria debates; and critiques
   of bias-list taxonomies generally (e.g., Gigerenzer's "bias bias" critique) — see
   [[epistemic-guardrails]].

## See also

- [[master-taxonomy]] — how mechanism files relate to tactics, contexts, and defenses
- [[epistemic-guardrails]] — base rates, concept creep, and the observer-side bias register
- [[coverage-audit]] — repo-wide gap analysis; Tier 9 counts land there on completion
