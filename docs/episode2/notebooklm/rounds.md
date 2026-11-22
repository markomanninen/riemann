# Generation rounds for Part 2

Each round uploads the current scripts to the NotebookLM notebook “Mathematics and the Riemann Hypothesis in the Era of AI”, generates the long audio and the explainer video, and checks both against the script with a Whisper transcript. The ids of every round are in `runs.json`. The downloads, the uploaded texts and the transcripts of each round stay on the local machine in `sources/episode2/notebooklm/<round>/` and `transcripts/episode2/<round>/`.

The check has two parts. `scripts/episode2_check.py` looks for the cue lines, the facts and the status phrases in the transcript. A separate reader then compares the whole audio transcript with the script and lists every deviation. Whisper sometimes drops a few sentences, so a fact that the transcript lacks is confirmed from the audio before it counts as missing.

## Round v1, 21 November 2026

| | Audio | Video |
|---|---|---|
| Length | 47.5 min | 10.4 min |
| Cue lines found | 4 of 4 | 2 of 2 |
| Facts of the script found | 40 of 43 | 28 of 35 |

What the round got right. Both narrations followed the order of the script, said every cue line and kept the quotations of Alpöge, Sutherland, Tao and Pasten intact.

What went wrong in the audio.

- The hosts added facts from outside the script, such as other families of zeta functions, a guess about why the code skips a first inspection, and an invented explanation of theta lifts.
- The hosts stated the result as settled in about fifteen places, for example “completely machine checked” and “absolute certainty”.
- The hosts credited Claude with the chain of theta lifts, while the note credits Claude with the length of the chain.
- The printout of 250,000 pages was mixed up with the 17.4 million lines of code.
- The hosts spoke of “a stack of sources on the desk”.

What went wrong in the video.

- The narration said that Claude suggested replacing the derivative with theta lifts.
- The narration called the code “a 250,000-page proof”.
- The names of the three kernels, the 28 minutes and Mathlib were left out.

Changes for the next round. The script gained a sentence that fixes the facts to the script, a list of sentence subjects such as “the claimed proof says”, a rule that keeps pages and lines apart, a pronunciation list, exact wording for the credit to Claude, and clearer versions of the ceiling, the lattices and the engine.

## Round v2, 21 November 2026

| | Audio | Video |
|---|---|---|
| Length | 41.2 min | 9.0 min |
| Cue lines found | 4 of 4 | 2 of 2 |
| Facts of the script found | 39 of 43 | 31 of 34 |

What improved. The outside facts, the strong overclaims, the wrong credit to Claude, the mix-up of pages and lines, and the talk about sources were gone from the audio. The video named all six results of the first day and kept pages and lines apart.

What was still wrong in the audio.

- The hosts read the step numbers aloud, as in “Step 5.1”.
- The number 1,468,418 and Tao's remark on the second manuscript were left out.
- The second announcement was placed “at the exact same time” as the first, while it came a few hours later.
- Milder overclaims remained, such as “ultimate confirmation” and “astronomically low”.
- The lattices part dropped the sentence that nobody has confirmed the map, and the explanation of vanishing many times over was muddled.

What was still wrong in the video.

- The key sentence of the note was not read aloud.
- The narration said “the square root of a thousand” where the script says that the square root of one million is 1,000.
- The narration said that Claude discovered “the exact length” and added that Claude navigated the chain.
- The sentence about the two mirror-image claims came out as “unread by almost nobody”.

Changes for the next round. The parts of the argument are now named the mirror, the ceiling, the lattices and the engine, and the step numbers are gone. Every sentence of the lattices part starts with “according to the map”. The numbers of the ceiling example, the Clay rule, the second kernel's count, the titles of Vakil and Conrad and Tao's remark on the second manuscript are written as sentences of their own. The mirror-image sentences are simpler.

## Round v3, 21 November 2026

| | Audio | Video |
|---|---|---|
| Length | 38.3 min | 9.0 min |
| Length with the inserts | 40.9 min | 10.9 min |
| Cue lines found | 4 of 4 | 2 of 2 |
| Facts of the script found | 43 of 43 after listening to the two that Whisper misspelled | 34 of 34 |

