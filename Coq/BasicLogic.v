Require Import Bool.

(* Ideas at https://en.wikipedia.org/wiki/Propositional_calculus#Basic_and_derived_argument_forms *)

Theorem deMorganFirst: (forall A B, Is_true (negb (orb A B)) <-> Is_true (andb (negb A) (negb B))).
Proof.
  intros.
  unfold iff.
  refine (conj _ _).
    intro.
    destruct A, B.
    case H. case H. case H. exact I.

    intro.
    destruct A, B.
    case H. case H. case H. exact I.
Qed.

Theorem deMorganSecond: (forall A B, Is_true (negb (andb A B)) <-> Is_true (orb (negb A) (negb B))).
Proof.
  intros.
  unfold iff.
  refine (conj _ _).
    intro.
    destruct A, B.
    case H. exact I. exact I. exact I.

    intro.
    destruct A, B.
    case H. exact I. exact I. exact I.
Qed.

Theorem materialImplication: (forall p q : bool, (Is_true p -> Is_true q) <-> Is_true (orb (negb p) q)).
Proof.
  intros.
  unfold not, iff.
  refine (conj _ _).
    case p, q.
      simpl. trivial.
      simpl. intros. case H. exact I.
      simpl. trivial.
      simpl. trivial.
    case p, q.
      simpl. trivial.
      simpl. trivial.
      simpl. trivial.
      simpl. trivial.
Qed.

Theorem negb_is_not : (forall a, Is_true (negb a) <-> (~(Is_true a))).
Proof.
  intros.
  unfold iff, not.
  case a.
  simpl. refine (conj _ _).
    trivial.
    intros. case H. exact I.
  simpl. refine (conj _ _).
    trivial.
    trivial.
Qed.
