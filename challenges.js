// set of challenges in Javascript



/* 1

Given an array of integers, find the pair of adjacent
elements that has the largest product and return that product.
Example:
For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.
7 and 3 produce the largest product.

*/ 

function adjacentElementsProduct(inputArray) {
    largest = inputArray[0] * inputArray[1]
    for (let i = 1; i < inputArray.length - 1; i++){
        if ((inputArray[i] * inputArray[i + 1]) > largest){
           largest = inputArray[i] * inputArray[i + 1] 
        }
        
    }
    return largest
    
}