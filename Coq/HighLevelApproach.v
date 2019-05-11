Require Import Rbase Rfunctions Rlimit R_sqrt Classical_Prop Arith Field.
(* Real numbers, classical logic, and the `ring` and `field` tactics for quick algebraic simplifications. *)
Local Open Scope R_scope.

(* Here is how to create a useful hint database:

Create HintDb arithHelp.
Hint Resolve Nat.mul_assoc Nat.mul_comm Nat.mul_shuffle0 Nat.mul_shuffle1 : arithHelp.

  Then, use the lines below. The second one is more powerful.

auto with arithHelp.
eauto with arithHelp.

  Don't forget to use About or Search if you need to.
*)

Create HintDb realHelp.
Hint Resolve Rmult_lt_reg_r Rplus_opp_r Rle_lt_trans not_eq_sym Rlt_not_eq Rinv_0_lt_compat Rplus_minus : realHelp.
Hint Rewrite Rmult_assoc Rinv_l Rmult_1_r Rinv_r Rabs_R0 Rminus_0_r Rmult_0_l Rplus_assoc : realHelp.
Hint Unfold not Rdiv Rminus : realHelp.

(* Probably should move these into separate files, some for basic calculus definitions
(once usability in practice is proven) and some for basic real number theorems that are trivial to
prove but very useful in simplification (esp. with hint databases). *)

Theorem Rdiv_inv: forall a b : R, a/b = a*/b.
Proof.
  intros. trivial.
Qed.
Hint Rewrite Rdiv_inv : realHelp.

Theorem Rlt_lt_trans: forall a b c : R, a < b < c -> a < c.
Proof.
  intros. destruct H. apply (Rlt_le a b) in H. eauto with realHelp.
  (* apply (Rle_lt_trans a b c). auto. auto. *)
Qed.
Hint Resolve Rlt_lt_trans : realHelp.

Theorem Rminus_zero: forall a : R, a - a = 0.
Proof.
  eauto with realHelp.
  (* intros. unfold Rminus. apply Rplus_opp_r. *)
Qed.
Hint Rewrite Rminus_zero : realHelp.

Theorem Rlt_div: forall a b c : R, 0 < b -> a * b < c <-> a < c / b.
Proof.
  unfold iff. intros. refine (conj _ _).
  intros. apply (Rmult_lt_reg_r b a (c / b)). auto.
  unfold Rdiv. autorewrite with realHelp using auto.
  (* rewrite Rmult_assoc. eauto with realHelp. rewrite Rinv_l. rewrite Rmult_1_r. auto. *)
  eauto with realHelp. (* apply not_eq_sym. apply Rlt_not_eq. auto. *)
  intros. apply (Rmult_lt_reg_r (/ b) (a * b) c). auto with realHelp. (* apply Rinv_0_lt_compat. *)
  rewrite <- Rdiv_inv. rewrite <- Rdiv_inv. autorewrite with realHelp using auto. eauto with realHelp.
Qed.

(* Limit of f as x goes to c is L *)
(* Proven with epsilon-delta *)
Definition lim f c L := forall eps x, exists delta, 0 < Rabs(x-c) < delta -> Rabs(f(x)-L) < eps.

