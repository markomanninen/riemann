---
title: "EPISODE SCRIPT, Predicting Primes Part 2. The proof that machines have checked and nobody has read"
subtitle: "Follow this script segment by segment, in order. It contains every fact needed for the episode."
---

# How to use this script

This document is the complete plan for one long episode. It is the sequel to the episode “Predicting Primes”, which explained how the zeros of the Riemann zeta function control the error in counting primes. The hosts follow the segments in order and cover every beat in each segment.

Every statement of fact in the episode comes from this script. The hosts keep to the names, numbers, dates, mechanisms and quotations written here, and they use the pictures that the script gives, which are the mirror, the waves under a ceiling, the pieces with a cap, and the exam. The hosts speak as two people who know this story well. They call the earlier episode “our last episode” and they call the show “this episode”.

The script holds enough material for a long episode. Some beats give a question for Host B to ask, and some beats end with an aside. An aside is a short remark that a host may add at that spot. The hosts take their reactions, comparisons and small jokes from these asides, so every remark in the episode has its place in the script.

The finished episode will have short clips of real people inserted into it. Each insert point is marked like this.

> **[INSERT, CLIP SET A]**

At an insert point one host says the cue line written just before the mark, in full and word for word, and stops. The other host then continues with the reaction line that follows the mark. The editor places the clips between the two lines. The listener hears each clip in the speaker's own voice, so the hosts introduce a clip with its cue line alone and talk about it only afterwards.

The one question of the episode is this. *Has the Riemann Hypothesis been proved, and what does “proved” mean when the proof exists only as computer code?* Every segment connects back to this question.

Three phrases carry the status of the result, and the hosts use them throughout.

- The result is a **claimed proof**.
- It is **machine-checked**, which means that several independent programs have accepted it and that the last runs were still under way on 21 November 2026.
- It is **still being digested**, because no mathematician has yet explained in readable form why it works.

Every sentence about what the proof does starts from one of these subjects.

- “The claimed proof says”
- “According to the code”
- “According to the map”
- “According to the author”

People are introduced like this, each with this one line.

- Brian Greene is a physicist at Columbia University and a founder of the World Science Festival.
- Andrew Sutherland is a mathematician at MIT.
- Terence Tao is a mathematician at UCLA and a winner of the Fields Medal.
- Hector Pasten is a mathematician at the Pontifical Catholic University of Chile.
- Ravi Vakil is a mathematician at Stanford and the president of the American Mathematical Society.
- Brian Conrad is a mathematician at Stanford.

Names are said like this, the same way every time.

- Levent Alpöge is said “LEH-vent AL-puh-geh”.
- Terence Tao is said “TOW”, to rhyme with “now”.
- Ravi Vakil is said “RAH-vee vah-KEEL”.
- Alessandro Masullo is said “mah-SOO-loh”.
- Hector Pasten is said “pah-STEN”.
- Lean is said like the English word “lean”.
- Mathlib is said “MATH-lib”.
- Dirichlet is said “dee-ree-KLAY”.
- Stepanov is said “steh-PAH-nov”.
- Chowla and Selberg are said “CHOW-la” and “SEL-berg”.
- The kernel names are said “nah-NO-dah”, “con LEH-cheh” and “lean four lean”.

---

# Segment 0. Cold open (about 2 minutes)

Beats:

1. Host A opens with the date. On Friday the twentieth of November 2026 the mathematical corner of the internet caught fire.
2. Host A says the cue line in full and word for word. **“Here is how the news sounded.”**

> **[INSERT, CLIP SET A]**

3. Host B says the reaction line. “Breaking news, a robe, a song, and one calm voice saying it is unconfirmed. So what actually happened?”
4. Host A states it plainly. A mathematician published a claimed proof of the Riemann Hypothesis, found together with an AI model. The proof was published only as computer code. Several independent programs have accepted it. No human has read it from start to finish.
5. Host B states the one question of the episode. Has the Riemann Hypothesis been proved, and what does “proved” mean when the proof exists only as code?
6. Host A makes the promise in these words. “By the end of this episode you will know what was claimed, how a machine checks a proof, what the argument looks like from a distance, and what is still open.”

# Segment 1. Where our last episode left us (about 3 minutes)

Beats:

