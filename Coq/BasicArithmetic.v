Require Import Bool.
Require Import Setoid.
Require Import Omega.
(* This makes arithmetic relatively easy to handle *)

Lemma zeroX_is_zero: (forall x, 0 * x = 0).
Proof.
  trivial.
Qed.

Lemma Xzero_is_zero: (forall x, x * 0 = 0).
Proof.
  intros.
  omega.
  (* Alternatively...
  elim x.
    trivial.
    trivial. *)
Qed.

Lemma subtractOne: (forall a b, S(a) = S(b) <-> a = b).
Proof.
  intros.
  unfold iff.
  refine (conj _ _). intro f. injection f. trivial.
  intro. f_equal. exact H.
Qed.

Theorem distributive: (forall a x y, a*(x+y)=a*x+a*y).
Proof.
  intros.
  elim a.
    reflexivity.
    elim x.
      elim y.
        trivial.
        simpl. intros.
        rewrite Xzero_is_zero.
        trivial. intros. simpl.
        simpl in H0. rewrite H0.
        omega.
Qed.
