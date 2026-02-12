# Inteligencia de Ingresos y Segmentación de Clientes en E-commerce

Proyecto end-to-end de análisis de datos que integra ETL, análisis exploratorio, modelado de Machine Learning y visualización en BI utilizando datos transaccionales de e-commerce.

El proyecto simula un flujo real de analítica empresarial: desde datos crudos almacenados en la nube hasta la generación de insights estratégicos y segmentación de clientes basada en comportamiento.

---

## Flujo del Proyecto

![FLujo de trabajo](../Images/flujo_proyecto.png)

---

## Objetivos

- Analizar la distribución y concentración del revenue.
- Evaluar la dependencia del negocio mediante análisis de Pareto.
- Segmentar órdenes por nivel de ticket (bajo, medio y alto).
- Estudiar comportamiento de pagos e installments.
- Construir un modelo de segmentación de clientes.
- Entregar insights accionables a nivel ejecutivo.

---

## Stack Tecnológico

- Python (Pandas, NumPy, Matplotlib)
- Scikit-learn (K-Means)
- Supabase (Base de datos en la nube)
- Power BI
- Git & GitHub

---

## ETL y Preparación de Datos

- Conexión segura mediante archivo `.env`.
- Extracción de múltiples tablas relacionales desde Supabase.
- Conversión y estandarización de tipos de datos (fechas).
- Tratamiento de valores nulos (imputación por moda cuando aplica).
- Creación de variables derivadas:
  - `payment_value` consolidado por orden.
  - `quantity` como número de productos por orden.
- Validación estructural:
  - Se identificaron 774 órdenes sin detalle en `order_items`.
  - Decisión: no eliminar datos, documentar inconsistencia estructural.

---

## Análisis Exploratorio (EDA)

### Distribución del Revenue

- Media aproximada: 160
- Desviación estándar: 221
- Coeficiente de variación ≈ 1.3

La variabilidad es alta y la distribución presenta fuerte asimetría positiva.  
La transformación logarítmica confirma que el revenue no sigue una distribución normal.

### Análisis de Pareto

El 80% del revenue proviene aproximadamente del 49% de las órdenes.  

Esto indica una concentración moderada: el negocio no depende de un grupo extremadamente pequeño de compras, pero sí existe un segmento relevante que genera la mayor parte del ingreso.

### Segmentación por Nivel de Ticket

Al dividir las órdenes en tres grupos (bajo, medio y alto):

- El segmento alto genera aproximadamente el 68% del revenue total.
- El segmento medio aporta cerca del 21%.
- El segmento bajo contribuye alrededor del 10%.

Aunque las órdenes de bajo valor son más frecuentes, el ingreso está claramente concentrado en el tercil superior.

### Comportamiento de Pago

- Métodos dominantes: tarjeta de crédito y boleto.
- Installments más frecuentes: 1, 3, 2, 10 y 8.
- En el segmento de alto valor se observan cuotas extendidas (hasta 24), lo que sugiere dependencia del financiamiento para compras premium.

---

## Principales Insights de Negocio

- Existe concentración relevante en clientes de alto ticket.
- El negocio presenta riesgo estructural si el segmento premium disminuye.
- Oportunidades detectadas:
  - Programas de fidelización para clientes de alto valor.
  - Estrategias de financiamiento propio.
  - Upselling dirigido al segmento medio.
- El uso intensivo de cuotas confirma la importancia del crédito en el comportamiento de compra.

---

## Fase de Machine Learning (En Desarrollo)

Se implementará un modelo de clustering (K-Means) para segmentar clientes según comportamiento transaccional.

Variables consideradas:
- Revenue total por cliente.
- Frecuencia de compra.
- Cantidad promedio por orden.
- Uso de cuotas.
- Métodos de pago.

Resultado esperado:
Asignación de `cluster_id` a cada cliente para análisis estratégico posterior en BI.

---

## Fase de Business Intelligence (Próxima Etapa)

El dashboard incluirá:

- Revenue por cluster.
- Revenue por categoría y estado.
- Distribución de cuotas.
- Análisis de concentración.
- KPIs estratégicos para toma de decisiones.

---

## Conclusión

Este proyecto integra:

- Ingeniería de datos
- Análisis estadístico
- Machine Learning no supervisado
- Arquitectura en la nube
- Inteligencia de negocio

Simulando un flujo real de analítica empresarial end-to-end.
