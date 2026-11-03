
# Northstar Trading GmbH — Corporate Finance & Business Performance Analytics

**Project Status: In Progress**

## Overview

Northstar Trading GmbH is a simulated B2B wholesale and distribution company used to develop an end-to-end finance analytics project.

The project focuses on transforming financial and operational data into reliable management reporting and actionable business insights across revenue, profitability, expenses, budgeting, cash flow, accounts receivable, accounts payable, and working capital.

By combining accounting principles with data analysis, the project demonstrates how interconnected financial data can support performance monitoring, financial control, and business decision-making.

## Business Objectives

The project aims to:

- Analyse revenue, cost of goods sold, gross profit, and operating expenses.
- Compare actual financial performance against budget and investigate variances.
- Monitor cash receipts, cash payments, and cash flow patterns.
- Analyse customer receivables, payment behaviour, and overdue invoices.
- Evaluate supplier payables, payment obligations, and settlement patterns.
- Assess inventory, working capital, and key financial performance indicators.
- Validate financial data and reconcile operational records with accounting information.
- Develop management reports and dashboards to support business decisions.

## Tools and Technologies

- **Python:** Data generation, data validation, and exploratory analysis.
- **SQL Server:** Relational data modelling, financial queries, and reporting analysis.
- **Excel:** Financial analysis and reporting.
- **Power BI:** Interactive financial dashboards and business performance reporting.

## Data Approach

A comprehensive, end-to-end analysis of a company's financial performance requires access to interconnected datasets covering sales, purchasing, payments, inventory, banking, budgeting, and general ledger transactions. In practice, obtaining a complete and consistent dataset across these areas from a single company is challenging due to data availability, confidentiality, and commercial sensitivity.

To address this, the project uses a structured dataset designed to simulate the financial and operational activities of a B2B trading company. The datasets are designed to reflect realistic business processes and accounting relationships, enabling integrated financial analysis, reconciliation, and management reporting across the business.

## Project Methodology

The project is being developed in stages:

1. Generate and validate master data.
2. Create sales, purchasing, payment, inventory, banking, accounting, and budget datasets.
3. Establish relationships between datasets and load the data into SQL Server.
4. Develop financial analysis queries and perform reconciliation checks.
5. Build Excel reporting outputs and Power BI dashboards.
6. Document findings, business implications, and project limitations.

The financial model incorporates relevant accounting relationships, including invoice and payment allocations, double-entry journal entries, inventory movements, and reconciliations between operational records and the general ledger.

## Current Progress

### Completed

- Initial project structure and version control setup.
- Python data-generation script.
- Customer master data.
- Supplier master data.
- Product master data.
- Department master data.
- Chart of accounts.

### In Progress

- Sales invoice and invoice-line datasets.
- Customer and supplier payment records and allocations.
- Purchasing and inventory datasets.
- Bank transactions, general ledger entries, and budget data.
- SQL Server data modelling and financial analysis.
- Excel reporting and Power BI dashboard development.

## Repository Structure

```text
Northstar_Trading_Finance_Analytics/
├── Data/
├── Python/
├── SQL/
├── Excel/
├── PowerBI/
├── Docs/
├── .gitignore
└── README.md
```

## Expected Deliverables

- Structured and validated financial datasets.
- Relational SQL Server data model.
- Financial analysis queries and reconciliation checks.
- Excel financial reporting workbook.
- Power BI business performance dashboard.
- Documented financial findings and business recommendations.

## Scope and Limitations

This project focuses on financial management reporting and business performance analytics. It is not intended to be a production accounting system or a complete implementation of German statutory accounting requirements.

The analysis will be based on the defined project assumptions, with financial calculations and reconciliations validated as the project develops.

## Author

Developed as a portfolio project demonstrating the application of accounting knowledge, financial analysis, data modelling, data quality practices, SQL, Python, Excel, and Power BI to business performance reporting.
