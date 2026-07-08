// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract MotoCarbonToken {

    struct Viaje {
        uint256 idViaje;
        string conductor;
        string distrito;
        uint256 kmRecorridos;
        uint256 co2Evitado;
        uint256 tokensGenerados;
        uint256 fechaRegistro;
    }

    mapping(uint256 => Viaje) private viajes;

    uint256 public totalViajes;

    event ViajeRegistrado(
        uint256 idViaje,
        string conductor,
        string distrito,
        uint256 co2Evitado,
        uint256 tokensGenerados
    );

    function registrarViaje(
        uint256 _idViaje,
        string memory _conductor,
        string memory _distrito,
        uint256 _kmRecorridos,
        uint256 _co2Evitado,
        uint256 _tokensGenerados
    ) public {

        viajes[_idViaje] = Viaje({
            idViaje: _idViaje,
            conductor: _conductor,
            distrito: _distrito,
            kmRecorridos: _kmRecorridos,
            co2Evitado: _co2Evitado,
            tokensGenerados: _tokensGenerados,
            fechaRegistro: block.timestamp
        });

        totalViajes++;

        emit ViajeRegistrado(
            _idViaje,
            _conductor,
            _distrito,
            _co2Evitado,
            _tokensGenerados
        );
    }

    function obtenerViaje(uint256 _idViaje)
        public
        view
        returns (
            uint256,
            string memory,
            string memory,
            uint256,
            uint256,
            uint256,
            uint256
        )
    {
        Viaje memory v = viajes[_idViaje];

        return (
            v.idViaje,
            v.conductor,
            v.distrito,
            v.kmRecorridos,
            v.co2Evitado,
            v.tokensGenerados,
            v.fechaRegistro
        );
    }

}
