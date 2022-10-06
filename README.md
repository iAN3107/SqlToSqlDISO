<h1 align="center"> API SQL TO SQL </h1>
<p> Desenvolvida pensando em transportar dados de um banco SQL para outro, apenas replicar esses dados para outro lugar.</p>

<p> Para utilização para teste, o schema do banco está no pasta database/edith.bak, restaurando esse banco de dados, você podera testar a API rodando se configurar corretamente os arquivos dentro de service/ com os dados dos dois bancos. Para teste, foi utilizado um docker com 2 SQL Express rodando em portas diferentes.</p>

<p>Logs são gerados no diretório logs/, caso queira mexer na geração arquivo de logs, a configuração fica presente em services/sqlOrigem.</p>
