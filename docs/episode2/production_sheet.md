# Production sheet for Part 2, clips and assembly (for editing, kept out of NotebookLM)

Part 2 is built from two NotebookLM narrations and four inserts of real voices. The long audio follows `episode_script.md` and the explainer video follows `video_script.md`. The inserts are defined in `inserts.json`, cut by `video/episode2_collage.py` and placed at the spoken cue lines by `video/episode2_assemble.py`.

## How the inserts are marked

Every change of clip is marked for the eye and for the ear, so a listener of the audio episode hears each change as clearly as a viewer sees it.

- An insert with several clips opens with a title card and a whoosh of 1.3 seconds.
- The news collage is a mosaic that fills the screen clip by clip. The first clip plays full screen, and the next eleven clips join it in a grid of 2 by 2, then 3 by 3, then 4 by 4. The thirteenth clip closes the collage on the full screen.
- In the mosaic the newest clip enters with a white flash, carries a red frame and its caption, and has the sound at full level. The earlier clips keep running from their own source videos, a little darker, each with a small name tag.
- In the mosaic every clip keeps its words whole. After its last word the clip drops by 15 decibels within 0.25 seconds and then fades out under the next two clips, so up to two earlier voices lie under the newest one. A soft whoosh marks every change.
- The mosaic speeds up, and the steps of speed grow towards the end. The first clip runs at normal speed, the sixth at 1.2 times, the ninth at 1.5 times and the twelfth at twice normal speed. All tiles on screen run at the speed of the newest clip, and the pitch of the voices stays as it is. The fastest clips serve the rush of the collage, so their words may be hard to follow.
- The twelve tiles fill three rows of the 4 by 4 grid, and the fourth row carries the title of the insert.
- The closing clip starts at the size of a tile in the centre of the mosaic and grows to the full screen within 0.45 seconds. It runs at normal speed. The earlier voices are silent half a second after it starts, and its picture stays for 0.6 seconds after its last word.
- In the closing collage a red band sweeps across a dark card between two clips while a short whoosh plays. The sweep lasts 0.5 seconds.
- A bell over a fading card closes the insert before the narration returns.
- Every clip carries a caption with the speaker and the title of the video, and every clip is brought to the same loudness. In the 4 by 4 grid a tile is 320 by 180 pixels, so its caption gives the speaker only.

## Source videos

All times below refer to these YouTube videos. View counts were read on 21 November 2026.

| Id | Channel | Title | Published | Views |
|---|---|---|---|---|
| eyDKuSdB9Tk | Lektor Lainz | BREAKING: Riemann solved?? | 20 Nov 2026 | 2,004 |
| 74e_cdErfvo | The Pretrained Pod | BREAKING: Claude may have just solved the Riemann hypothesis | 20 Nov 2026 | 7,991 |
| DsDSxUDuXFQ | Zeta Explained | Zeta Explained #125.5: Alpöge (with Claude) Claims Proof of Riemann Hypothesis and GRH | 20 Nov 2026 | 49,736 |
| B6mus94uce4 | Hissera | Riemann Hipotezi Çözüldü mü? , Levent Alpöge ve Claude | 20 Nov 2026 | 24,681 |
| lzXtBlLij_8 | Sitcomexe | An Anthropic mathematician says he and Claude proved the Riemann hypothesis… it's not verified yet | 20 Nov 2026 | 62 |
| MZ_LChGzBSQ | Dylan Bradley | Claude May Have Just Solved Math's Most Famous Problem... | 20 Nov 2026 | 9,427 |
| _FrHwi9ZVtg | Dr. Samuel Allen Alexander | The Riemann Hypothesis has been solved!! Anthropic's Levent Alpöge announces lean verified GRH! | 20 Nov 2026 | 90,543 |
| GXTC-G_oOtQ | World Science Festival | Has AI Solved Math's Pinnacle Problem? , World Science Festival | 20 Nov 2026 | 150,383 |
| sMZMpsHeFKc | Numberphile | The Riemann Hypothesis Falls (reaction) - Numberphile | 20 Nov 2026 | 663,814 |
| V71iiqTfRwg | Oneironaut | It Took 17,000,000 Lines to Test This Hypothesis | 20 Nov 2026 | 214 |
| xjX3jESpZqs | Wes Roth | Claude JUST solved the Riemann Hypothesis... | 21 Nov 2026 | 143,659 |
| p0dPPhzRBm4 | SciencePetr | Did AI Just Prove The Riemann Hypothesis? | 21 Nov 2026 | 42,065 |
| Y8A5L5og_mk | The Math Sorcerer | Riemann Hypothesis Solved by Claude AI? | 20 Nov 2026 | 228,404 |
| P8MJEShDaK4 | Martin Weiss | The Riemann Hypothesis Proof No One Bothered To Read | 20 Nov 2026 | 43,784 |
| j45eJqAi-tw | Dwarkesh Clips | What If AI Proves the Riemann Hypothesis and No One Understands It? – @3blue1brown | 5 Jul 2026 | 42,892 |
| PU1LMVGcyXA | Dwarkesh Clips | Will AI Prove the Riemann Hypothesis Without Understanding It? – Terence Tao | 2 Apr 2026 | 235,844 |