1. The question of our last episode was how accurately we can predict how many primes there are up to a number x. Counting the primes is one of the oldest questions in mathematics. Gauss found a smooth estimate around 1795, called Li(x), and the whole story is about the error of that estimate.
2. Riemann showed in 1859 that the error is set by the zeros of one function, the zeta function. A zero is a point where the function has the value zero. The estimate is a smooth curve, and every zero adds a wave to it.
3. The position of a zero sets the height of its wave. A zero has an east–west position, its real part, written σ (sigma). The wave of a zero grows like x to the power σ. The farther east a zero sits, the bigger the error can be.
4. The zeta function has easy zeros at −2, −4, −6 and so on, which are called trivial. All the other zeros are called non-trivial, and they lie in the critical strip, the band where the real part is between 0 and 1.
5. The Riemann Hypothesis says every non-trivial zero has real part exactly one half. Then every wave is about the size of the square root of x, and roughly half the digits of Gauss's estimate are right. The word is roughly, and the hosts keep it. Give the example. The number of primes up to one trillion is 37,607,912,018, which is about 37.6 billion. Gauss's estimate is 37,607,950,281. The difference is only 38,263.
6. The scoreboard at the end of our last episode had three lines, and the hosts go straight from one line to the next. In 1896 it was proved that no zero has real part 1. In autumn 2026 an AI system wrote a proof that every zero has real part between one eighth and seven eighths, and a proof checker verified that proof. That result is called the quasi-Riemann hypothesis. The Riemann Hypothesis itself was still open.
7. Our last episode ended with a question. Would the last step, from seven eighths to one half, come from AI, from humans, or from both? Seven weeks after that autumn result there is a claimed answer, and it says both.

# Segment 2. What was announced (about 4 minutes)

Beats:

1. The author is Levent Alpöge, a mathematician who works at the AI company Anthropic. On 20 November 2026 he posted a four-page note on his website. The note has the plain title “remark”.
2. The key sentence of the note is this, and the hosts read it exactly. “I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis.” Claude is Anthropic's AI model.
3. The note says more. He writes that the method also resolves the Generalized Riemann Hypothesis, and that he and Claude have “formalized the arguments without assumptions”. Formalized means written in a language that a computer can check line by line.
4. The note is unusually frank. He writes that near the end the AI moved faster than he could follow. His words are these. “Claude far outpaced me near the finish line. No, Claude flew, and danced, and sparkled near that finish line.”
5. The note describes how the two worked. The author set the direction and the AI carried the argument forward. His words are these. “I guided us to the right situation analogous to that toy setting, and then Claude began to leave me in awe.”
6. He also writes that he is presenting a complete argument before he has mastered all of the mathematics around it. He promises to study it and to write it up properly.
7. Host B asks why he published only code. Host A answers from the note. A readable version would have been enormous, and he writes “I decided to only present Lean.” Lean is the proof checker that the code is written for.
8. One host says the cue line in full and word for word. **“Here is Brian Greene, in his own words.”**

> **[INSERT, CLIP B]**

9. The other host says the reaction line. “A quarter of a million pages, and nobody on Earth who understands it yet.”
10. The hosts then keep two numbers apart. The first number is pages. The author generated a printed, human-style version of the argument, and he says it ran past 250,000 pages. He kept that printout to himself, and nobody has checked it. He jokes that its Theorem 1 begins by noting that a real number that is different from one half is either bigger or smaller than one half. Aside. “That is a small library.”
11. The second number is lines of code. What he published, and what the machines checked, is the Lean code. The code has 175,187 files and about 17.4 million lines. It states and proves 818,755 theorems and lemmas. It has no comments at all. The main file is 12 lines long. Aside. “A tower of logic with a tiny flag on top.”
12. The note gives a timeline. Its first entry is dated 6 October 2026 and its last entry, which says only “GRH”, is dated 16 November 2026. That is six weeks. The note also credits the earlier AI results of the autumn as a spark for the idea.
13. The note thanks many people by name. Among them are Maksym Radziwiłł and Peter Sarnak, two mathematicians who commented on the autumn result in our last episode.
14. The note is open about the timing. The announcement came one day after Anthropic's stock market debut, as Scientific American noted. The author writes “The precise timing is horrible”, and he writes that the cynical reading of the timing is false.

# Segment 3. What exactly is claimed (about 3 minutes)

Beats:

