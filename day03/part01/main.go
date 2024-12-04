package main

import (
        "fmt"
        "os"
        "regexp"
        "strconv"
        "strings"
)

func main() {
        filename := os.Args[1]

        data, err := os.ReadFile(filename)
        if err != nil {
            panic(err)
        }

        dataset := strings.TrimSuffix(string(data), "\n")
        r, _ := regexp.Compile("mul\\(\\d{1,3},\\d{1,3}\\)")
        match := r.FindAllString(dataset, -1)

        var sum int64
        r2, _ := regexp.Compile("\\d{1,3}")
        for _, v := range match {
            num_match := r2.FindAllString(v, -1)

            if len(num_match) != 2 {
                panic("Expected 2 numbers")
            }

            a, err := strconv.ParseInt(num_match[0], 10, 64)
            if err != nil {
                panic(err)
            }

            b, err := strconv.ParseInt(num_match[1], 10, 64)
            if err != nil {
                panic(err)
            }

            sum += a * b
        }

        fmt.Println(sum)
}
