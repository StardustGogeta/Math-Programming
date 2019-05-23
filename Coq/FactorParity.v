Require Import Bool Setoid Arith Classical_Prop (* Excluded middle *) Omega BasicArithmetic.
(* Omega makes arithmetic relatively easy to handle *)

Definition EvenParity x := exists n, Nat.divide (4^n) x /\ ~Nat.Even (x/(4^n)).
Definition OddParity x := ~EvenParity x.

(* Lemma twoAsFactor_implies_even: forall x, (exists y, y * 2 = x) <-> Nat.Even x.
Proof. (* TODO: Use the identities used here in order to remove nonzero condition in div_implies_mul *)
  unfold iff. intros. refine (conj _ _).
  intros. destruct H as [A B].
  refine (ex_intro _ A _). (* I came upon this by mistake *)
  rewrite Nat.mul_comm. symmetry. exact B. intros.
  remember (x/2) as y.
  cut (Nat.divide 2 x). intro A.
  cut (2 * y = 2 * (x / 2)). intro B.
  cut (2 * y = x * 2 / 2). intro C.
  rewrite Nat.div_mul in C.
  refine (ex_intro _ y _). rewrite Nat.mul_comm. exact C. omega.
  Focus 2.
  rewrite Nat.mul_cancel_l. exact Heqy. omega.
  rewrite B. cut (x=2*(x/2)). intro D.
  Focus 3.
  apply even_div_2. apply H.
  Focus 2.
  rewrite Nat.div_exact.
  apply Nat.mod_divide. omega. apply even_div_2. apply H. omega.
  rewrite <- D. rewrite Nat.div_mul. trivial. omega.
Qed. *)

Theorem not_even_imp_odd: forall x, ~Nat.Even x -> Nat.Odd x.
Proof.
  intros. cut (Nat.Even x \/ Nat.Odd x). intro. destruct H0.
  contradiction. apply H0. apply Nat.Even_or_Odd.
Qed.

Theorem not_odd_imp_even: forall x, ~Nat.Odd x -> Nat.Even x.
Proof.
  intros. cut (Nat.Even x \/ Nat.Odd x). intro. destruct H0.
  apply H0. contradiction. apply Nat.Even_or_Odd.
Qed.

Theorem eq_imp_eq_fact_parity: forall x y, x = y -> (EvenParity x <-> EvenParity y) /\ (OddParity x <-> OddParity y).
Proof.
  intros. rewrite H. unfold iff. auto.
Qed.

Theorem greater_pwr_divides_smaller_pwr: forall a b c, c <= b -> Nat.divide (a ^ c) (a ^ b).
Proof.
  intros.
  remember (b-c) as d.
  cut (c + d = b). intro.
  rewrite <- H0. rewrite Nat.pow_add_r.
  apply Nat.divide_factor_l.
  rewrite Heqd. apply le_plus_minus_r. apply H.
Qed.

Theorem mult_two_even_to_odd_parity: forall x, EvenParity x -> OddParity (2*x).
Proof.
  unfold EvenParity, OddParity. intros.
  unfold EvenParity, not. intros.
  destruct H, H0. destruct H, H0.
  apply not_even_imp_odd in H1. apply H2.
  remember (4 ^ x0) as L.
  remember (4 ^ x1) as M.
  remember (x/M) as M2.
  refine (ex_intro _ M2 _).
  rewrite HeqM2.
  apply Nat.divide_div_mul_exact.
  rewrite HeqM. apply Nat.pow_nonzero. omega.
  apply (Nat.divide_trans M L x).
  Focus 2. apply H.
  cut (x1 <= x0). intro exp_ineq.
  rewrite HeqL, HeqM. apply greater_pwr_divides_smaller_pwr.
  apply exp_ineq.
  apply not_even_imp_odd in H2.
  