What improved. Every number, date, name and quotation of the script is in the audio and is correct, including 1,468,418, the Clay rule, the titles of Vakil and Conrad and Tao's remark on the second manuscript. The step numbers are gone. The lattices part says that nobody has confirmed the map and defines the arithmetic size. The engine part defines vanishing many times over in one sentence. The video reads the key sentence of the note, gives the numbers of the ceiling example in the right order and credits Claude with the length of the chain.

What a human edit should still fix in the audio before publishing. Times refer to the narration without the inserts.

| Time | Words | Fix |
|---|---|---|
| 01:25 and 21:50 | “this entire deep dive”, “this deep dive” | The show is called “this episode” |
| 02:39 | banking encryption as “the invisible bedrock of your digital life” | Cut, the script makes no claim about encryption |
| 10:12 | “the machine had finished the formalized code, so he released it to the world” | Cut, the note gives no such reason |
| 14:12 | “That is a massive safeguard against cheating.” | Cut |
| 17:58 and 18:40 | two checkers in the same language “might share the same underlying compiler bugs”, “a completely different programming language” | Cut, the script only names Rust for nanoda |
| 18:40 | “No hidden assumptions.” | Cut |
| 24:25 | “an error of 11 is far, far below the square root of 1,000” | The square root of one million is 1,000 |
| 30:05 | “because the AI generated the formal logic so rapidly” | Cut |
| 31:13 to 31:55 | “massive paradigm shift”, “fear of obsolescence”, “everyone was skeptical” | Cut |
| 32:22 | Tao “is considered by many to be the greatest living mathematician” | Cut |
| 35:43 and 36:05 | “absolutely follows”, “It is mathematically rigorous evidence.” | The script says “strong evidence” |

What is imperfect and acceptable in the audio. The hosts add harmless pictures, such as a strict bouncer for the kernel and a zero at 0.3 with its mirror image at 0.7, and they say “part one” to “part four” for the four parts of the argument.

What is still off in the video.

- The narration reads an agenda of six sections aloud near the start.
- The mirror-image sentence says that almost no humans have “checked” the first claimed proof, where the script says that very few people have read it.
- The narration adds one question before the closing words, “What happens when machines understand the universe better than we do?”
- The Comparator sentence speaks of “the final 17.4 millionth line of code”.

State after three rounds. The third round is the closest to the script in both forms. The audio needs the light edit listed above, and the video needs a decision on the added closing question.

Changes for round v4. The reader's comparison showed that most remaining faults were filler that the hosts invented to reach the length. The audio script therefore grew from about 4,600 to about 5,200 words and now supplies its own filler.

- Every reaction, comparison and joke has a place in the script as an aside, such as “That is a small library” for the printout.
- Host B has scripted questions, such as why one checker is not enough.
- Each person has a one-line introduction, so the hosts have an accurate description to use.
- New sourced content fills the length. It covers why only code was published, how the author describes the collaboration, the remark on the timing, the people thanked in the note, the two Lean versions, the memory that the check needs, Chebyshev's device of 1850 and the view count of the Numberphile reaction.
- The ceiling example ends with “Eleven is far below one thousand”, so the phrase “square root” is said once.
- The promise of the cold open and the opening of the argument segment contain the words “this episode”.
- The prompt asks the hosts to fill the time with the beats, quotations, questions and asides of the script, and it has no target length in minutes.
- The video script sends the narration from each scene straight into the next, gives the mirror-image sentences in a simpler form and fixes the two closing sentences as the last words.

## Round v4, 21 November 2026

| | Audio | Video |
|---|---|---|
| Length | 37.2 min | 8.5 min |
| Length with the inserts | 39.8 min | 10.5 min |
| Length with the inserts after the edit list | 38.8 min | 10.1 min |
| Cue lines found | 4 of 4 | 2 of 2 |
| Facts of the script found | 50 of 50 after listening to the four that Whisper misspelled | 34 of 34 |

What improved in the audio. The words “deep dive” are gone and the hosts say “this episode”. The ceiling example is right, “the square root of 1 million is 1,000. 11 is far below 1,000.” The invented technical claims of round v3 are gone, and the hosts use the asides, the scripted questions and the one-line introductions of the script. All the new material is in, including the two quotations from the note, the remark on the timing, the Lean versions and the view count.

