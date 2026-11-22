---
title: "VIDEO SCRIPT, Predicting Primes Part 2. The proof that machines have checked and nobody has read"
subtitle: "Plan for one long explainer video. Follow the scenes in order. It contains every fact needed for the video."
---

# How to use this script

This document is the complete plan for one long explainer video of about fourteen minutes. It is the sequel to the video “Predicting Primes”. The narration follows the scenes in order and covers every beat.

Every statement of fact in the video comes from this script, and so does every word and number on a slide. The narration keeps to the names, numbers, dates, mechanisms and quotations written here, and it uses the pictures that the script gives, which are the mirror, the waves under a ceiling, the pieces with a cap, and the exam.

Two short sets of clips of real people will be edited into the finished video. Each insert point is marked like this.

> **[INSERT, CLIP SET A]**

At an insert point the narrator says the cue line written just before the mark, in full and word for word, and then continues with the line that follows the mark. The editor places the clips between the two lines.

The narration goes from the last beat of one scene straight to the first beat of the next. Scene numbers, scene titles and suggested pictures are notes for the editor.

The one question of the video is this. *Has the Riemann Hypothesis been proved, and what does “proved” mean when the proof exists only as computer code?*

Three phrases carry the status of the result, and the narration uses them throughout.

- The result is a **claimed proof**.
- It is **machine-checked**, which means that several independent programs have accepted it and that the last runs were still under way on 21 November 2026.
- It is **still being digested**, because no mathematician has yet explained in readable form why it works.

Every sentence about what the proof does starts from one of these subjects.

- “The claimed proof says”
- “According to the code”
- “According to the reader's map”
- “According to the author”

Names are said like this, the same way every time.

- Levent Alpöge is said “LEH-vent AL-puh-geh”.
- Terence Tao is said “TOW”, to rhyme with “now”. He is a mathematician at UCLA and a winner of the Fields Medal.
- Ravi Vakil is said “RAH-vee vah-KEEL”.
- Alessandro Masullo is said “mah-SOO-loh”.
- Lean is said like the English word “lean”.
- Mathlib is said “MATH-lib”.
- Dirichlet is said “dee-ree-KLAY”.
- Stepanov is said “steh-PAH-nov”.
- The kernel names are said “nah-NO-dah”, “con LEH-cheh” and “lean four lean”.

---

# Scene 1. The news (about 1 minute)

Beats:

1. Open with the date. On Friday the twentieth of November 2026 the mathematical corner of the internet caught fire.
2. Say what happened. A mathematician published a claimed proof of the Riemann Hypothesis, found together with an AI model. The proof was published only as computer code. Several independent programs have accepted it. No human has read it from start to finish.
3. Say the cue line in full and word for word. **“Here is how the news sounded.”**

> **[INSERT, CLIP SET A]**

4. Continue with this line. “That was the sound of that Friday. This video asks one question.”
5. State the one question of the video, and go straight on to Scene 2.

Suggested picture. A title card with the date 20 November 2026 and the three words “claimed, checked, understood”.

# Scene 2. Where Part 1 left us (about 1 minute)

Beats:

1. Part 1 asked how accurately we can predict how many primes there are up to a number x. Gauss's smooth estimate Li(x) is very good, and the story is about its error.
2. Riemann showed in 1859 that every zero of the zeta function adds a wave to that error. A zero with real part σ (sigma) gives a wave that grows like x to the power σ.
3. The Riemann Hypothesis says every non-trivial zero has real part exactly one half. Then the error is about the square root of x, and roughly half the digits of the estimate are right.
4. In autumn 2026 an AI system wrote a proof that every zero has real part between one eighth and seven eighths, and a proof checker verified it. The hypothesis itself stayed open. This video picks up the story from there.

Suggested picture. The critical strip from 0 to 1 with the central line at one half, zeros as dots on the line, and the band from one eighth to seven eighths shaded.

# Scene 3. What was announced (about 2 minutes)

Beats:

1. The author is Levent Alpöge, a mathematician who works at the AI company Anthropic. On 20 November 2026 he posted a four-page note titled “remark”.
2. Read the key sentence of the note aloud in full and show it on screen. “I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis.”
3. He writes that near the end the AI moved faster than he could follow. Read his words aloud in full and show them on screen. “Claude far outpaced me near the finish line. No, Claude flew, and danced, and sparkled near that finish line.”
4. Keep two numbers apart. The first number is lines of code. What he published, and what the machines checked, is code for a proof checker called Lean. The code has 175,187 files and about 17.4 million lines, which is a rounded number. It proves 818,755 theorems and lemmas, it has no comments, and the main file is 12 lines long.
5. The second number is pages. The author says that a printed, human-style version ran past 250,000 pages. He kept that printout to himself, and nobody has checked it.
6. The code proves five theorems. The first is the Riemann Hypothesis in the exact form defined by Mathlib, the public library of mathematics for Lean. The other four say the same about Dirichlet L-functions, which count the primes in one class, such as the primes whose last digit is 7.

Suggested picture. Four large numbers side by side, 175,187 files, 17.4 million lines, 818,755 theorems and 12 lines in the main file.

# Scene 4. Inside the repository (about 2 minutes)

Every number in this scene was counted from the published files or comes from the notes of the people who check them.

Beats:

