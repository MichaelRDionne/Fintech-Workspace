pragma solidity ^0.5.0;

import "./ArcadeTokenMintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract ArcadeTokenCrowdsale is Crowdsale, MintedCrowdsale {

        constructor(
        uint rate,
        address payable wallet, // sale beneficiary
        ArcadeToken token // the ArcadeToken itself that the ArcadeTokenCrowdsale will work with
    )
        Crowdsale(rate, wallet, token)
        public
    {
        // constructor can stay empty
    }

}

contract ArcadeTokenCrowdsaleDeployer {

    // @TODO: Add public addresses to keep track of the token_address and arcade_sale_address
    
    address public arcade_crowdsale_address;
    address public arcade_token_address;


    constructor(
        string memory name,
        string memory symbol,
        address payable wallet // this address will receive all Ether raised by the sale
    ) public {
        // @TODO: create the ArcadeToken and keep its address handy
        ArcadeToken token = new ArcadeToken(name, symbol, 0);
        arcade_token_address = address(token);

        // @TODO: create the ArcadeTokenCrowdsale and tell it about the token, then keep its address handy
        ArcadeTokenCrowdsale arcade_crowdsale = 
            new ArcadeTokenCrowdsale(1, wallet, token);
        arcade_crowdsale_address = address(arcade_crowdsale);


        // @TODO: make the ArcadeTokenCrowdsale contract a minter, then have the ArcadeTokenCrowdsaleDeployer renounce its minter role
        token.addMinter(arcade_crowdsale_address);
        token.renounceMinter();
    }
}
