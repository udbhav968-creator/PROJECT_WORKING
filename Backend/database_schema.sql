-- ============================================================================
-- Healthcare Clinic Website Backend Database Schema (MySQL DDL Dump)
-- Company: PY Digital Services Pvt. Ltd.
-- Complete Enterprise Full-Stack Architecture (Modules 1, 2, 3 & 4)
-- Reference: https://divitpurehealthclinic.com/
-- ============================================================================

CREATE DATABASE IF NOT EXISTS `clinic_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `clinic_db`;

-- ----------------------------------------------------------------------------
-- Module 1: roles (Inherits TimeStampedModel)
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
-- Module 1: user_profiles (Inherits TimeStampedModel)
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
-- Module 2 & 4: doctor_roster (Inherits TimeStampedModel)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `doctor_roster` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL,
    `updated_at` DATETIME(6) NOT NULL,
    `is_deleted` TINYINT(1) NOT NULL DEFAULT 0,
    `doctor_name` VARCHAR(255) NOT NULL UNIQUE,
    `department` VARCHAR(100) NOT NULL DEFAULT 'General_Consultation',
    `consultation_fee_inr` DECIMAL(10, 2) NOT NULL DEFAULT 500.00,
    `shift_hours` VARCHAR(100) NOT NULL DEFAULT '09:00 AM - 05:00 PM',
    `duty_status` VARCHAR(50) NOT NULL DEFAULT 'on_duty',
    `room_number` VARCHAR(50) NOT NULL DEFAULT 'OPD Room 101',
    `max_daily_patients` INT NOT NULL DEFAULT 30,
    `current_queue_count` INT NOT NULL DEFAULT 0,
    INDEX `idx_roster_duty_status` (`duty_status`),
    INDEX `idx_roster_is_deleted` (`is_deleted`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- Module 2 & 4: appointments (Inherits TimeStampedModel)
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
    `department` VARCHAR(100) NOT NULL DEFAULT 'General_Consultation',
    `priority` VARCHAR(50) NOT NULL DEFAULT 'routine',
    `consultation_type` VARCHAR(50) NOT NULL DEFAULT 'OPD',
    `consultation_fee_inr` DECIMAL(10, 2) NOT NULL DEFAULT 500.00,
    `video_room_url` VARCHAR(200) NULL,
    `emergency_escalation_code` VARCHAR(50) NULL,
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
-- Module 3: medical_services
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `medical_services` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL,
    `updated_at` DATETIME(6) NOT NULL,
    `is_deleted` TINYINT(1) NOT NULL DEFAULT 0,
    `title` VARCHAR(255) NOT NULL,
    `slug` VARCHAR(255) NOT NULL UNIQUE,
    `category` VARCHAR(100) NOT NULL DEFAULT 'General',
    `description` LONGTEXT NOT NULL,
    `full_details` LONGTEXT NULL,
    `icon_name` VARCHAR(100) NOT NULL DEFAULT 'Stethoscope',
    `image_url` VARCHAR(200) NULL,
    `consultation_fee_inr` DECIMAL(10, 2) NOT NULL DEFAULT 500.00,
    `is_featured` TINYINT(1) NOT NULL DEFAULT 1,
    INDEX `idx_services_slug` (`slug`),
    INDEX `idx_services_category` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- Module 3: doctors
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `doctors` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL,
    `updated_at` DATETIME(6) NOT NULL,
    `is_deleted` TINYINT(1) NOT NULL DEFAULT 0,
    `name` VARCHAR(255) NOT NULL,
    `specialty` VARCHAR(255) NOT NULL,
    `qualifications` VARCHAR(255) NOT NULL DEFAULT 'MBBS, MD',
    `experience_years` INT NOT NULL DEFAULT 10,
    `bio` LONGTEXT NOT NULL,
    `image_url` VARCHAR(200) NULL,
    `consultation_fee_inr` DECIMAL(10, 2) NOT NULL DEFAULT 600.00,
    `opd_timings` VARCHAR(100) NOT NULL DEFAULT '09:00 AM - 05:00 PM',
    `is_available` TINYINT(1) NOT NULL DEFAULT 1,
    INDEX `idx_doctors_specialty` (`specialty`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- Module 3: blog_posts
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog_posts` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL,
    `updated_at` DATETIME(6) NOT NULL,
    `is_deleted` TINYINT(1) NOT NULL DEFAULT 0,
    `title` VARCHAR(255) NOT NULL,
    `slug` VARCHAR(255) NOT NULL UNIQUE,
    `author` VARCHAR(255) NOT NULL DEFAULT 'Dr. Divit Shah',
    `category` VARCHAR(100) NOT NULL DEFAULT 'Preventive Health',
    `summary` LONGTEXT NOT NULL,
    `content` LONGTEXT NOT NULL,
    `image_url` VARCHAR(200) NULL,
    `published_date` DATE NOT NULL,
    `is_published` TINYINT(1) NOT NULL DEFAULT 1,
    INDEX `idx_blogs_slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- Module 3: testimonials
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `testimonials` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL,
    `updated_at` DATETIME(6) NOT NULL,
    `is_deleted` TINYINT(1) NOT NULL DEFAULT 0,
    `patient_name` VARCHAR(255) NOT NULL,
    `treatment` VARCHAR(255) NOT NULL DEFAULT 'General OPD Care',
    `rating` INT NOT NULL DEFAULT 5,
    `comment` LONGTEXT NOT NULL,
    `is_approved` TINYINT(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- Module 3: gallery_images
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `gallery_images` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL,
    `updated_at` DATETIME(6) NOT NULL,
    `is_deleted` TINYINT(1) NOT NULL DEFAULT 0,
    `title` VARCHAR(255) NOT NULL,
    `category` VARCHAR(100) NOT NULL DEFAULT 'Facility',
    `image_url` VARCHAR(200) NOT NULL,
    `caption` VARCHAR(255) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- Module 3: contact_inquiries
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `contact_inquiries` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL,
    `updated_at` DATETIME(6) NOT NULL,
    `is_deleted` TINYINT(1) NOT NULL DEFAULT 0,
    `full_name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(254) NOT NULL,
    `phone` VARCHAR(50) NOT NULL,
    `subject` VARCHAR(255) NOT NULL,
    `message` LONGTEXT NOT NULL,
    `is_resolved` TINYINT(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- Module 4: admin_audit_logs (Inherits TimeStampedModel)
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