What improved in the video. The narration follows the script almost sentence by sentence. The mirror-image sentences, the Comparator sentence and the two closing sentences are as written, and the added closing question of round v3 is gone.

What went wrong in the video. The narrator read the scene headings aloud, as in “Scene 3. What was announced?”, and read the words of the suggested title card. The instruction to show the scene titles on screen caused this.

What went wrong in the audio. The hosts added a passage of about 45 seconds after the voices of caution, which includes the sentence “The Riemann hypothesis is solved.” They also added a few smaller remarks, such as “Six weeks to topple a 167-year-old giant” and a description of Sutherland as “deeply skeptical, almost dismissive”.

The edit lists. `video/episode2_assemble.py` now takes an edit list, a text file with the phrases to cut, and removes them from the narration by their word timestamps.

- `v4_video_drop.txt` removes the seven spoken scene headings. The result is `build/episode2/v4_video_edited.mp4`.
- `v4_audio_drop.txt` removes seven added passages, among them the 45 seconds after the voices of caution. The result is `build/episode2/v4_audio_edited.m4a`.

A Whisper transcript of both edited files confirms that the cut passages are gone and that the sentences on both sides of each cut are complete. Nobody has listened to the joins yet.

What the slides showed. A Whisper check only hears the narration, so the slides of the round v4 video were also read frame by frame, one frame every twelve seconds. One slide was wrong. Its checklist, on screen from 3:38 to 4:25, listed items that the script lacks, such as “System security audit passed” and “Performance optimization review needed”. `video/episode2_slide_fix.py` draws a corrected checklist over that span from `v4_video_slides.json`, with the six results of the first day and the three runs that were still under way. All other slides of round v4 match the script. The slides of the earlier rounds were only sampled.

What cutting cannot fix in the audio, with times in the narration without the inserts.

| Time | Words | Fix |
|---|---|---|
| 22:50 | “that same reasoning instantly solves the Riemann hypothesis” | The script says that the same reasoning gives the Riemann Hypothesis |
| 26:31 | “We know the shape piece from Chowla and Selberg. Therefore, the prime pieces must also be capped.” | The sentence needs “according to the map” |
| 29:40 | “That ceiling guarantees the right half of the critical strip is completely empty of zeros.” | The sentence needs “according to the code” |
| 34:28 | “incredibly strong evidence” | The script says “strong evidence” |
| 17:25 | The Lean versions sound like “4.3.3.1” and “4.3.6.0” in the transcript | Listen and decide |

Two beats moved or dropped. The hosts left out the sentence that the author presents the argument before mastering all of its mathematics, and they told the Clay rule last in its segment.

State after four rounds. Round v4 with its edit lists is the closest to the script in both forms. The audio has four spoken overstatements left that only a new take or a new round can change.

## New inserts and round v5, 22 November 2026

The inserts were rebuilt after feedback on round v4.

- The news collage now has thirteen takes of one to four seconds from thirteen different videos, where it had six takes of 8 to 15 seconds. It runs 44 seconds.
- The closing collage now has five whole statements of 7 to 23 seconds, where it had five fragments. It runs 71 seconds.
- Every change of clip is marked in the picture and in the sound, with a title card and a whoosh at the start, a red sweep with a short whoosh between clips and a bell at the end.
- The cuts are defined in `docs/episode2/inserts.json`.

The scripts gained a part about the published code itself, called “Inside the repository”. Its numbers were counted from the files of the proof repository or come from the notes of the people who check it. They cover the size of the archive, the seven libraries, the folder and file names, the 12-line main file, the text search for “sorry” and for axioms, the reading of the statements by hand and the cost of the build.

| | Audio | Video |
|---|---|---|
| Length | 41.2 min | 11.0 min |
| Length with the inserts | 43.8 min | 13.0 min |
| Cue lines found | 4 of 4 | 2 of 2 |
| Facts of the script found | 63 of 63 after listening to the five that Whisper misspelled | 42 of 42 |

What the video did. The narration covers the new scene with every number right, reads no scene headings aloud and ends on the two closing sentences. All 23 slides were read as pictures, and none carries words that the script lacks. The narrator said “11%” where the script says 11, left out the question of the video after announcing it, and added a few glosses, such as a sentence about the Langlands program. `v5_video_drop.txt` cuts six such passages. The result is `build/episode2/v5_video_edited.mp4`, 12.7 minutes long.

