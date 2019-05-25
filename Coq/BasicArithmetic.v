Require Import Bool Setoid Arith Classical_Prop (* Excluded middle *) Omega.
(* Omega makes arithmetic relatively easy to handle *)

(* If I ever need fancy notation:
Notation "A | B" := (Nat.divide A B) (at level 0).
*)

Lemma contrapositive: forall P Q : Prop, (P -> Q) -> (~Q -> ~P).
Proof.
  intuition.
Qed.

Lemma zeroX_is_zero: (forall x, 0 * x = 0).
Proof.
  trivial.
Qed.

Lemma Xzero_is_zero: (forall x, x * 0 = 0).
Proof.
  intros. omega.
Qed.

Lemma subtractOne: (forall a b, S(a) = S(b) <-> a = b).
Proof.
  intros. unfold iff.
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
Proof. (* TODO: Remove the nonzero condition, if possible *)
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
  apply Nat.divide_factor_r. ring.
  - apply (div_implies_mul y d c D c_div_d Heqy).
  - apply Nat.lt_neq in B. apply neq_refl in B.
    apply (div_implies_mul x b a B a_div_b Heqx).
Qed.

Corollary squaredFactor_divides_square: forall x y, 0 < x -> Nat.divide y x -> Nat.divide (y*y) (x*x).
Proof.
  intros.
  apply (divide_mul y x y x H (neq_refl 0 x (Nat.lt_neq 0 x H)) H0 H0).
Qed.

Lemma evenSquare_implies_even: forall x, Nat.Even (x*x) -> Nat.Even x.
Proof.
  intros. rewrite <- Nat.pow_2_r in H. apply Nat.even_spec in H.
  rewrite Nat.even_pow in H. apply Nat.even_spec. exact H. omega.
Qed.

Lemma twoAsFactor_implies_even: forall x, (exists y, x = y * 2) <-> Nat.Even x.
Proof.
  unfold Nat.Even. intuition.
  destruct H. refine (ex_intro _ x0 _).
  rewrite Nat.mul_comm. auto.
  destruct H. refine (ex_intro _ x0 _).
  rewrite Nat.mul_comm. auto.
Qed.

(* There is a massive schism between the Nat.divide, Nat.modulo, and Nat.even / Nat.Even
  parts of Coq, making it incredibly difficult to switch between them. It was a miracle
  that I could finally achieve this without setting a new axiom. *)
Theorem even_div_2: forall x, Nat.Even x <-> Nat.divide 2 x.
Proof.
  unfold Nat.divide. symmetry.
  apply twoAsFactor_implies_even.
Qed.

(* The following use a worse definition of coprimality that forced me to use an axiom to complete the proof:

Definition coprime x y := (forall a, a > 1 -> Nat.divide a x -> ~ Nat.divide a y) /\ (x <> 0) /\ (y <> 0).

Axiom coprime_reduction: forall p q : nat, exists a b, coprime a b /\ p * b = a * q.

Lemma coprime_comm: forall x y, coprime x y -> coprime y x.
Proof.
  unfold coprime. intros. refine (conj _ _). destruct H. Focus 2. destruct H. destruct H0. exact (conj H1 H0).
  intros. specialize H with a. intro. apply H. exact H1. exact H3. exact H2.
Qed.

Lemma not_coprime_0_0: ~coprime 0 0.
Proof.
  unfold coprime, not. intros. destruct H. destruct H0. destruct H0. trivial.
Qed.

Theorem evens_not_coprime: forall x y, Nat.Even x /\ Nat.Even y -> ~coprime x y.
Proof.
  unfold not, coprime. intros.
  rewrite even_div_2 in H. rewrite even_div_2 in H.
  destruct H.
  cut (~Nat.divide 2 y). intro.
  contradiction. (* This is where the magic happens *)
  apply H0. omega. exact H.
Qed.

*)

Definition coprime x y := Nat.gcd x y = 1.

Lemma coprime_comm: forall x y, coprime x y -> coprime y x.
Proof.
  unfold coprime. intros. rewrite Nat.gcd_comm. exact H.
Qed.

Lemma not_coprime_0_0: ~coprime 0 0.
Proof.
  unfold coprime, not. rewrite Nat.gcd_0_r. trivial. discriminate.
Qed.

Theorem evens_not_coprime: forall x y, Nat.Even x /\ Nat.Even y -> ~coprime x y.
Proof.
  unfold not, coprime. intros.
  rewrite even_div_2 in H. rewrite even_div_2 in H.
  rewrite <- Nat.gcd_divide_iff in H. rewrite H0 in H.
  apply Nat.divide_1_r in H. discriminate.
Qed.

Theorem fraction_simplification: forall p q : nat, q <> 0 -> exists a b, coprime a b /\ p * b = a * q.
Proof.
  intros. remember (Nat.gcd p q) as f.
  refine (ex_intro _ (p/f) _). refine (ex_intro _ (q/f) _). refine (conj _ _).
  Focus 2. rewrite Heqf. rewrite Nat.gcd_div_swap. trivial.
  unfold coprime. apply Nat.gcd_div_gcd. intro.
  rewrite H0 in Heqf. symmetry in Heqf. apply Nat.gcd_eq_0_r in Heqf.
  contradiction. exact Heqf.
Qed.
