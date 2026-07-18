// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract MotoCarbonToken {

    string public projectName = "MotoCarbon Token";
    string public tokenSymbol = "MCT";

    address public owner;

    uint256 public gasolineEmissionFactor = 70;
    uint256 public electricEmissionFactor = 15;

    uint256 public totalTrips;
    uint256 public totalCO2Avoided;
    uint256 public totalTokensIssued;
    uint256 public totalTokensRetired;

    struct Driver {
        string name;
        string vehicleId;
        string district;
        bool registered;
    }

    struct Trip {
        uint256 tripId;
        address driver;
        uint256 distanceKm;
        uint256 co2Avoided;
        uint256 tokensIssued;
        string route;
        uint256 timestamp;
    }

    mapping(address => Driver) public drivers;
    mapping(uint256 => Trip) public trips;
    mapping(address => uint256) public balances;

    event DriverRegistered(
        address indexed driver,
        string name,
        string vehicleId,
        string district
    );

    event TripRegistered(
        uint256 indexed tripId,
        address indexed driver,
        uint256 distanceKm,
        uint256 co2Avoided,
        uint256 tokensIssued
    );

    event TokensRetired(
        address indexed user,
        uint256 amount,
        string reason
    );

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this function");
        _;
    }

    modifier onlyRegisteredDriver(address driverAddress) {
        require(drivers[driverAddress].registered == true, "Driver is not registered");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function registerDriver(
        address driverAddress,
        string memory name,
        string memory vehicleId,
        string memory district
    ) public onlyOwner {
        drivers[driverAddress] = Driver(name, vehicleId, district, true);

        emit DriverRegistered(driverAddress, name, vehicleId, district);
    }

    function registerTrip(
        address driverAddress,
        uint256 distanceKm,
        string memory route
    ) public onlyOwner onlyRegisteredDriver(driverAddress) {
        require(distanceKm > 0, "Distance must be greater than zero");

        uint256 co2AvoidedPerKm = gasolineEmissionFactor - electricEmissionFactor;
        uint256 co2Avoided = distanceKm * co2AvoidedPerKm;
        uint256 tokensToIssue = co2Avoided;

        totalTrips++;

        trips[totalTrips] = Trip(
            totalTrips,
            driverAddress,
            distanceKm,
            co2Avoided,
            tokensToIssue,
            route,
            block.timestamp
        );

        balances[driverAddress] += tokensToIssue;
        totalCO2Avoided += co2Avoided;
        totalTokensIssued += tokensToIssue;

        emit TripRegistered(
            totalTrips,
            driverAddress,
            distanceKm,
            co2Avoided,
            tokensToIssue
        );
    }

    function retireTokens(uint256 amount, string memory reason) public {
        require(balances[msg.sender] >= amount, "Insufficient token balance");

        balances[msg.sender] -= amount;
        totalTokensRetired += amount;

        emit TokensRetired(msg.sender, amount, reason);
    }

    function getDriver(address driverAddress) public view returns (
        string memory,
        string memory,
        string memory,
        bool
    ) {
        Driver memory driver = drivers[driverAddress];

        return (
            driver.name,
            driver.vehicleId,
            driver.district,
            driver.registered
        );
    }

    function getTrip(uint256 tripId) public view returns (
        uint256,
        address,
        uint256,
        uint256,
        uint256,
        string memory,
        uint256
    ) {
        Trip memory trip = trips[tripId];

        return (
            trip.tripId,
            trip.driver,
            trip.distanceKm,
            trip.co2Avoided,
            trip.tokensIssued,
            trip.route,
            trip.timestamp
        );
    }

    function getBalance(address user) public view returns (uint256) {
        return balances[user];
    }
}