What the audio did. The new segment has every number and name right. The hosts were looser than in round v4 everywhere else. They stated as fact that the AI built whole theories, read four of the script's instructions aloud, as in “every sentence here must start with, according to the map”, and dropped most of the hedges in the part about the shape of the argument. A reader's comparison listed 36 passages to cut and about fifteen faults that cutting cannot fix.

The joined audio. Round v4 has the better discipline and round v5 has the repository segment, so `video/episode2_splice.py` joins the two. It takes the round v4 narration with its edit list, and it places the repository segment of round v5 before the part about how a machine checks a proof, with six added passages of that segment cut out by `v5_audio_repo_drop.txt`. The recipe is in `hybrid_audio.json`. The result with the inserts is `build/episode2/hybrid_audio_edited.m4a`.

## The news collage as a mosaic, 22 November 2026

The news collage was rebuilt as a mosaic after feedback on the new inserts, and further rounds of feedback added speed, fading voices and a closing clip on the full screen. Its thirteen takes and their order stay the same.

- The first take plays full screen. The next eleven takes join it in a grid of 2 by 2, then 3 by 3, then 4 by 4. Twelve tiles fill three rows of the last grid, and the fourth row carries the title.
- The newest take has the sound at full level, a red frame and a white flash on entry. The earlier takes keep running from their own source videos, a little darker.
- Every take keeps its words whole. After its last word it drops by 15 decibels within 0.25 seconds and fades out under the next two takes, and a soft whoosh marks every change.
- The takes speed up, and the steps of speed grow towards the end. The first take runs at normal speed, the sixth at 1.2 times, the ninth at 1.5 times and the twelfth at twice normal speed, with the pitch of the voices kept.
- The thirteenth take, “It is unconfirmed”, starts at the size of a tile in the centre of the mosaic, grows to the full screen within 0.45 seconds and runs at normal speed. The earlier voices are silent half a second after it starts. An earlier build let it appear alone in the fourth row first, which looked clumsy.
- The insert runs 31 seconds, where the version with sweeps ran 44 seconds.

Three faults turned up in the builds and were fixed. The first build faded every take out inside its last word, which turned “historical” into “historic” in the transcript. At a change of grid some tiles stayed empty for two or three frames, because their source video delivered its first frame late. A tail level of 12 decibels below the words made Whisper hear “the big one” for “a big one”, and at 15 decibels below it heard the words right.

How the speed was chosen. A first version rose in equal steps to a top speed of 1.4. That speed came from a test in which the sound was built at top speeds of 1.2, 1.3, 1.4 and 1.5 and transcribed each time. Eleven of the twelve English takes came out right at every speed. The take of Tony Padilla, “Do you want to know what my reaction was?”, came out right at 1.3 and 1.4 and wrong at 1.2 and 1.5, so Whisper is unsure about this take whenever it is sped up. The rise to 1.4 in equal steps was hard to notice, and the feedback was that a transcriber may miss the fastest words at the end. The final version therefore rises in growing steps to twice normal speed.

What was checked on the final build.

- A Whisper transcript of the finished insert has the words of eleven of the twelve English takes, also of the three fastest ones. The opening words of Tony Padilla came out as “I just wonder what my reaction was”. Whisper also wrote “You're welcome” over the bell at the end, where nobody speaks.
- A script read all 931 frames of the insert and found no frame with an empty tile, and it found the closing clip on the full screen in the 59 frames after its growth.
- The speed of the picture was measured for four tiles by matching two of their frames to the source video. The tiles set to 1.21, 1.53, 1.83 and 2.00 measured 1.20, 1.44, 1.84 and 2.01.
- Frames of the grid stages, of the growth of the closing clip and of the closing view were read as pictures.

Listening to the insert and watching it in motion are still open.

The joined audio and the round v5 video were assembled again with the mosaic. `build/episode2/hybrid_audio_edited.m4a` runs 44.4 minutes and `build/episode2/v5_video_edited.mp4` runs 12.4 minutes. The audio episode uses the sound of the same insert, so its listeners hear the same speed, voices and whooshes.