1. The code proves five theorems. The first is the Riemann Hypothesis itself. Every non-trivial zero of the zeta function has real part one half.
2. The statement is taken from a public library called Mathlib. Mathlib is the shared library of mathematics for Lean, written by a large community over many years. The author used the library's own definition of the Riemann Hypothesis, so the goal was fixed by others before the proof was written. Host B asks whether an author could quietly prove an easier statement under the same name. Host A answers that the library's definition closes that door, because the goal was written by other people, and that a tool described later in this episode checks that the proof ends in exactly that goal.
3. The other four theorems are about relatives of the zeta function called Dirichlet L-functions. The zeta function adds up one over n to the power s over all whole numbers n. A Dirichlet L-function does the same and multiplies each term by a repeating pattern of numbers called a character.
4. Explain why these relatives matter with one example. The zeta function counts all primes. Dirichlet L-functions count the primes in one class, such as the primes whose last digit is 7. The claim says that the estimate for every such class has an error of about the square root of x, the same size of error as for all primes together.
5. Be precise about the word “generalized”. In this result it covers the Dirichlet L-functions. Other families of zeta functions are outside the five theorems. The note says the author expects to reach more with more time.
6. Close the segment with what the claim would give for the primes. The error of Gauss's estimate would be about the square root of x, and that is the best size that is possible. Roughly half the digits would be right for every x and for every such class of primes.

# Segment 4. Inside the repository (about 6 minutes)

This segment walks through the published code itself. Every number in it was counted from the files or comes from the notes of the people who check them.

Beats:

1. Host B asks what the proof looks like when you open it. Host A answers. It arrives as a compressed archive of 239 megabytes, split into 14 parts. Unpacked it is about one gigabyte of plain text in 175,187 files. An average file has about a hundred lines.
2. The files are sorted into seven libraries. The largest is called Development, with 141,928 files and 12.2 million lines. The second is called Formalism, with 18,254 files and 3.2 million lines. The smallest is called Lemmata, with 167 files and 9,232 lines.
3. The folder names read like the shelves of a research library. There are folders for étale cohomology, for the resolution of singularities, for class field theory, for the Weil bound and for the theta correspondence. The folder names suggest that the code builds these theories itself, on top of Mathlib. Aside. “It does not borrow the library. It rebuilds the shelves.”
4. The code carries the fingerprints of a machine. It has no comments at all. Many folders have names such as “General B Fact Left Bis Alt” and “Misc Lemmas Q”. The longest file name has 67 characters. The deepest files sit eleven folders down. One single file has 17,981 lines. Aside. “No person names a folder Misc Lemmas Q.”
5. At the top sits the main file with its 12 lines. It states the five theorems, and each one is proved in a single line that points to a result elsewhere. The theorem called “riemann Hypothesis” is proved by one name, “r h of all”. That name points to a statement called “Every Character”, which is the heart of the proof. Everything else in the gigabyte hangs below those three names.
6. The people who check the code first searched all 175,187 files as text. Lean has a word for a hole in a proof, and the word is “sorry”. It occurs zero times. The code declares zero axioms of its own. The search also found 57,554 places where the code asks Lean for more time to finish a hard step.
7. Then they read the five statements by hand. Host B asks what could go wrong in a statement. Host A gives the example of one half. In Lean, one divided by two is zero when the numbers are whole numbers. The readers confirmed that the one half in the statement is the real number one half. They also confirmed that the statement leaves out the point s equals 1, where the library gives the zeta function a made-up value.
8. Building the code is heavy work. Compiling it takes between 7 and 10 hours on a machine with 48 processor cores and 503 gigabytes of memory. The build writes a helper file for every module, and together these would fill about a terabyte, so the builders delete them as they go.
9. Compiling the code also runs parts of the code. For that reason the checkers compile it in a sealed container with no network connection, and they hand only the finished proof file to the kernels.

# Segment 5. How a machine checks a proof (about 5 minutes)

Beats:

