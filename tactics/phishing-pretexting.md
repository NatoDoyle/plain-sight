---
id: phishing-pretexting
type: tactic
name: Phishing & Pretexting
aliases: [phishing, pretexting, spear-phishing, whaling, business email compromise, BEC, smishing, vishing, social engineering]
domains: [scams-fraud, digital-platforms]
exploits: [authority, fear-exploitation, scarcity-urgency, trust-mechanics, information-asymmetry]
co-occurs-with: [ai-enabled-manipulation]
countered-by: [verification-rituals, detection-heuristics]
distinguished-from: [genuine-warning]
severity: high
evidence: supported
status: complete
last-updated: 2026-06-27
---

# Phishing & Pretexting

> A message that impersonates someone you trust — your bank, your IT department, your boss, a delivery service — wrapped in a believable backstory and a ticking clock, to get you to click, pay, or hand over a password or code. The lure is the **phish**; the cover story ("I'm from the fraud team and need to verify your login") is the **pretext**. The single defense that beats nearly all of it: **verify through a channel you chose, not the one in the message.**

## Definition

Phishing and pretexting are the core of **social engineering — deceiving a person into clicking, paying, or disclosing credentials by impersonating a trusted party and supplying a plausible reason to comply**. **Phishing** is the deceptive *lure* (usually email, but also text or voice) that mimics a trusted brand or person; **pretexting** is the fabricated *scenario/backstory* that justifies the ask ("this is IT — there's a breach and I need to confirm your password") [1][2]. Pretexting is the setup; phishing is one delivery of it. The category exploits people, not just machines — Mitnick's framing of the human as the "weakest link" [1]. The diagnostic — the file's center — is **impersonation + a fabricated reason + a request to act (click/pay/disclose) outside a channel you initiated**; it is distinguished from the genuine security alerts and transactional messages legitimate organizations really do send (*genuine warning*).

## Variants & aliases

- **Spear-phishing** — targeted at a specific person/org using personalized detail (name, role, a real project).
- **Whaling** — spear-phishing aimed at executives ("big fish").
- **Business Email Compromise (BEC) / CEO fraud** — impersonating an executive or vendor to redirect a wire or change payment details; often *no malware*, pure pretext — and the costliest variant (FBI IC3: **$2.77B in 2024**, ~$55.5B cumulative 2013–2023) [3].
- **Smishing** (SMS text), **vishing** (voice/phone call), **quishing** (malicious QR code — a payload type more than a true vector, but in common use).
- **Clone phishing** — copying a real prior email, swapping in a malicious link/attachment, resending it as an "update/correction."
- **Angler phishing** — posing as a brand's support account on social media to intercept complaining customers.

## How it works

