Require Import Omega.

Theorem main: forall (f : nat -> nat), (forall (x y : nat), f (x+y) = f(x) + f(y)) -> exists a : nat, forall x : nat, f(x) = a*x.
Proof.
  intros.
  cut (f(0) = 0). intros.
  cut (forall n x: nat, f (n*x) = n*f(x)).
  intro. Focus 2. intros. induction n.
  rewrite Nat.mul_0_l. rewrite Nat.mul_0_l. exact H0.
  rewrite Nat.mul_succ_l. rewrite Nat.mul_succ_l.
  remember (n*x) as a. rewrite <- IHn. apply H.
  cut (forall n : nat, f(n) = n * f(1)). intro.
  remember (f 1) as c. refine (ex_intro _ c _).
  intros. rewrite Nat.mul_comm. apply H2.
  intros. specialize H1 with n 1. rewrite Nat.mul_1_r in H1. apply H1.
  cut (forall x : nat, f(x) = f(x) + f(0)). intros.
  specialize H0 with 0. rewrite (plus_minus (f 0) (f 0)) in H0.
  rewrite Nat.sub_diag in H0. exact H0.
  rewrite <- H0. apply H0. intros. specialize H with x 0.
  rewrite Nat.add_0_r in H. apply H.
Qed.
