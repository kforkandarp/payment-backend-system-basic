# Payment Processing Backend Simulation System

This project is a backend system that simulates real-world payment processing workflows.  
It demonstrates how payment transactions are created, processed with retry logic, logged for audit purposes, and stored in a SQL Server database.

The goal of this project is to showcase backend engineering concepts such as reliability handling, state management, logging, and professional Git workflows.

---

## 🚀 Features

- RESTful APIs for payment creation and processing
- SQL Server database integration using SQLAlchemy ORM
- Unique transaction ID generation for each payment
- Automated retry mechanism for failed payments
- Audit trail with payment status history logging
- Structured backend logging with timestamps and log levels
- Professional Git workflow using branches and pull requests

-----

## 🔄 Payment Workflow

1. Client sends request to create payment  
2. Backend stores payment with PENDING status  
3. System processes payment with retry attempts  
4. Status updates to SUCCESS or FAILED  
5. Each status change is logged in audit table  
6. Data persists in SQL Server  

---

