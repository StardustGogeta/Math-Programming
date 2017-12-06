Require Import Classical_Prop Omega BasicArithmetic.

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

Theorem strong_sqrt2_is_irrational: forall p q, q <> 0 -> p * p <> q * q * 2.
Proof.
  intros.
  cut (coprime p q \/ ~coprime p q). intro.
  Focus 2. apply classic.
  destruct H0.
  apply weak_sqrt2_is_irrational. exact H0. exact H.
  (* If p and q are not coprime, this implies that there exists
  a coprime a and b such that a*a = b*b*2, which is false *)
  cut (exists a b, coprime a b /\ p * b = a * q). intro. destruct H1. destruct H1. destruct H1.
  cut (x0 <> 0). intro x0_neq_0.
  Focus 2.
    intro. rewrite H3 in H2. rewrite Nat.mul_0_r in H2.
    rewrite <- H3 in H2. cut (Nat.divide x x0). intro.
    cut (~coprime x x0). contradiction.
    rewrite H2 in H3. apply Nat.eq_mul_0_l in H3.
    rewrite H3 in H2. rewrite Nat.mul_0_l in H2. rewrite H2. rewrite H3.
    apply not_coprime_0_0. exact H. refine (ex_intro _ q _). rewrite Nat.mul_comm. exact H2.
  intro. cut (p * p * x0 * x0 = x * x * q * q). intro.
  rewrite H3 in H4.
  cut (q * q * 2 * x0 * x0 = x0 * x0 * 2 * q * q). intro.
  rewrite H5 in H4. rewrite Nat.mul_cancel_r in H4. rewrite Nat.mul_cancel_r in H4.
  symmetry in H4. cut (x * x <> x0 * x0 * 2).
  contradiction.
  apply weak_sqrt2_is_irrational. exact H1. exact x0_neq_0.
  exact H. exact H.
  rewrite Nat.mul_comm. cut (x0 * x0 * 2 * q * q = x0 * (x0 * 2 * q * q)). intro. rewrite H5. rewrite Nat.mul_cancel_l.
  rewrite Nat.mul_comm. cut (x0 * 2 * q * q = x0 * (2 * q * q)). intro. rewrite H6. rewrite Nat.mul_cancel_l.
  rewrite Nat.mul_shuffle0. rewrite Nat.mul_cancel_r. rewrite Nat.mul_comm. trivial.
  exact H. exact x0_neq_0.
  rewrite Nat.mul_assoc. rewrite Nat.mul_assoc. reflexivity. exact x0_neq_0.
  rewrite Nat.mul_assoc. rewrite Nat.mul_assoc. rewrite Nat.mul_assoc. reflexivity.
  rewrite Nat.mul_comm. rewrite Nat.mul_assoc. rewrite Nat.mul_shuffle0. rewrite Nat.mul_shuffle3.
  rewrite Nat.mul_assoc. rewrite Nat.mul_assoc. rewrite H2. rewrite Nat.mul_comm. rewrite Nat.mul_shuffle3. rewrite H2.
  rewrite Nat.mul_assoc. rewrite Nat.mul_cancel_r. rewrite Nat.mul_shuffle0. reflexivity. exact H.
  apply fraction_simplification. exact H.
Qed.
