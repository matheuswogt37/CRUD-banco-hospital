<?php
    require_once "ConnectDB.php";

    class InternadoDAO {
        
        function consultarInternado() {
            $conn = ConnectDB::getConn();
            $sql = "select * from internado";
            $resul = pg_query($conn, $sql);

            return pg_fetch_all($resul);
        }

        function consultarIdNome() {
            $conn = ConnectDB::getConn();
            $sql = "select internado.id_PK, paciente.nome from internado, paciente where internado.id_paciente_fk = paciente.id_pk";
            $resul = pg_query($conn, $sql);

            return pg_fetch_all($resul);
        }
    }



?>