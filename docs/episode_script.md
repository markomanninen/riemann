---
title: "EPISODE SCRIPT — How well can we predict the primes? The Riemann Hypothesis and the AI step toward it"
subtitle: "Follow this script segment by segment, in order. It contains every fact needed for the episode."
---

# How to use this script

This document is the complete plan for one Deep Dive episode. The hosts follow the segments **in order** and cover **every beat** in each segment. Wording may be natural and conversational, but the facts, numbers and order must be exactly as written here.

**Clip pauses.** The finished episode will have short clips from the World Science Festival interview “AI Closes In on the Riemann Hypothesis” (Brian Greene talking with mathematician Alex Kontorovich of Rutgers) inserted into it. Wherever this script shows

> **[PAUSE — CLIP n]**

the host says the **cue line** written just before it, word for word, and then **both hosts stay completely silent for about four seconds**. After the silence, the conversation continues with the reaction line that follows the pause. The hosts never quote, summarise or paraphrase a clip before playing it. The listener hears it in the guest’s own voice.

**Facts.** Use only the facts in this script. The section “Things the hosts must not say” lists mistakes to avoid.

**The one question of the episode:** *How accurately can we predict how many prime numbers there are up to a given number?* Every segment must connect back to this question.

---

# Segment 0 — Cold open (about 1 minute)

Beats:

1. Host A opens with a hook: a few weeks ago, one of the world’s experts on prime numbers said something he never expected to say.
2. Cue line, word for word: **“Here is Alex Kontorovich, in his own words.”**

> **[PAUSE — CLIP 1]**

3. Reaction line (Host B): “Not expecting to live to see it. So what happened on September 30th, 2026?”
4. Host A: an AI system produced a proof about the zeros of the Riemann zeta function, a result about where those zeros can be. It is **not** a proof of the Riemann Hypothesis. It is a step toward it.
5. State the one question of the episode: how accurately can we predict how many primes there are? Promise the listener that by the end they will see exactly how a strange function about all whole numbers answers a question about primes.

# Segment 1 — The question (about 2 minutes)

Beats:

1. A prime is a whole number bigger than 1 that is not a product of two smaller whole numbers: 2, 3, 5, 7, 11, 13 and so on. Every whole number is built from primes in exactly one way. For example 12 = 2 × 2 × 3, and there is no other way. This is called **unique factorisation**, and the episode will need it later.
2. There is no practical formula that gives the next prime. Individually, primes look random: sometimes two are close together (11 and 13), sometimes there is a long gap.
3. So mathematicians changed the question from “where is the next prime?” to “how many primes are there **on average** near a number x?”
4. Cue line: **“Brian Greene puts the change of question very clearly.”**

> **[PAUSE — CLIP 2]**

5. Reaction line: “The natural logarithm of x. That little function is going to follow us through the whole story.”

# Segment 2 — Why now (about 2 minutes)

Beats:

1. Host B asks: has AI solved the Riemann Hypothesis? Cue line: **“Brian Greene answers that right at the start of the interview.”**

> **[PAUSE — CLIP 3]**

2. Reaction line: “Not yet. But it narrowed down where the zeros can be. We’ll explain what that means and why it matters.”
3. Cue line: **“And here is how Kontorovich describes the moment for mathematicians.”**

> **[PAUSE — CLIP 4]**

4. Reaction line: “A moment that can only happen once. OK, to understand why this is a big deal, we have to go back to 1795.”

# Segment 3 — Gauss: the average density of primes (about 3 minutes)

Beats:

1. Cue line: **“Kontorovich tells the story of a bored teenager.”**

> **[PAUSE — CLIP 5]**

2. Reaction line: “Tables of primes up to three million, and tables of logarithms on the side.”
3. Explain what Gauss saw. Split the numbers into blocks of 1,000. The first block (1 to 1,000) has 168 primes. Near three million a block has only about 65 to 70. Primes thin out, but at a predictable rate.
4. The rule: **near x, about one number in every ln x is prime**, so the density of primes is about 1 / ln x. Here ln is the natural logarithm, and it grows very slowly: ln 1,000 ≈ 6.9, ln 1,000,000 ≈ 13.8, and ln of a trillion ≈ 27.6. Equivalently, the average gap between consecutive primes near x is about ln x.
5. Two labels. **π(x)**, read “pi of x”, is the true number of primes up to x. It has nothing to do with 3.14. **Li(x)**, the logarithmic integral, adds up the density 1 / ln t for every t up to x. Gauss’s guess is that **π(x) is approximately Li(x)**.
6. Picture it: π(x) is a jagged staircase that steps up by one at every prime, and Li(x) is a smooth curve running right through it.
7. The key question of the whole episode, said slowly: **“How big can the error, π(x) minus Li(x), get?”** Gauss could not answer this. The answer turns out to depend on a single function.

