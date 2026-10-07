---
name: recover
description: Revive after a session limit — interrupted work reruns and resumes rather than restarting.
---

Load and follow the [Mops skill](../mops/SKILL.md), executing
its `/multica-team:recover` flow. Revive after limits: rerun interrupted in_progress/in_review, revive marker-less cancels.
The reset is a known moment, so **the resume can be scheduled** rather than waited for — one
shot, after the reset, and the trigger is deleted once it fires.
