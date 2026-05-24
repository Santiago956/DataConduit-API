Funcionalidade: Permitir criação da regra de qualidade para uma determinada tabela e coluna desta tabela

    Cenário: Solicitada uma criação de uma regra de qualidade com todos os atributos fornecidos: tipo de regra, nome da tabela, coluna e parâmetros dependendo da regra
        Dado a criação de uma nova regra de unicidade com todos os atributos: tipo de regra (unicidade), tabela e coluna
        Quando o método de criação for utilizado passando esses atributos
        Então verifica a existência da tabela
        E se a regra em questão já existe
        E criar a regra de qualidade