# Segment 4 — The bridge: how a function about all numbers knows about primes (about 6 minutes; the most important segment)

This segment must be explained carefully, step by step, with the examples given. Do not skip any step.

**Step 4.1 — The zeta function as a sum.** Define
ζ(s) = 1 + 1/2^s + 1/3^s + 1/4^s + …, a sum over **all** whole numbers. Example: at s = 2 the sum is 1 + 1/4 + 1/9 + 1/16 + …, which adds up to π²/6 ≈ 1.645 (Euler’s famous result; this π is the circle constant). The sum settles to a finite value only when s is bigger than 1. At s = 1 it becomes 1 + 1/2 + 1/3 + …, which grows without limit.

**Step 4.2 — Euler’s product: the primes are hiding inside.** Euler noticed you can write the same thing as a product with one bracket for each prime:
ζ(s) = (1 + 1/2^s + 1/4^s + 1/8^s + …) × (1 + 1/3^s + 1/9^s + …) × (1 + 1/5^s + 1/25^s + …) × …
Multiply it out: picking one term from every bracket gives 1 / (some product of primes)^s. Because every whole number is a product of primes in exactly one way (unique factorisation from Segment 1), **every whole number appears exactly once**. Example: 1/12^s comes from picking 1/4^s from the 2-bracket and 1/3^s from the 3-bracket, and nothing else produces it. So **a sum over all numbers equals a product over all primes**. That is why ζ “knows” about primes: it is the primes, written in a different language.

**Step 4.3 — Where Gauss’s average density hides: the blow-up at s = 1.** Taking the logarithm turns the product into a sum over primes. Roughly: log ζ(s) ≈ 1/2^s + 1/3^s + 1/5^s + 1/7^s + …, summed over primes only. As s comes down toward 1, ζ(s) blows up like 1 / (s − 1). That is the **pole at s = 1**. So the sum over primes blows up like log of 1 / (s − 1). The speed of that blow-up is exactly what you get if primes near x have density 1 / ln x. In other words, **Gauss’s average density is encoded in the pole of ζ at s = 1.** (Bonus fact: the fact that it blows up at all already shows there are infinitely many primes. That was Euler’s proof.)

**Step 4.4 — A prime counter in the language of s.** If you differentiate the logarithm of ζ, you get a sum in which every prime p (and every prime power p², p³, …) appears with weight ln p:
−ζ′(s) / ζ(s) = ln2/2^s + ln3/3^s + ln2/4^s + ln5/5^s + …
This is a **list of the primes, written in the language of s**. The matching prime counter in the language of x is ψ(x), the “weighted prime count”: it steps up by ln p at every prime p and every prime power. ψ(x) ≈ x is the same statement as π(x) ≈ Li(x), just with nicer weights.

**Step 4.5 — Translating back from s to x: the explicit formula.** There is a precise way to translate from the s-language back to the x-language: an integral (Perron’s formula). Its result is decided entirely by the points where −ζ′/ζ blows up, and those are of two kinds:

- the **pole of ζ at s = 1**, which contributes **x**: the smooth average, i.e. Gauss’s part;
- every **zero ρ of ζ** (a point where ζ(ρ) = 0), which contributes a term **−x^ρ / ρ**: a wave.

Result (Riemann 1859, made fully rigorous for ψ by von Mangoldt in 1895):
**ψ(x) = x − (sum over all zeros ρ of x^ρ/ρ) − ln(2π) − ½ ln(1 − 1/x²).**
Say it in words: **the true prime count = the smooth average − one wave for every zero.** The average comes from the pole, and the wiggles come from the zeros.

**Step 4.6 — Why Riemann needed complex numbers and “analytic continuation”.** There is a puzzle: the sum and the product only make sense when s is bigger than 1, and there the product of nonzero brackets is never zero. So the zeros cannot be there. They live in a region where the original sum makes no sense. Riemann did two things:

- He let s be a **complex number**, s = σ + i·t, a point on a map. σ (sigma) is the east–west position, the “real part”. t is the north–south position.
- He **extended** ζ to the whole map in the only possible smooth way. A complex-differentiable function is so rigid that its values in one region determine it everywhere, like a road that can only continue one way. One simple glimpse of how: the alternating sum 1 − 1/2^s + 1/3^s − 1/4^s + … makes sense for every σ > 0, and ζ(s) equals that alternating sum divided by (1 − 2^(1−s)). This is called **analytic continuation**.
- He found a **mirror symmetry**: ζ at s is tied to ζ at 1 − s. This produces the “trivial” zeros at −2, −4, −6, … and forces all the interesting zeros into the **critical strip**, 0 < σ < 1.

