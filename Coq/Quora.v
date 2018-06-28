Require Import Arith.
Require Import Omega.
Require Import BasicArithmetic.

(* Problem taken from https://www.quora.com/How-do-I-prove-by-induction-that-2-n+2-+-3-2n+1-is-divisible-by-7 *)
Theorem quora1: forall n : nat, (2^(n+2)+3^(2*n+1)) mod 7 = 0.
Proof.
  intros. induction n.
  trivial.
  cut (S n = n + 1). intro.
  rewrite H. rewrite Nat.add_shuffle0.
  rewrite Nat.pow_add_r.
  rewrite Nat.add_comm. rewrite Nat.mul_add_distr_l.
  cut (2 * n + 2 * 1 + 1 = 2 * n + 1 + 2). intro. rewrite H0. rewrite Nat.pow_add_r.
  rewrite Nat.add_comm.
  cut (2 ^ 1 = 2). intro. rewrite H1.
  cut (3 ^ 2 = (2+7)). intro. rewrite H2.
  rewrite Nat.mul_add_distr_l.
  rewrite Nat.add_assoc.
  rewrite <- Nat.mul_add_distr_r.
  rewrite <- Nat.add_mod_idemp_l.
  rewrite <- Nat.add_mod_idemp_r.
  rewrite Nat.mod_mul. rewrite Nat.add_0_r.
  rewrite Nat.mod_mod.
  rewrite Nat.mul_mod.
  rewrite IHn. rewrite Nat.mul_0_l. trivial.
  omega. omega. omega. omega. omega. trivial. trivial. omega. omega.
Qed.

(* Problem taken from https://www.quora.com/How-do-you-prove-3-n-1-is-even *)
Theorem quora2: forall n, Nat.Even (3^n-1).
Proof.
  intros. apply Nat.Odd_succ. rewrite <- Nat.add_1_r. rewrite Nat.sub_add.
  rewrite <- Nat.odd_spec.
  induction n. trivial.
  rewrite Nat.pow_succ_r'.
  rewrite Nat.odd_mul. simpl. exact IHn.
  induction n. rewrite Nat.pow_0_r. trivial.
  rewrite Nat.pow_succ_r'.
  cut (3 <= 3 * 3^n). intro.
  specialize Nat.le_trans with 1 3 (3*3^n). intro.
  apply H0. omega. exact H.
  cut (3 = 3 * 1). intro. rewrite H.
  apply Nat.mul_le_mono_l. apply IHn. omega.
Qed.
