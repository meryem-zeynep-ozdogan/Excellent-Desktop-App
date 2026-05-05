pipeline {
    agent any
    
    // Hem Rust'ın hem de PyO3'ün yollarını Jenkins'e öğretiyoruz
    environment {
        RUSTUP_HOME = "C:\\Users\\merzey\\.rustup"
        CARGO_HOME  = "C:\\Users\\merzey\\.cargo"
        PYO3_PYTHON = "C:\\Users\\merzey\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
    }
    
    stages {
        stage('Checkout') {
            steps { 
                git branch:'main', url:'https://github.com/meryem-zeynep-ozdogan/Excellent-Desktop-App.git' 
            }
        }
        
        stage('Rust QR Performance Check') {
            steps {
                echo 'Running Rust QR decoding algorithms...'
                dir('rust_qr') {
                    bat '"C:\\Users\\merzey\\.cargo\\bin\\cargo.exe" test' 
                }
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                bat '"C:\\Users\\merzey\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install pytest'
            }
        }
        
        stage('Database Stress Test') {
            steps {
                echo 'Executing Database Integrity and Stress Tests...'
                bat 'venv\\Scripts\\python.exe tests/db_stress_test.py'
            }
        }

        stage('UI Asset & Logic Verification') {
            steps {
                echo 'Checking application assets and Input Validation...'
                bat 'venv\\Scripts\\pytest tests/test_ui_logic.py'
            }
        }
    }
    post {
        failure { echo 'PIPELINE FAILED! Missing assets or validation bug detected.' }
        success { echo 'ALL CLEAR! Ready for deployment.' }
    }
}