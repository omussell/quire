package main

import (
	"crypto/rand"
	"fmt"
    "math/big"
    "io"
)

func main() {
    var Reader io.Reader
    b := big.NewInt(10)
    c, err := rand.Int(Reader, b)
    if err != nil {
        return
    }
    fmt.Print(c)
}

