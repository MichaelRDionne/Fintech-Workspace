pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract ArtRegistry is ERC721Full {
    constructor() public ERC721Full("ArtRegistryToken", "ART") public { }
}

struct Artwork {
    string name;
    string artist;
    uint256 appraisalValue;
}

mapping(uint256 => Artwork) public artCollection;
 
event Appraisal (uint 256 token_id, appraisalValue, stringReportURI);
