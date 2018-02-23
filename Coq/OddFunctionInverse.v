Require Import Rbase Rfunctions.

Local Open Scope nat_scope.
Local Open Scope R_scope.

Definition inverse (f g : R -> R) := forall x, g(f(x)) = x /\ f(g(x)) = x.

Definition odd (f : R -> R) := forall x, f(-x) = -f(x).

Theorem inv_of_odd_is_odd: forall (f f' : R -> R), inverse f f' -> odd f -> odd f'.
Proof.
  unfold inverse, odd.
  intros.
  cut (forall a, -a = -f'(f(a))).
  cut (forall a, f'(-f(a)) = -a). intros.
  cut (forall a, f'(-f(a)) = -f'(f(a))).
  intros.
  Focus 2. intros. specialize H1 with a. specialize H2 with a. rewrite <- H2. apply H1.
  Focus 2. intros. specialize H0 with a. rewrite <- H0. specialize H with (-a). apply H.
  Focus 2. intros. (* SearchAbout Ropp. *)
  apply Ropp_eq_compat. specialize H with a. symmetry. apply H.
  specialize H3 with (f'(x)).
  specialize H with x. destruct H. rewrite H4 in H3. apply H3.
Qed.
