"use client";
import { useState } from "react";
import { nextInterval } from "../../lib/scheduler";

const cards = [{ word: "manzana", picture: "/cards/apple.png" }];

export default function Flashcards() {
  const [step, setStep] = useState(0);
  const card = cards[0];
  return (
    <section>
      <h1>Flashcards</h1>
      <img src={card.picture} width={240} height={240} />
      <p>{card.word}</p>
      <button onClick={() => setStep(step + 1)}>I knew it</button>
      <button onClick={() => setStep(0)}>Show again</button>
      <p>Next review in {nextInterval(step, true)} days</p>
    </section>
  );
}
