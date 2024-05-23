<?php
    require_once "ConnectDB.php";

    class AcompanhanteDAO {
        
        function consultAcompanhante() {
            $conn = ConnectDB::getConn();
            $sql = "select * from acompanhante";
            $resul = $conn->query($sql);

            return $resul->fetchAll(PDO::FETCH_ASSOC);
        }
    }



?>