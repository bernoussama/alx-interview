package main

import "fmt"

func main() {
	matrix := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}

	printMatrix(matrix)
	rotate90(matrix)
	fmt.Println("after rotate 90")
	printMatrix(matrix)
}

func rotate90(matrix [][]int) {
	tmp := make([][]int, len(matrix))
	for i := range tmp {
		tmp[i] = make([]int, len(matrix[0]))
	}

	n := len(matrix)
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			tmp[n-j-1][i] = matrix[i][j]
		}
	}
	copy(matrix, tmp)
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
