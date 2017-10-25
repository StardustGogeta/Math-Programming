Require Import Bool.

Theorem deMorganFirst: (forall A B, Is_true (negb (orb A B)) <-> Is_true (andb (negb A) (negb B))).
Proof.
  intros.
  unfold iff.
  refine (conj _ _).
    intros F.
    destruct A, B.
    exact F.
    exact F.
    exact F.
    exact F.

    intros T.
    destruct A, B.
    exact T.
    exact T.
    exact T.
    exact T.
Qed.

Theorem deMorganSecond: (forall A B, Is_true (negb (andb A B)) <-> Is_true (orb (negb A) (negb B))).
Proof.
  intros.
  unfold iff.
  refine (conj _ _).
    intros F.
    destruct A, B.
    exact F.
    exact F.
    exact F.
    exact F.

    intros T.
    destruct A, B.
    exact T.
    exact T.
    exact T.
    exact T.
Qed.
