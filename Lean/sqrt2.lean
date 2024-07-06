import Batteries
import Mathlib.Algebra.Ring.Parity
import Mathlib.Data.Nat.Prime.Basic

theorem weak_sqrt2_is_irrational: ∀ p q, q ≠ 0 ∧ Nat.Coprime p q -> p ^ 2 ≠ q ^ 2 * 2 := by
  intro p q hq
  obtain ⟨ hq, h ⟩ := hq
  by_contra h2
  have h3 : (Even (p ^ 2)) := by
    rw [Even]
    use q ^ 2
    rw [← mul_two]
    apply h2
  have h4 : Even p := by
    rw [Nat.even_pow'] at h3
    apply h3
    simp
  have h4a := h4
  obtain ⟨ k, hk ⟩ := h4
  rw [← mul_two] at hk
  rw [hk] at h2
  have ksq : (k * 2) ^ 2 = k ^ 2 * 4 := by
    repeat rw [Nat.pow_two]
    rw [mul_assoc, mul_assoc]
    rw [Nat.mul_left_cancel_iff]
    omega
    by_contra hk0
    push_neg at hk0
    rw [Nat.le_zero_eq] at hk0
    rw [hk0, zero_mul, zero_pow, Nat.zero_eq_mul] at h2
    cases' h2 with h2 h2
    rw [pow_two, Nat.mul_eq_zero, or_self] at h2
    repeat tauto
  rw [ksq] at h2
  have : 4 = 2 * 2 := by
    tauto
  rw [this, ← mul_assoc, Nat.mul_right_cancel_iff] at h2
  have h5 : Even (q ^ 2) := by
    use k ^ 2
    rw [← mul_two]
    symm
    apply h2
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

theorem sqrt2_is_irrational: ∀ p q, q ≠ 0 -> p ^ 2 ≠ q ^ 2 * 2 := by
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
