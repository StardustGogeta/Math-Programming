Require Import Bool.
Require Import Setoid.
Require Import Arith.
Require Import Classical_Prop. (* Excluded middle *)
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
  apply Nat.mul_add_distr_l.
Qed.

(*
SearchAbout Nat.modulo.
SearchAbout Nat.divide.
*)

Lemma y_divides_x_plus_y: forall x y, Nat.divide y (x+y) <-> Nat.divide y x.
Proof.
  unfold iff. intros. refine (conj _ _). intros.
  cut (Nat.divide y (x+y) -> Nat.divide y y -> Nat.divide y x).
  intros.
  exact (H0 H (Nat.divide_refl y)).
  cut ((x + y) - y = x).
  intros.
  rewrite <- H0.
  apply Nat.divide_sub_r.
  exact H1. exact H2. omega.
  intros.
  apply Nat.divide_add_r.
  exact H. apply Nat.divide_refl.
Qed.

(* Nat.divide_add_r: forall n m p : nat,
  Nat.divide n m -> Nat.divide n p -> Nat.divide n (m + p) *)
Corollary evenPlusTwoIsEven: forall x, x mod 2 = 0 -> (S (S x)) mod 2 = 0.
Proof.
  intros.
  rewrite Nat.mod_divide in H.
  rewrite <- Nat.add_1_r.
  rewrite <- Nat.add_1_r.
  rewrite Nat.mod_divide.
  cut (x + 1 + 1 = x + 2).
  intros. rewrite H0.
  apply y_divides_x_plus_y.
  exact H. omega. omega. omega.
Qed.

Theorem evenPlusTwoIsEven_alternate: forall x, Nat.even x = Nat.even (S(S x)).
Proof.
  apply Nat.even_succ_succ.
Qed.

(* T1 is not my code *)
Theorem T1 : forall p q, (~q->~p)->(p->q).
Proof.
intros.
apply NNPP.
intro.
apply H in H1.
contradiction.
Qed.

Lemma divides_implies_notZero: forall a b, b <> 0 -> Nat.divide a b -> a <> 0.
Proof.
  unfold not. intros.
  apply H.
  rewrite H1 in H0.
  apply Nat.divide_0_l.
  exact H0.
Qed.

Lemma div_implies_mul: forall a b c, b <> 0 -> Nat.divide c b -> a = b / c -> c * a = b.
Proof.
  intros. rewrite H1.
  cut (b mod c = 0). intro.
  cut (c * (b/c) + 0 = c * (b/c)). intro.
  - rewrite <- H3. rewrite <- H2. symmetry.
    apply Nat.div_mod. exact (divides_implies_notZero c b H H0).
  - apply Nat.add_0_r.
  - apply Nat.mod_divide. exact (divides_implies_notZero c b H H0). exact H0.
Qed.

Lemma neq_refl: forall a b : nat, a <> b -> b <> a.
Proof.
  unfold not. intros.
  apply H. symmetry.
  exact H0.
Qed.

Lemma divide_mul: forall a b c d, 0 < b -> d <> 0 -> Nat.divide a b -> Nat.divide c d -> Nat.divide (a*c) (b*d).
Proof.
  intros a b c d B D a_div_b c_div_d.
  remember (b/a) as x.
  cut (a*x = b). intro ax_b.
  rewrite <- ax_b.
  remember (d/c) as y.
  cut (c*y = d). intro cy_d.
  rewrite <- cy_d.
  cut (x*y*(a*c)=a*x*(c*y)). intro xyac_axcy.
  rewrite <- xyac_axcy.
  apply Nat.divide_factor_r.
  rewrite Nat.mul_comm.
  apply Nat.mul_shuffle1.
  - apply (div_implies_mul y d c D c_div_d Heqy).
  - apply Nat.lt_neq in B. apply neq_refl in B.
    apply (div_implies_mul x b a B a_div_b Heqx).
Qed.

Corollary squaredFactor_divides_square: forall x y, 0 < x -> Nat.divide y x -> Nat.divide (y*y) (x*x).
Proof.
  intros.
  apply (divide_mul y x y x H (neq_refl 0 x (Nat.lt_neq 0 x H)) H0 H0).
Qed.

(*
Theorem sqrt2_is_irrational: forall p q, q <> 0 -> p * p <> q * q * 2.
Proof.
  intros.
  cut (Nat.divide 2 p).
*)
