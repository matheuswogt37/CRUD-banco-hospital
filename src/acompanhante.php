<?php
    require_once('DAO/AcompanhanteDAO.php');
?>
<body>
    <main>
        <section>
            <table>
                    <tr>
                        <th>Nome completo</th>
                        <th>Telefone</th>
                        <th>Relação</th>
                    </tr>
                <?php
                    $acompanhanteDAO = new AcompanhanteDAO();
                    $acompanhantes = $acompanhanteDAO->consultAcompanhante();
                    foreach ($acompanhantes as $a):
                        ?>
                        <tr>
                            <th><?=$a['nome_completo']?></th>
                            <th><?=$a['numero_telefone']?></th>
                            <th><?=$a['relacao']?></th>
                        </tr>
                        <?php
                        endforeach;
                ?>
            </table>
        </section>
    </main>
</body>