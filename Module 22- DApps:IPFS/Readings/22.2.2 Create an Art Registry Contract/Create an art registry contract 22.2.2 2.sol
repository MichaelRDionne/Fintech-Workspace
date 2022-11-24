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

function registerArtwork(
    address owner,
    string memory name,
    string memory artist,
    uint256 appraisalValue,
string memory tokenURI
) public returns (uint256) {
    uint256 tokenId = totalSupply();

    _mint(owner, tokenId);
    _setTokenURI(tokenId, tokenURI);

    artCollection[tokenId] = Artwork(name, artist, appraisalValue);

    return tokenId;
}

function newAppraisal (
    uint256 token_id, 
    uint256 newAppraisalValue,
    string memory reportURI
   )public returns (uint256) {
    artCollection[token_id].appraisalValue = newAppraisalValue;
    emit Appraisal(token_id, newAppraisalValue, reportURI);
    return artCollection[token_id].appraisalValue
 }





