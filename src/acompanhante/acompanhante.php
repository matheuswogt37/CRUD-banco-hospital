<?php
require_once __DIR__ . '/../DAO/AcompanhanteDAO.php';
require_once __DIR__ . '/../DAO/InternadoDAO.php';
?>

<body>
    <main>
        <h1>Lista atuais</h1>
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
                foreach ($acompanhantes as $a) :
                ?>
                    <tr>
                        <th><?= $a['nome_completo'] ?></th>
                        <th><?= $a['numero_telefone'] ?></th>
                        <th><?= $a['relacao'] ?></th>
                    </tr>
                <?php
                endforeach;
                ?>
            </table>
        </section>
        </br>
        <h1>Inserir novo</h1>
        <section>
            <form method="POST" action="cadastro_acompanhante" enctype="multipart/form-data">
                <div>
                    <label for="input_nome_completo">Nome completo</label>
                    <input type="text" id="input_nome_completo" name="input_nome_completo">
                </div>
                <div>
                    <label for="input_telefone">Telefone</label>
                    <input type="text" id="input_telefone" name="input_telefone">
                </div>
                <div>
                    <label for="input_relacao">Relação</label>
                    <input type="text" id="input_relacao" name="input_relacao">
                </div>
                <div>
                    <label for="input_data">Data nascimento</label>
                    <input type="date" id="input_data" name="input_data">
                </div>
                <label for="input_internado">Internado</label>
                <select name="select_internado" id="input_internado" name="input_internado">
                    <?php
                    $internadoDAO = new InternadoDAO();
                    $internadoDados = $internadoDAO->consultarIdNome();

                    foreach ($internadoDados as $dado) {
                    ?>
                        <option value="<?= $dado['id_pk'] ?>">
                            <?= $dado['nome'] ?>
                        </option>
                    <?php
                    }
                    ?>
                </select>
                <div>
                    <button type="submit">
                        Cadastrar
                    </button>
                </div>
            </form>
        </section>

    </main>
</body>