The two Dwarkesh clips were recorded before the announcement. Their captions carry the label “recorded earlier” and the month of publication. Full videos are in `sources/episode2/video/`, and the opening sections of the other videos are in `sources/episode2/heads/`.

## Inserts

Cut points come from Whisper word timestamps and sit just outside the first and last word. Times are positions in the full video.

### Insert A, the news collage, after the cue “Here is how the news sounded.”

Thirteen clips of one to four seconds from thirteen different videos, shown as a mosaic. Clips A1 to A12 take the next free tile in the order of the table, and clip A13 closes the collage on the full screen. The clips are 37 seconds long in their sources and run 28 seconds in the collage because of the speed. The insert runs 31 seconds with its title card and the bell.

| Cut | Source | In | Out | Speaker | Words |
|---|---|---|---|---|---|
| A1 | eyDKuSdB9Tk | 0:01.0 | 0:04.8 | Lektor Lainz | Breaking news! The Riemann hypothesis may have just been proven. |
| A2 | 74e_cdErfvo | 0:11.8 | 0:13.1 | The Pretrained Pod | This is a big one, dude. |
| A3 | DsDSxUDuXFQ | 0:02.0 | 0:03.6 | Zeta Explained | Something remarkable has occurred. |
| A4 | B6mus94uce4 | 0:07.5 | 0:10.0 | Hissera | Riemann hipotezi ispatlandı mı? (Has the Riemann hypothesis been proved?) |
| A5 | lzXtBlLij_8 | 0:00.0 | 0:02.4 | Sitcomexe | We did it! We proved Riemann! |
| A6 | MZ_LChGzBSQ | 0:11.5 | 0:15.3 | Dylan Bradley | I had to run down here. I still have my robe on. |
| A7 | _FrHwi9ZVtg | 1:39.5 | 1:42.3 | Dr. Samuel Allen Alexander | Oh my god, this is historical. |
| A8 | GXTC-G_oOtQ | 0:10.1 | 0:12.4 | Brian Greene | Perhaps one of the greatest breakthroughs of all time. |
| A9 | sMZMpsHeFKc | 1:31.5 | 1:35.8 | Tony Padilla | Do you want to know what my reaction was? Yeah. FFS. |
| A10 | V71iiqTfRwg | 0:07.5 | 0:10.8 | Oneironaut | Four pages, 17 million lines. (sung) |
| A11 | xjX3jESpZqs | 0:21.1 | 0:23.7 | Wes Roth | This can't be real. This has to be fake. |
| A12 | p0dPPhzRBm4 | 5:19.9 | 5:23.7 | SciencePetr | Frankly, I'm having a hard time believing that any of this is real. |
| A13 | Y8A5L5og_mk | 0:15.8 | 0:17.7 | The Math Sorcerer | It is unconfirmed. |

### Insert B, Brian Greene, after the cue “Here is Brian Greene, in his own words.” Audio episode only.

One clip of 37 seconds.

| Cut | Source | In | Out | Speaker | Words |
|---|---|---|---|---|---|
| B1 | GXTC-G_oOtQ | 1:19.0 | 1:56.1 | Brian Greene | The proof is reported to run to something like a quarter of a million pages. So it is not like any human being on planet Earth yet understands it. But my understanding is that the proof has already been run through the automated theorem checker, Lean. And the claim is that the proof has passed. And right now, as I speak, other experts with Lean across the globe, they are doing independent verifications. And who knows? Maybe they will find a problem, a bug. But all vectors seem to be pointing toward the AI proof being correct. |

