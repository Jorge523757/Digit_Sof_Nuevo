-- ============================================================================
-- DIGITSOFT - SCRIPT DE CREACIÓN DE BASE DE DATOS MYSQL
-- ============================================================================
-- Eliminar base de datos si existe (CUIDADO: borra todos los datos)
DROP DATABASE IF EXISTS digitsoft_db;
-- Crear base de datos con codificación UTF-8
CREATE DATABASE digitsoft_db 
    CHARACTER SET utf8mb4 
    COLLATE utf8mb4_unicode_ci;
-- Crear usuario si no existe
CREATE USER IF NOT EXISTS 'digitsoft_user'@'localhost' IDENTIFIED BY 'digitsoft2024';
-- Otorgar todos los permisos al usuario
GRANT ALL PRIVILEGES ON digitsoft_db.* TO 'digitsoft_user'@'localhost';
-- Aplicar cambios
FLUSH PRIVILEGES;
-- Usar la base de datos
USE digitsoft_db;
SELECT 'Base de datos digitsoft_db creada exitosamente!' AS STATUS;
