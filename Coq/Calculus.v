Require Import Rbase Rfunctions Rlimit Classical_Prop.
(* Imports arithmetic helper, real numbers, limits, and classical logic *)
(* Theorem, Lemma, Remark, Fact, Corollary, and Proposition all mean the same thing. *)
(* Local Open Scope nat_scope. *)
Local Open Scope R_scope.

(*
Rplus_eq_reg_r: forall r r1 r2 : R, r1 + r = r2 + r -> r1 = r2
Rplus_eq_compat_l: forall r r1 r2 : R, r1 = r2 -> r + r1 = r + r2
Rplus_eq_compat_r: forall r r1 r2 : R, r1 = r2 -> r1 + r = r2 + r
*)

Theorem Rminus_opp: forall a b : R, a-b = a+-b.
Proof.
  intros. trivial.
Qed.

Theorem Rdiv_inv: forall a b : R, a/b = a*/b.
Proof.
  intros. trivial.
Qed.

(* Limit of f as x goes to c is L *)
(* Proven with epsilon-delta *)
Definition lim f c L := forall eps x, exists delta, 0 < Rabs(x-c) < delta -> Rabs(f(x)-L) < eps.

(* This version of the example proves the limit using the proper epsilon-delta conversion *)
Remark limit_example_naive: lim (fun x : R => x) 3 3.
Proof.
  unfold lim. intros. refine (ex_intro _ eps _).
  intros. destruct H. exact H0.
Qed.

(* The function f is continuous at c *)
Definition continuousAt f c := lim f c (f(c)).
(* The function f is continuous for all real x *)
Definition continuous f := forall x : R, continuousAt f x.

(* If a function f is continuous, substitution is a valid limit technique *)
Theorem continuousSubstitution: forall f c, continuous f -> lim f c (f c).
Proof.
  intros. unfold continuous in H.
  specialize H with c. exact H.
Qed.

(* The function f(x)=x is continuous *)
Theorem x_is_continuous_naive: continuous (fun x : R => x).
Proof.
  unfold continuous, continuousAt, lim. intros.
  refine (ex_intro _ eps _). intros. destruct H. exact H0.
Qed.

