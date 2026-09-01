-- =============================================================================
-- PY Digital Services Pvt. Ltd. - Production Database Schema DDL
-- Project: Healthcare Clinic Website Backend & Appointment Management System
-- Lead System Architect: Udbhav (Bennett University)
-- Database Engine: MySQL 8.0.35 / SQLite3 Production Fallback
-- =============================================================================

CREATE DATABASE IF NOT EXISTS pure_health_clinic_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE pure_health_clinic_db;

-- -----------------------------------------------------------------------------
-- Table: users (Authentication & RBAC - Thota Harshavardhan Reddy)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS users (
    id CHAR(36) PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role ENUM('admin', 'doctor', 'staff', 'patient') DEFAULT 'patient',
    is_active BOOLEAN DEFAULT TRUE,
    is_staff BOOLEAN DEFAULT FALSE,
    is_superuser BOOLEAN DEFAULT FALSE,
    totp_secret VARCHAR(64) NULL,
    mfa_enabled BOOLEAN DEFAULT FALSE,
    last_login DATETIME NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_user_email (email),
    INDEX idx_user_role (role)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------------------------------
-- Table: appointments (Appointment Management - Alok Verma)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS appointments (
    id CHAR(36) PRIMARY KEY,
    patient_name VARCHAR(255) NOT NULL,
    patient_phone VARCHAR(50) NOT NULL,
    patient_email VARCHAR(255) NULL,
    doctor_name VARCHAR(255) NOT NULL,
    department VARCHAR(100) NOT NULL DEFAULT 'General_Consultation',
    priority ENUM('routine', 'urgent', 'emergency') DEFAULT 'routine',
    consultation_type ENUM('OPD', 'IPD', 'Emergency', 'Teleconsultation') DEFAULT 'OPD',
    consultation_fee_inr DECIMAL(10, 2) DEFAULT 500.00,
    token_number VARCHAR(100) UNIQUE NOT NULL,
    video_room_url VARCHAR(500) NULL,
    emergency_escalation_code VARCHAR(50) NULL,
    appointment_date DATETIME NOT NULL,
    status ENUM('scheduled', 'in_consultation', 'completed', 'cancelled', 'no_show') DEFAULT 'scheduled',
    notes TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_appointment_token (token_number),
    INDEX idx_appointment_date (appointment_date),
    INDEX idx_appointment_dept (department),
    INDEX idx_appointment_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------------------------------
-- Table: medical_services (Content Management - Aniket Ghatage)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS medical_services (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    short_description VARCHAR(500) NOT NULL,
    full_description TEXT NOT NULL,
    icon_class VARCHAR(100) DEFAULT 'fas fa-stethoscope',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------------------------------
-- Table: doctors (Specialist Directory - Aniket Ghatage)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS doctors (
    id CHAR(36) PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    specialty VARCHAR(255) NOT NULL,
    qualification VARCHAR(255) NOT NULL,
    department VARCHAR(100) NOT NULL,
    consultation_fee_inr DECIMAL(10, 2) DEFAULT 600.00,
    shift_hours VARCHAR(100) DEFAULT '09:00 AM - 05:00 PM',
    duty_status ENUM('on_duty', 'off_duty', 'in_surgery', 'emergency_call') DEFAULT 'on_duty',
    room_number VARCHAR(50) DEFAULT 'Room 101',
    bio TEXT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- -----------------------------------------------------------------------------
-- Table: admin_audit_logs (Administration & System Integration - Udbhav)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS admin_audit_logs (
    id CHAR(36) PRIMARY KEY,
    admin_email VARCHAR(255) NOT NULL,
    action VARCHAR(255) NOT NULL,
    resource VARCHAR(255) NOT NULL,
    severity ENUM('info', 'warning', 'critical') DEFAULT 'info',
    compliance_category VARCHAR(100) DEFAULT 'HIPAA_AUDIT',
    ip_address VARCHAR(50) NOT NULL,
    details JSON NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_audit_created (created_at),
    INDEX idx_audit_severity (severity)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =============================================================================
-- End of Schema Definition
-- =============================================================================