### Insert C, the voices of caution, after the cue “Here are the voices of caution.”

Five longer statements of 7 to 23 seconds. The clips run 67 seconds and the insert runs 71 seconds.

| Cut | Source | In | Out | Speaker | Words |
|---|---|---|---|---|---|
| C1 | P8MJEShDaK4 | 7:55.7 and 8:30.8 | 7:59.9 and 8:34.1 | Martin Weiss | So in his own account, the proof exists, but we don't understand it. If it compiles and no person read it, is it proved? |
| C2 | p0dPPhzRBm4 | 6:06.6 | 6:21.1 | SciencePetr | I'd be 98 or 99% certain. Lean is a robust proof checker, Dr. Maynard said, but added, you have to be a little bit careful about making sure that a Lean verification is proving the thing you want it to be proving. |
| C3 | j45eJqAi-tw | 2:14.3 | 2:26.4 | Grant Sanderson, recorded earlier | And then if the nature of the progress was just like raw hustle, right? It's just this super long thing, no new theories, but it's just a long, long, long chain of reasoning. Then you would have that worry of, okay, there's this whole digestion process. |
| C4 | PU1LMVGcyXA | 5:56.6 | 6:19.2 | Terence Tao, recorded earlier | Once you actually have one proof, we actually have a lot of tools now to deconstruct it and interpret it. It's a very nascent area of science or mathematics. But I'm not as worried about, you know, so some people are concerned, what if the Riemann hypothesis is proved with a completely incomprehensible proof? I think once you have the artifact of a proof, we can do a lot of analysis on it. |
| C5 | sMZMpsHeFKc | 10:06.1 | 10:16.0 | Tony Padilla | Now we're entering a new age. What are going to be the things that we need to dream about? Is it even going to be us that are dreaming about them? Or is it just the AI that dreams about them? |

### Insert D, the closing sting, after the cue “Brian Greene summed up the mood in three words.” Audio episode only.

One clip of 3 seconds.

| Cut | Source | In | Out | Speaker | Words |
|---|---|---|---|---|---|
| D1 | GXTC-G_oOtQ | 2:50.8 | 2:53.8 | Brian Greene | Exciting and terrifying. |

## Notes for the edit

- The same video may appear in the news collage and in the closing collage, and it does so with different passages. Numberphile and SciencePetr are in both.
- The Numberphile picture is 640 by 360 and is scaled up, because YouTube refused the larger formats on the day of the download. The opening sections of the further videos have the same size.
- Cut A4 is in Turkish, and its caption gives the English meaning.
- Cut A10 is a sung line from a song about the proof.
- In cut A7 the speaker says “solved” as a plain fact, and the hosts hedge the status right after the collage.
- In cut C2 the speaker reads words of James Maynard from the New York Times, and the caption says so.
- Brian Greene says “a quarter of a million pages” in insert B. The hosts explain after the clip that this number is the printout and that the published code has about 17.4 million lines.
- The World Science Festival clips keep the festival's own logo visible in the corner.

## Assembly

1. Put the source videos into `sources/episode2/video/` and the opening sections into `sources/episode2/heads/`, each as `<id>.mp4`.
2. Run `python3 video/episode2_collage.py` to cut and caption the inserts into `build/episode2/`. An insert with `"mosaic": true` in `inserts.json` is built as a mosaic of up to 16 tiles with one time range per clip. The header of the script lists the fields that set its speeds, the tails of the voices, the closing clip and the whoosh.
3. Run `scripts/episode2_run.sh v6` to upload the scripts, generate both narrations, download them, transcribe them with Whisper, check them and place the inserts. The round name is free to choose.
4. Read the check reports in `transcripts/episode2/<round>/` and the transcripts next to them before using a round.
5. Read the slides of the video as pictures as well, because the transcript only covers the narration. `video/episode2_slide_fix.py` replaces a wrong slide.
6. Put passages to cut into an edit list and pass it to `video/episode2_assemble.py` as its last argument. The lists of each round are in `docs/episode2/notebooklm/`.

## Credits lines

Reaction excerpts come from the YouTube videos listed above and are used for commentary and education. All rights remain with their makers. The narration was made with NotebookLM from an original script.