1. A proof checker reads a proof in a strict formal language. At its centre is a small program called the kernel. The kernel accepts a step only when the step follows from the rules of logic. Ideas, intuition and reputation play no part. Aside. “The kernel is a doorman with one list, and every step has to be on the list.”
2. The checker can be trusted for a simple reason, and the hosts give it. The kernel is a small program, so people can inspect it. The proof may be millions of lines, and the kernel checks every one of them in the same way.
3. Host B asks why one checker is not enough. Host A answers. A kernel is still a program, and programs have bugs. Bugs were found and fixed in Lean's kernel during 2026. One of them made it possible to prove a false statement, and the version used here already has that fix. For that reason the checkers ran the proof through several kernels that different people wrote independently. A flaw would have to appear in all of them in the same way to let a wrong proof through, and that is the whole reason for using several kernels.
4. One more detail about versions. The code was built with Lean version 4.33.1, and the final judging uses the newer version 4.36.0, which has kernel fixes that came after the older version.
5. Give the results of the first day, as reported by Andrew Sutherland on the evening of 20 November 2026.
   - All 175,187 files compiled without errors.
   - The five theorems depend only on the three standard axioms that almost all formal mathematics uses. That means the proof adds no axioms of its own.
   - Lean's own kernel accepted every file when it was replayed.
   - An independent kernel called nanoda, written in the programming language Rust, accepted the whole proof in about 28 minutes on 80 processor threads.
   - A second independent kernel called con-leche accepted the whole proof in about three minutes. The hosts say the size of what it checked, which is 1,468,418 definitions and theorems.
   - A third independent kernel called lean4lean accepted every file.
   - Two older builds of other checkers declined to run, because the code uses one unusual kind of data type that they cannot read. The people checking count that as declined, which is different from rejected.
6. Say what was still running that evening. Lean's own kernel was still working through the whole proof in one piece, a file of 61.6 gigabytes that needs about 100 gigabytes of memory to check. A final end-to-end run with a tool called Comparator was also still running. A separate community group was rebuilding everything inside a sealed environment with no network.
7. Explain Comparator with a picture of an exam. The examiner writes the question on a clean sheet of paper, using only the public library. The student hands in a thick stack of work, which here is the 17.4 million lines of code. Comparator checks that the last line of the student's work is exactly the examiner's question, and that the work uses only the allowed axioms. So the answer is an answer to the examiner's question, and that is the tool that Host A promised earlier.
8. Name one caution from the people doing the checking. In 67 of the 175,187 files the code uses a shortcut that skips Lean's usual first inspection and hands the step straight to the kernel. That is allowed, because the kernel checks everything in the end. It does mean the kernels carry all the weight, which is the reason for using several of them.
9. Close the segment with the ladder of three words. Claimed, then checked, then understood. The result has climbed the first step. It is well up the second step, and the last runs are still under way. The third step has barely begun.

# Segment 6. The shape of the argument (about 8 minutes, the most important segment)

Host A opens the segment with this sentence. “This is the most important part of this episode.” The segment has four parts and a recap. The parts are called the mirror, the ceiling, the lattices and the engine, and the hosts use these names. The whole chain is said once, in the recap at the end of the segment.

**The mirror.** This part can be read directly in the code, in a file called “Crit Line”. According to the code, the heart of the claimed proof is one statement. No Dirichlet L-function is zero anywhere to the right of the line where the real part is one half. The rest follows from a mirror symmetry that has been known since the nineteenth century, the functional equation. The symmetry takes a zero in the critical strip with real part σ to a zero with real part 1 − σ. A zero to the left of the central line would therefore have a mirror image to the right of it. If the right side is empty, the left side of the strip is empty too, and the zeros of the strip can only sit on the line. The zeta function is the simplest Dirichlet L-function, so according to the code the same reasoning gives the Riemann Hypothesis. Aside. “A zero with real part 0.3 would have a mirror image with real part 0.7.”

**The ceiling.** This part can also be read in the code, where the step is called “Landau window”. The code defines a weighted count of primes up to x. It adds up a small weight for every prime and for every power of a prime up to x. The code then subtracts a smooth main term, which is the value the count would have if the primes were spread perfectly evenly. This main term is a different formula from the Li(x) of our last episode, and it plays the same role. Call the difference the error.

Give the listener one real number here. At x equal to one million the weighted count and its main term are both about 12.2 million, and the error between them is about 11. The square root of one million is 1,000. Eleven is far below one thousand. That is all this one example shows.

Our last episode said that every zero adds a wave to the error, and that a zero with real part β (beta) gives a wave of height about x to the power β. Now the key idea, said slowly. The ceiling is x to the power one half plus a tiny amount, for any tiny amount you like. Suppose the error stays below that ceiling for all large x. A zero to the right of the line would make a wave that grows faster than such a ceiling, and for large enough x the wave would break through. So a zero to the right of the line cannot exist. A ceiling alone is enough, and a floor is unnecessary, because every wave swings above zero again and again. A theorem of Edmund Landau from the early twentieth century makes this exact even though there are infinitely many waves.

