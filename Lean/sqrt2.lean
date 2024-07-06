import Batteries
import Mathlib.Algebra.Ring.Parity
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Rat.Cast.CharZero
import Mathlib.Data.Int.Defs
import Mathlib.Algebra.Order.Group.Abs
import Mathlib.Data.Int.Defs

theorem weak_sqrt2_is_irrational: ∀ p q, q ≠ 0 ∧ Nat.Coprime p q -> p ^ 2 ≠ q ^ 2 * 2 := by
  intro p q hq
  obtain ⟨ hq, h ⟩ := hq
  by_contra h2
  have h3 : (Even (p ^ 2)) := by
    use q ^ 2
    omega
  have h4 : Even p := by
    rw [Nat.even_pow'] at h3
    apply h3
    simp
  have h4a := h4
  obtain ⟨ k, hk ⟩ := h4
  rw [← mul_two] at hk
  rw [hk] at h2
  have ksq : (k * 2) ^ 2 = k ^ 2 * 4 := by
    repeat rw [Nat.pow_two, mul_assoc]
    rw [Nat.mul_left_cancel_iff]
    omega
    by_contra hk0
    simp_all
  rw [ksq] at h2
  have : 4 = 2 * 2 := by
    tauto
  rw [this, ← mul_assoc, Nat.mul_right_cancel_iff] at h2
  have h5 : Even (q ^ 2) := by
    use k ^ 2
    omega
  rw [Nat.even_pow'] at h5
  have h6 : ¬ p.Coprime q := by
    rw [Nat.Prime.not_coprime_iff_dvd]
    use 2
    apply And.intro Nat.prime_two
    apply And.intro
    use (p / 2)
    rw [Nat.two_mul_div_two_of_even]
    apply h4a
    use (q / 2)
    rw [Nat.two_mul_div_two_of_even]
    apply h5
  repeat tauto

theorem strong_sqrt2_is_irrational: ∀ p q, q ≠ 0 -> p ^ 2 ≠ q ^ 2 * 2 := by
  intro p q hq
  by_cases h : Nat.Coprime p q
  apply weak_sqrt2_is_irrational
  apply And.intro hq h
  by_contra h2
  have ex_coprime := Nat.exists_coprime p q
  obtain ⟨ a, b, h3, h4, h5 ⟩ := ex_coprime
  rw [h4] at h2
  nth_rewrite 2 [h5] at h2
  repeat rw [pow_two] at h2
  simp_arith at h2
  repeat rw [← mul_assoc] at h2
  rw [Nat.mul_right_cancel_iff] at h2
  rw [mul_comm] at h2
  rw [mul_assoc, ← mul_comm b (Nat.gcd p q)] at h2
  repeat rw [← mul_assoc] at h2
  rw [Nat.mul_right_cancel_iff, mul_assoc] at h2
  repeat rw [← pow_two] at h2
  rw [mul_comm] at h2
  apply weak_sqrt2_is_irrational a b
  apply And.intro _ h3
  by_contra h6
  rw [h6, zero_mul] at h5
  tauto
  apply h2
  apply Nat.gcd_pos_of_pos_right
  apply Nat.zero_lt_of_ne_zero hq
  apply Nat.gcd_pos_of_pos_right
  apply Nat.zero_lt_of_ne_zero hq

theorem int_ge_zero_exists_nat: ∀ x : ℤ, x ≥ 0 → ∃ n : ℕ, x = n := by
  intro x h
  use x.natAbs
  omega

lemma lemma_sqrt_2_is_irrational: ∀ x : ℚ, x.num ≥ 0 → x.num ^ 2 ≠ 2 * ↑x.den ^ 2 := by
  intro x x_pos h
  have h1 := int_ge_zero_exists_nat x.num x_pos
  obtain ⟨ x_abs, h1 ⟩ := h1
  have h2 := strong_sqrt2_is_irrational x_abs x.den
  have h3 : x.den ≠ 0 := by simp_all
  apply h2 h3
  simp_all
  rw [mul_comm] at h2
  apply h2
  rw [← Int.natCast_inj, Int.natCast_pow, Int.natCast_mul, Int.natCast_pow]
  apply h

theorem sqrt2_is_irrational: ¬ ∃ x : ℚ, x ^ 2 = 2 := by
  push_neg
  intro x h
  rw [Rat.eq_iff_mul_eq_mul] at h
  simp_all
  by_cases x_pos : x.num ≥ 0
  apply lemma_sqrt_2_is_irrational x x_pos h
  have neg_x_pos : -x.num >= 0 := by omega
  apply lemma_sqrt_2_is_irrational (-x) neg_x_pos
  simp_all

#check sqrt2_is_irrational
