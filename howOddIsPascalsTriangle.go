/*
 * Solution to MPMP16: HOW ODD IS PASCAL'S TRIANGLE?
 * https://www.youtube.com/watch?v=tjJ2qL9uaz4
 * 
 * We'll generate Pascal's Triangle as 1's & 0's in a 64 bit int. As the row is symetric,
 * only the first half of the row is stored, allowing up to row 128 (128 0's and 1's)
 * 
 * A quicker (differently fun) method is using the formula from Daniel Mathews:
 *     odds += pow(2, count_1s(i))
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
        odds += count_odds_in_row(row, (i+1)%2)
        total += i+1

        // Get next row
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


func count_odds_in_row(x uint64, is_even_row int) int {
    m := int(x&1) & is_even_row
    odds := 0
    for ; x > 0 ; x >>= 1 {
        odds += int(x&1)
    }
    return odds * 2 - m
}
