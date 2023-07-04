# Projeto-Final-M5-Kenzie-Ecommerce

INTRODUÇÃO
O seu objetivo neste projeto é criar uma API para sustentar uma plataforma de e-commerce. A plataforma terá diferentes níveis de acesso.

PRODUTOS
O usuário deve ter acesso a uma rota onde pode buscar os produtos por nome, categoria e id.
Deverá ter um estoque dos itens, quando o item estiver com 0 unidades deverá ter um campo indicando que o produto está indisponível.
Caso um usuário tenha um produto no carrinho e ao finalizar a compra este produto estiver indisponível deve retornar um erro indicando que o produto não está mais disponível.
Ao ser criado um pedido, deve subtrair a quantidade dos produtos do estoque.

CARRINHO
Será necessário desenvolver uma model para armazenar os produtos que o usuário selecionou, antes de finalizar a compra.
Deve conter a lista dos produtos que foram pedidos, com o valor nos items.
Um pedido não pode ser finalizado se não tiver estoque.
Se os produtos do carrinho forem de diferentes vendedores, deve ser criado um pedido para cada.

PEDIDO
Associado a cada pedido deve conter seu status PEDIDO REALIZADO, EM ANDAMENTO ou ENTREGUE para acompanhamento do usuário.
Toda vez que o status do pedido for atualizado deve ser enviado um email ao comprador.
Deve conter todos os dados dos produtos, menos a quantidade em estoque.
O vendedor do produto deve conseguir atualizar o status do pedido.
Deverá conter o horário que o pedido foi feito.

ENDEREÇO
Usuário deve ter uma relacionamento com um campo de endereço.

USUÁRIOS
O sistema deve permitir o cadastro de usuários. Deve haver, no mínimo, 3 tipos de usuários:
Administrador
Vendedor
Cliente
Deve ser possível também usuários não autenticados acessarem a plataforma para visualizar informações sobre os produtos.

FUNCIONALIDADES DO ADMINISTRADOR:
O administrador pode transformar um usuário comum em vendedor.
O usuário administrador deve ter acesso a todas as rotas.

FUNCIONALIDADES PERMITIDAS POR VENDEDORES:
Cadastrar novos produtos na plataforma.
Atualizar o estoque do produto.
Verificar pedidos realizados.
Deve ter uma rota para visualizar todos os pedidos vendidos.
Deve ter todos os acessos de um cliente. (O vendedor também pode ser cliente).

FUNCIONALIDADES PERMITIDAS PARA OS CLIENTES:
Pode atualizar o perfil para se tornar vendedor.
Adicionar produtos ao carrinho.
Finalizar a compra dos produtos.
Deve ter uma rota para visualizar todos os pedidos comprados.
