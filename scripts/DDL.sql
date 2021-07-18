/*==============================================================*/
/* DBMS name:      PostgreSQL 8                                 */
/* Created on:     01/07/2021 22:59:58                          */
/*==============================================================*/


/*==============================================================*/
/* Table: ENDERECO                                              */
/*==============================================================*/
create table ENDERECO (
   ENDERECO_ID          SERIAL                 not null,
   RUA                  VARCHAR(50)          not null,
   BAIRRO               VARCHAR(50)          not null,
   CIDADE               VARCHAR(50)          not null,
   ESTADO               VARCHAR(50)          not null,
   CEP                  VARCHAR(50)           not null,
   constraint PK_ENDERECO primary key (ENDERECO_ID)
);

/*==============================================================*/
/* Table: GERENTE                                               */
/*==============================================================*/
create table GERENTE (
   GERENTE_ID           SERIAL                not null,
   EMAIL                VARCHAR(50)          not null,
   CPF_GERENTE          VARCHAR(50)          null,
   NOME_GER             VARCHAR(50)          null,
   SOBRENOME_GER        VARCHAR(50)          null,
   constraint PK_GERENTE primary key (GERENTE_ID)
);

/*==============================================================*/
/* Table: FRANQUIA                                              */
/*==============================================================*/
create table FRANQUIA (
   FRANQUIA_ID          SERIAL                not null,
   GERENTE_ID           INTEGER                 not null,
   ENDERECO_ID          INTEGER                 not null,
   UNIDADE_FRANQUIA     VARCHAR(50)          not null,
   constraint PK_FRANQUIA primary key (FRANQUIA_ID),
   constraint FK_FRANQUIA_R10_ENDERECO foreign key (ENDERECO_ID)
      references ENDERECO (ENDERECO_ID)
      on delete restrict on update restrict,
   constraint FK_FRANQUIA_R12_GERENTE foreign key (GERENTE_ID)
      references GERENTE (GERENTE_ID)
      on delete restrict on update restrict
);


/*==============================================================*/
/* Table: CARRO                                                 */
/*==============================================================*/
create table CARRO (
   CARRO_ID             SERIAL                not null,
   FRANQUIA_ID          INTEGER                 not null,
   PLACA                VARCHAR(50)          not null,
   MODELO               VARCHAR(50)          not null,
   ANO                  VARCHAR(50)           not null,
   MARCA_CARRO          VARCHAR(50)          null,
   constraint PK_CARRO primary key (CARRO_ID),
   constraint FK_CARRO_RELATIONS_FRANQUIA foreign key (FRANQUIA_ID)
      references FRANQUIA (FRANQUIA_ID)
      on delete restrict on update restrict
);

/*==============================================================*/
/* Table: CLIENTE                                               */
/*==============================================================*/
create table CLIENTE (
   CLIENTE_ID           SERIAL               not null,
   CPF_CLIENTE          VARCHAR(50)          not null,
   CELULAR              VARCHAR(50)          not null,
   ENDERECO_ID          INTEGER              not null,
   NOME_CLI             VARCHAR(50)          null,
   SOBRENOME_CLI        VARCHAR(50)          null,
   constraint PK_CLIENTE primary key (CLIENTE_ID),
   constraint FK_CLIENTE_R13_ENDERECO foreign key (ENDERECO_ID)
      references ENDERECO (ENDERECO_ID)
      on delete restrict on update restrict
);

/*==============================================================*/
/* Table: FUNCIONARIO                                           */
/*==============================================================*/
create table FUNCIONARIO (
   NOME_FUNC            VARCHAR(50)          not null,
   SOBRENOME_FUNC       VARCHAR(50)          not null,
   CARGO                VARCHAR(50)          not null,
   FUNCIONARIO_ID       SERIAL               not null,
   SUPERVISOR_ID        INTEGER                  null,
   FRANQUIA_ID          INTEGER              not null,
   DATA_ADMISSAO        DATE                 not null,
   CPF_FUNC             VARCHAR(50)          null,
   constraint PK_FUNCIONARIO primary key (FUNCIONARIO_ID),
   constraint FK_FUNCIONA_RELATIONS_FUNCIONA foreign key (SUPERVISOR_ID)
      references FUNCIONARIO (FUNCIONARIO_ID)
      on delete restrict on update restrict,
   constraint FK_FUNCIONA_RELATIONS_FRANQUIA foreign key (FRANQUIA_ID)
      references FRANQUIA (FRANQUIA_ID)
      on delete restrict on update restrict
);

