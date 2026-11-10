// Spaced-repetition scheduler, adapted from an open-source flashcard app.
// SPDX-License-Identifier: AGPL-3.0-or-later
// Copyright (C) the original authors.

const STEPS_DAYS = [1, 3, 7, 14, 30];

export function nextInterval(step: number, remembered: boolean): number {
  if (!remembered) return 0;
  return STEPS_DAYS[Math.min(step, STEPS_DAYS.length - 1)];
}
