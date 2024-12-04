use std::env;
use std::fs::read_to_string;

#[derive(PartialEq, Eq)]
enum Direction {
    Increasing,
    Decreasing,   
}

fn main() -> std::io::Result<()> {
    let args: Vec<String> = env::args().collect();
    let filename = args[1].clone();

    let mut safe: i32 = 0;

    for line in read_to_string(filename).unwrap().lines() {
        let dataline = line.to_string();
        let data: Vec<&str> = dataline.split(" ").collect();


        let mut numbers = vec!();

        for entry in data.iter() {
            let num = entry.parse::<i32>().unwrap();
            numbers.push(num);
        }

        let start: usize = 0;

        let mut a = numbers[start];
        let mut b = numbers[start+1];

        let direction = if a < b {Direction::Increasing} else {Direction::Decreasing};

        let mut is_safe = true;
        for i in start+1..numbers.len() {
            a = numbers[i-1];
            b = numbers[i];

            if a == b {
                is_safe = false;
                continue;
            } else if a < b && direction == Direction::Decreasing {
                is_safe = false;
                continue;
            } else if a > b && direction == Direction::Increasing {
                is_safe = false;
                continue;
            }

            let diff = (a - b).abs();
            if diff > 3 {
                is_safe = false;
                continue;
            }

        }
        if is_safe {
            safe += 1;
        }
    }

    println!("Safe count is {}", safe);

    Ok(())
}
