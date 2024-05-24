<?php
    require_once "ConnectDB.php";

    class AcompanhanteDAO {
        
        function consultAcompanhante() {
            $conn = ConnectDB::getConn();
            $sql = "select * from acompanhante";
            $resul = pg_query($conn, $sql);

            return pg_fetch_all($resul);
        }

        function insert($dados) {
            $conn = ConnectDB::getConn();
            if (!isset($dados['select_internado'])) {
                $dados['select_internado'] = NULL;
            }

            $sql = "INSERT INTO acompanhante (nome_completo, data_nascimento, numero_telefone, relacao,id_internado_fk) VALUES ('".$dados['input_nome_completo']."','".$dados['input_data']."','".$dados['input_telefone']."','".$dados['input_relacao']."',".$dados['select_internado'].")";
            var_dump($sql);
            
            // $sql = "insert into acompanhante (nome_completo, data_nascimento, numero_telefone, relacao, id_internado_fk) values ('{$dados['input_nome_completo']}, '{$dados['input_data']}, '{$dados['input_telefone']}, '{$dados['input_relacao']}, '{$dados['select_internado']})";
            // var_dump($sql);
            $result = pg_query($conn, $sql);
            if (!$result) {
                echo pg_last_error($conn);
            } else {
                echo "sucess";
            }


        }
    }



?>