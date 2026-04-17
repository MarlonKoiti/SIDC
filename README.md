# 🛡️ SIDC - Sistema Inteligente de Dinâmica Criminal

## 📖 Propósito
O **SIDC** nasce com o propósito de revolucionar a análise de segurança pública na região da Baixada Santista. Ao unir dados abertos de criminalidade com conceitos neurocientíficos e comportamentais, o sistema busca ir além da simples contagem de ocorrências, entendendo a dinâmica, o fluxo e a motivação espacial dos crimes para atuar de forma preditiva.

## 🎯 Objetivo Principal
Construir um pipeline de dados escalável e um motor de Machine Learning capaz de processar dados brutos da Secretaria de Segurança Pública (SSP-SP), geocodificar os eventos e prever *hotspots* (manchas criminais) com alta precisão, fornecendo inteligência acionável para o monitoramento urbano.

---

## ⚙️ Funcionalidades (Requisitos Funcionais)
O que o sistema faz na prática:

* **Ingestão Automatizada de Dados Abertos:** Leitura de bases brutas da SSP-SP (Furtos, Roubos, etc.) a partir de arquivos despadronizados.
* **Limpeza e Padronização Semântica:** Tratamento de nomenclaturas, remoção de caracteres especiais e adequação de codificação de texto.
* **Processamento em Arquitetura Medallion:**
  * **Camada Bronze:** Armazenamento imutável do dado bruto original.
  * **Camada Silver:** Dados limpos, tipados e convertidos para formato colunar de alta performance.
  * **Camada Gold:** (Em desenvolvimento) Dados agregados, enriquecidos com coordenadas geográficas e modelados para consumo de Machine Learning.
* **Geocodificação de Ocorrências:** Transformação de endereços textuais e cruzamentos de ruas em coordenadas exatas (Latitude/Longitude).
* **Predição de Manchas Criminais (Hotspots):** Algoritmos de Machine Learning aplicados para identificar aglomerações e prever a migração da dinâmica criminal na cidade.

---

## 🛠️ Requisitos Não Funcionais
Como o sistema se sustenta (Arquitetura, Desempenho e Segurança):

* **Isolamento de Ambiente:** Gerenciamento estrito de dependências garantido pelo **Poetry**, evitando conflitos sistêmicos.
* **Segurança de Código (Shift-Left Security):** Varredura automática pré-commit via `detect-secrets` para impedir vazamento de credenciais, chaves de API e senhas no repositório.
* **Padronização e Linting de Alta Velocidade:** Formatação automática de código Python via **Ruff**, garantindo que toda a base de código siga padrões globais de legibilidade (PEP-8).
* **Alta Performance de Leitura:** Uso do formato **Parquet** na camada Silver, reduzindo consumo de armazenamento e acelerando as consultas analíticas e o treinamento de modelos.
* **Compatibilidade com Big Data:** Código Python base desenhado para transição fluida para **PySpark** e ambientes distribuídos (como Databricks) conforme o volume de dados escalar.

---

## 🚀 Espaço em Aberto para Melhorias (Roadmap Futuro)
* [ ] **Automação da Camada Bronze (Web Scraping/API):** Substituir o download manual no portal da SSP-SP por um crawler ou consumo de API agendado.
* [ ] **Orquestração de Dados:** Implementar Apache Airflow ou Mage.ai para rodar os pipelines de forma agendada e monitorada.
* [ ] **Módulo de Streaming:** Adaptar a arquitetura para receber eventos de segurança em tempo real (Kafka/Spark Streaming).
* [ ] **Dashboards Interativos:** Consumo da Camada Gold por uma ferramenta de BI ou aplicação web para visualização de mapas de calor.
* [ ] **Modelagem Multivariada:** Cruzar os dados criminais com fatores externos (clima, eventos locais, dados demográficos do IBGE) para enriquecer o modelo comportamental.

## Progresso do Projeto

### Fase 1: Setup & Governança (Concluído)
- [x] Configuração de ambiente isolado com Poetry.
- [x] Implementação de Git Hooks (Pre-commit, Ruff, Detect-secrets).
- [x] Estrutura de pastas Medallion (Bronze/Silver/Gold).

### Fase 2: Engenharia de Dados (Em andamento)
- [x] Ingestão de dados brutos da SSP-SP (Janeiro 2025 - Santos).
- [x] Pipeline de limpeza inicial e conversão para Parquet (Camada Silver).
- [ ] Próximo passo: Geocodificação e tratamento de coordenadas (Camada Gold).
