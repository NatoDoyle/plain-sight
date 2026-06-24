---
id: dark-patterns-obstruction
type: tactic
name: Dark Patterns — Obstruction
aliases: [roach motel, forced continuity, cancellation maze, sneak into basket, hard to cancel, privacy zuckering]
domains: [digital-platforms, sales]
exploits: [cognitive-overload-confusion]
co-occurs-with: [dark-patterns-social-urgency]
countered-by: [verification-rituals, detection-heuristics]
distinguished-from: [good-faith-ux]
severity: medium
evidence: supported
status: drafted
last-updated: 2026-06-24
---

# Dark Patterns — Obstruction

> Interface design that makes the thing *you* want hard and the thing *the company* wants easy: sign up in one tap, cancel through a six-click maze; a free trial that silently becomes a charge; items that sneak into your cart; settings that bury the private option. The asymmetry is the tell — easy in, deliberately hard out.

## Definition

Obstruction dark patterns are **interface designs that deliberately impede actions in the user's interest — cancelling, leaving, declining, protecting privacy — while making the company-favored action frictionless** (Brignull's "deceptive patterns," 2010; Mathur et al.'s "Dark Patterns at Scale," 2019, which catalogs *obstruction*, *sneaking*, and *forced action* among its categories) [1]. The signatures: the **roach motel** (easy to enter, hard to exit), **forced continuity** (a free trial that auto-converts to charges and is hard to cancel), **sneak into basket** (items added by default/side-path without explicit consent), and **privacy zuckering** (coined by EFF's Tim Jones, 2010 — confusing UIs that trick users into oversharing data). The diagnostic — the file's center — is **asymmetry and intent**: friction engineered to trap or extract, distinguished from the legitimate confirmation and security steps of honest design ([[good-faith-ux]]).

## Variants & aliases