create table CLT (
   FUNCIONARIO_ID       INTEGER               not null,
   SALARIO              MONEY                not null,
   constraint PK_CLT primary key (FUNCIONARIO_ID),
   constraint FK_CLT foreign key (FUNCIONARIO_ID)
      references FUNCIONARIO (FUNCIONARIO_ID)
      on delete restrict on update restrict
);

/*==============================================================*/
/* Table: VENDA                                                 */
/*==============================================================*/
create table VENDA (
   VENDA_ID             SERIAL               not null,
   FUNCIONARIO_ID       INTEGER              not null,
   FRANQUIA_ID          INTEGER              not null,
   CLIENTE_ID           INTEGER              not null,
   CAIXA             INTEGER              not null,
   VALOR                MONEY                not null,
   DATA_VENDA           DATE                 not null,
   PARCELAS             smallint               not null,
   constraint PK_VENDA primary key (VENDA_ID),
   constraint FK_VENDA_R2_CLIENTE foreign key (CLIENTE_ID)
      references CLIENTE (CLIENTE_ID)
      on delete restrict on update restrict,
   constraint FK_VENDA_RELATIONS_FRANQUIA foreign key (FRANQUIA_ID)
      references FRANQUIA (FRANQUIA_ID)
      on delete restrict on update restrict,
   constraint FK_VENDA_R19_FUNCIONA foreign key (FUNCIONARIO_ID)
      references CLT (FUNCIONARIO_ID)
      on delete restrict on update restrict
);

/*==============================================================*/
/* Table: TERCEIRO                                              */
/*==============================================================*/
create table TERCEIRO (
   FUNCIONARIO_ID       INTEGER               not null,
   NOME_EMPRESA         VARCHAR(50)          not null,
   constraint PK_TERCEIRO primary key (FUNCIONARIO_ID),
   constraint FK_TERCEIRO_INHERITAN_FUNCIONA foreign key (FUNCIONARIO_ID)
      references FUNCIONARIO (FUNCIONARIO_ID)
      on delete restrict on update restrict
);

/*==============================================================*/
/* Table: ENTREGA                                               */
/*==============================================================*/
create table ENTREGA (
   ENTREGA_ID           SERIAL                 not null,
   CARRO_ID             INTEGER                not null,
   VENDA_ID             INTEGER                not null,
   ENDERECO_ID          INTEGER                not null,
   FUNCIONARIO_ID       INTEGER                not null,
   DATA_ENTREGA         DATE                 null,
   constraint PK_ENTREGA primary key (ENTREGA_ID),
   constraint FK_ENTREGA_R3_ENDERECO foreign key (ENDERECO_ID)
      references ENDERECO (ENDERECO_ID)
      on delete restrict on update restrict,
   constraint FK_ENTREGA_R9_CARRO foreign key (CARRO_ID)
      references CARRO (CARRO_ID)
      on delete restrict on update restrict,
   constraint FK_ENTREGA_R4_VENDA foreign key (VENDA_ID)
      references VENDA (VENDA_ID)
      on delete restrict on update restrict,
   constraint FK_ENTREGA_R7_TERCEIRO foreign key (FUNCIONARIO_ID)
      references TERCEIRO (FUNCIONARIO_ID)
      on delete restrict on update restrict
);

/*==============================================================*/
/* Table: FORNECEDOR                                            */
/*==============================================================*/
create table FORNECEDOR (
   FORNECEDOR_ID        SERIAL                not null,
   NOME_FORN            VARCHAR(50)          null,
   CNPJ_FORNECEDOR      VARCHAR(50)          not null,
   EMAIL_FORNECEDOR     VARCHAR(50)          not null,
   constraint PK_FORNECEDOR primary key (FORNECEDOR_ID)
);

