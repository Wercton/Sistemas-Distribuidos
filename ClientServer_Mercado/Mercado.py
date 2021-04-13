class Mercado:
    
    produtos = {}
    
    def inserir_produto(self, produto):
        if self.verificar_produto(produto):
            return "\nProduto já existente."
        else:
            self.produtos[produto] = 0
            return "\nProduto cadastrado."
        
    def atualizar_produto(self, produto, qt):
        if self.verificar_produto(produto):
            self.produtos[produto] = self.produtos[produto] + qt
            if self.produtos[produto] < 0:
                self.produtos[produto] = 0
            return f"\nEstoque atualizado e quantidade de {self.produtos[produto]}."
        else:
            return "\nProduto não existente."
        
    def verificar_produto(self, produto):
        if produto in self.produtos:
            return True
        else:
            return False
        
    def listar_produtos(self):
        msg = ""
        
        for key in self.produtos:
            msg += str(key) + ": " + str(self.produtos[key]) + "\n"
            
        return msg