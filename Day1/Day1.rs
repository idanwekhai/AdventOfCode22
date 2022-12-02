use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut cal_counts = Vec::new();
    let mut count  = 0;
    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines("src/input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(num) = line {
              if num.trim() != "" {
                count += num.parse::<i32>().unwrap();
              } else {
                cal_counts.push(count);
                count = 0;
              }
               
            }
        }
       
    }
    cal_counts.sort_by(|a, b| b.partial_cmp(a).unwrap());
    let max_value = cal_counts.iter().max();
    let sum: i32 = cal_counts[..3].iter().sum();
    
    println!("{:?}", max_value);
    println!("{:?}", sum);
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