- **Roach motel / cancellation maze** — one-click signup vs. a multi-page, multi-option, phone-only cancellation gauntlet (Amazon's "Iliad Flow" — a four-page, six-click, fifteen-option cancellation maze — drew a $2.5B FTC settlement, 2025) [2].
- **Forced continuity** — a free trial silently converting to a recurring charge, with cancellation obstructed.
- **Sneak into basket / hidden costs** — add-ons, insurance, or fees inserted by default or revealed only at the final step.
- **Privacy zuckering / obstructed opt-out** — "accept all" trivially easy, "reject all" buried behind layers; the private choice obstructed.
- **Nagging** — repeated prompts/interruptions until you give in (a milder obstruction-adjacent move).

## How it works

Obstruction weaponizes **effort and confusion** ([[cognitive-overload-confusion]]): every extra step, maze, or buried option imposes cognitive and time cost, and people predictably abandon a goal (cancelling, opting out, removing the add-on) when the friction exceeds their patience — so the company keeps the subscription, the data, or the add-on by attrition rather than consent. It also exploits inertia and the sunk-cost feeling of "I've already started." The asymmetry is deliberate: the *same* company can make signup a single tap, proving the friction on the exit is a choice, not a technical necessity.

## Recognition

- Signing up takes seconds; cancelling requires calls, multiple screens, "retention offers," or hunting for a hidden link.
- A free trial converts to a charge you have to actively (and effortfully) prevent.
- Items, add-ons, fees, or insurance appear in your cart/total without an explicit add.
- "Accept all" is one obvious button; "reject all" / the private option is buried or multi-step.
- Repeated nagging prompts that wear you down toward the company-favored choice.

### Typical phrases / patterns

"Call us during business hours to cancel." · "Are you *sure*? Here's 50% off…" (repeated) · pre-checked add-on boxes · a "manage preferences" path that loops back to "accept all." · "Your trial ends soon" with no easy cancel.

### Felt-sense indicators

- Exhaustion and the urge to give up on cancelling/opting-out — the design is working.
- Discovering a charge or add-on you never knowingly agreed to.
- The sense that leaving is being made deliberately painful.

### Escalation signs

Obstruction paired with [[dark-patterns-social-urgency]] (fake timers/counters pushing the signup) and [[manufactured-urgency]]; forced continuity that's nearly impossible to escape; data opt-outs that don't actually work.

## Where it appears

Digital platforms, e-commerce, subscriptions, and app interfaces ([[digital-platforms]], [[sales]]) — anywhere a company benefits from your inertia, continued subscription, or data.

## Typical sequences & co-occurrence

The "easy-in/hard-out" half of the dark-patterns playbook: it co-occurs with [[dark-patterns-social-urgency]] (declared here — fake urgency drives the easy signup that obstruction then traps) and pairs with [[manufactured-urgency]]. It exploits [[cognitive-overload-confusion]] (friction/sludge).

## Counter-strategies

- **Recognize the asymmetry** ([[detection-heuristics]]): if entry was one tap and exit is a maze, that's by design — the difficulty is the tactic, not your incompetence. Persist (or use the legal routes below).
- **Pre-empt forced continuity** ([[verification-rituals]]): set a reminder before any free trial converts; use virtual/single-use card numbers where possible; screenshot the cancellation terms at signup.
- **Cancel via the strongest channel**: cancel in writing, dispute the charge with your card issuer citing **ROSCA**/state auto-renewal law, and check what was actually added at checkout before paying.
- **Audit defaults**: hunt for the buried "reject all"/opt-out; uncheck pre-checked boxes; don't accept the easy default just because it's easiest.

## Legal protections & reporting

*US, jurisdiction-labeled; not legal advice — and this area is in flux.* The FTC's "Click-to-Cancel" Negative Option Rule was **vacated** (8th Cir., July 2025), but cancellation/auto-renewal practices remain governed by **ROSCA** (federal — clear disclosure, informed consent, simple cancellation), **state auto-renewal laws** (e.g., California), and **FTC Act §5 / state UDAP** — and the FTC still sues (the Amazon Prime "Iliad Flow" $2.5B settlement, 2025) [2]. (The FTC has signaled it may re-promulgate the cancellation rule — verify current status.) **EU:** the **Digital Services Act, Article 25** prohibits deceptive/manipulative interface designs. Report to the **FTC (reportfraud.ftc.gov)** and your state attorney general; dispute improper charges with your bank.

## Caveats & false positives

- **Not all friction is a dark pattern** ([[good-faith-ux]]): confirmation steps ("are you sure you want to delete?"), security friction (2FA, re-authentication for sensitive actions), and genuinely multi-step processes are honest, user-protective design. The line is **asymmetry and intent** — friction that serves the *company* against your clear intent (trivially easy in, deliberately hard out), not friction that protects *you*.
- **Some complexity is unavoidable**: real cancellations sometimes involve genuine steps (final billing, data export). Obstruction is the *engineered* maze, not every multi-click flow.
- **It's medium-severity**: the harm is financial (unwanted charges, lock-in) and privacy, recoverable but real ([[epistemic-guardrails]]); don't read every confirmation dialog as manipulation.

## Evidence & debates

Graded `supported` and regulatory-grounded: the patterns are empirically documented (Mathur et al.'s large crawl) [1], catalogued by Brignull/deceptive.design, named in the FTC's 2022 dark-patterns staff report, prohibited by EU DSA Art. 25, and actively enforced (Amazon, Epic) [1][2]. Brignull's specific terms ("roach motel," etc.) are practitioner coinages now adopted by regulators. The honest note: the regulatory line is *deception/coercion/obstruction against the user's interest*, not friction per se — so the construct is solid while its boundary (the [[good-faith-ux]] caveat) requires judgment.

## Sources

1. Mathur, A., et al. (2019). "Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites." *Proc. ACM HCI (CSCW)* — taxonomy incl. obstruction, sneaking, forced action. Brignull, H. (2010), "dark patterns"/deceptive.design — roach motel, forced continuity, sneak into basket. "Privacy zuckering" — Tim Jones, EFF (2010). FTC, "Bringing Dark Patterns to Light" (2022). Supported.
2. Regulation (US, jurisdiction-/date-specific; not legal advice): FTC "Click-to-Cancel" Negative Option Rule vacated (8th Cir., July 8, 2025) — ROSCA + state auto-renewal laws + FTC §5 still apply; FTC v. Amazon, Prime "Iliad Flow" cancellation maze, $2.5B settlement (Sept 25, 2025: $1B penalty + $1.5B refunds). EU Digital Services Act Art. 25. Established/regulatory.

## See also

[[dark-patterns-social-urgency]] · [[manufactured-urgency]] · [[fake-reviews-astroturfing]] · [[cognitive-overload-confusion]] · [[verification-rituals]] · [[detection-heuristics]] · [[digital-platforms]] · [[sales]] · [[epistemic-guardrails]] · [[good-faith-ux]]
