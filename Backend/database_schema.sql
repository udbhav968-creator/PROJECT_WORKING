-- ==============================================================================
-- PURE HEALTH CLINIC & HOSPITAL SYSTEMS - MYSQL DATABASE SCHEMA DDL
-- Author: Udbhav (udbhav968-creator)
-- Email: snojkumar968@gmail.com
-- Modules: Auth (Mod 1), OPD (Mod 2), Content (Mod 3), Administration (Mod 4)
-- Timestamp: 2026-08-02
-- ==============================================================================

CREATE TABLE IF NOT EXISTS `users` (
  `id` CHAR(36) NOT NULL PRIMARY KEY,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `password` VARCHAR(255) NOT NULL,
  `role` VARCHAR(50) NOT NULL DEFAULT 'patient',
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `phone_number` VARCHAR(20),
  `is_active` TINYINT(1) DEFAULT 1,
  `is_staff` TINYINT(1) DEFAULT 0,
  `created_at` DATETIME(6) NOT NULL,
  `updated_at` DATETIME(6) NOT NULL,
  INDEX `idx_users_role` (`role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `appointments` (
  `id` CHAR(36) NOT NULL PRIMARY KEY,
  `patient_name` VARCHAR(255) NOT NULL,
  `patient_phone` VARCHAR(50) NOT NULL,
  `patient_email` VARCHAR(255),
  `doctor_name` VARCHAR(255) NOT NULL,
  `department` VARCHAR(100) NOT NULL,
  `priority` VARCHAR(50) NOT NULL DEFAULT 'routine',
  `consultation_type` VARCHAR(50) NOT NULL DEFAULT 'OPD',
  `consultation_fee_inr` DECIMAL(10,2) NOT NULL DEFAULT 500.00,
  `token_number` VARCHAR(100),
  `video_room_url` VARCHAR(500),
  `emergency_escalation_code` VARCHAR(50),
  `appointment_date` DATETIME(6) NOT NULL,
  `status` VARCHAR(50) NOT NULL DEFAULT 'scheduled',
  `notes` TEXT,
  `is_deleted` TINYINT(1) DEFAULT 0,
  `created_at` DATETIME(6) NOT NULL,
  `updated_at` DATETIME(6) NOT NULL,
  INDEX `idx_appt_dept_status` (`department`, `status`, `is_deleted`),
  INDEX `idx_appt_date_status` (`appointment_date`, `status`),
  INDEX `idx_appt_token` (`token_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `doctor_roster` (
  `id` CHAR(36) NOT NULL PRIMARY KEY,
  `doctor_name` VARCHAR(255) NOT NULL UNIQUE,
  `department` VARCHAR(100) NOT NULL,
  `consultation_fee_inr` DECIMAL(10,2) NOT NULL DEFAULT 500.00,
  `shift_hours` VARCHAR(100) DEFAULT '09:00 AM - 05:00 PM',
  `duty_status` VARCHAR(50) NOT NULL DEFAULT 'on_duty',
  `room_number` VARCHAR(50) DEFAULT 'OPD Room 101',
  `max_daily_patients` INT DEFAULT 30,
  `current_queue_count` INT DEFAULT 0,
  `estimated_wait_time_minutes` INT DEFAULT 15,
  `is_deleted` TINYINT(1) DEFAULT 0,
  `created_at` DATETIME(6) NOT NULL,
  `updated_at` DATETIME(6) NOT NULL,
  INDEX `idx_roster_status_dept` (`duty_status`, `department`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `admin_audit_logs` (
  `id` CHAR(36) NOT NULL PRIMARY KEY,
  `admin_email` VARCHAR(255) NOT NULL,
  `action` VARCHAR(100) NOT NULL,
  `resource` VARCHAR(100) NOT NULL,
  `severity` VARCHAR(20) NOT NULL DEFAULT 'INFO',
  `compliance_category` VARCHAR(100) DEFAULT 'NABH_HIPAA_AUDIT',
  `ip_address` VARCHAR(45),
  `details` TEXT,
  `is_deleted` TINYINT(1) DEFAULT 0,
  `created_at` DATETIME(6) NOT NULL,
  `updated_at` DATETIME(6) NOT NULL,
  INDEX `idx_audit_severity` (`severity`, `created_at`),
  INDEX `idx_audit_email` (`admin_email`, `severity`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
