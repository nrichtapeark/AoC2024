use std::env;
use std::fs::read_to_string;

#[derive(PartialEq, Eq, Clone)]
enum Direction {
    Increasing,
    Decreasing,   
}

fn check_safety(numbers: &Vec<i32>) -> bool {
    let mut is_safe = true;

    let direction = if numbers[0] < numbers[1] {Direction::Increasing} else {Direction::Decreasing};

    for i in 1..numbers.len() {
        let a = numbers[i-1];
        let b = numbers[i];

        if a == b {
            is_safe = false;
            break;
        }

        if a < b && direction == Direction::Decreasing {
            is_safe = false;
            break;
        } else if a > b && direction == Direction::Increasing {
            is_safe = false;
            break;
        }

        let diff = (a - b).abs();
        if diff > 3 {
            is_safe = false;
            break;
        }
    }

    return is_safe;
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

        if check_safety(&numbers) {
            safe += 1;
        } else {
            for i in 0..numbers.len() {
                let mut copy_of_numbers = numbers.clone();

                copy_of_numbers.remove(i);

                if check_safety(&copy_of_numbers) {
                    println!("Now safe removing {i}");
                    safe += 1;
                    break;
                }
            }
        }
    }

    println!("Safe count is {}", safe);

    Ok(())
}
