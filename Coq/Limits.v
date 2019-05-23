Require Import Omega Rbase Rfunctions Rlimit Classical_Prop.
(* Imports arithmetic helper, real numbers, limits, and classical logic *)

Local Open Scope R_scope.
(* This makes real number-related notation far easier *)

(* SearchAbout Rle. *)
Theorem test: forall r : R, r > 0 \/ r <= 0.
Proof.
  intros.
  classical_left.
  apply Rnot_le_lt.
  exact H.
Qed.

Lemma distRmet_equals_Rdist: dist R_met = R_dist.
Proof.
  trivial. (* This is magic right here *)
Qed.

(* Prove that x + 1 approaches 1 as x approaches 0 *)
Theorem basicLimit: limit1_in (fun x => x + 1) (fun x:R => x <> 0) 1 0.
Proof.
  unfold limit1_in, limit_in.
  intros.
  refine (ex_intro _ eps _).
  refine (conj H _).
  rewrite distRmet_equals_Rdist.
  SearchAbout R_dist.
  unfold R_dist. simpl. intros. destruct H0.
  cut (x-0 = x+1-1).
  intro. rewrite H2 in H1.
  apply H1. simpl. SearchAbout Rminus.
(* Rplus_eq_reg_r: forall r r1 r2 : R, r1 + r = r2 + r -> r1 = r2 *)
  rewrite (Rplus_eq_reg_l x (-0) (1-1)). rewrite <- H2.