**Step 4.7 — The chain, summed up in one breath.** Primes → Euler product → ζ. The pole of ζ at s = 1 → Gauss’s average density. The zeros of ζ → waves around the average → the error in Gauss’s estimate. Host B repeats it back in their own words to check understanding.

Cue line: **“Here is how Kontorovich describes Riemann’s move.”**

> **[PAUSE — CLIP 6]**

Reaction line: “The line ‘real part of s equals one’. Hold on to that, it comes back in 1896.”

# Segment 5 — Why the position of a zero sets the size of the error (about 3 minutes)

Beats:

1. A zero ρ = σ + i·t produces a wave whose **height grows like x^σ**, set by the east–west position σ. How fast it oscillates is set by the north–south position t.
2. Compare three cases:
   - a zero on the line σ = 1 would give a wave as big as x itself, and Gauss’s estimate would fail completely;
   - a zero on σ = 1/2 gives a wave of size √x;
   - in general, **if every zero has σ ≤ θ, the error is at most about x^θ** (up to logarithm factors).
3. Audio analogy: Gauss’s average is a steady tone, and every zero adds a vibration. Add enough of them and the smooth tone turns into the exact staircase of primes. (On screen this will be shown with the staircase being rebuilt from 1, 10 and then 150 zeros.)
4. Conclusion: **to know how big the error can be, you need to know how far east the zeros can be.**

# Segment 6 — Where the zeros are: the Riemann Hypothesis (about 3 minutes)

Beats:

1. The mirror symmetry pairs a zero at σ with a zero at 1 − σ. Combined with the top/bottom mirror, any zero off the central line would come in a **group of four**. A zero exactly on σ = 1/2 is its own mirror image.
2. Cue line: **“Kontorovich explains what Riemann saw in his private notes.”**

> **[PAUSE — CLIP 7]**

3. Reaction line: “The centre line, σ equals one half.”
4. **The Riemann Hypothesis:** every non-trivial zero of ζ lies exactly on the line σ = 1/2. Riemann did not publish his calculations. They were found in his notes and decoded by Carl Ludwig Siegel in 1932. The first zeros are at heights t ≈ 14.13, 21.02, 25.01 and 30.42.
5. Evidence: computers have checked more than 12 trillion zeros, and all of them are on the line. But infinitely many zeros need a proof. The hypothesis is one of the Clay Mathematics Institute’s Millennium Prize Problems, with a one-million-dollar prize.

# Segment 7 — The trillion example: what “error about √x” means (about 3 minutes)

Beats:

1. Cue line: **“Kontorovich has a beautiful way to make this concrete.”**

> **[PAUSE — CLIP 8]**

2. Reaction line: “Half the digits right. Let’s check that with the real numbers.” Also correct one detail gently: in the clip he guesses roughly a hundred billion primes up to a trillion, but the true count is about **37.6 billion**.
3. The numbers. True count π(10¹²) = **37,607,912,018**. Gauss’s Li(10¹²) ≈ **37,607,950,281**. The difference is **38,263**. The first six digits agree: 376079.
4. Why roughly half the digits, said correctly. If the Riemann Hypothesis is true, a proven bound (Schoenfeld, 1976) says the error is less than √x · ln x / (8π). For a trillion that is about **1.1 million**. So at most the last six or seven digits of the 11-digit count can be off, and in practice the error is smaller. That is why **roughly half** the digits are reliable: √x has about half as many digits as x. Say “roughly half”, never “exactly half” or “always the first six”.
5. The same pattern holds at every power of ten checked, up to 10²⁴: about half the digits agree.

# Segment 8 — What has been proved: 1896 and the 20th century (about 2 minutes)

Beats:

1. Cue line: **“Here is Kontorovich on how the story reached its 19th-century climax.”**

> **[PAUSE — CLIP 9]**