**The lattices.** This part comes from an unofficial reader's map that volunteers posted. Nobody has confirmed the map yet, so the hosts present this part as a reading, and every sentence about it starts with “according to the map”. A lattice is a regular grid of points in a space of many dimensions. According to the map, each lattice has an arithmetic size, which is one number that measures how big the lattice is. According to the map, that number is a sum of pieces, with one piece for each prime and one more piece that depends on the shape of the lattice. The picture is a sum of pieces with a cap on the total. According to the map, the claimed proof builds special lattices whose prime pieces add up to at least the weighted count of primes. According to the map, the prime pieces are measured with a device that Chebyshev used in 1850, which counts how many times each prime divides a factorial. According to the map, a result from arithmetic geometry called the slope inequality puts a cap on the total size. According to the map, a classical formula named after Chowla and Selberg computes the shape piece. According to the map, a cap on the total and a known shape piece mean that the prime pieces are capped too. So, according to the map, the weighted count of primes stays below its main term plus a small error, and that is the ceiling.

One sentence ties the two parts together. Geometry gives a limit from one side only, and the ceiling is a limit from one side only.

**The engine.** This part is the author's account in his note. According to the author, the argument is a descendant of a method that Sergei Stepanov introduced in 1969. Stepanov's method proves the matching statement in a simpler world, where polynomials play the role of whole numbers and where the things being counted are the points of a curve. The method builds a helper function that vanishes many times over at each of those points. A function vanishes many times over at a point when the function and several of its derivatives are all zero there. A function can only vanish a limited number of times in total, so the number of points is limited.

Whole numbers have no derivative, and that is where the method stops working for ordinary primes. Aside. “You cannot take the derivative of the number seven.” According to the author, the claimed proof replaces the derivative with a chain of theta lifts. The code has a folder called “Theta Correspondence” for them. A theta lift is a construction from number theory, and the hosts leave it at that, because nobody has yet explained in plain terms how it works here. According to the note, each lift in the chain supplies one more order of vanishing, and for a prime count that reaches up to x the chain is about the square root of x lifts long. According to the note, the chain of lifts came out of the joint work of the author and Claude, and the length of the chain was Claude's suggestion. That length is the whole of what the note credits to Claude by name.

The hosts end this part with what is open. Nobody has yet explained the engine in readable form, and the author writes that he is still learning some of the mathematics that the chain uses.

**The recap.** Host A says the chain once, and each link starts with “the claimed proof says” or “according to”. According to the author, a chain of theta lifts builds special lattices. According to the map, the size of the lattices is at least a weighted count of primes, and geometry caps that size. According to the code, the cap is a ceiling for the error in counting primes, the ceiling empties the right half, and the mirror symmetry empties the left half. So the claimed proof says that every zero of the strip is on the line. Host B repeats the chain back in their own words with the same careful subjects.

# Segment 7. The reactions (about 5 minutes)

Beats:

1. The reaction was wide. The reaction video of the channel Numberphile passed 660,000 views by the next day.
2. Andrew Sutherland reported the first checks. Before the checks he told Scientific American this. “An AI that can prove the Riemann hypothesis is not one I'd want to meet.”
3. After Sutherland had compiled the code himself he said three things, and the hosts read all three.
   - “This is indeed an historic moment.”
   - “to me this is a human triumph, and a day for celebration.”
   - “There is much work to be done to understand the mathematical details of the proof.”
4. Terence Tao wrote on his blog after a very first look. The hosts read his words.
   - Alpöge “has generated an (enormous) Lean-only proof of the Generalized Riemann Hypothesis”.
   - It “appears to use the full power of modern developments on the Langlands program and arithmetic geometry”.
   - “I imagine the digestion process will take some time.”
   - “at least we have a human author to communicate with”.
5. Hector Pasten told Scientific American what is at stake for understanding. “If the proof is correct and understood, this completes a dictionary between different branches of math.”
6. One host says the cue line in full and word for word, straight after the Pasten quotation. **“Here are the voices of caution.”**

> **[INSERT, CLIP SET C]**

