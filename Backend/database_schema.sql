-- ============================================================================
-- Healthcare Clinic Website Backend Database Schema (MySQL DDL Dump)
-- Company: PY Digital Services Pvt. Ltd.
-- Module Owner: Udbhav (Module 4 - Administration & System Integration)
-- Reference: https://divitpurehealthclinic.com/
-- ============================================================================

CREATE DATABASE IF NOT EXISTS `clinic_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `clinic_db`;

-- ----------------------------------------------------------------------------
-- Table: roles (Inherits TimeStampedModel)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `roles` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL,
    `updated_at` DATETIME(6) NOT NULL,
    `is_deleted` TINYINT(1) NOT NULL DEFAULT 0,
    `name` VARCHAR(50) NOT NULL UNIQUE,
    `description` VARCHAR(255) NULL,
    INDEX `idx_roles_is_deleted` (`is_deleted`),
    INDEX `idx_roles_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- Table: user_profiles (Inherits TimeStampedModel)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_profiles` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL,
    `updated_at` DATETIME(6) NOT NULL,
    `is_deleted` TINYINT(1) NOT NULL DEFAULT 0,
    `email` VARCHAR(254) NOT NULL UNIQUE,
    `full_name` VARCHAR(255) NOT NULL,
    `role_id` CHAR(36) NULL,
    `is_active` TINYINT(1) NOT NULL DEFAULT 1,
    INDEX `idx_user_profiles_email` (`email`),
    INDEX `idx_user_profiles_is_deleted` (`is_deleted`),
    CONSTRAINT `fk_user_profiles_role` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- Table: appointments (Inherits TimeStampedModel)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `appointments` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL,
    `updated_at` DATETIME(6) NOT NULL,
    `is_deleted` TINYINT(1) NOT NULL DEFAULT 0,
    `token_number` VARCHAR(100) NULL,
    `patient_name` VARCHAR(255) NOT NULL,
    `patient_phone` VARCHAR(50) NOT NULL,
    `patient_email` VARCHAR(254) NULL,
    `doctor_name` VARCHAR(255) NOT NULL,
    `department` VARCHAR(100) NOT NULL DEFAULT 'General_Medicine',
    `priority` VARCHAR(50) NOT NULL DEFAULT 'routine',
    `consultation_type` VARCHAR(50) NOT NULL DEFAULT 'OPD',
    `appointment_date` DATETIME(6) NOT NULL,
    `status` VARCHAR(50) NOT NULL DEFAULT 'scheduled',
    `notes` LONGTEXT NULL,
    INDEX `idx_appointments_is_deleted` (`is_deleted`),
    INDEX `idx_appointments_status` (`status`),
    INDEX `idx_appointments_department` (`department`),
    INDEX `idx_appointments_priority` (`priority`),
    INDEX `idx_appointments_token` (`token_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- Table: admin_audit_logs (Inherits TimeStampedModel)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `admin_audit_logs` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL,
    `updated_at` DATETIME(6) NOT NULL,
    `is_deleted` TINYINT(1) NOT NULL DEFAULT 0,
    `admin_email` VARCHAR(254) NOT NULL,
    `action` VARCHAR(100) NOT NULL,
    `resource` VARCHAR(100) NOT NULL,
    `severity` VARCHAR(20) NOT NULL DEFAULT 'INFO',
    `compliance_category` VARCHAR(100) NOT NULL DEFAULT 'NABH_HIPAA_AUDIT',
    `ip_address` VARCHAR(39) NULL,
    `details` LONGTEXT NULL,
    INDEX `idx_audit_admin_email` (`admin_email`),
    INDEX `idx_audit_severity` (`severity`),
    INDEX `idx_audit_is_deleted` (`is_deleted`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