(* The derivative of f as x approaches a is f' *)
Definition derivative f a f' := lim (fun x : R => (f x-f a)/(x-a)) a f'.

(* The derivative of f as x approaches a is f' *)
Definition derivativeAlt f a f' := lim (fun h : R => (f (a+h)-f a)/h) 0 f'.

Theorem derivativeEquivalence: forall f a f', derivative f a f' <-> derivativeAlt f a f'.
Proof.
  unfold iff, derivative, derivativeAlt, lim. intros. refine (conj _ _).
  intros. specialize H with eps (a+x). destruct H as [delta H].
  refine (ex_intro _ delta _). intros. cut (a+x-a=x). intros.
  rewrite H1 in H. autorewrite with realHelp in H0. apply H, H0. ring.
  intros. specialize H with eps (x-a). rewrite Rminus_0_r in H. cut (a+(x-a)=x). intros.
  rewrite H0 in H. auto. ring.
Qed.

Theorem derivativeOfXIsOne: forall a, derivative (fun x : R => x) a 1.
Proof.
  intros. apply derivativeEquivalence.
  unfold derivativeAlt, lim.
  intros. rewrite Rminus_0_r.
  refine (ex_intro _ eps _). intros.
  cut (a+x-a = x). intros. rewrite H0.
  rewrite Rdiv_inv. rewrite <- (Rinv_r_sym x).
  rewrite Rminus_zero. rewrite Rabs_R0.
  apply (Rlt_lt_trans 0 (Rabs x) eps). auto.
  destruct H. unfold not. intros. rewrite H2 in H. rewrite Rabs_R0 in H.
  apply (Rlt_irrefl 0). auto. ring.
  (* unfold Rminus. rewrite Rplus_assoc. apply Rplus_minus. *)
Qed.

Lemma derivativeOfZero: forall a, derivative (fun x : R => 0) a 0.
Proof.
  unfold derivative, lim. intros. autorewrite with realHelp.
  (* rewrite Rminus_0_r. rewrite Rminus_0_r. rewrite Rdiv_inv. rewrite Rmult_0_l. *)
  refine (ex_intro _ eps _). eauto with realHelp.
Qed.

(* Step one to proving linearity: constant multiplier. *)
Theorem derivativeMult: forall (F : R -> R) (a b c d : R), derivative F c d -> derivative (fun x => a * (F x)) c (a * d).
Proof.
  unfold iff. intros. cut (a = 0 \/ a <> 0). intros. destruct H0.
  rewrite H0. unfold derivative, lim. intros. autorewrite with realHelp.
  refine (ex_intro _ eps _). eauto with realHelp.
  unfold derivative, lim. intros. unfold derivative, lim in H.
  specialize H with (eps / (Rabs a)) x. destruct H as [delta H].
  refine (ex_intro _ delta _). intros.
  rewrite <- Rmult_minus_distr_l. unfold Rdiv.
  rewrite Rmult_assoc. rewrite <- Rmult_minus_distr_l. rewrite Rabs_mult. rewrite Rmult_comm. apply Rlt_div.
  apply Rabs_pos_lt, H0. apply H, H1.
  apply classic.
Qed.

(* Step two: preservation of addition. *)
Theorem derivativeAddition: forall (F G : R -> R) (a b c : R), derivative F a b -> derivative G a c -> derivative (fun x => F(x) + G(x)) a (b + c).
Proof.
  unfold derivative, lim. intros. specialize H with (eps/2) x. specialize H0 with (eps/2) x.
  destruct H as [delta H]. destruct H0 as [delta0 H0].
  refine (ex_intro _ (Rmin delta delta0) _). intros.
  remember (x-a) as dx. cut (F x + G x - (F a + G a) = (F x - F a) + (G x - G a)). intros. rewrite H2.
  remember (F x - F a) as dF. remember (G x - G a) as dG.
  remember (Rabs ((dF + dG) / dx - (b + c))) as err. remember (Rabs (dF / dx - b)) as errF. remember (Rabs (dG / dx - c)) as errG.
  cut (err <= errF + errG).
  intros. apply (Rle_lt_trans err (errF + errG) eps). auto.
  cut (eps = eps/2 + eps/2). intros. rewrite H4. apply (Rplus_lt_compat errF (eps/2) errG (eps/2)).
  apply H. destruct H1. refine (conj H1 _). cut (Rmin delta delta0 <= delta). intros.
  apply (Rlt_le_trans (Rabs dx) (Rmin delta delta0) delta) in H6. auto. auto. apply Rmin_l.
  apply H0. destruct H1. refine (conj H1 _). cut (Rmin delta delta0 <= delta0). intros.
  apply (Rlt_le_trans (Rabs dx) (Rmin delta delta0) delta0) in H6. auto. auto. apply Rmin_r. field.
  rewrite Heqerr, HeqerrF, HeqerrG. cut ((dF + dG) / dx - (b + c) = (dF / dx - b) + (dG / dx - c)). intros. rewrite H3.
  apply Rabs_triang. field. destruct H1. unfold not. intros. rewrite H4 in H1. rewrite Rabs_R0 in H1.
  apply (Rlt_irrefl 0), H1. ring.
Qed.

Theorem derivativeChainRule: forall (F G : R -> R) (a b c : R), derivative G a b -> derivative (fun g => F(g)) (G a) c -> derivative (fun x => F(G(x))) a (b * c).
Proof.
  unfold derivative, lim. intros. specialize H with (sqrt eps) x. specialize H0 with (sqrt eps) (G x).
  destruct H as [delta H], H0 as [delta0 H0]. remember (G x) as g. remember (G a) as g0. remember (x-a) as dx.
  remember (g-g0) as dG. remember (F g - F g0) as dF. Search Rabs Rmult.
  remember (Rmin delta (dx * ((sqrt eps) + b ))) as newDelta. refine (ex_intro _ newDelta _). intros.
  assert (Rabs (dG / dx - b) < sqrt eps). apply H. destruct H1. refine (conj H1 _). cut (newDelta <= delta). intros.
  apply (Rlt_le_trans (Rabs dx) newDelta delta). auto. auto. rewrite HeqnewDelta. apply Rmin_l.
  assert (0 < Rabs dG < delta0).







  rewrite <- (sqrt_def eps). cut ((F g - F g0) / (x - a) = ((F g - F g0) / (g - g0)) * ((g - g0) / (x - a))). intros. rewrite H2.
  








