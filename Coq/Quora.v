Require Import Arith.
Require Import Omega.

(* Problem taken from
https://www.quora.com/How-do-I-prove-by-induction-that-2-n+2-+-3-2n+1-is-divisible-by-7

Nat.pow_succ_r:
  forall a b : nat,
  0 <= b -> a ^ S b = a * a ^ b
Nat.pow_add_r: forall a b c : nat, a ^ (b + c) = a ^ b * a ^ c
Nat.le_0_l: forall n : nat, 0 <= n
Nat.pow_mul_r: forall a b c : nat, a ^ (b * c) = (a ^ b) ^ c
Nat.mod_mul: forall a b : nat, b <> 0 -> (a * b) mod b = 0
Nat.add_1_r: forall n : nat, n + 1 = S n
Nat.add_shuffle0: forall n m p : nat, n + m + p = n + p + m
Nat.mul_add_distr_r: forall n m p : nat, (n + m) * p = n * p + m * p
Nat.mul_add_distr_l: forall n m p : nat, n * (m + p) = n * m + n * p
Nat.add_mod_idemp_l:
  forall a b n : nat, n <> 0 -> (a mod n + b) mod n = (a + b) mod n
Nat.add_mod_idemp_r:
  forall a b n : nat, n <> 0 -> (a + b mod n) mod n = (a + b) mod n
Nat.mul_mod:
  forall a b n : nat, n <> 0 -> (a * b) mod n = (a mod n * (b mod n)) mod n

SearchAbout Nat.pow.
SearchAbout Nat.add.
SearchAbout Nat.modulo.
SearchAbout Nat.mul.

*)

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
