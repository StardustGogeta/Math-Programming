Require Import Bool.
Require Import Setoid.
Require Import Classical_Prop.

Module WikiLogic.

(* Ideas at https://en.wikipedia.org/wiki/Propositional_calculus#Basic_and_derived_argument_forms *)
(* The tactic `intuition` can replace most of these (that don't require Classical_Prop),
  but it is deliberately not used for practice purposes *)

Theorem modusPonens: (forall p q : Prop, (p -> q) /\ p -> q).
Proof.
  intros.
  destruct H.
  pose (Q := H H0).
  exact Q.
Qed.

Theorem modusTollens: (forall p q : Prop, (p -> q) /\ ~q -> ~p).
Proof.
  unfold not. intros.
  destruct H.
  exact (H1 (H H0)).
Qed.

Theorem hypotheticalSyllogism: (forall p q r : Prop, (p -> q) /\ (q -> r) -> (p -> r)).
Proof.
  intros.
  destruct H.
  refine (H1 (H H0)).
Qed.

Theorem disjunctiveSyllogism: (forall p q : Prop, (p \/ q) /\ ~p -> q).
Proof.
  unfold not. intros.
  destruct H. destruct H.
  case (H0 H). exact H.
Qed.

Theorem constructiveDilemma: (forall p q r s : Prop, (p -> q) /\ (r -> s) /\ (p \/ r) -> (q \/ s)).
Proof.
  intros.
  destruct H.
  destruct H0.
  destruct H1.
  refine (or_introl (H H1)).
  refine (or_intror (H0 H1)).
Qed.

Theorem destructiveDilemma: (forall p q r s : Prop, (p -> q) /\ (r -> s) /\ (~q \/ ~s) -> (~p \/ ~r)).
Proof.
  unfold not. intros.
  destruct H.
  destruct H0.
  destruct H1.
  refine (or_introl _).
    intros.
    refine (H1 (H H2)).
  refine (or_intror _).
    intros.
    refine (H1 (H0 H2)).
Qed.

Theorem bidirectionalDilemma: (forall p q r s : Prop, (p -> q) /\ (r -> s) /\ (p \/ ~s) -> (q \/ ~r)).
Proof.
  unfold not. intros.
  destruct H.
  destruct H0.
  destruct H1.
  refine (or_introl (H H1)).
  refine (or_intror _).
    intros.
    refine (H1 (H0 H2)).
Qed.

Theorem simplification: (forall p q : Prop, p /\ q -> p).
Proof.
  intros.
  destruct H.
  exact H.
Qed.

Theorem conjunction: (forall p q : Prop, p -> q -> p /\ q).
Proof.
  intros.
  refine (conj H H0).
Qed.

Theorem addition: (forall p q : Prop, p -> p \/ q).
Proof.
  intros.
  refine (or_introl H).
Qed.

Theorem composition: (forall p q r : Prop, (p -> q) /\ (p -> r) -> (p -> (q /\ r))).
Proof.
  intros.
  destruct H.
  refine (conj (H H0) (H1 H0)).
Qed.

Theorem deMorganFirst: (forall p q : Prop, ~(p /\ q) <-> (~p \/ ~q)).
Proof.
  unfold iff.
  intros.
  refine (conj _ _).
    apply not_and_or. (* Requires Classical_Prop for law of excluded middle *)
    apply or_not_and. (* This means Props can be treated as booleans *)
Qed.

Theorem deMorganSecond: (forall p q : Prop, ~(p \/ q) <-> (~p /\ ~q)).
Proof.
  unfold iff.
  intros.
  refine (conj _ _).
    apply not_or_and.
    apply and_not_or.
  (* Alternatively, without using Classical_Prop:
  unfold iff, not.
  constructor.
  intros.
  constructor.
  - intro. apply H. left. apply H0.
  - intro. apply H. right. apply H0.
  - intros. destruct H. destruct H0. exact (H H0). exact (H1 H0). *)
Qed.

Theorem commutation1: (forall p q : Prop, p \/ q -> q \/ p).
Proof.
  intros.
  destruct H.
  refine (or_intror H).
  refine (or_introl H).
Qed.

Theorem commutation2: (forall p q : Prop, p /\ q -> q /\ p).
Proof.
  intros.
  destruct H.
  refine (conj H0 H).
Qed.

Theorem commutation3: (forall p q : Prop, p <-> q -> q <-> p).
Proof.
  intros.
  destruct H.
  unfold iff.
  refine (conj H0 H).
Qed.

Theorem association1: (forall p q r : Prop, p \/ (q \/ r) -> (p \/ q) \/ r).
Proof.
  intros.
  destruct H.
  refine (or_introl (or_introl H)).
  destruct H.
  refine (or_introl (or_intror H)).
  refine (or_intror H).
Qed.

Theorem association2: (forall p q r : Prop, p /\ (q /\ r) -> (p /\ q) /\ r).
Proof.
  intros.
  destruct H.
  destruct H0.
  refine (conj (conj H H0) H1).
Qed.

Theorem distribution1: (forall p q r : Prop, p /\ (q \/ r) -> (p /\ q) \/ (p /\ r)).
Proof.
  intros.
  destruct H.
  destruct H0.
  refine (or_introl (conj H H0)).
  refine (or_intror (conj H H0)).
Qed.

Theorem distribution2: (forall p q r : Prop, p \/ (q /\ r) -> (p \/ q) /\ (p \/ r)).
Proof.
  intros.
  destruct H.
  refine (conj (or_introl H) (or_introl H)).
  destruct H.
  refine (conj (or_intror H) (or_intror H0)).
Qed.

Theorem doubleNegation: (forall p : Prop, p -> ~~p).
Proof. (* Note that Coq relies on intuitionist logic, and cannot prove ~~p -> p *)
  unfold not.
  intros.
  exact (H0 H).
Qed.

Theorem transposition: (forall p q : Prop, (p -> q) -> (~q -> ~p)).
Proof.
  unfold not.
  intros.
  exact (H0 (H H1)).
Qed.

Theorem materialImplication: (forall p q : Prop, (p -> q) -> (~p \/ q)).
Proof.
  apply imply_to_or. (* Classical_Prop saves the day *)
Qed.

Theorem materialEquivalence1: (forall p q : Prop, (p <-> q) -> ((p -> q) /\ (q -> p))).
Proof.
  unfold iff.
  intros.
  exact H.
Qed.

Theorem materialEquivalence2: (forall p q : Prop, (p <-> q) -> ((p /\ q) \/ (~p /\ ~q))).
Proof.
  unfold iff.
  intros.
  destruct H.
  classical_left. (* This also needs Classical_Prop to work out correctly *)
  apply deMorganFirst in H1.
  destruct H1.
  apply NNPP in H1.
  refine (conj H1 (H H1)).
  apply NNPP in H1.
  refine (conj (H0 H1) H1).
Qed.

Theorem materialEquivalence3: (forall p q : Prop, (p <-> q) -> (p \/ ~q) /\ (~p \/ q)).
Proof.
  unfold iff.
  intros.
  destruct H.
  refine (conj _ _).
    classical_left. (* Once again, this needs Classical_Prop to work out correctly *)
    apply NNPP in H1.
    exact (H0 H1).
    classical_right.
    apply NNPP in H1.
    exact (H H1).
Qed.

Theorem exportation_importation: (forall p q r : Prop, ((p /\ q) -> r) <-> (p -> (q -> r))).
Proof.
  unfold iff.
  intros.
  refine (conj _ _).
    intros.
    exact (H (conj H0 H1)).
    intros.
    destruct H0.
    exact (H H0 H1).
Qed.

Theorem tautology1: (forall p : Prop, p -> (p \/ p)).
Proof.
  intros.
  refine (or_introl H).
Qed.

Theorem tautology2: (forall p : Prop, p -> (p /\ p)).
Proof.
  intros.
  refine (conj H H).
Qed.

Theorem excludedMiddle: (forall p : Prop, p \/ ~p).
Proof.
  apply classic. (* The pinnacle of Classical_Prop usages *)
Qed.

Theorem nonContradiction: (forall p : Prop, ~(p /\ ~p)).
Proof.
  intros.
  apply deMorganFirst. (* Requires Classical_Prop one last time *)
  apply excludedMiddle.
Qed.

End WikiLogic.

(* Unrelated to the Wikipedia page *)
Theorem negb_is_not : (forall a, Is_true (negb a) <-> (~(Is_true a))).
Proof.
  intros.
  unfold iff, not.
  case a.
  simpl. refine (conj _ _).
    trivial.
    intros. case H. exact I.
  simpl. refine (conj _ _).
    trivial.
    trivial.
Qed.
