use std::collections::HashSet;

fn find_factor(n : u128, start : u128) -> u128 {
    for i in start..(n as f64).sqrt().ceil() as u128 {
        if n % i == 0 {
            return i
        }
    }
    n
}

fn find_factors(mut n : u128) -> HashSet<u128> {
    let mut ret = HashSet::new();
    ret.insert(1);
    let mut f = 2;
    while n > 1 {
        f = find_factor(n, f);
        n /= f;
        for i in ret.clone().into_iter() {
            ret.insert(f * i);
        }
    }
    ret
}

fn print_factors(x : u128) {
    let mut factors = find_factors(x).into_iter().collect::<Vec<_>>();
    factors.sort();
    println!("The factors of {x:?} are {factors:?}");
}

fn main() {
    /*
    for offset in 0..10 {
        let x = 1000000000000111111 + offset;
        printFactors(x);
    }
    */
    // Product of large primes
    let x : u128 = 101214161 * 101373101 * 101838101;
    print_factors(x);
}
