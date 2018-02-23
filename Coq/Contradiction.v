Require Import BasicArithmetic Classical_Prop Omega.

(* Taken from http://www.math-cs.gordon.edu/courses/mat231/notes/proof-contradiction.pdf *)
Theorem practice_1: forall n, Nat.Odd (n^3+5) -> Nat.Even n.
Proof.
  intros. cut (~Nat.Odd n).
  Focus 2. intro. rewrite <- Nat.odd_spec in H. rewrite Nat.odd_add in H.
  rewrite <- Nat.odd_spec in H0. rewrite Nat.odd_pow in H. rewrite H0 in H. discriminate. omega.
  cut (Nat.Even n \/ Nat.Odd n). intros.
  destruct H0. exact H0. contradiction. apply Nat.Even_or_Odd.
Qed.

Lemma flip_ge: forall a b, a >= b -> b <= a.
Proof.
  easy.
Qed.

Theorem practice_2: forall a b, a + b >= 19 -> a >= 10 \/ b >= 10.
Proof.
  intros. omega. (* I can't believe it. *)
Qed.
