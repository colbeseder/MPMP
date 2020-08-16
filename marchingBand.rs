/*
Solution to MPMP12: MARCHING BAND PROBLEM
https://www.youtube.com/watch?v=2DNokQGxqjE

Output:
    Use 7560 marchers to make 64 options

*/


// Every option will have one side less than the root of the numOfMarchers
// Edge case: both sides are equal to the square root
fn number_of_options(num_of_marchers: i32) -> i32{
	let root_of = (num_of_marchers as f32).sqrt().floor() as i32;

	let mut count = 0;
	for i in 1..(root_of+1) {
		if (num_of_marchers as f32) % (i as f32) == 0.0 {
			count += 1 ;
			if i != root_of { //check for the edge case
				count += 1;
			}
		}
    }
	return count;
}


fn main() {
	let target = 64;
	
	let mut i = 1;
	loop {
		if number_of_options(i) == target {
			println!("Use {} marchers to make {} options\n", i, target);
			break;
		}
		i += 1;
	}
}
