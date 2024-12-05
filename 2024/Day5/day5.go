package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

const filepath = "input.txt"

func parseInput() (map[int][]int, [][]int) {
	file, ferr := os.Open(filepath)
	check(ferr)

	scanner := bufio.NewScanner(file)
	rules := make(map[int][]int)
	var updates [][]int
	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, "|") {
			order := strings.Split(line, "|")
			page1, err := strconv.Atoi(order[0])
			check(err)
			page2, err := strconv.Atoi(order[1])
			check(err)
			rules[page1] = append(rules[page1], page2)
		} else if strings.Contains(line, ",") {
			updateString := strings.Split(line, ",")
			var update []int
			for _, value := range updateString {
				intValue, err := strconv.Atoi(value)
				check(err)
				update = append(update, intValue)
			}
			updates = append(updates, update)
		}
	}
	file.Close()

	return rules, updates
}

func validateUpdate(values []int, rules map[int][]int) (int, bool) {
	middleIndex := int(math.Floor(float64(len(values)) / 2))
	modified := false
	sort := true
	for sort {
		sort = false
		for i := range len(values) - 1 {
			if slices.Contains(rules[values[i+1]], values[i]) {
				values[i], values[i+1] = values[i+1], values[i]
				sort = true
				modified = true
			}
		}
	}

	return values[middleIndex], modified
}

func main() {
	rules, updates := parseInput()
	values := make(map[bool]int)
	for _, update := range updates {
		score, modified := validateUpdate(update, rules)
		values[modified] += score
	}

	fmt.Println(values[false])
	fmt.Println(values[true])
}