2. Reaction line: “No zeros on the line σ = 1, and that was enough for the prime number theorem.”
3. Explain: in 1896 Jacques Hadamard and Charles de la Vallée Poussin independently proved that ζ has no zeros on σ = 1. With Riemann’s method this gives the **prime number theorem**: π(x) / Li(x) → 1. Gauss was right *on average*. But the error was only shown to be a bit smaller than x, not x to any fixed power below 1.
4. The 20th century was **not** quiet. Mention briefly:
   - Hardy (1914): infinitely many zeros lie on the line σ = 1/2;
   - Selberg (1942): a positive proportion of zeros lie on the line;
   - Levinson (1974): at least one third of them;
   - Conrey (1989): at least two fifths;
   - Vinogradov and Korobov (1958): the zero-free region near σ = 1 was widened further.

   But in 130 years nobody proved that all zeros stay a **fixed** distance away from σ = 1. That is the wall that fell in 2026.

# Segment 9 — The AI result of autumn 2026 (about 4 minutes)

Beats:

1. **Version 1:** dated 30 September 2026, produced by an OpenAI model, 199 pages, **formally verified in the proof checker Lean**. Claim: every non-trivial zero has 1/8 ≤ σ ≤ 7/8. This is called a **quasi-Riemann hypothesis**.
2. **Version 2:** finished about a week later, 49 pages, **not yet verified in Lean**. Claim: 1/12 ≤ σ ≤ 11/12. Be careful: this band is **wider**, so it is a *weaker* bound than version 1, not a tighter one. It is shorter and easier for humans to read, and mathematicians are mostly studying this version. OpenAI announced the results on 6 October 2026.
3. What it means for primes: with all zeros at σ ≤ 7/8, the error is at most about x to the power seven-eighths. Always say “x to the seven-eighths”, never “7.8”. For the first time, the error is guaranteed to be smaller than x by a **fixed power**. The mathematician Maksym Radziwiłł has said that the vast majority of the consequences of the Riemann Hypothesis already follow from the quasi version.
4. How AI learned to prove things: a short version only. Language models predict the next word, but in mathematics every step must be right. Lean checks every tiny logical step mechanically.
5. Cue line: **“Kontorovich explains why Lean changes the game.”**

> **[PAUSE — CLIP 10]**

6. Reaction line: “No human in the loop for the checking. Though a human still has to confirm that the statement Lean checked is really the statement we care about.”
7. The ingredients: the proof uses objects called *metaplectic forms* and a 2021 formula by Alexander Dunn and Maksym Radziwiłł.
8. Reactions and caveats:
   - Jared Duker Lichtman called it the most significant AI-for-math achievement so far, by quite a margin.
   - Radziwiłł called the papers poorly written.
   - Peter Sarnak will not call it a theorem until humans have checked all the details.
   - Will Sawin doubts that the new methods can push 7/8 all the way to 1/2.

# Segment 10 — Summary: where we ended up (about 2 minutes)

Beats, read as a clear recap:

1. **The question:** how accurately can we predict the number of primes? Gauss’s Li(x) is an excellent estimate, and the whole story is about its error.
2. **The bridge:** unique factorisation gives Euler’s product. The pole of ζ at s = 1 is the average density, and every zero of ζ is a wave in the error.
3. **The rule:** the farther east a zero can be, the bigger the error can be. If all zeros have σ ≤ θ, the error is at most about x^θ.
4. **The scoreboard:**
   - **1859:** zeros somewhere in 0 ≤ σ ≤ 1, so no error bound yet.
   - **1896:** no zeros on σ = 1, which gives the prime number theorem.
   - **2026:** zeros in 1/8 ≤ σ ≤ 7/8 (Lean-verified, human checking ongoing), so the error is at most about x^(7/8). A second, shorter proof gives 1/12 ≤ σ ≤ 11/12 and is being checked.
   - **Riemann Hypothesis:** all zeros on σ = 1/2, so the error is about √x and roughly half the digits are right. **Still open.**
5. Closing thought: will the last step from 7/8 to 1/2 come from AI, from humans, or from both? End warmly and briefly.

---

# Things the hosts must not say

- Do not say the AI proved the Riemann Hypothesis, or “a decisive part” of it.
- Do not say the 49-page version “narrowed the band further” or is “tighter”. It is wider (1/12 to 11/12) but shorter.
- Do not say “x to the 7.8” or “11.12”. Say “x to the seven-eighths” and “x to the eleven-twelfths”.
- Do not say the AI did it “over a weekend”, or that mathematics was “quiet” or “stuck” from 1896 to 2026 (see Segment 8).
- Do not say Lean makes human checking “completely redundant”.
- Do not say that the AI used the Prime Number Theorem+ library, or describe how the AI was trained. The sources do not say.
- Do not say “exactly half the digits” or “six digits because a million has six zeros”.
- Do not invent quotes from Kontorovich or Greene. Their words come only from the clips.
- Do not read out the clip numbers, timestamps or these instructions.