7. The other host says the reaction line. “Checked is one thing, and understood is another. That gap is the whole story today.”
8. Then tell the twist of the same day. A few hours after Alpöge's note, later on the same Friday, came a second announcement. It came from Ravi Vakil, and he called it a hurried announcement. It said that a mathematician named Alessandro Masullo has a proposed proof of the Generalized Riemann Hypothesis, that Brian Conrad has been looking closely at it for months, and that it is “all human, with no AI”.
9. Describe the two claims as mirror images. The first claimed proof has machine checks and almost no human readers. The second has human readers and almost no checks. Terence Tao wrote about the second manuscript, and the hosts read his words. “it will take some time to digest that manuscript also.” Both are claims today.

# Segment 8. What happens next (about 3 minutes)

Beats:

1. The first task is to finish the machine checks. That means the last kernel run on the whole proof, the end-to-end Comparator run, and the independent rebuild in a sealed environment.
2. The second task is the hard one. People have to extract the argument from 17.4 million lines of code and find out why it works. Volunteers have already started to draw maps of the proof. The author has promised a readable account, and he expects the argument to become much shorter once it is understood.
3. The million-dollar prize of the Clay Mathematics Institute has its own rules, and the hosts say this sentence in full. The rules ask for a published proof and for about two years of acceptance by the mathematical community.
4. Say what a finished check would show, in these words. It would show that the formal statement, which is Mathlib's own definition of the Riemann Hypothesis, follows from the three standard axioms according to several independent kernels. That is strong evidence that the statement is true. Strong evidence is the right phrase, because the kernels and the library were also made by people.
5. Say what remains for people. The reason why it is true, the ideas that other mathematicians can reuse, and the confidence that comes from many people having understood the proof.

# Segment 9. Summary and close (about 2 minutes)

Beats, read as a clear recap:

1. The question was whether the Riemann Hypothesis has been proved, and what “proved” means when the proof is code.
2. The claim is that every zero of the zeta function and of every Dirichlet L-function in the critical strip lies on the central line. The statement comes from Mathlib's own definition.
3. The check is that several independent kernels have accepted all 17.4 million lines, with the last runs still under way on 21 November 2026.
4. The shape of the argument, as far as it is known, is that a ceiling on a prime count empties the right half, that geometry supplies the ceiling according to the map, and that a chain of theta lifts stands in for an idea of Stepanov according to the author.
5. The updated scoreboard has four lines.
   - In 1859 it was known only that the zeros lie somewhere in the strip from 0 to 1.
   - In 1896 the line where the real part is 1 was cleared, which gave the prime number theorem.
   - In autumn 2026 the strip was narrowed to the range from one eighth to seven eighths.
   - On 20 November 2026 a claimed proof put every zero on the line at one half. It is machine-checked and still being digested.
6. Closing thought. For 167 years the hard part was finding a proof. Now the hard part may be reading one.
7. One host says the cue line in full and word for word. **“Brian Greene summed up the mood in three words.”**

> **[INSERT, CLIP D]**

8. The other host says the last line and the episode ends. “Exciting and terrifying. We will be back when the reading is done.”

---

# Wording guide

The hosts keep to these wordings.

- Say “a claimed proof”, “machine-checked” and “still being digested” for the status of the result.
- Say “accepted by several independent kernels” and “strong evidence” as the strongest words for the checking.
- Say “the code has about 17.4 million lines” for what was published and checked, and “a printout of more than 250,000 pages that the author kept to himself” for the page count.
- Say “the last runs were still under way on 21 November 2026” every time the checking is summed up.
- Say “Dirichlet L-functions” when describing how far the generalized claim reaches.
- Say “a published proof and about two years of acceptance” for the rules of the Clay prize.
- Say “an unofficial reader's map” for the source of the lattices part, and “the author's own description” for the engine part.
- Say “the length of the chain was Claude's suggestion” for the part that the note credits to Claude.
- Say “Here is” and “Here are” in full in the cue lines.
- Quote people with the exact words given in this script. Clips carry the words of the speakers in them.
- Introduce each person with the one line that the script gives for that person.
- Take every reaction, comparison and joke from the asides of the script.
- Call the four parts of the argument the mirror, the ceiling, the lattices and the engine.
- Call the show “this episode”.
- Say the names from the code the way the script writes them, in plain words.
- Keep clip marks, segment numbers, picture labels and these instructions silent.
