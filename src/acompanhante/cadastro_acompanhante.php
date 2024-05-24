<?php
require_once __DIR__ .'/../DAO/AcompanhanteDAO.php'
?>

<h3>
    Cadastrando
</h3>

<?php

    $acompDAO = new AcompanhanteDAO();
    $acompDAO->insert($_POST);

?>

<h3>
    Dados cadastrados
</h3>