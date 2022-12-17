// SPDX-License-Identifier: Unlicense



/*
Assignment
Write a function that lets a user to claim a certain amount of tokens
by calling the claimTokens() function.
Please take into consideration that the user can only claim the tokens
only one time and after the claim its balance gets updated.

Interpretation:
a) claim a certain amount, is assumed to mean that the user has to
indicate how many to claim each time he/she does a claim
b) the token can only be claimed once, meaning the claimed tokens
need to be deducted from the availability after having claimed them
c) no total available balance is provided, I assumed it to be 50 tokens.
*/

pragma solidity >=0.5.0 <=0.8.0;

contract mappingActivity {

    // Declare Variables
    uint256 public counter;                             //only count the number of times claims were made
    mapping (address => uint256) public balanceOf;      //mapping the initial and remaining balance per address after each claim
    mapping (address => uint256) public totalClaimed;   //mapping of the total claimed tokens per address
    uint256 public tokenClaim;
 
    // Set initial Value of tokens  assume 50 were made available
    constructor() public{
        balanceOf[msg.sender] = 50;
    }

    // Function to claim tokens

function claimTokens(uint256 _tokenClaim) public {                                    //user intake variable set
    require(balanceOf[msg.sender] >= _tokenClaim ,"All your tokes have been Claimed or your claim is higher than  the tokens available"); // claim amount cannot be more than available amount
    tokenClaim = _tokenClaim;                                                         //set the tokenclainm variable to the variable
    totalClaimed[msg.sender] =  totalClaimed[msg.sender] + tokenClaim;                //increment total amount claimed with the new claimed amount
    balanceOf[msg.sender] = balanceOf[msg.sender]- _tokenClaim;                       //update the reduced balance of the sender
    counter ++;                                                                       //counter indicating how often claims were made
    }

 function showTokenbalance() public view returns(uint256)  {                          //To show the balance of the user
     balanceOf[msg.sender];
      return balanceOf[msg.sender];
 
 }

}