(* This new version of the example proves that f(3)=3 and uses f's continuity to solve the problem *)
Remark limit_example: lim (fun x : R => x) 3 3.
Proof.
  remember (fun x : R => x) as f.
  cut (f(3) = 3). intros. Focus 2. rewrite Heqf. trivial.
  cut (continuous f). cut (lim f 3 3 = lim f 3 (f(3))). intros.
  unfold continuous in H1. specialize H1 with 3.
  rewrite H0. exact H1. rewrite H. trivial. rewrite Heqf. exact x_is_continuous_naive.
Qed.

(* The function f is linear *)
Definition linear1 f := exists a b, forall x, f(x)=a*x+b. (* Slope-intercept *)
Definition linear2 f := exists a h k, forall x, f(x)-k=a*(x-h). (* Point-slope *)
Definition linear3 f := exists a b c, b <> 0 /\ forall x, a*x+b*f(x)+c=0. (* Standard form *)
Definition linear f := linear1 f.

Theorem linearEquiv12: forall f, linear1 f <-> linear2 f.
Proof.
  unfold iff, linear1, linear2. intros. refine (conj _ _). intro.
  destruct H as [a H]. destruct H as [b H].
  refine (ex_intro _ a _). refine (ex_intro _ 0 _). refine (ex_intro _ b _).
  intros. rewrite Rminus_0_r. specialize H with x. rewrite Rminus_opp.
  rewrite H. rewrite Rplus_assoc. rewrite Rplus_opp_r. rewrite Rplus_0_r. trivial.
  intros. destruct H as [a H]. destruct H as [h H]. destruct H as [k H].
  refine (ex_intro _ a _). refine (ex_intro _ (-(a*h)+k) _). intro. specialize H with x.
  rewrite <- Rplus_assoc. apply (Rplus_eq_reg_r (-k) (f x) (a*x+-(a*h)+k)).
  rewrite Rplus_assoc. rewrite Rplus_opp_r. rewrite Rplus_0_r.
  rewrite <- Rminus_opp. rewrite <- Rminus_opp. rewrite H. apply (Rmult_minus_distr_l a x h).
Qed.

Theorem linearEquiv13: forall f, linear1 f <-> linear3 f.
Proof.
  unfold iff, linear1, linear3. intros. refine (conj _ _). intro.
  destruct H as [a H]. destruct H as [b H].
  refine (ex_intro _ (-a) _). refine (ex_intro _ 1 _). refine (ex_intro _ (-b) _). refine (conj _ _). apply R1_neq_R0.
  intros. rewrite Rmult_1_l. specialize H with x. rewrite H.
  rewrite <- Rplus_assoc. rewrite <- Ropp_mult_distr_l. rewrite Rplus_opp_l. rewrite Rplus_0_l. rewrite Rplus_opp_r. trivial.
  intros. destruct H as [a H]. destruct H as [b H]. destruct H as [c H].
  refine (ex_intro _ (-a*/b) _). refine (ex_intro _ (-c*/b) _). intro. destruct H. specialize H0 with x.
  apply (Rmult_eq_compat_l (/b) (a * x + b * f x + c) 0) in H0. rewrite Rmult_plus_distr_l in H0. rewrite Rmult_plus_distr_l in H0.
  rewrite Rmult_0_r in H0. rewrite <- Rmult_assoc in H0. rewrite <- Rmult_assoc in H0. rewrite Rinv_l in H0.
  rewrite Rmult_1_l in H0. apply (Rplus_eq_reg_l (a * / b * x) (f x) (- a * / b * x + - c * / b)).
  remember (a*/b) as A. rewrite <- Rplus_assoc. rewrite <- Ropp_mult_distr_l. rewrite <- HeqA. rewrite <- Ropp_mult_distr_l. rewrite Rplus_opp_r. rewrite Rplus_0_l.
  rewrite <- Ropp_mult_distr_l. remember (c*/b) as C. apply (Rplus_eq_reg_l C (A*x+f x) (-C)). rewrite Rplus_opp_r. Focus 2. exact H.
  rewrite Rmult_comm in HeqC. rewrite <- HeqC in H0. rewrite Rmult_comm in HeqA. rewrite <- HeqA in H0. rewrite Rplus_comm. exact H0.
Qed.

(* The function f(x)=x is linear *)
Theorem x_is_linear: linear (fun x : R => x).
Proof.
  refine (ex_intro _ 1 _). refine (ex_intro _ 0 _).
  intros. rewrite Rplus_0_r. rewrite Rmult_1_l. trivial.
Qed.

(* All linear functions are continuous *)
Theorem linear_is_continuous: forall f, linear f -> continuous f.
Proof.
  unfold linear, continuous, continuousAt, lim. intros.
  destruct H as [a H]. destruct H as [b H].
  cut (a <> 0 \/ a = 0). intros. Focus 2. rewrite or_comm. apply classic. (* The line is either flat, or it is not *)
  destruct H0. refine (ex_intro _ (eps * /(Rabs a)) _). intro E.
  destruct E. rewrite H. rewrite H. cut (a*x0+b-(a*x+b)=a*(x0-x)). intro S.
  rewrite S. rewrite Rabs_mult. cut (Rabs a * (eps * (/ (Rabs a))) = eps). intro S2.
  rewrite <- S2. apply Rmult_lt_compat_l. apply Rabs_pos_lt. exact H0. exact H2.
  (* SearchAbout Rinv. *) rewrite <- Rmult_assoc. apply Rinv_r_simpl_m.
  apply Rabs_no_R0. exact H0. rewrite Rminus_opp. rewrite Rminus_opp.
  rewrite Ropp_plus_distr. rewrite <- Rplus_assoc.
  rewrite Rmult_plus_distr_l. rewrite Rplus_comm. rewrite Rplus_assoc.
  rewrite Rplus_comm. rewrite Rplus_assoc. apply Rplus_eq_compat_l.
  rewrite Rplus_assoc. rewrite Rplus_comm. rewrite Rplus_comm. rewrite <- Rplus_assoc.
  rewrite Rplus_comm. rewrite <- Rplus_assoc. rewrite Rplus_opp_l. rewrite Rplus_0_l. apply Ropp_mult_distr_r.

  refine (ex_intro _ eps _). rewrite H0 in H. rewrite H. rewrite H.
  rewrite Rmult_0_l. rewrite Rmult_0_l. rewrite Rplus_0_l. intros. rewrite Rminus_opp. rewrite Rplus_opp_r. rewrite Rabs_R0.
  apply (Rle_lt_trans 0 (Rabs (x0-x)) eps). apply Rabs_pos. destruct H1. exact H2.
Qed.

(* The function f(x)=x is continuous *)
Corollary x_is_continuous: continuous (fun x : R => x).
  apply linear_is_continuous. apply x_is_linear.
Qed.

(* The limit of f(x)=5x-3 as x goes to 1 is 2 *)
Remark limit_example_2: lim (fun x : R => 5*x-3) 1 (5-3).
Proof. (* Coq is not smart enough to simplify 5-3=2 *)
  remember (fun x : R => 5*x-3) as f. cut (linear f). intros.
  cut (f(1)=(5-3)). intros. rewrite <- H0. apply continuousSubstitution.
  apply linear_is_continuous. apply H. rewrite Heqf. rewrite Rmult_1_r. trivial.
  refine (ex_intro _ 5 _). refine (ex_intro _ (-3) _).
  intros. rewrite Heqf. rewrite Rminus_opp. trivial.
Qed.




