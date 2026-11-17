"""Shared locations for the build.

Every path is resolved from the repository itself, so the scripts run from any
working directory on any machine. Two environment variables move the folders
that hold large local files:

  RIEMANN_SOURCES  local media (default: <repo>/sources, git-ignored)
  RIEMANN_BUILD    rendered output (default: <repo>/build, git-ignored)
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO = ROOT / "video"
DATA = ROOT / "data" / "zeta_data.json"
ART = VIDEO / "art"
FONTS = VIDEO / "fonts"

SOURCES = Path(os.environ.get("RIEMANN_SOURCES", ROOT / "sources")).expanduser()
BUILD = Path(os.environ.get("RIEMANN_BUILD", ROOT / "build")).expanduser()

# Interview excerpts cut from the World Science Festival video (clip01.mp4 … clip10.mp4)
INTERVIEW_CLIPS = SOURCES / "clips"
# NotebookLM narration videos, used for their audio track
NARRATION_MAIN = SOURCES / "Predicting_Primes.mp4"
NARRATION_EX = SOURCES / "The_Explainer.mp4"


def build_dir(name):
    """Return BUILD/<name>, creating it on first use."""
    p = BUILD / name
    p.mkdir(parents=True, exist_ok=True)
    return p


def need(path):
    """Return path as a string, or stop with a clear message when the file is missing."""
    p = Path(path)
    if not p.exists():
        raise SystemExit(f"Missing input file: {p}\nSee README.md, section 'Media that is not in git'.")
    return str(p)
