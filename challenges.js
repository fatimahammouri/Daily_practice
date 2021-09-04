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

function unique_string_second(givenString){
    for (let i = 0; i < givenString.length; i++){
        let currentChar = givenString[i];
        for (let j = 0; j < givenString.length; j++){
            if (givenString[j] == currentChar){
                return false;
            }
        }
    }
    return true;
}
    
    
/* 2
Given a Node Class 
class ListNode {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
let node1 = new ListNode(1);
    How node1 looks on the inside:
    {
    value: 1
    next: null
    }
Write a function that reverses the linkedlist and return head of the 
llist reversed
*/

function reverse(head) {
    // Step 1
      let previous = null
      let current = head
      let following = head
    // Step 2
      while(current !== null) {
        following = following.next
        current.next = previous
        previous = current          
        current = following
      }
    // Step 3  
      return previous
}


