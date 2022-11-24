pragma solidity ^0.5.0;

import "github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";

contract ArcadeToken {
	using SafeMath for uint;

	// ...
}

function transfer(address recipient, uint value) public {
	balances[msg.sender] = balances[msg.sender].sub(value); // prevents integer underflow
	balances[recipient] = balances[recipient].add(value);
}

fallback function 
function() external payable {
    purchase();
}