package main

import (
	"fmt"
	"slices"
)

func main() {
	matrix := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}

	printMatrix(matrix)
	rotateCW(matrix)
	fmt.Println("after rotate 90")
	printMatrix(matrix)
}

func rotateCW(matrix [][]int) {
	n := len(matrix)
	for i := range n {
		for j := i + 1; j < n; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
		slices.Reverse(matrix[i])
	}
}

// printMatrix prints the matrix
func printMatrix(matrix [][]int) {
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			fmt.Printf("%d ", matrix[i][j])
		}
		fmt.Println()
	}
}