The load-bearing pair is **authority + fear/urgency**. **Authority** ([[authority]]): the message comes from a bank, the IRS/HMRC, the police, IT, or the boss — figures we're conditioned to obey, so the request skips scrutiny. **Fear-exploitation and urgency** ([[fear-exploitation]], [[scarcity-urgency]]): "your account will be closed," "unusual login detected," "invoice overdue — pay today," "warrant for your arrest" — manufactured pressure that suppresses the pause in which you'd verify (the DBIR's median **21 seconds to click** a phishing link shows how fast this works) [3]. **Trust-mechanics** ([[trust-mechanics]]): spoofed look-alike domains, cloned logos, hijacked real email threads, and caller-ID spoofing borrow the visual/relational trust of the real party. **Information asymmetry** ([[information-asymmetry]]): you usually can't see message headers, the true URL behind a link, or whether "the vendor's new bank details" are genuine — the attacker exploits that gap. It is the digital, industrialized form of [[manufactured-urgency]] aimed at a credential or a payment.

## Recognition

### Behavioral markers

- An **unexpected** message asking you to **click a link, open an attachment, log in, pay, or share a code** — especially urgently.
- The sender **address/domain is a look-alike** (paypa1, brand-support-secure.com) even if the display name looks right.
- A link whose true destination (on hover/long-press) is **not the official domain**.
- A request for **credentials, full card numbers, or a one-time passcode (OTP)** — which no legitimate organization asks you to hand over.
- A **payment or bank-detail change** requested by email/text, especially "urgently" or "confidentially" (BEC).

### Typical phrases

"Unusual sign-in detected — verify your account within 24 hours or it will be locked." · "This is the IRS; a warrant has been issued — call immediately." · "Hi, it's [CEO] — I need you to pay this vendor today, keep it between us." · "Your package couldn't be delivered; confirm your details here." · "I'm from the bank's fraud team; read me the code we just texted you."

### Felt-sense indicators

- A jolt of **fear or urgency** pushing you to act *right now*.
- Flattery or pressure from an apparent **authority** you don't want to disappoint.
- A small unease that the **address, link, or request is slightly "off"** — trust that.

### Escalation signs

A pretext that escalates (more "verification" steps, more access requested); a phone follow-up to an email (multi-channel pressure); requests to move money, buy gift cards, install "support" software, or read out OTP codes — the point to stop and verify independently.

## Where it appears

Email, SMS, phone, messaging apps, and social media ([[digital-platforms]]) — against individuals (bank/delivery/government imposters) and organizations (BEC, IT-helpdesk pretexts) ([[scams-fraud]]); the entry vector for most data breaches and a frequent first step in [[con-anatomy]] and [[romance-scam-arc]].

## Typical sequences & co-occurrence

It co-occurs with [[ai-enabled-manipulation]] (declared here — voice clones, deepfakes, and AI-written lures now supercharge pretexting) and shares the pressure-close with [[manufactured-urgency]]. It exploits [[authority]], [[fear-exploitation]], [[scarcity-urgency]], [[trust-mechanics]], and [[information-asymmetry]], and is the opening move of many [[con-anatomy]] and [[romance-scam-arc]] sequences.

## Counter-strategies

### In the moment

- **Verify through an independent channel** ([[verification-rituals]]) — the one move that beats almost all of it: do **not** use any link or number *in the message*. Look up the bank/company/colleague via the official website, the back of your card, a prior statement, or your own contacts, and confirm there. Both CISA and the FTC state this explicitly [4].
- **Don't click links or open unexpected attachments**; type known web addresses yourself.
- **Never give a password, full card number, or OTP code** to an inbound contact — *no legitimate organization asks for your OTP.*

### Structural / long-term

- **Turn on MFA, ideally phishing-resistant (passkeys/FIDO2)** rather than SMS codes (CISA) [4].
- **For organizations**: out-of-band **callback verification** for any payment or bank-detail change; a no-blame **reporting culture**; email authentication (**DMARC/SPF/DKIM**); security-awareness training.
- **Slow the channel down**: a personal rule that urgent money/credential requests always get verified, never actioned on first contact.

### When to exit or escalate

If you clicked, entered credentials, or paid: change the password (and anywhere it's reused), enable MFA, contact your bank to stop/recall the payment, and report (below). For BEC wire fraud, speed matters — call your bank and the FBI immediately (the IC3 "Financial Fraud Kill Chain" can sometimes recall a recent wire).

## Legal protections & reporting

*US/UK, jurisdiction-labeled; not legal advice.* Phishing is criminal — **wire fraud, computer-fraud (CFAA), and identity-theft** statutes in the US; **Fraud Act 2006 / Computer Misuse Act 1990** in the UK. Report: forward suspicious emails to the **Anti-Phishing Working Group (reportphishing@apwg.org)** and the spoofed brand; to the **FTC (reportfraud.ftc.gov)**; financial loss or BEC to the **FBI IC3 (ic3.gov)**; **forward scam texts to 7726 ("SPAM")**. (UK: report to **Action Fraud** and forward email to report@phishing.gov.uk, texts to 7726.)

## Caveats & false positives

### Not this tactic when…

- **Legitimate organizations really do send transactional and security messages** (*genuine warning*): genuine "new-device login" alerts, password resets *you just requested*, MFA prompts, shipping notices, and real fraud-hold calls from your bank. **Urgency alone is not phishing** — banks really do freeze cards.
- **The distinguishing tells**, not the urgency: a **mismatched/look-alike domain**; a request to **supply** credentials/OTP/payment (legit alerts tell you to log in *yourself* via the normal site, not hand over secrets); a **fake login** link; a **generic greeting**; the message being **unexpected** relative to your actual activity; a **channel mismatch** (your bank texting a clickable login link).

### Base rates & severity calibration

The over-correction is its own harm ([[epistemic-guardrails]]): treating *every* notification as phishing makes people ignore real fraud alerts, miss genuine resets, or berate legitimate support staff; reporting a real sender as an attacker is the false-positive failure mode. The resolution is the same single discipline — **don't trust or dismiss based on the message; independently verify** via a channel you chose. Severity is **high**: phishing is the leading breach vector and BEC alone runs to billions annually [3] — credential theft, account takeover, identity theft, and wire fraud are serious and sometimes hard to reverse.

## Evidence & debates

Graded `supported` — measured by industry and government, not lab experiment. Defensible figures (cite by source + year): the **Verizon 2025 DBIR** found a **human element in ~60% of breaches** (note: the often-quoted **74% is the stale 2023 figure** — methodology changed) and **phishing began 16% of breaches** [3]; **FBI IC3** reported **$2.77B in BEC losses in 2024** (≈$55.5B cumulative 2013–2023) and **$16.6B total** reported fraud losses; **FTC** logged imposter scams as the most-reported category (**$2.95B**, 2024); **APWG** recorded **~4.8M phishing attacks in 2024** [3]. The canonical practitioner texts are **Mitnick & Simon, *The Art of Deception* (2002)** and **Hadnagy, *Social Engineering* (2018)** [1][2]; Cialdini's influence principles are a useful *organizing lens* for why lures work, not measured per-principle conversion rates. **Do not cite** the folkloric "90–91% of attacks start with phishing" (vendor marketing; the measured number is 16%), a "$6.3B BEC" figure (conflates sources — IC3's annual is $2.77B), or any "$X million average phishing-breach cost" without attributing it to IBM's modeled estimate. The honest line: the *prevalence* is well-established; the boundary from a legitimate alert is **independent verification**, not suspicion-by-default.

## Sources

1. Mitnick, K. D., & Simon, W. L. (2002). *The Art of Deception: Controlling the Human Element of Security.* Wiley — foundational social-engineering text; the "human as weakest link" framing; pretexting. Practitioner (canonical).
2. Hadnagy, C. (2018). *Social Engineering: The Science of Human Hacking* (2nd ed.). Wiley — elicitation, pretexting, phishing taxonomy. Practitioner (canonical).
3. Verizon, *2025 Data Breach Investigations Report* — ~60% of breaches involve a human element; 16% begin with phishing; pretexting >50% of social-engineering incidents; median 21s-to-click (2024 DBIR). FBI IC3, *2024 Internet Crime Report* + PSA I-091124-PSA ("BEC: The $55 Billion Scam") — BEC $2.77B (2024), ~$55.5B cumulative; $16.6B total 2024 losses. APWG, *Phishing Activity Trends* (2024) — ~4.8M attacks. FTC Consumer Sentinel *2024 Data Book* — imposter scams most-reported, $2.95B; $12.5B total fraud. Measured/industry+government. (Flag: "74% human element" is the 2023 figure; cite ~60%/2025.)
4. CISA, "Recognize and Report Phishing" and "Avoiding Social Engineering and Phishing Attacks"; FTC, "How To Recognize and Avoid Phishing Scams" — verify via an independent channel; don't click/share OTP; phishing-resistant MFA; reporting channels (APWG, FTC, IC3, 7726). Regulatory/government guidance (US; not legal advice).

## See also

[[ai-enabled-manipulation]] · [[manufactured-urgency]] · [[con-anatomy]] · [[romance-scam-arc]] · [[authority]] · [[fear-exploitation]] · [[scarcity-urgency]] · [[trust-mechanics]] · [[information-asymmetry]] · [[verification-rituals]] · [[detection-heuristics]] · [[scams-fraud]] · [[digital-platforms]] · *genuine warning*
