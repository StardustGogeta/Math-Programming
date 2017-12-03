Require Import Bool.
Require Import Setoid.
Require Import Arith.
Require Import Classical_Prop. (* Excluded middle *)
Require Import Omega.
(* Omega makes arithmetic relatively easy to handle *)

(* If I ever need fancy notation:
Notation "A | B" := (Nat.divide A B) (at level 0).
*)

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

SearchAbout Nat.even.
SearchAbout Nat.divide.
(*
Nat.even_add_mul_2: forall n m : nat, Nat.even (n + 2 * m) = Nat.even n
Nat.even_0: Nat.even 0 = true
Nat.even_spec: forall n : nat, Nat.even n = true <-> Nat.Even n
Nat.even_mul:
  forall n m : nat, Nat.even (n * m) = Nat.even n || Nat.even m
orb_diag: forall b : bool, b || b = b
Nat.divide_factor_r: forall n m : nat, Nat.divide n (m * n)
*)

Lemma evenSquare_implies_even: forall x, Nat.Even (x*x) -> Nat.Even x.
Proof.
  (* Maybe use Nat.even_pow instead? *)
  intros. apply Nat.even_spec in H.
  rewrite Nat.even_mul in H.
  rewrite orb_diag in H.
  apply Nat.even_spec. exact H.
Qed.

(* There is a massive schism between the Nat.divide, Nat.modulo, and Nat.even / Nat.Even
  parts of Coq, making it incredibly difficult to switch between them. It was a miracle
  that I could finally achieve this without setting a new axiom. *)
Theorem even_div_2: forall x, Nat.Even x <-> Nat.divide 2 x.
Proof.
  intros. unfold iff. refine (conj _ _). intros.
  destruct H. rewrite H. apply Nat.divide_factor_l.
  intros. destruct H. rewrite <- Nat.even_spec.
  rewrite H. rewrite <- Nat.even_0.
  cut (x0 * 2 = 0 + x0 * 2). intro. rewrite H0.
  rewrite Nat.mul_comm.
  SearchAbout Nat.even.
  rewrite Nat.even_add_mul_2. trivial. omega.
Qed.

SearchAbout Nat.divide.
Lemma twoAsFactor_implies_even: forall x, x <> 0 -> (exists y, y * 2 = x) <-> Nat.Even x.
Proof.
  unfold iff. intros. refine (conj _ _).
  intros. destruct H0 as [A B].
  refine (ex_intro _ A _). (* I came upon this by mistake *)
  rewrite Nat.mul_comm. symmetry. exact B.
  intros.
  remember (x/2) as y.
  apply div_implies_mul in Heqy.
  refine (ex_intro _ y _). rewrite Nat.mul_comm. exact Heqy.
  exact H. apply even_div_2. exact H0.
Qed.

Definition coprime x y := forall a, a <> 1 -> Nat.divide a x -> ~ Nat.divide a y.

Theorem evens_not_coprime: forall x y, Nat.Even x /\ Nat.Even y -> ~coprime x y.
Proof.
  unfold not, coprime. intros.
  rewrite even_div_2 in H. rewrite even_div_2 in H.
  destruct H.
  cut (~Nat.divide 2 y). intro.
  contradiction. (* This is where the magic happens *)
  apply H0. omega. exact H.
Qed.

(*
  There is a major flaw with the following proof, so far:
  this is only shown to hold for rationals with coprime numerators and denominators.
*)
Theorem weak_sqrt2_is_irrational: forall p q, coprime p q -> q <> 0 -> p * p <> q * q * 2.
Proof.
  unfold not. intros p q COPRIME q_neq_0 main.
  remember (p*p) as p_sq.
  remember (q*q) as q_sq.
  cut (Nat.Even p_sq). intro p_sq_even.
  Focus 2. 
    apply twoAsFactor_implies_even.
    unfold not. intro. apply q_neq_0.
    cut (q_sq = 0). intro. rewrite Heqq_sq in H0.
    apply Nat.eq_square_0. exact H0.
    rewrite H in main. symmetry. cut (0 * 2 = q_sq * 2).
    apply Nat.mul_cancel_r. omega. exact main.
    refine (ex_intro _ q_sq _).
    symmetry. exact main.
  rewrite Heqp_sq in p_sq_even.
  apply evenSquare_implies_even in p_sq_even.
  remember (p/2) as k.
  apply even_div_2 in p_sq_even.
  rename p_sq_even into p_even.
  cut (p <> 0). intro p_neq_0.
  Focus 2.
    intro p0. apply q_neq_0. rewrite p0 in Heqp_sq. rewrite Heqp_sq in main.
    simpl in main. rewrite Heqq_sq in main. cut (0 * 2 = q * q * 2). intro.
    apply Nat.mul_cancel_r in H. symmetry in H. rewrite Nat.eq_square_0 in H. exact H.
    omega. rewrite <- main. omega.
  cut (2 * k = p). intro k_mul.
  Focus 2.
    exact (div_implies_mul k p 2 p_neq_0 p_even Heqk).
  rewrite Nat.mul_comm in k_mul.
  rewrite Heqp_sq in main. rewrite Heqq_sq in main. rewrite <- k_mul in main.
  SearchAbout Nat.mul.
  rewrite Nat.mul_assoc in main. apply Nat.mul_cancel_r in main.
  rewrite Nat.mul_shuffle0 in main.
  rewrite <- Heqq_sq in main. cut (Nat.Even q). intro q_even.
  Focus 2.
    apply evenSquare_implies_even. rewrite <- Heqq_sq.
    apply twoAsFactor_implies_even. intro N. apply q_neq_0.
    rewrite <- Nat.eq_square_0. rewrite <- Heqq_sq. exact N.
    refine (ex_intro _ (k*k) _). exact main.
  apply even_div_2 in p_even.
  cut (~coprime p q). intro NOT_COPRIME.
  Focus 2.
    apply (evens_not_coprime p q (conj p_even q_even)).
  contradiction. omega.
Qed.