1. The proof arrives as a compressed archive of 239 megabytes. Unpacked it is about one gigabyte of plain text in 175,187 files.
2. The files are sorted into seven libraries. The largest is called Development, with 141,928 files and 12.2 million lines. The smallest is called Lemmata, with 167 files.
3. The folder names suggest that the code builds whole theories itself. Among them are étale cohomology, the resolution of singularities, class field theory and the theta correspondence.
4. The code carries the fingerprints of a machine. It has no comments, many folders have names such as “Misc Lemmas Q”, and one single file has 17,981 lines.
5. At the top sits the main file with its 12 lines. The theorem called “riemann Hypothesis” is proved there by one name, and that name points to a statement called “Every Character”, the heart of the proof.
6. The people who check the code searched every file as text. Lean's word for a hole in a proof is “sorry”, and it occurs zero times. The code declares zero axioms of its own.
7. They also read the statements by hand. In Lean, one divided by two is zero when the numbers are whole numbers, and the readers confirmed that the one half in the statement is the real number one half.
8. Compiling everything takes between 7 and 10 hours on a machine with 48 processor cores and 503 gigabytes of memory.

Suggested picture. The seven libraries as bars, with Development far longer than the others, and the 12-line main file on top.

# Scene 5. How a machine checks a proof (about 2 minutes)

Beats:

1. A proof checker has a small program at its centre called the kernel. The kernel accepts a step only when the step follows from the rules of logic.
2. A kernel is a program and can have bugs, so the proof was run through several kernels that different people wrote independently.
3. Give the results of the first day one by one, as reported by Andrew Sutherland of MIT on the evening of 20 November 2026.
   - All 175,187 files compiled without errors.
   - The five theorems depend only on the three standard axioms.
   - Lean's own kernel accepted every file.
   - The independent kernel nanoda accepted the whole proof in about 28 minutes.
   - The independent kernel con-leche accepted the whole proof in about three minutes.
   - The independent kernel lean4lean accepted every file.
4. Three runs were still under way that evening. They were Lean's own kernel on the whole proof in one piece, a final end-to-end run with a tool called Comparator, and an independent rebuild in a sealed environment.
5. Comparator works like an examiner. The question is written on a clean sheet using only Mathlib, and the tool checks that the theorem proved by the code is exactly that question.

Suggested picture. A checklist with six green ticks, each with its name, and three items marked “running”.

# Scene 6. The shape of the argument (about 3 minutes)

Beats:

1. **The mirror.** This part can be read directly in the code. According to the code, the heart of the claimed proof is one statement. No Dirichlet L-function is zero to the right of the line where the real part is one half. A mirror symmetry known since the nineteenth century takes a zero in the strip with real part σ to a zero with real part 1 − σ. If the right side is empty, the left side of the strip is empty too, and the zeros of the strip can only sit on the line.
2. **The ceiling.** This part can also be read in the code. The code defines a weighted count of primes up to x and subtracts its smooth main term. At x equal to one million both are about 12.2 million, and their difference is about 11. The square root of one million is 1,000, so the difference of 11 is far below 1,000. Now take a ceiling of x to the power one half plus a tiny amount. According to the code, if the difference stays below that ceiling for all large x, a zero to the right of the line is impossible, because its wave would grow faster than the ceiling and break through it for large enough x.
3. **The geometry.** According to an unofficial reader's map that nobody has confirmed yet, the ceiling comes from special lattices, which are regular grids of points in many dimensions. The size of such a lattice is a sum of pieces, one for each prime and one for its shape. The prime pieces add up to at least the weighted count of primes, and a result called the slope inequality puts a cap on the total.
4. **The engine.** According to the author, the argument is a descendant of a method that Sergei Stepanov introduced in 1969. Stepanov's method needs a function that vanishes many times over at each point, which requires derivatives, and whole numbers have none. According to the author, the claimed proof replaces the derivative with a chain of theta lifts. A theta lift is a construction from number theory, and this one sentence is all that the narration says about it. For a prime count that reaches up to x, the chain is about the square root of x lifts long. According to the note, that length of the chain was Claude's suggestion.
5. Nobody has yet explained the geometry and the engine in readable form.

Suggested pictures. The strip with a zero on the left and its mirror image on the right, crossed out. A wave that stays under a ceiling next to a growing wave that breaks through it. A row of pieces under a cap. A chain of boxes with arrows marked “plus one”.

# Scene 7. The reactions (about 2 minutes)

Beats:

1. Andrew Sutherland of MIT, who reported the first checks, told Scientific American “This is indeed an historic moment”. He also said “There is much work to be done to understand the mathematical details of the proof.”
2. Terence Tao wrote that the proof “appears to use the full power of modern developments on the Langlands program and arithmetic geometry”, and added “I imagine the digestion process will take some time.”
3. Say the cue line in full and word for word. **“Here are the voices of caution.”**

> **[INSERT, CLIP SET C]**

4. Continue with this line. “Checked is one thing, and understood is another.”
5. The same day brought a twist. Ravi Vakil of Stanford announced that Alessandro Masullo has a proposed proof of the Generalized Riemann Hypothesis, and that it is “all human, with no AI”. The first claimed proof has machine checks and almost no human readers. The second has human readers and almost no checks.

# Scene 8. What happens next, and the scoreboard (about 1 minute)

Beats:

1. The machine checks have to finish, and then people have to find out why the claimed proof works. The million-dollar prize of the Clay Mathematics Institute has its own rules, which ask for a published proof and about two years of acceptance by the mathematical community.
2. Show the scoreboard, built line by line.
   - In 1859 the zeros were somewhere in the strip from 0 to 1.
   - In 1896 the line where the real part is 1 was cleared, which gave the prime number theorem.
   - In autumn 2026 the strip was narrowed to the range from one eighth to seven eighths.
   - On 20 November 2026 a claimed proof put every zero on the line at one half. It is machine-checked and still being digested.
3. Close with these two sentences as the very last words of the video. For 167 years the hard part was finding a proof. Now the hard part may be reading one.
