/*
 * Solution to MPMP16: HOW ODD IS PASCAL'S TRIANGLE?
 * https://www.youtube.com/watch?v=tjJ2qL9uaz4
 * 
 * We'll generate Pascal's Triangle as 1's & 0's in a 64 bit int. As the row is synetric, only the first half of the row is stored, allowing up to row 128 (128 0's and 1's)
 * 
 * 
 * Output:
 *     26.489825581395348 % of numbers are odd in the top 128 rows of Pascal's Triangle (2187 out of 8256)
 * 
 */

package main

import "fmt"

var stop =  128


func main() {
    var odds = 0
    var total = 0

    // row is the first half of the row (including middle) in binary (0: even, 1: odd)
    var row uint64 = 1
    for i := 0 ; i < stop ; i++ {
        o, t := count_bits(row, i%2==1)
        odds += o
        total += t
        
        if i%2 == 0 {
            row ^= (row >> 1)
        } else {
            row ^= (row << 1)|(1 & row)
        }
    }
    percentage := 100 * float64(odds) / float64(total)
    fmt.Printf("%v %% of numbers are odd in the top %v rows" +
        "of Pascal's Triangle (%v out of %v)\n", percentage, stop, odds, total)
}


func count_bits(x uint64, is_odd_row bool) (int, int) {
    odds  := 0
    total := 0
    middle_digit := int(uint64(1) & x)
    for x > 0 { // Row always starts with 1
        total += 2
        odds += 2 * int(x&1)
        x >>= 1
    }
    if !is_odd_row {
        // Fix that middle digit of row was counted twice
        total -= 1
        odds -= middle_digit
    }
    return odds, total
}
