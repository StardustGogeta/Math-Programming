use std::collections::HashSet;


fn findFactor(n : usize) -> usize {
    for i in 2..(n as f64).sqrt().ceil() as usize {
        if n % i == 0 {
            return i
        }
    }
    n
}

fn findFactors(mut n : usize) -> HashSet<usize> {
    let mut ret = HashSet::new();
    ret.insert(1);
    while n > 1 {
        let f = findFactor(n);
        n /= f;
        for i in ret.clone().into_iter() {
            ret.insert(f * i);
        }
    }
    ret
}

fn main() {
    let x = 1000000000000111111;
    let mut factors = findFactors(x).into_iter().collect::<Vec<_>>();
    factors.sort();
    println!("The factors of {x:?} are {factors:?}");
}