/*==============================================================*/
/* Table: FORNECIMENTO                                          */
/*==============================================================*/
create table FORNECIMENTO (
   FORNECIMENTO_ID      SERIAL                not null,
   FRANQUIA_ID          INTEGER                 not null,
   FORNECEDOR_ID        INTEGER                 not null,
   DATA_FORN            DATE                 null,
   constraint PK_FORNECIMENTO primary key (FORNECIMENTO_ID),
   constraint FK_FORNECIM_R6_FORNECED foreign key (FORNECEDOR_ID)
      references FORNECEDOR (FORNECEDOR_ID)
      on delete restrict on update restrict,
   constraint FK_FORNECIM_R14_FRANQUIA foreign key (FRANQUIA_ID)
      references FRANQUIA (FRANQUIA_ID)
      on delete restrict on update restrict
);

/*==============================================================*/
/* Table: PROPRIETARIO                                          */
/*==============================================================*/
create table PROPRIETARIO (
   PROP_ID              SERIAL                not null,
   CPF_PROP             VARCHAR(50)          null,
   NOME_PROP            VARCHAR(50)          null,
   SOBRENOME_PROP       VARCHAR(50)          null,
   constraint PK_PROPRIETARIO primary key (PROP_ID)
);

/*==============================================================*/
/* Table: LOJA_TERCEIRA                                         */
/*==============================================================*/
create table LOJA_TERCEIRA (
   LOJA_ID              SERIAL                 not null,
   FRANQUIA_ID          INTEGER                 not null,
   PROP_ID              INTEGER                 null,
   SALAO                INT2                 not null,
   constraint PK_LOJA_TERCEIRA primary key (LOJA_ID),
   constraint FK_LOJA_TER_R16_PROPRIET foreign key (PROP_ID)
      references PROPRIETARIO (PROP_ID)
      on delete restrict on update restrict,
   constraint FK_LOJA_TER_R1_FRANQUIA foreign key (FRANQUIA_ID)
      references FRANQUIA (FRANQUIA_ID)
      on delete restrict on update restrict
);

/*==============================================================*/
/* Table: SECAO                                                 */
/*==============================================================*/
create table SECAO (
   SECAO_ID             SERIAL                 not null,
   NOME_SEC             VARCHAR(50)          null,
   constraint PK_SECAO primary key (SECAO_ID)
);

/*==============================================================*/
/* Table: PRODUTO                                               */
/*==============================================================*/
create table PRODUTO (
   PRODUTO_ID           SERIAL                not null,
   SECAO_ID             INTEGER                 not null,
   FRANQUIA_ID          INTEGER                 not null,
   FORNECIMENTO_ID      INTEGER                 not null,
   VENDA_ID             INTEGER                 null,
   MARCA_PRODUTO        VARCHAR(50)          not null,
   PRECO_UNITARIO       MONEY                not null,
   NOME_PRODUTO         VARCHAR(50)          null,
   constraint PK_PRODUTO primary key (PRODUTO_ID),
   constraint FK_PRODUTO_R5_FRANQUIA foreign key (FRANQUIA_ID)
      references FRANQUIA (FRANQUIA_ID)
      on delete restrict on update restrict,
   constraint FK_PRODUTO_R15_SECAO foreign key (SECAO_ID)
      references SECAO (SECAO_ID)
      on delete restrict on update restrict,
   constraint FK_PRODUTO_R11_FORNECIM foreign key (FORNECIMENTO_ID)
      references FORNECIMENTO (FORNECIMENTO_ID)
      on delete restrict on update restrict,
   constraint FK_PRODUTO_R21_VENDA foreign key (VENDA_ID)
      references VENDA (VENDA_ID)
      on delete restrict on update restrict
);

/*==============================================================*/
/* Table: PROMOCAO                                              */
/*==============================================================*/
create table PROMOCAO (
   PORCENTAGEM          SERIAL                 not null,
   PROMOCAO_ID          INTEGER                not null,
   SECAO_ID             INTEGER                 not null,
   constraint PK_PROMOCAO primary key (PROMOCAO_ID),
   constraint FK_PROMOCAO_RELATIONS_SECAO foreign key (SECAO_ID)
      references SECAO (SECAO_ID)
      on delete restrict on update restrict
);