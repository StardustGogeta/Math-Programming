Require Import Bool.
Require Import Setoid.
Require Import Arith.
Require Import Omega.
(* Omega makes arithmetic relatively easy to handle *)

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

SearchAbout Nat.modulo.
SearchAbout Nat.divide.

Lemma y_divides_x_plus_y: forall x y, Nat.divide y (x+y) -> Nat.divide y x.
Proof.
  intros.
  cut (Nat.divide y (x+y) -> Nat.divide y y -> Nat.divide y x).
  intros.
  exact (H0 H (Nat.divide_refl y)).
  cut ((x + y) - y = x).
  intros.
  rewrite <- H0.
  apply Nat.divide_sub_r.
  exact H1. exact H2. omega.
Qed.

(* Nat.divide_add_r: forall n m p : nat,
  Nat.divide n m -> Nat.divide n p -> Nat.divide n (m + p) *)
Theorem evenPlusTwoIsEven: forall x, x mod 2 = 0 -> (S (S x)) mod 2 = 0.
Proof.
  intros.
  rewrite Nat.mod_divide in H.
  rewrite <- Nat.add_1_r.
  rewrite <- Nat.add_1_r.
  rewrite Nat.mod_divide.
  cut (x + 1 + 1 = x + 2).
  intros. rewrite H0.
  apply Nat.divide_add_r.
  exact H. apply Nat.divide_refl.
  omega. omega. omega.
Qed.
