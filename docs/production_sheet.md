# Production sheet: clips and visuals (for editing, NOT a NotebookLM source)

Source video: World Science Festival, *AI Closes In on the Riemann Hypothesis* (Brian Greene & Alex Kontorovich), youtu.be/ljFZfYZLHj8. Times are taken from the auto-subtitles and need about ±1 s fine-tuning against the real audio.

## Clips (in episode order)

| Clip | In | Out | ≈ s | Content | Starts with | Ends with |
|---|---|---|---|---|---|---|
| 1 | 0:00.0 | 0:21.3 | 21 | Kontorovich: not expecting to live to see it | Is this a kind of thing where you will | expecting to to live to see this. |
| 2 | 1:03.2 | 1:42.4 | 39 | Greene: average gap between primes is ln x = prime number theorem | So mathematicians have approached primes | known as the prime number theorem. Now, |
| 3 | 2:24.2 | 2:50.9 | 27 | Greene: AI has not solved it yet, it narrowed down where zeros can be | problems. Now, you may be expecting | it has blown mathematicians away. |
| 4 | 5:08.9 | 5:42.4 | 34 | Kontorovich: the 'holy crap' moment can only happen once | means soon enough. I mean, the uh holy | going, not not yesterday. |
| 5 | 14:18.0 | 15:24.4 | 66 | Kontorovich: Gauss, prime tables to 3 million, density 1/log | >> So Gauss was playing around with | Gauss's conjecture. |
| 6 | 15:46.0 | 16:35.2 | 49 | Kontorovich: Riemann 1859, zeta to complex numbers, zeros, line Re s = 1 | But he also this one paper in 1859 is | real part of s equals one. |
| 7 | 16:58.1 | 17:38.0 | 39 | Kontorovich: Riemann's notebooks, symmetry s <-> 1-s, the 1/2 line | moreover, he he said, I think, and now | theorem, but the best possible error |
| 8 | 17:38.0 | 18:30.9 | 53 | Kontorovich: a trillion, half the digits right | other words, if you want to know how | because there are zeros on the half |
| 9 | 18:43.2 | 19:18.7 | 36 | Kontorovich: 1896 Hadamard & de la Vallee Poussin | >> And it wasn't until 1896 when two | asymptotic estimate for the numbers. |
| 10 | 11:48.6 | 12:15.6 | 27 | Kontorovich: Lean - no human in the loop | Um as opposed to the formal ones where | needed. |

Total clip time ≈ 6.5 min. Clip 5 can be shortened by cutting the smartphone joke (≈14:28–14:40). Clip 8 contains Kontorovich's '100 billion' slip, and the hosts correct it right after the clip.

## Visuals per segment (animations and graphs instead of slides)

| Seg | Narration | Visual | Status |
|---|---|---|---|
| 0 | Cold open | Clip 1 full screen → title card | clip |
| 1 | Primes, unique factorisation | Animated factor tree 12 = 2·2·3; number line with primes lighting up | **new** |
| 2 | Why now | Clips 3–4; 'strip narrowing' teaser (anim5, first 3 s) | clips + existing |
| 3 | Gauss density, π(x) vs Li(x) | anim1 (blocks of 1000), staircase π(x) drawing with Li(x) | existing + **new** (staircase draw-on) |
| 4.1 | ζ as a sum | Partial sums of 1+1/4+1/9+… converging to π²/6; harmonic sum diverging | **new** |
| 4.2 | Euler product | Brackets per prime; terms multiply out and land on the integers 1…30, each exactly once (12 highlighted) | **new** |
| 4.3 | Pole at s=1 = average density | ζ(s) on the real axis blowing up at s=1; Σ 1/pˢ next to log 1/(s−1) | **new** |
| 4.4 | −ζ′/ζ as a prime list | Spikes of height ln p at primes/prime powers → staircase ψ(x) | **new** |
| 4.5 | Explicit formula | anim4 (waves from 1→150 zeros rebuild ψ) with formula overlay: pole → x, zero → wave | existing + overlay |
| 4.6 | Analytic continuation | Complex plane: region σ>1 where the series works lights up, then the colour map of |ζ| spreads left over the whole plane; mirror line ½; trivial zeros | **new** |
| 4.7 | The chain | One animated diagram: primes → product → ζ → pole (average) + zeros (waves) → error | **new** |
| 5 | Wave height x^σ | Three single waves side by side for σ = 1, 7/8, ½ growing with x | **new** |
| 6 | Symmetry, RH, Z(t) | fig 04 animated (rogue zero → 4 mirrors), anim2 (ζ path through origin), Clip 7 | existing |
| 7 | Trillion | anim3 (digits table); fig 06; RH bound bar 1.1 million vs actual 38 263 | existing + small new |
| 8 | 1896 + 20th c. | Clip 9; timeline 1859 → 1896 → 1914 → 1942 → 1974 → 1989 → 2026 | **new** |
| 9 | AI result | anim5 (strip narrowing, corrected labels: 1/12–11/12 is wider), Clip 10 | existing (fix) |
| 10 | Summary | Scoreboard table built row by row | **new** |

## Assembly

1. NotebookLM Audio Overview (Deep Dive, Longer, English) with the episode script as its only source.
2. Find each cue line in the audio (silence detection + transcript) and insert the matching clip there.
3. Lay the visuals on the narration timeline using the transcript timestamps; clips play full screen with their own picture.
4. Burn in English subtitles (Finnish optional).