import Batteries
import Mathlib.Algebra.Ring.Parity
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Rat.Cast.CharZero
import Mathlib.Data.Int.Defs
import Mathlib.Algebra.Order.Group.Abs
import Mathlib.Data.Int.Defs
import Mathlib.Data.Real.Irrational
import Mathlib.Algebra.Squarefree.Basic
import Mathlib.Data.Nat.Prime.Defs
import Mathlib.Data.Nat.Squarefree

-- We want results that show sqrt(r) is irrational for squarefree positive naturals r
-- Note that Lean already offers this and more at https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Real/Irrational.html

-- Assumes r > 1 is squarefree, p and q are coprime
theorem weak_sqrt_sqfree_is_irrational: ∀ p q r : ℕ, Nat.Coprime p q ∧ Squarefree r ∧ r > 1 -> p ^ 2 ≠ q ^ 2 * r := by
  intro p q r hq
  obtain ⟨ h, sqfree, gt1 ⟩ := hq
  by_contra h2
  have h0 : r ∣ p ^ 2 := by
    use q ^ 2
    rw [mul_comm]
    simp_all
  have h4 : r ∣ p := by
    rw [Squarefree.dvd_pow_iff_dvd] at h0
    repeat simp_all
  have h4a := h4
  obtain ⟨ k, hk ⟩ := h4
  have ksq : (k * r) ^ 2 = k ^ 2 * r ^ 2 := by apply mul_pow
  --rw [← mul_two] at hk
  rw [hk, mul_comm, ksq] at h2
  rw [pow_two r, ← mul_assoc, Nat.mul_right_cancel_iff] at h2
  have h5 : r ∣ q ^ 2 := by
    use k ^ 2
    rw [mul_comm]
    simp_all
  have h4 : r ∣ q := by
    rw [Squarefree.dvd_pow_iff_dvd] at h5
    repeat simp_all
  have commonfactor : r ∣ Nat.gcd p q := by
    apply Nat.dvd_gcd
    repeat simp_all
  have ne1 : r ≠ 0 := by simp_all
  apply ne1
  rw [Nat.Coprime] at h
  rw [h] at commonfactor
  rw [Nat.dvd_one] at commonfactor
  simp_all
  omega

-- Assumes r > 1 is squarefree, q ≠ 0
theorem strong_sqrt_sqfree_is_irrational: ∀ p q r : ℕ, q ≠ 0 -> Squarefree r ∧ r > 1 -> p ^ 2 ≠ q ^ 2 * r := by
  intro p q r ne0 h hq
  obtain ⟨ sqfree, gt1 ⟩ := h
  by_cases h : Nat.Coprime p q
  apply weak_sqrt_sqfree_is_irrational p q r ⟨ h, sqfree, gt1 ⟩ hq
  have ex_coprime := Nat.exists_coprime p q
  obtain ⟨ a, b, h3, h4, h5 ⟩ := ex_coprime
  rw [h4] at hq
  nth_rw 2 [h5] at hq
  repeat rw [pow_two, ← mul_assoc] at hq
  rw [← mul_comm r, ← mul_assoc, Nat.mul_right_cancel_iff, mul_comm, ← mul_comm b] at hq
  repeat rw [← mul_assoc] at hq
  rw [Nat.mul_right_cancel_iff, mul_assoc] at hq
  repeat rw [← pow_two] at hq
  rw [mul_comm] at hq
  apply weak_sqrt_sqfree_is_irrational a b r ⟨ h3, sqfree, gt1 ⟩ hq
  apply Nat.gcd_pos_of_pos_right
  omega
  apply Nat.gcd_pos_of_pos_right
  omega

lemma lemma_sqrt_sqfree_is_irrational: ∀ x : ℚ, ∀ r : ℕ, x.num ≥ 0 → Squarefree r ∧ r > 1 -> x.num ^ 2 ≠ r * ↑x.den ^ 2 := by
  intro x r x_pos sqfree h
  have h2 := strong_sqrt_sqfree_is_irrational x.num.natAbs x.den r
  have h3 : x.den ≠ 0 := by simp_all
  apply h2 h3 sqfree
  simp_all
  rw [mul_comm, ← Int.natCast_inj] at h2
  simp_all

lemma sqrt_sqfree_is_irrational_alt: ∀ r : ℕ, Squarefree r ∧ r > 1 → ¬ ∃ x : ℚ, x ^ 2 = r := by
  intro r sqfree
  push_neg
  intro x h
  rw [Rat.eq_iff_mul_eq_mul] at h
  simp_all
  by_cases x_pos : x.num ≥ 0
  apply lemma_sqrt_sqfree_is_irrational x r x_pos sqfree h
  have neg_x_pos : -x.num >= 0 := by omega
  apply lemma_sqrt_sqfree_is_irrational (-x) r neg_x_pos sqfree
  simp_all

lemma sqrt_sqfree_is_irrational: ∀ r : ℕ, Squarefree r ∧ r > 1 → Irrational √r := by
  intro r sqfree
  rw [Irrational]
  by_contra h
  obtain ⟨ sqrt2, h ⟩ := h
  apply sqrt_sqfree_is_irrational_alt r sqfree
  use sqrt2
  have square_both_sides: ∀ x y : ℝ, x = y → x ^ 2 = y ^ 2 := by simp
  apply square_both_sides at h
  have rat_to_real: ∀ x y : ℚ, x = y ↔ x = (@Rat.cast ℝ Real.instRatCast y) := by simp
  rw [rat_to_real]
  simp_all

theorem sqrt2_is_irrational: Irrational √2 := by
  apply sqrt_sqfree_is_irrational
  simp
  apply Nat.squarefree_two

#check sqrt2_is_irrational

