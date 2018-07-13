Require Import Classical_Prop Omega BasicArithmetic.
Create HintDb arithHelp.
Hint Resolve Nat.mul_assoc Nat.mul_comm Nat.mul_shuffle0 Nat.mul_shuffle1 : arithHelp.

Theorem weak_sqrt2_is_irrational: forall p q, coprime p q -> q <> 0 -> p * p <> q * q * 2.
Proof.
  unfold not. intros p q COPRIME q_neq_0 main.
  remember (p*p) as p_sq.
  remember (q*q) as q_sq.
  cut (Nat.Even p_sq). intro p_sq_even.
  2: {
    refine (ex_intro _ q_sq _).
    rewrite Nat.mul_comm. exact main. }
  rewrite Heqp_sq in p_sq_even.
  apply evenSquare_implies_even in p_sq_even.
  cut (p <> 0). intro p_neq_0.
  2: {
    intro p0. apply q_neq_0. rewrite p0 in Heqp_sq. rewrite Heqp_sq in main. simpl in main.
    symmetry in main. rewrite Nat.mul_comm in main. apply Nat.mul_eq_0_r in main.
    rewrite Heqq_sq in main. apply Nat.eq_square_0. exact main. omega. }
  assert (p_even := p_sq_even). destruct p_sq_even as [k k_mul].
  rewrite Nat.mul_comm in k_mul.
  rewrite Heqp_sq in main. rewrite Heqq_sq in main. rewrite k_mul in main.
  rewrite Nat.mul_assoc in main. apply Nat.mul_cancel_r in main.
  rewrite Nat.mul_shuffle0 in main.
  rewrite <- Heqq_sq in main. cut (Nat.Even q). intro q_even.
  2: {
    apply evenSquare_implies_even. rewrite <- Heqq_sq.
    refine (ex_intro _ (k*k) _). symmetry. rewrite Nat.mul_comm. exact main. }
  cut (~coprime p q). intro NOT_COPRIME.
  2: apply (evens_not_coprime p q (conj p_even q_even)).
  contradiction. omega.
Qed.

Theorem strong_sqrt2_is_irrational: forall p q, q <> 0 -> p * p <> q * q * 2.
Proof.
  intros.
  cut (coprime p q \/ ~coprime p q). intro.
  2: apply classic.
  destruct H0.
  apply weak_sqrt2_is_irrational. exact H0. exact H.
  (* If p and q are not coprime, this implies that there exists
  a coprime a and b such that a*a = b*b*2, which is false *)
  cut (exists a b, coprime a b /\ p * b = a * q). intro. destruct H1. destruct H1. destruct H1.
  cut (x0 <> 0). intro x0_neq_0.
  2: {
    intro. apply H. rewrite H3 in H2. rewrite Nat.mul_0_r in H2.
    apply (Nat.eq_mul_0_r x q). symmetry. exact H2.
    unfold coprime in H1. rewrite H3 in H1.
    rewrite Nat.gcd_0_r in H1. rewrite H1. omega. }
  intro. cut (p * p * x0 * x0 = x * x * q * q). intro.
  rewrite H3 in H4.
  cut (q * q * 2 * x0 * x0 = x0 * x0 * 2 * q * q). intro.
  rewrite H5 in H4. rewrite Nat.mul_cancel_r in H4. rewrite Nat.mul_cancel_r in H4.
  symmetry in H4. cut (x * x <> x0 * x0 * 2).
  contradiction.
  apply (weak_sqrt2_is_irrational x x0 H1 x0_neq_0). exact H. exact H.
  remember (q*q) as q_sq. remember (x0*x0) as x0_sq. rewrite <- Nat.mul_assoc. rewrite <- Heqx0_sq.
  rewrite <- Nat.mul_assoc. rewrite <- Nat.mul_assoc. rewrite <- Heqq_sq. rewrite Nat.mul_comm. auto with arithHelp.
  rewrite Nat.mul_comm. rewrite Nat.mul_assoc. rewrite Nat.mul_assoc. rewrite Nat.mul_comm in H2. rewrite H2. rewrite Nat.mul_shuffle0.
  rewrite <- Nat.mul_assoc. rewrite H2. rewrite Nat.mul_shuffle1. auto with arithHelp.
  apply fraction_simplification. exact H.
Qed.
