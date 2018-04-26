pragma solidity ^0.4.18;

contract lottery 
{
    bytes32 res;
    mapping (address=>uint) tokens;
    uint flag = 1;
    address winner;
    address owner;
    
    modifier check
    {
        require(flag==1);
        _;
    }
    modifier onlyOwner
    {
        require(msg.sender==owner);
        _;
    }
    
     modifier onlywinner
    {
        require((msg.sender==owner)||(msg.sender==winner));
        _;
    }
    function lottery(bytes32 num) public payable
    {
        res = keccak256(num);
        owner=msg.sender;
    }
    
    function get() view returns (bytes32 hash)
    {
        return res;
    }
    
   function deposit() check public payable {
    tokens[msg.sender] += msg.value;
    if((msg.value-uint(msg.value))>0)
    {
        msg.sender.transfer((msg.value-uint(msg.value)));
    }
    
    }
    
    function makeGuess(bytes32 guess) check public returns(bool success)
    {
        require(tokens[msg.sender]>=1 ether);
        tokens[msg.sender]-=1 ether;
        if(keccak256(guess)==res)
        {
            winner = msg.sender;
            return true;
        }
        else
        {
            return false;
        }
    }
    
    function getTokens() public constant returns(uint tok)
    {
        return tokens[msg.sender]/1000000000000000000;
        
    }
    
    function getBalance() public constant returns(uint bal)
    {
        
        return this.balance;
    }
    function getBal() public constant returns(uint balan)
    {
        return msg.sender.balance/1000000000000000000;
    }
    
    function closeGame() onlyOwner public
    {
        flag=0;
    }
    
    function getprice() public onlywinner
    {
        
        winner.transfer(this.balance/2);
        owner.transfer(this.balance);
        
        
    }
}

