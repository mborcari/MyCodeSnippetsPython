# -*- coding: utf-8 -*-
import sqlite3
from sys import exc_info
import io

class bancoDeDados:
    ''' Classe para banco de dados mysql'''

    def __init__(self, nome='lucas.db'):
        self.nome, self.conexao = nome, None

    def conecta(self):
        '''Metodo para conectar'''
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        '''Metodo para desconectar'''
        self.conexao.close()

    def consultar(self, statement):
        '''Metodo para consultar tabelas'''
        try:
            cursor = self.conexao.cursor()
            cursor.execute(statement)
            for linha in cursor.fetchall():
                print(linha)
        except AttributeError:
            print(exc_info(1))
            print("Você não está conectado no banco de dados.")

    def criar_tabelas(self, statement):
        '''Metodo para criar tabelas'''
        try:
            cursor = self.conexao.cursor()
            cursor.execute(statement)
        except AttributeError:
            print(exc_info(1))
            print("Você não está conectado no banco de dados.")
        
    def inserir_valores(self, statement):
        '''Metodo para inserir valores'''
        try:
            cursor = self.conexao.cursor()
            cursor.execute(statement)
            self.conexao.commit()
        except AttributeError:
            print(exc_info(1))
            print("Você não está conectado no banco de dados.")
    
    def deleta_valores(self, statement):
        '''Metodo para deletar linhas'''
        try:
            cursor = self.conexao.cursor()
            cursor.execute(statement)
            self.conexao.commit()
        except AttributeError:
            print(exc_info(1))
            print("Você não está conectado no banco de dados.")
    
    def backup_banco(self):
        try:
            with io.open('banco.sql', 'w') as f:
                for linha in self.conexao.iterdump():
                    f.write('%s\n' % linha)
        except AttributeError:
            print(exc_info(1))
            print("Você não está conectado no banco de dados.")
     