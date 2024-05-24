<?php

class ConnectDB {
    public static function getConn() {
        $env = file(__DIR__ . '/../../.env', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
        foreach ($env as $line) {
            list($name, $value) = explode('=', $line, 2);
            $_ENV[$name] = $value;
        }
        
        // $connection_string = "host={$host} port={$port} dbname={$dbname} user={$user} password={$password} ;
        $dns = "host=localhost port=5432 dbname=".$_ENV['DB_NAME']." user=".$_ENV['USER']." password=".$_ENV['PASS']."";
        // $dns = "pgsql:host=localhost;port=5432;dbname=".$_ENV['DB_NAME'];
        $conn = pg_connect($dns);
        if ($conn) {
            echo "Connected";
        }

        return $conn;
    }

    // public static function getConn():PDO {
    //     $env = file(__DIR__ . '/../../.env', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    //     foreach ($env as $line) {
    //         list($name, $value) = explode('=', $line, 2);
    //         $_ENV[$name] = $value;
    //     }
    //     $dns = "pgsql:host=localhost;port=5432;dbname=".$_ENV['DB_NAME'];
    //     $conn = new PDO($dns, $_ENV['USER'], $_ENV['PASS'], [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);

    //     if ($conn) {
    //         echo "Connected";
    //     }

    //     return $conn;
    // }
}

ConnectDB::getConn();