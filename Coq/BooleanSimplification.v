Require Import BasicLogic.
Require Import Classical_Prop.

Proposition ExampleProblem: forall X Y Z : Prop, ~(~X /\ ~X) \/ ((Z /\ Y) \/ (Z /\ ~Y)) -> X \/ Z.
Proof.
  intros. destruct H.
  apply deMorganFirst in H.
  destruct H.
  apply NNPP in H.
  refine (or_introl H).
  apply NNPP in H.
  refine (or_introl H).
  destruct H. destruct H.
  refine (or_intror H). destruct H.
  refine (or_intror H).
Qed.

(* Ideas taken from http://web.mit.edu/6.111/www/s2007/PSETS/pset1.pdf *)
Theorem P01: forall a : Prop, a \/ False -> a.
Proof.
  intros. destruct H.
  exact H. case H.
Qed.

Theorem P02: forall a : Prop, ~a /\ False -> False.
Proof.
  intros.
  destruct H.
  case H0.
Qed.

Theorem P03: forall a : Prop, a \/ ~a.
Proof.
  apply excludedMiddle.
Qed.

Theorem P04: forall a : Prop, a \/ a -> a.
Proof.
  intros. destruct H.
  exact H. exact H.
Qed.

Theorem P05: forall a b : Prop, a \/ (a /\ b) -> a.
Proof.
  intros. destruct H.
  exact H. destruct H. exact H.
Qed.

Theorem P06: forall a b : Prop, a \/ (~a /\ b) -> a \/ b.
Proof.
  unfold not. intros.
  destruct H.
  refine (or_introl H).
  destruct H.
  refine (or_intror H0).
Qed.

Theorem P07: forall a b : Prop, a /\ (~a \/ b) -> a /\ b.
Proof.
  unfold not. intros.
  destruct H. destruct H0.
  case (H0 H). refine (conj H H0).
Qed.

Theorem P08: forall a b : Prop, (a /\ b) \/ (~a /\ b) -> b.
Proof.
  unfold not. intros.
  destruct H.
  destruct H. exact H0.
  destruct H. exact H0.
Qed.

Theorem P09: forall a b : Prop, (~a \/ ~b) /\ (~a \/ b) -> ~a.
Proof.
  unfold not. intros.
  destruct H. destruct H, H1.
  exact (H H0). exact (H H0).
  exact (H1 H0). exact (H H1).
Qed.

(* I don't know how to make an infinite list, so b
  represents an infinite chain of propositions
  combined into one with the `\/` operator *)
Theorem P10: forall a b : Prop, a /\ b -> a.
Proof.
  apply simplification.
Qed.

Theorem P11: forall a b : Prop, a \/ b \/ (a /\ b) -> a \/ b.
Proof.
  intros. destruct H.
  refine (or_introl H).
  destruct H. refine (or_intror H).
  destruct H. refine (or_introl H).
Qed.

Theorem P12: forall a b : Prop, a \/ b \/ (~a /\ ~b).
Proof.
  intros. classical_left.
  apply deMorganSecond in H. destruct H.
  apply deMorganFirst in H0. destruct H0.
  apply NNPP in H0. exact H0. case (H0 H).
Qed.

Theorem P13: forall a b : Prop, a \/ b \/ ~(a /\ b).
Proof.
  intros. classical_left.
  apply deMorganSecond in H. destruct H.
  apply NNPP in H0. destruct H0.
  exact H0.
Qed.

Theorem P14: forall y : Prop, y \/ (y /\ ~y) -> y.
Proof.
  intros. apply P05 in H.
  exact H.
Qed.

Theorem P15: forall x y : Prop, (x /\ y) \/ (x /\ ~y) -> x.
Proof.
  intros. destruct H.
  destruct H. exact H.
  destruct H. exact H.
Qed.

Theorem P16: forall x y : Prop, ~x \/ (y /\ ~x) -> ~x.
Proof.
  intros. destruct H. exact H.
  destruct H. exact H0.
Qed.

Theorem P17: forall w x y z : Prop, (w \/ ~x \/ y \/ ~z) /\ y -> y.
Proof.
  intros. destruct H. exact H0.
Qed.

Theorem P18: forall x y : Prop, (x \/ ~y) /\ (x \/ y) -> x.
Proof.
  intros. destruct H.
  destruct H0. exact H0.
  destruct H. exact H. case (H H0).
Qed.

Theorem P19: forall w x : Prop, w \/ (w \/ (w /\ x)) -> w.
Proof.
  intros. destruct H. exact H.
  destruct H. exact H.
  destruct H. exact H.
Qed.

Theorem P20: forall x y : Prop, x /\ (x \/ (x /\ y)) -> x.
Proof.
  intros. destruct H. exact H.
Qed.

Theorem P21: forall x : Prop, ~(~x \/ ~x) -> x.
Proof.
  intros. apply deMorganSecond in H.
  destruct H. apply NNPP in H. exact H.
Qed.

Theorem P22: forall x : Prop, ~(x \/ ~x) -> False.
Proof.
  intros. apply deMorganSecond in H.
  destruct H. case (H0 H).
Qed.

Theorem P23: forall w x y z : Prop, w \/ (w /\ ~x /\ y /\ z) -> w.
Proof.
  intros. destruct H. exact H.
  destruct H. exact H.
Qed.

Theorem P24: forall w x y z : Prop, ~w /\ ~(w /\ x /\ y /\ z) -> ~w.
Proof.
  intros. destruct H. exact H.
Qed.

Theorem P25: forall x y z : Prop, (x /\ z) \/ (~x /\ y) \/ (z /\ y) -> (x /\ z) \/ (~x /\ y).
Proof.
  intros. destruct H.
  refine (or_introl H).
  destruct H. refine (or_intror H).
  classical_right. apply deMorganFirst in H0.
  destruct H, H0. refine (conj H0 H1).
  case (H0 H).
Qed.

Theorem P26: forall x y z : Prop, (x \/ z) /\ (~x \/ y) /\ (z \/ y) -> (x /\ y) \/ (~x /\ z).
Proof.
  intros.
  destruct H. destruct H, H0.
  destruct H0. case (H0 H).
  refine (or_introl (conj H H0)).
  classical_right. apply deMorganFirst in H2.
  destruct H0, H1, H2. refine (conj H0 H1). refine (conj H0 H1).
  refine (conj H0 H). refine (conj H0 H). refine (conj H2 H).
  case (H2 H0). refine (conj H2 H). case (H2 H0).
Qed.

Theorem P27: forall x y z : Prop, ~x \/ ~y \/ (x /\ y /\ ~z) -> ~x \/ ~y \/ ~z.
Proof.
  intros.
  destruct H. refine (or_introl H).
  destruct H. refine (or_intror (or_introl H)).
  destruct H. destruct H0. refine (or_intror (or_intror H1)).
Qed.
